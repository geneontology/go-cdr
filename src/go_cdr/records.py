"""Load, build and validate GO Consortium Decision Records.

Layout (paths relative to the repository root):

- ``records/<CHAPTER>/<ID>.md``: one record; its YAML frontmatter is a
  ``Record`` (``src/go_cdr/schema/go_cdr.yaml``).
- ``records/<CHAPTER>/README.md``: the chapter; its frontmatter is a
  ``Chapter``, which says what kind of records the folder holds and which
  kinds of group sign off on them.
- ``groups/<GROUP>.yaml``: a contributing group or pipeline and its sign-offs.

The frontmatter is the single source of truth. Two things are derived from it
and kept in the Markdown so that GitHub shows them too: the block between
:data:`BEGIN` and :data:`END` at the end of each record (record table,
differences, open questions, sources), and the record index between
:data:`INDEX_BEGIN` and :data:`INDEX_END` in each README. ``build`` rewrites
both and writes the browser payload ``site/data.js`` (not committed);
``validate`` reports schema errors, broken cross-references and stale text.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

RECORDS_DIR = Path("records")
GROUPS_DIR = Path("groups")
SITE_DIR = Path("site")
SCHEMA_PATH = Path(__file__).parent / "schema" / "go_cdr.yaml"
REPO_BLOB = "https://github.com/geneontology/go-cdr/blob/main/"

BEGIN = "<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->"
END = "<!-- END GENERATED -->"
INDEX_BEGIN = "<!-- BEGIN GENERATED RECORD INDEX -->"
INDEX_END = "<!-- END GENERATED RECORD INDEX -->"

LINK = re.compile(r"(\[[^\]]*\]\()([^)\s]+)(\))")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)
PROVENANCE_LABEL = {"GOC": "[GOC]", "GOC_PLUS": "[GOC+]", "NEW": "[NEW]"}


def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    """Split a Markdown file into its YAML frontmatter and body.

    >>> parse_frontmatter("---\\nid: MF-1\\n---\\n# Body\\n")
    ({'id': 'MF-1'}, '# Body\\n')
    >>> parse_frontmatter("# No frontmatter\\n")
    ({}, '# No frontmatter\\n')
    """
    m = FRONTMATTER.match(text)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def dump_frontmatter(meta: Dict[str, Any]) -> str:
    """Serialise a record's frontmatter block.

    >>> print(dump_frontmatter({"id": "MF-1", "title": "x"}), end="")
    ---
    id: MF-1
    title: x
    ---
    """
    text = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100)
    return f"---\n{text}---\n"


@dataclass
class Record:
    """A record or chapter file: its repo path, frontmatter and body."""

    path: Path
    meta: Dict[str, Any]
    body: str

    @property
    def id(self) -> str:
        return str(self.meta.get("id", ""))


@dataclass
class Group:
    """A contributing group or pipeline file."""

    path: Path
    meta: Dict[str, Any]

    @property
    def id(self) -> str:
        return str(self.meta.get("id", ""))


@dataclass
class Collection:
    """Every record, chapter and group under a repository root."""

    root: Path
    records: Dict[str, Record] = field(default_factory=dict)
    chapters: Dict[str, Record] = field(default_factory=dict)
    groups: Dict[str, Group] = field(default_factory=dict)

    def chapter_of(self, record_id: str) -> Record:
        return self.chapters[self.records[record_id].path.parent.name]

    def applies(self, group: Group, record_id: str) -> bool:
        """Whether a record's chapter asks this kind of group to sign off."""
        return group.meta.get("group_kind") in (self.chapter_of(record_id).meta.get("applies_to") or [])

    def signoff(self, group: Group, record_id: str) -> Optional[Dict[str, Any]]:
        """A group's effective sign-off on a record: record level, else chapter level."""
        chapter = self.records[record_id].path.parent.name
        by_target = {s["target"]: s for s in group.meta.get("signoffs") or []}
        if record_id in by_target:
            return {**by_target[record_id], "via": "record"}
        if chapter in by_target:
            return {**by_target[chapter], "via": "chapter"}
        return None


