"""One-off: import the GO guidelines drafted in ai-gene-review as decision records.

    uv run --extra terms python scripts/migrate_from_aigr.py <ai-gene-review>/projects/GO_GUIDELINES

The guidelines were drafted in ai4curation/ai-gene-review
(``projects/GO_GUIDELINES``, PR #6445). There, the MF chapter had already been
split into one file per rule; the other 15 chapters were single documents with
``### X-N. Title`` rule headings. This script:

1. copies the guideline files into a staging area and rewrites every link that
   leaves the guidelines folder: the project page becomes ``docs/origin.md``,
   the source inventory moves to ``sources/``, other ai-gene-review project
   pages link to their rendered pages, and any other file links to GitHub;
2. splits each remaining chapter into ``records/<TOPIC>/README.md`` plus one
   ``records/<TOPIC>/<ID>.md`` per rule, with frontmatter extracted from the
   text (provenance, GO terms with labels from the GO build, evidence codes,
   related rules, validators, sources). A difference row or open question that
   cites exactly one rule goes to that rule; the rest stay on the chapter;
3. writes ``docs/origin.md`` from the project page.

Run ``just build`` afterwards to fill in the generated blocks.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path
from typing import Any, Dict, List, Tuple

from oaklib import get_adapter

from go_cdr.records import BEGIN, END, INDEX_BEGIN, INDEX_END, LINK, dump_frontmatter, parse_frontmatter

AIGR_BLOB = "https://github.com/ai4curation/ai-gene-review/blob/main/"
AIGR_PAGES = "https://ai4curation.io/ai-gene-review/pages/"
AIGR_ISSUES = "https://github.com/ai4curation/ai-gene-review/issues/"
AIGR_GUIDELINES = Path("projects/GO_GUIDELINES/guidelines")
ROOT_SCHEME = "cdrroot:"  # placeholder for a link to a file in this repository, resolved at the end
STAGING = Path("staging/GO_GUIDELINES/guidelines")
PROJECT_PAGE = Path("staging/GO_GUIDELINES.md")  # sits where it did in ai-gene-review, relative to STAGING
DATE = "2026-11-15"

EVIDENCE_CODES = (
    "EXP IDA IPI IMP IGI IEP HTP HDA HMP HGI HEP IBA IBD IKR IRD ISS ISO ISA ISM IGC RCA TAS NAS IC ND IEA"
).split()
PREFIXES = "EV LIT MF TR BP RS CC PC QN AE PH IEA CAM MO REV ONT".split()
RULE_REF = re.compile(r"\b(" + "|".join(PREFIXES) + r")-(\d+)\b")
HEADING = re.compile(r'^<a id="[^"]+"></a>\n+### ([A-Z]+-\d+)\. (.+)$', re.M)
ASPECTS = {"MF": ["F"], "BP": ["P"], "RS": ["P"], "TR": ["F", "P"], "CC": ["C"], "PC": ["C", "F"]}
CHAPTER_ONLY = ("Rules", "Differences from prior guidance", "Open questions")


def external(aigr_path: str, anchor: str) -> str:
    """Where a link to an ai-gene-review file should point from this repository.

    >>> external("projects/GO_GUIDELINES.md", "")
    'cdrroot:docs/origin.md'
    >>> external("projects/GO_GUIDELINES/sources/SOURCES.md", "x")
    'cdrroot:sources/SOURCES.md#x'
    >>> external("projects/IBA_REVIEW.md", "")
    'https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html'
    >>> external("CLAUDE.md", "nd")
    'https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md#nd'
    """
    tail = f"#{anchor}" if anchor else ""
    if aigr_path == "projects/GO_GUIDELINES.md":
        return ROOT_SCHEME + "docs/origin.md" + tail
    if aigr_path.startswith("projects/GO_GUIDELINES/sources/"):
        return ROOT_SCHEME + aigr_path[len("projects/GO_GUIDELINES/") :] + tail
    if aigr_path.startswith("projects/") and aigr_path.endswith(".md"):
        return AIGR_PAGES + aigr_path[:-3] + ".html" + tail
    return AIGR_BLOB + aigr_path + tail


def externalise(text: str, aigr_file: Path) -> str:
    """Rewrite links in a file at ``aigr_file`` that leave the guidelines folder."""

    def fix(m: re.Match) -> str:
        target = m.group(2)
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            return m.group(0)
        path_part, _, anchor = target.partition("#")
        resolved = Path(os.path.normpath(aigr_file.parent / path_part))
        if AIGR_GUIDELINES in resolved.parents:
            return m.group(0)
        return m.group(1) + external(resolved.as_posix(), anchor) + m.group(3)

    return LINK.sub(fix, text)


def sections(text: str) -> Dict[str, str]:
    """Top-level ``## `` sections by heading, plus ``_head`` for the preamble."""
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    out = {"_head": parts[0]}
    for name, body in zip(parts[1::2], parts[2::2]):
        out[name.strip()] = body
    return out