def load(root: Path = Path(".")) -> Collection:
    """Load all records, chapters and groups under ``root``."""
    coll = Collection(root=root)
    for md in sorted((root / RECORDS_DIR).glob("*/*.md")):
        meta, body = parse_frontmatter(md.read_text())
        rec = Record(md.relative_to(root), meta, body)
        if md.name == "README.md":
            coll.chapters[md.parent.name] = rec
        else:
            coll.records[md.stem] = rec
    for path in sorted((root / GROUPS_DIR).glob("*.yaml")):
        coll.groups[path.stem] = Group(path.relative_to(root), yaml.safe_load(path.read_text()) or {})
    return coll


def rel_link(from_file: Path, target: Path) -> str:
    """Relative Markdown link from one repo file to another.

    >>> rel_link(Path("records/MF/MF-1.md"), Path("records/MF/MF-2.md"))
    'MF-2.md'
    >>> rel_link(Path("records/MF/MF-1.md"), Path("records/BP/README.md"))
    '../BP/README.md'
    """
    return os.path.relpath(target, from_file.parent)


def record_link(coll: Collection, from_file: Path, record_id: str) -> str:
    """Markdown link for a record id, or the bare id if it is unknown."""
    if record_id not in coll.records:
        return record_id
    return f"[{record_id}]({rel_link(from_file, coll.records[record_id].path)})"


def sort_key(record_id: str) -> Tuple[str, int]:
    """Sort ``MF-2`` before ``MF-10``.

    >>> sorted(["MF-10", "MF-2"], key=sort_key)
    ['MF-2', 'MF-10']
    """
    prefix, _, num = record_id.partition("-")
    return prefix, int(num)


def _cell(text: Any) -> str:
    return " ".join(str(text).split()).replace("|", "\\|")


def _source_line(rec_path: Path, src: Dict[str, Any]) -> str:
    title = src.get("title") or src.get("url") or src.get("path")
    target = src.get("url") or rel_link(rec_path, Path(src["path"]))
    return f"- {src['kind']}: [{title}]({target})"


def _differences_table(diffs: List[Dict[str, Any]]) -> List[str]:
    lines = ["| Prior source | What it said | What we recommend | Why |", "|---|---|---|---|"]
    for d in diffs:
        why = _cell(d["why"])
        if d.get("issue"):
            why += f" ([issue]({d['issue']}))"
        lines.append(f"| {_cell(d['prior_source'])} | {_cell(d['prior_said'])} | {_cell(d['we_recommend'])} | {why} |")
    return lines


def generated_block(coll: Collection, rec: Record) -> str:
    """The derived Markdown block for a record (or chapter)."""
    m = rec.meta
    out = [BEGIN, ""]
    if rec.path.name != "README.md":
        out += ["## Record", "", "| | |", "|---|---|", f"| Status | {m.get('status', '')} |"]
        prov = PROVENANCE_LABEL.get(m.get("provenance", ""), "")
        note = _cell(m.get("provenance_note", ""))
        if note:
            prov = note if note.startswith(prov) else f"{prov} {note}"
        out.append(f"| Provenance | {prov} |")
        if m.get("requirement_level"):
            out.append(f"| Requirement | {m['requirement_level']} |")
        if m.get("date"):
            out.append(f"| Date | {m['date']} |")
        for key, label in (("supersedes", "Supersedes"), ("related", "Related")):
            if m.get(key):
                out.append(f"| {label} | " + ", ".join(record_link(coll, rec.path, r) for r in m[key]) + " |")
        if m.get("superseded_by"):
            out.append(f"| Superseded by | {record_link(coll, rec.path, m['superseded_by'])} |")
        if m.get("enforced_by"):
            out.append("| Enforced by | " + ", ".join(f"<{u}>" for u in m["enforced_by"]) + " |")
        if m.get("evidence_codes"):
            out.append("| Evidence codes | " + ", ".join(m["evidence_codes"]) + " |")
        if m.get("go_terms"):
            terms = [
                f"`{t['term_id']}` " + (t.get("label") or "") + (" (obsolete)" if t.get("obsolete") else "")
                for t in m["go_terms"]
            ]
            out.append("| GO terms | " + "; ".join(x.strip() for x in terms) + " |")
        for r in m.get("reviews") or []:
            words = [
                r["reviewed_by"],
                str(r.get("review_date", "")),
                r.get("review_status", ""),
                _cell(r.get("notes", "")),
            ]
            out.append("| Review | " + " ".join(w for w in words if w) + " |")
        out.append("")
    if m.get("differences"):
        out += ["## Differences from prior guidance", ""] + _differences_table(m["differences"]) + [""]
    if m.get("open_questions"):
        out += ["## Open questions", ""]
        out += [f"{i}. {' '.join(q.split())}" for i, q in enumerate(m["open_questions"], 1)] + [""]
    if m.get("sources"):
        out += ["## Sources", ""] + [_source_line(rec.path, s) for s in m["sources"]] + [""]
    out.append(END)
    return "\n".join(out)


def record_index(coll: Collection, chapter: str) -> str:
    """The generated record table for a chapter README."""
    readme = coll.chapters[chapter].path
    lines = [INDEX_BEGIN, "", "| Id | Record | Status | Provenance |", "|---|---|---|---|"]
    for rid in sorted((r for r in coll.records if coll.records[r].path.parent.name == chapter), key=sort_key):
        m = coll.records[rid].meta
        lines.append(
            f"| [{rid}]({rel_link(readme, coll.records[rid].path)}) | {_cell(m['title'])} | "
            f"{m.get('status', '')} | {PROVENANCE_LABEL.get(m.get('provenance', ''), '')} |"
        )
    return "\n".join(lines + ["", INDEX_END])


def _replace_between(text: str, begin: str, end: str, block: str) -> str:
    """Replace ``begin..end`` (inclusive) with ``block``, or append it.

    >>> _replace_between("a\\nB\\nold\\nE\\n", "B", "E", "B\\nnew\\nE")
    'a\\nB\\nnew\\nE\\n'
    >>> _replace_between("a\\n", "B", "E", "B\\nE")
    'a\\n\\nB\\nE\\n'
    """
    if begin in text and end in text:
        head, rest = text.split(begin, 1)
        _, tail = rest.split(end, 1)
        return head + block + tail
    return text.rstrip("\n") + "\n\n" + block + "\n"


def expected_text(coll: Collection, rec: Record) -> str:
    """The full file text a record should have after ``build``."""
    text = (coll.root / rec.path).read_text()
    if rec.path.name == "README.md":
        text = _replace_between(text, INDEX_BEGIN, INDEX_END, record_index(coll, rec.path.parent.name))
        if rec.meta.get("differences") or rec.meta.get("open_questions") or rec.meta.get("sources"):
            text = _replace_between(text, BEGIN, END, generated_block(coll, rec))
        return text
    return _replace_between(text, BEGIN, END, generated_block(coll, rec))


def strip_generated(body: str) -> str:
    """Body without its derived blocks.

    >>> strip_generated("x\\n\\n" + BEGIN + "\\nstuff\\n" + END + "\\n")
    'x'
    """
    for begin, end in ((BEGIN, END), (INDEX_BEGIN, INDEX_END)):
        if begin in body:
            head, rest = body.split(begin, 1)
            body = head + rest.split(end, 1)[1] if end in rest else head
    return body.strip()


def browser_href(coll: Collection, from_file: Path, target: str) -> str:
    """Where a Markdown link in ``from_file`` should point inside the browser.

    Links to records and chapters become in-app routes; other repository
    files go to GitHub.
    """
    if re.match(r"^[a-z]+:", target) or target.startswith("#"):
        return target
    path_part, _, anchor = target.partition("#")
    repo = Path(os.path.normpath(from_file.parent / path_part))
    for rid, rec in coll.records.items():
        if rec.path == repo:
            return f"#{rid}"
    if repo.name == "README.md" and repo.parent.name in coll.chapters and repo.parent.parent == RECORDS_DIR:
        return f"#chapter/{repo.parent.name}"
    return REPO_BLOB + repo.as_posix() + (f"#{anchor}" if anchor else "")


def browser_markdown(coll: Collection, from_file: Path, text: str) -> str:
    """Rewrite every relative link in ``text`` for the browser."""
    return LINK.sub(lambda m: m.group(1) + browser_href(coll, from_file, m.group(2)) + m.group(3), text)