def deepen(text: str, rule_ids: set) -> str:
    """Rewrite links for text moving one folder deeper (into ``<TOPIC>/``)."""

    def fix(m: re.Match) -> str:
        target = m.group(2)
        if re.match(r"^[a-z]+:", target):
            return m.group(0)
        if target.startswith("#"):
            anchor = target[1:]
            if anchor.upper() in rule_ids:
                return m.group(1) + f"{anchor.upper()}.md" + m.group(3)
            return m.group(1) + f"README.md{target}" + m.group(3)
        return m.group(1) + "../" + target + m.group(3)

    return LINK.sub(fix, text)


def classify(target: str) -> Dict[str, str] | None:
    """A SourceRef for a link target, or None for links that are not sources."""
    if target.startswith(ROOT_SCHEME):
        return {"kind": "repo", "path": target[len(ROOT_SCHEME) :].split("#")[0]}
    if not re.match(r"^https?://", target):
        return None  # another guideline: a relation, not a source
    if "wiki.geneontology.org" in target:
        kind = "wiki"
    elif "drive.google.com" in target or "docs.google.com" in target:
        kind = "drive"
    elif "/issues/" in target or "/pull/" in target:
        kind = "issue"
    elif "europepmc.org" in target or "pubmed" in target or "doi.org" in target:
        kind = "paper"
    elif target.startswith(AIGR_BLOB) or "github.com" in target:
        kind = "repo"
    else:
        kind = "web"
    return {"kind": kind, "url": target}


def extract_sources(text: str) -> List[Dict[str, str]]:
    seen, out = set(), []
    for m in re.finditer(r"\[([^\]]*)\]\(([^)\s]+)\)", text):
        src = classify(m.group(2))
        if src is None:
            continue
        key = src.get("url") or src.get("path")
        if key in seen:
            continue
        seen.add(key)
        title = re.sub(r"^(wiki|Drive|drive):\s*", "", m.group(1)).strip("` ")
        out.append({"kind": src["kind"], "title": title or str(key), **{k: v for k, v in src.items() if k != "kind"}})
    return out


def go_terms(text: str, adapter: Any, obsolete: set) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for tid in dict.fromkeys(re.findall(r"\bGO:\d{7}\b", text)):
        if tid in obsolete:
            out.append({"term_id": tid, "obsolete": True})
        else:
            label = adapter.label(tid)
            if label is None:
                raise SystemExit(f"{tid} is neither live nor obsolete in the GO build")
            out.append({"term_id": tid, "label": label})
    return out


def provenance(note: str) -> str:
    tags = re.findall(r"\[(GOC\+?|NEW)\]", note)
    if "NEW" in tags:
        return "NEW"
    if "GOC+" in tags:
        return "GOC_PLUS"
    if "GOC" in tags:
        return "GOC"
    raise SystemExit(f"no provenance tag in: {note[:80]}")


PROV_LABEL = re.compile(r"^[*_]{0,2}Provenance[*_]{0,2}[.:][*_]{0,2}\s*")
TAG_START = re.compile(r"^\[(GOC\+?|NEW)\]")
RATIONALE_LABEL = re.compile(r"^[*_]{0,2}Rationale[.:][*_]{0,2}\s*")
APPLICATION_START = re.compile(r"^[*_]{0,2}(Worked|Examples?\b|In review)")


def split_rule(body: str, title: str) -> Tuple[str, str, str, str]:
    """(decision, context, application, provenance note) of a rule body.

    The chapters were drafted separately and label their parts differently:
    the provenance paragraph is ``Provenance:``, ``*Provenance:*``,
    ``**Provenance.**`` or just starts with its tag; the decision is a bold
    first paragraph, or else only the heading.

    >>> split_rule("**Do X.**\\n\\nRationale: because.\\n\\n*Example.* Y.\\n\\n[GOC] Sources: z", "T")
    ('Do X.', 'because.', '*Example.* Y.', '[GOC] Sources: z')
    >>> split_rule("Text.\\n\\n*Provenance:* [NEW].", "Do Y")
    ('Do Y', 'Text.', '', '[NEW].')
    """
    paras = [p.strip() for p in re.split(r"\n\s*\n", body.strip()) if p.strip()]
    prov = [p for p in paras if PROV_LABEL.match(p)] or [p for p in paras if TAG_START.match(p)]
    if not prov:
        raise SystemExit(f"no provenance paragraph in rule {title[:80]}")
    paras.remove(prov[-1])
    note = PROV_LABEL.sub("", prov[-1])
    decision = title
    if (
        paras
        and paras[0].startswith("**")
        and not re.match(r"^\*\*(Rationale|Rule detail|Example|Worked|In review)", paras[0])
    ):
        decision = paras.pop(0)
        if decision.startswith("**") and decision.endswith("**") and decision.count("**") == 2:
            decision = decision[2:-2]
    if paras:
        paras[0] = RATIONALE_LABEL.sub("", paras[0])
    ctx: List[str] = []
    app: List[str] = []
    target = ctx
    for p in paras:
        if APPLICATION_START.match(p):
            target = app
        target.append(p)
    return decision, "\n\n".join(ctx), "\n\n".join(app), note


def table_rows(section: str) -> List[List[str]]:
    rows = []
    for line in section.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line) and "What we recommend" not in line:
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
            if len(cells) == 4:
                rows.append(cells)
    return rows


def list_items(section: str) -> List[str]:
    items: List[str] = []
    for line in section.splitlines():
        m = re.match(r"^\d+\.\s+(.*)$", line)
        if m:
            items.append(m.group(1))
        elif items and line.strip():
            items[-1] += " " + line.strip()
    return items


def owner(text: str, own_ids: set) -> str:
    refs = [f"{p}-{k}" for p, k in RULE_REF.findall(text)] + [a.upper() for a in re.findall(r"\(#([a-z]+-\d+)\)", text)]
    mine = [r for r in dict.fromkeys(refs) if r in own_ids]
    return mine[0] if len(mine) == 1 else ""