def _browser_item(coll: Collection, rec: Record) -> Dict[str, Any]:
    item = json.loads(json.dumps(rec.meta, default=str))
    body = strip_generated(rec.body)
    if rec.path.name == "README.md":  # the browser lists the records itself
        body = re.sub(r"^## Records[ \t]*$.*?(?=^## |\Z)", "", body, flags=re.S | re.M).strip()
    item["body"] = browser_markdown(coll, rec.path, body)
    for d in item.get("differences") or []:
        for key in ("prior_source", "prior_said", "we_recommend", "why"):
            d[key] = browser_markdown(coll, rec.path, str(d[key]))
    item["open_questions"] = [browser_markdown(coll, rec.path, q) for q in item.get("open_questions") or []]
    item["sources"] = [
        {**s, "href": s.get("url") or browser_href(coll, rec.path, rel_link(rec.path, Path(s["path"])))}
        for s in item.get("sources") or []
    ]
    item["source_url"] = REPO_BLOB + rec.path.as_posix()
    return item


def browser_data(coll: Collection) -> Dict[str, Any]:
    """The payload the static browser reads.

    ``signoffs`` maps record id -> group id -> effective sign-off, for every
    group the record applies to; a group with no position is omitted.
    """
    signoffs: Dict[str, Dict[str, Any]] = {}
    for rid in coll.records:
        row = {}
        for gid, group in coll.groups.items():
            if coll.applies(group, rid):
                s = coll.signoff(group, rid)
                if s:
                    row[gid] = json.loads(json.dumps(s, default=str))
        signoffs[rid] = row
    groups = []
    for gid in sorted(coll.groups):
        meta = {k: v for k, v in coll.groups[gid].meta.items() if k != "signoffs"}
        meta["source_url"] = REPO_BLOB + coll.groups[gid].path.as_posix()
        groups.append(meta)
    return {
        "records": [_browser_item(coll, coll.records[r]) for r in sorted(coll.records, key=sort_key)],
        "chapters": [_browser_item(coll, coll.chapters[c]) for c in sorted(coll.chapters)],
        "groups": groups,
        "signoffs": signoffs,
    }


def browser_payload(coll: Collection) -> str:
    """Text of ``site/data.js``."""
    return "window.CDR_DATA = " + json.dumps(browser_data(coll), ensure_ascii=False, indent=1) + ";\n"


def build(root: Path = Path(".")) -> List[Path]:
    """Rewrite derived blocks and the browser payload; return files changed."""
    coll = load(root)
    changed = []
    for rec in [*coll.records.values(), *coll.chapters.values()]:
        target = root / rec.path
        new = expected_text(coll, rec)
        if new != target.read_text():
            target.write_text(new)
            changed.append(rec.path)
    coll = load(root)
    out = root / SITE_DIR / "data.js"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = browser_payload(coll)
    if not out.exists() or out.read_text() != payload:
        out.write_text(payload)
        changed.append(SITE_DIR / "data.js")
    return changed


def _schema_errors(path: Path, meta: Dict[str, Any], target_class: str) -> List[str]:
    from linkml.validator import validate as linkml_validate

    instance = json.loads(json.dumps(meta, default=str))
    report = linkml_validate(instance, str(SCHEMA_PATH), target_class)
    return [f"{path}: {r.message}" for r in report.results]


def term_errors(coll: Collection, adapter: Any) -> List[str]:
    """Check each ``go_terms`` entry against an OAK adapter."""
    obsolete = set(adapter.obsoletes())
    errors = []
    for rec in coll.records.values():
        for t in rec.meta.get("go_terms") or []:
            tid = t["term_id"]
            if tid in obsolete:
                if not t.get("obsolete"):
                    errors.append(f"{rec.path}: {tid} is obsolete but not flagged obsolete")
                continue
            label = adapter.label(tid)
            if label is None:
                errors.append(f"{rec.path}: {tid} is not in the ontology")
            elif t.get("obsolete"):
                errors.append(f"{rec.path}: {tid} ({label}) is flagged obsolete but is live")
            elif t.get("label") != label:
                errors.append(f"{rec.path}: {tid} label {t.get('label')!r} should be {label!r}")
    return errors