def split_chapter(chapter: Path, adapter: Any, obsolete: set) -> Tuple[str, set]:
    """Split one chapter file in the staging area; return its topic and rule ids."""
    text = chapter.read_text()
    secs = sections(text)
    rules_text = "\n".join(body for name, body in secs.items() if name.startswith("Rules"))
    heads = list(HEADING.finditer(rules_text))
    ids = [h.group(1) for h in heads]
    topic = ids[0].split("-")[0]
    own_ids = set(ids)
    folder = chapter.parent / topic

    records: Dict[str, Dict[str, Any]] = {}
    bodies: Dict[str, str] = {}
    for i, h in enumerate(heads):
        rid, title = h.group(1), h.group(2).strip()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(rules_text)
        raw = deepen(rules_text[h.end() : end], own_ids)
        decision, context, application, prov = split_rule(raw, title)
        note = " ".join(prov.split())
        note = re.sub(r"\s*Sources:.*$", "", note)  # the links are kept in `sources`
        related = [r for r in dict.fromkeys(f"{p}-{k}" for p, k in RULE_REF.findall(raw)) if r != rid]
        sources = extract_sources(raw)
        meta: Dict[str, Any] = {
            "id": rid,
            "title": title,
            "status": "proposed",
            "topic": topic,
            "provenance": provenance(note),
        }
        if not re.fullmatch(r"\[(GOC\+?|NEW)\]\.?", note):
            meta["provenance_note"] = note
        if topic in ASPECTS:
            meta["aspects"] = ASPECTS[topic]
        codes = [c for c in EVIDENCE_CODES if re.search(rf"(?<![\w-]){c}(?![\w-])", raw)]
        if codes:
            meta["evidence_codes"] = codes
        terms = go_terms(raw, adapter, obsolete)
        if terms:
            meta["go_terms"] = terms
        if related:
            meta["related"] = related
        enforced = [s["url"] for s in sources if "/src/ai_gene_review/validation/" in s.get("url", "")]
        if enforced:
            meta["enforced_by"] = enforced
        meta.update(differences=[], open_questions=[], sources=sources, date=DATE)
        records[rid] = meta
        parts = [f"# {rid}. {title}", "", "## Decision", "", decision, ""]
        if context:
            parts += ["## Context", "", context, ""]
        if application:
            parts += ["## Application", "", application, ""]
        bodies[rid] = "\n".join(parts)

    chapter_diffs: List[Dict[str, Any]] = []
    for src, said, rec, why in table_rows(secs.get("Differences from prior guidance", "")):
        d = {
            k: deepen(v, own_ids)
            for k, v in zip(("prior_source", "prior_said", "we_recommend", "why"), (src, said, rec, why))
        }
        who = owner(rec, own_ids) or owner(" ".join((src, said, why)), own_ids)
        if who:
            d["we_recommend"] = re.sub(rf"\s*\(\[{who}\]\({who}\.md\)\)", "", d["we_recommend"])
            records[who]["differences"].append(d)
        else:
            chapter_diffs.append(d)
    chapter_qs: List[str] = []
    for q in list_items(secs.get("Open questions", "")):
        q = deepen(q, own_ids)
        who = owner(q, own_ids)
        if who:
            records[who]["open_questions"].append(q)
        else:
            chapter_qs.append(q)
    print(
        f"{chapter.name} -> {topic}: {len(records)} records, "
        f"{len(chapter_diffs)} differences and {len(chapter_qs)} questions left on the chapter"
    )

    title_line = secs["_head"].splitlines()[0]
    head = deepen(secs["_head"], own_ids)
    head = re.sub(r"^Status: .*\n?", "", head, flags=re.M)
    readme_body = [head.rstrip(), ""]
    names = [n for n in secs if n != "_head" and n not in CHAPTER_ONLY and not n.startswith("Rules")]
    before = names[: names.index("Decision aid")] if "Decision aid" in names else [n for n in names if n != "Sources"]
    after = [n for n in names if n not in before]
    for name in before:
        readme_body += [f"## {name}", deepen(secs[name], own_ids).rstrip(), ""]
    readme_body += ["## Records", "", INDEX_BEGIN, INDEX_END, ""]
    for name in after:
        heading = "Reading list" if name == "Sources" else name
        readme_body += [f"## {heading}", deepen(secs[name], own_ids).rstrip(), ""]
    chapter_meta: Dict[str, Any] = {
        "id": topic,
        "title": re.sub(r"^# ", "", title_line).replace(": GO annotation guidelines", ""),
        "record_kind": "guideline",
        "applies_to": ["contributing_group"],
        "status": "proposed",
    }
    if topic in ASPECTS:
        chapter_meta["aspects"] = ASPECTS[topic]
    if chapter_diffs:
        chapter_meta["differences"] = chapter_diffs
    if chapter_qs:
        chapter_meta["open_questions"] = chapter_qs
    chapter_meta["date"] = DATE

    folder.mkdir(exist_ok=True)
    (folder / "README.md").write_text(dump_frontmatter(chapter_meta) + "\n" + "\n".join(readme_body).rstrip() + "\n")
    for rid, meta in records.items():
        meta = {k: v for k, v in meta.items() if v != []}
        (folder / f"{rid}.md").write_text(
            dump_frontmatter(meta) + "\n" + bodies[rid].rstrip() + "\n\n" + BEGIN + "\n" + END + "\n"
        )
    chapter.unlink()
    relink(chapter, folder, own_ids)
    return topic, own_ids


def relink(old: Path, folder: Path, own_ids: set) -> None:
    """Point links at a removed chapter file to its new records."""
    for f in list(STAGING.glob("*.md")) + list(STAGING.glob("*/*.md")) + [PROJECT_PAGE]:
        text = f.read_text()

        def fix(m: re.Match) -> str:
            target = m.group(2)
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                return m.group(0)
            path_part, _, anchor = target.partition("#")
            if Path(os.path.normpath(f.parent / path_part)) != Path(os.path.normpath(old)):
                return m.group(0)
            dest = folder / (f"{anchor.upper()}.md" if anchor.upper() in own_ids else "README.md")
            new = os.path.relpath(dest, f.parent)
            if anchor and anchor.upper() not in own_ids:
                new += f"#{anchor}"
            return m.group(1) + new + m.group(3)

        new_text = LINK.sub(fix, text)
        if new_text != text:
            f.write_text(new_text)


OLD_MARKERS = (
    ("<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->", "<!-- END GENERATED -->"),
    ("<!-- BEGIN GENERATED RULE INDEX -->", "<!-- END GENERATED RULE INDEX -->"),
)


def strip_old_blocks(text: str) -> str:
    """Remove blocks generated by ai-gene-review, whose markers differ from ours.

    >>> strip_old_blocks("a\\n\\n<!-- BEGIN GENERATED RULE INDEX -->\\nx\\n<!-- END GENERATED RULE INDEX -->\\nb\\n")
    'a\\n\\nb\\n'
    """
    for begin, end in OLD_MARKERS:
        while begin in text:
            head, rest = text.split(begin, 1)
            text = head.rstrip("\n") + "\n" + rest.split(end, 1)[1]
    return text


def fix_presplit(path: Path) -> None:
    """Bring a record split in ai-gene-review (MF) up to this repository's schema."""
    meta, body = parse_frontmatter(path.read_text())
    body = strip_old_blocks(body)
    if path.name == "README.md":
        body = re.sub(
            r"## Rules\n(.*?)\n(?=## )",
            lambda m: "## Records\n" + m.group(1).rstrip("\n") + f"\n\n{INDEX_BEGIN}\n{INDEX_END}\n\n",
            body,
            count=1,
            flags=re.S,
        )
    if path.name == "README.md":
        meta = {
            "id": meta["id"],
            "title": meta["title"],
            "record_kind": "guideline",
            "applies_to": ["contributing_group"],
            **{k: v for k, v in meta.items() if k not in ("id", "title")},
        }
    else:
        if meta.get("enforced_by"):
            meta["enforced_by"] = [AIGR_BLOB + p for p in meta["enforced_by"]]
        for s in meta.get("sources") or []:
            if s.get("path"):
                s["url"] = AIGR_BLOB + s.pop("path")
    for d in meta.get("differences") or []:
        if isinstance(d.get("issue"), int):
            d["issue"] = AIGR_ISSUES + str(d["issue"])
    path.write_text(dump_frontmatter(meta) + body)


def resolve_root_links(path: Path) -> None:
    """Turn ``cdrroot:`` placeholders into relative links from the file's final place."""
    text = path.read_text()

    def fix(m: re.Match) -> str:
        target = m.group(2)[len(ROOT_SCHEME) :]
        return (
            m.group(1)
            + os.path.relpath(target.split("#")[0], path.parent)
            + ("#" + target.split("#", 1)[1] if "#" in target else "")
            + m.group(3)
        )

    text = re.sub(r"(\[[^\]]*\]\()(" + ROOT_SCHEME + r"[^)\s]+)(\))", fix, text)
    path.write_text(text)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("aigr_project", type=Path, help="ai-gene-review projects/GO_GUIDELINES folder")
    args = ap.parse_args()
    if Path("records").exists() and any(Path("records").iterdir()):
        raise SystemExit("records/ is not empty")
    if PROJECT_PAGE.parent.exists():
        shutil.rmtree(PROJECT_PAGE.parent)
    shutil.copytree(args.aigr_project / "guidelines", STAGING)
    _, project = parse_frontmatter((args.aigr_project.parent / "GO_GUIDELINES.md").read_text())
    PROJECT_PAGE.write_text(externalise(project, Path("projects/GO_GUIDELINES.md")))
    for md in list(STAGING.glob("*.md")) + list(STAGING.glob("*/*.md")):
        aigr_file = AIGR_GUIDELINES / md.relative_to(STAGING)
        md.write_text(externalise(md.read_text(), aigr_file))
    for md in STAGING.glob("*/*.md"):
        fix_presplit(md)

    adapter = get_adapter("sqlite:obo:go")
    obsolete = set(adapter.obsoletes())
    for chapter in sorted(STAGING.glob("*.md")):
        split_chapter(chapter, adapter, obsolete)

    Path("records").mkdir(exist_ok=True)
    for folder in sorted(p for p in STAGING.iterdir() if p.is_dir()):
        shutil.move(str(folder), Path("records") / folder.name)
    for md in Path("records").glob("*/*.md"):
        resolve_root_links(md)

    body = PROJECT_PAGE.read_text().replace("](GO_GUIDELINES/guidelines/", "](../records/")
    origin = Path("docs/origin.md")
    origin.parent.mkdir(exist_ok=True)
    origin.write_text(
        "<!-- Imported from ai4curation/ai-gene-review projects/GO_GUIDELINES.md (PR #6445). -->\n\n" + body
    )
    resolve_root_links(origin)
    shutil.rmtree(PROJECT_PAGE.parent)
    print("done; now run `just build` and `just validate`")


if __name__ == "__main__":
    main()