def _record_errors(coll: Collection, rid: str, rec: Record) -> List[str]:
    m: Dict[str, Any] = rec.meta
    errors: List[str] = []
    topic = rec.path.parent.name
    if m.get("id") != rid:
        errors.append(f"{rec.path}: id {m.get('id')!r} does not match file name")
    if m.get("topic") != topic or not rid.startswith(topic + "-"):
        errors.append(f"{rec.path}: topic {m.get('topic')!r} and id must match folder {topic!r}")
    if topic not in coll.chapters:
        errors.append(f"{rec.path}: folder has no README.md chapter record")
    for key in ("related", "supersedes"):
        for ref in m.get(key) or []:
            if ref not in coll.records:
                errors.append(f"{rec.path}: {key} names unknown record {ref}")
    sup = m.get("superseded_by")
    if sup:
        if sup not in coll.records:
            errors.append(f"{rec.path}: superseded_by names unknown record {sup}")
        elif rid not in (coll.records[sup].meta.get("supersedes") or []):
            errors.append(f"{rec.path}: {sup} does not list {rid} in supersedes")
    if (m.get("status") == "superseded") != bool(sup):
        errors.append(f"{rec.path}: status 'superseded' and superseded_by must go together")
    for old in m.get("supersedes") or []:
        if old in coll.records and coll.records[old].meta.get("superseded_by") != rid:
            errors.append(f"{rec.path}: {old} does not name {rid} as superseded_by")
    return errors


def _source_errors(root: Path, rec: Record) -> List[str]:
    errors = []
    for s in rec.meta.get("sources") or []:
        if bool(s.get("url")) == bool(s.get("path")):
            errors.append(f"{rec.path}: source {s.get('title')!r} needs exactly one of url or path")
        elif s.get("path") and not (root / s["path"]).exists():
            errors.append(f"{rec.path}: source path {s['path']} does not exist")
    return errors


def _group_errors(coll: Collection, gid: str, group: Group) -> List[str]:
    errors = []
    if group.id != gid:
        errors.append(f"{group.path}: id {group.id!r} does not match file name")
    seen = set()
    for s in group.meta.get("signoffs") or []:
        target = s.get("target", "")
        if target in seen:
            errors.append(f"{group.path}: more than one sign-off for {target}")
        seen.add(target)
        if target in coll.chapters:
            chapter = coll.chapters[target]
        elif target in coll.records:
            chapter = coll.chapter_of(target)
        else:
            errors.append(f"{group.path}: sign-off target {target} is not a record or chapter")
            continue
        if group.meta.get("group_kind") not in (chapter.meta.get("applies_to") or []):
            errors.append(
                f"{group.path}: {target} is not signed off by a {group.meta.get('group_kind')} "
                f"(chapter {chapter.id} applies to {', '.join(chapter.meta.get('applies_to') or [])})"
            )
    return errors


def validate(root: Path = Path("."), check_terms: bool = False) -> List[str]:
    """Every problem found in the records and groups, as messages."""
    coll = load(root)
    errors: List[str] = []
    for topic, rec in coll.chapters.items():
        errors += _schema_errors(rec.path, rec.meta, "Chapter")
        if rec.id != topic:
            errors.append(f"{rec.path}: chapter id {rec.id!r} does not match folder {topic!r}")
        errors += _source_errors(root, rec)
    for rid, rec in coll.records.items():
        errors += _schema_errors(rec.path, rec.meta, "Record")
        errors += _record_errors(coll, rid, rec)
        errors += _source_errors(root, rec)
    for gid, group in coll.groups.items():
        errors += _schema_errors(group.path, group.meta, "Group")
        errors += _group_errors(coll, gid, group)
    if errors:
        return errors  # derived text is only defined for well-formed records
    for rec in [*coll.records.values(), *coll.chapters.values()]:
        if expected_text(coll, rec) != (root / rec.path).read_text():
            errors.append(f"{rec.path}: generated text is stale; run `just build`")
    if check_terms:
        from oaklib import get_adapter

        errors += term_errors(coll, get_adapter("sqlite:obo:go"))
    return errors
