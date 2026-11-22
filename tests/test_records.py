"""Tests for go_cdr.records and the go-cdr command line."""

from pathlib import Path
from typing import Any, Dict, Optional

import pytest
import yaml
from typer.testing import CliRunner

from go_cdr.cli import app
from go_cdr.records import (
    GROUPS_DIR,
    RECORDS_DIR,
    SITE_DIR,
    browser_data,
    browser_href,
    build,
    dump_frontmatter,
    load,
    parse_frontmatter,
    term_errors,
    validate,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


def _record(rid: str, **extra: Any) -> Dict[str, Any]:
    meta: Dict[str, Any] = {
        "id": rid,
        "title": f"Record {rid}",
        "status": "proposed",
        "topic": rid.split("-")[0],
        "provenance": "GOC",
    }
    meta.update(extra)
    return meta


def _write(root: Path, rel: str, meta: Dict[str, Any], body: str = "# Title\n\n## Decision\n\nDo it.\n") -> None:
    path = root / RECORDS_DIR / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_frontmatter(meta) + "\n" + body)


def _group(root: Path, gid: str, kind: str, signoffs: list) -> None:
    path = root / GROUPS_DIR / f"{gid}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump({"id": gid, "name": gid.title(), "group_kind": kind, "demo": True, "signoffs": signoffs})
    )


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A guideline chapter XX (two records), a rubric chapter PP, a group and a pipeline."""
    chapter = {
        "id": "XX",
        "title": "Example",
        "record_kind": "guideline",
        "applies_to": ["contributing_group"],
        "status": "proposed",
    }
    _write(tmp_path, "XX/README.md", chapter, "# Example\n\n## Records\n")
    _write(tmp_path, "XX/XX-1.md", _record("XX-1", related=["XX-2"]), "# XX-1\n\n## Decision\n\nSee [XX-2](XX-2.md).\n")
    _write(tmp_path, "XX/XX-2.md", _record("XX-2", sources=[{"kind": "wiki", "title": "W", "url": "https://w.org/x"}]))
    _write(
        tmp_path,
        "PP/README.md",
        {"id": "PP", "title": "Rubrics", "record_kind": "rubric", "applies_to": ["pipeline"], "status": "proposed"},
        "# Rubrics\n",
    )
    _write(tmp_path, "PP/PP-1.md", _record("PP-1", requirement_level="MUST"))
    _group(
        tmp_path,
        "DEMO-A",
        "contributing_group",
        [
            {"target": "XX", "signoff_status": "AGREED"},
            {"target": "XX-2", "signoff_status": "DECLINED", "notes": "not yet"},
        ],
    )
    _group(tmp_path, "DEMO-P", "pipeline", [{"target": "PP-1", "signoff_status": "IN_PROGRESS"}])
    build(tmp_path)
    return tmp_path


def _edit(root: Path, rel: str, **changes: Any) -> None:
    path = root / RECORDS_DIR / rel
    meta, body = parse_frontmatter(path.read_text())
    for key, value in changes.items():
        if value is None:
            meta.pop(key, None)
        else:
            meta[key] = value
    path.write_text(dump_frontmatter(meta) + body)


def test_repository_records_are_valid() -> None:
    """The committed records and groups pass schema, reference and staleness checks."""
    assert validate(REPO_ROOT) == []


def test_built_fixture_is_valid_and_has_generated_blocks(repo: Path) -> None:
    assert validate(repo) == []
    text = (repo / RECORDS_DIR / "XX/XX-1.md").read_text()
    assert "| Related | [XX-2](XX-2.md) |" in text
    readme = (repo / RECORDS_DIR / "XX/README.md").read_text()
    assert "| [XX-2](XX-2.md) | Record XX-2 | proposed | [GOC] |" in readme
    assert "| Requirement | MUST |" in (repo / RECORDS_DIR / "PP/PP-1.md").read_text()
    assert (repo / SITE_DIR / "data.js").read_text().startswith("window.CDR_DATA = ")
    assert build(repo) == []  # idempotent


def test_signoff_resolution(repo: Path) -> None:
    """A record-level sign-off overrides the chapter level; groups only see their chapters."""
    signoffs = browser_data(load(repo))["signoffs"]
    assert signoffs["XX-1"]["DEMO-A"]["signoff_status"] == "AGREED"
    assert signoffs["XX-1"]["DEMO-A"]["via"] == "chapter"
    assert signoffs["XX-2"]["DEMO-A"]["signoff_status"] == "DECLINED"
    assert signoffs["XX-2"]["DEMO-A"]["via"] == "record"
    assert "DEMO-P" not in signoffs["XX-1"]
    assert signoffs["PP-1"] == {"DEMO-P": {"target": "PP-1", "signoff_status": "IN_PROGRESS", "via": "record"}}


@pytest.mark.parametrize(
    "rel, changes, expected",
    [
        ("XX/XX-1.md", {"provenance": "MAYBE"}, "MAYBE"),
        ("XX/XX-1.md", {"id": "XX-9"}, "does not match file name"),
        ("XX/XX-1.md", {"related": ["XX-99"]}, "unknown record XX-99"),
        ("XX/XX-1.md", {"status": "superseded"}, "must go together"),
        ("XX/XX-1.md", {"status": "superseded", "superseded_by": "XX-2"}, "does not list XX-1 in supersedes"),
        ("XX/XX-1.md", {"enforced_by": ["src/missing.py"]}, "does not match"),
        ("XX/XX-2.md", {"sources": [{"kind": "repo", "title": "x"}]}, "exactly one of url or path"),
        ("XX/XX-2.md", {"sources": [{"kind": "repo", "title": "x", "path": "nope.md"}]}, "source path nope.md"),
        ("XX/XX-2.md", {"title": "Renamed"}, "generated text is stale"),
    ],
)
def test_validate_reports_record_problems(repo: Path, rel: str, changes: Dict[str, Any], expected: str) -> None:
    _edit(repo, rel, **changes)
    errors = validate(repo)
    assert any(expected in e for e in errors), errors


@pytest.mark.parametrize(
    "gid, kind, signoffs, expected",
    [
        ("DEMO-A", "contributing_group", [{"target": "ZZ-1", "signoff_status": "AGREED"}], "not a record or chapter"),
        ("DEMO-A", "contributing_group", [{"target": "PP-1", "signoff_status": "AGREED"}], "is not signed off by"),
        (
            "DEMO-A",
            "contributing_group",
            [{"target": "XX", "signoff_status": "AGREED"}, {"target": "XX", "signoff_status": "DECLINED"}],
            "more than one sign-off",
        ),
        ("DEMO-A", "contributing_group", [{"target": "XX", "signoff_status": "YES"}], "YES"),
    ],
)
def test_validate_reports_group_problems(repo: Path, gid: str, kind: str, signoffs: list, expected: str) -> None:
    _group(repo, gid, kind, signoffs)
    errors = validate(repo)
    assert any(expected in e for e in errors), errors


def test_unquoted_yes_is_rejected(repo: Path) -> None:
    """YAML reads a bare YES as true, which is why the statuses are AGREED/DECLINED."""
    path = repo / GROUPS_DIR / "DEMO-A.yaml"
    path.write_text(
        "id: DEMO-A\nname: A\ngroup_kind: contributing_group\nsignoffs:\n- target: XX\n  signoff_status: YES\n"
    )
    assert any("signoff_status" in e for e in validate(repo))


def test_group_file_name_must_match_id(repo: Path) -> None:
    (repo / GROUPS_DIR / "DEMO-A.yaml").rename(repo / GROUPS_DIR / "DEMO-B.yaml")
    assert any("does not match file name" in e for e in validate(repo))


def test_supersession_both_ways_is_valid(repo: Path) -> None:
    _edit(repo, "XX/XX-1.md", status="superseded", superseded_by="XX-2")
    _edit(repo, "XX/XX-2.md", supersedes=["XX-1"])
    build(repo)
    assert validate(repo) == []


@pytest.mark.parametrize(
    "target, expected",
    [
        ("XX-2.md", "#XX-2"),
        ("README.md", "#chapter/XX"),
        ("../PP/PP-1.md", "#PP-1"),
        ("../../docs/origin.md#x", "https://github.com/geneontology/go-cdr/blob/main/docs/origin.md#x"),
        ("https://example.org/x", "https://example.org/x"),
    ],
)
def test_browser_href(repo: Path, target: str, expected: str) -> None:
    assert browser_href(load(repo), RECORDS_DIR / "XX/XX-1.md", target) == expected


def test_browser_chapter_body_drops_records_heading(repo: Path) -> None:
    chapters = {c["id"]: c for c in browser_data(load(repo))["chapters"]}
    assert "## Records" not in chapters["XX"]["body"]


class FakeAdapter:
    def __init__(self, labels: Dict[str, Optional[str]], obsolete: set):
        self._labels, self._obsolete = labels, obsolete

    def obsoletes(self):
        return iter(self._obsolete)

    def label(self, curie: str) -> Optional[str]:
        return self._labels.get(curie)


def test_term_errors(repo: Path) -> None:
    _edit(
        repo,
        "XX/XX-1.md",
        go_terms=[
            {"term_id": "GO:0000001", "label": "right"},
            {"term_id": "GO:0000002", "label": "wrong"},
            {"term_id": "GO:0000003", "label": "x"},
            {"term_id": "GO:0000004", "obsolete": True},
            {"term_id": "GO:0000005", "obsolete": True},
        ],
    )
    adapter = FakeAdapter(
        {"GO:0000001": "right", "GO:0000002": "other", "GO:0000005": "live"}, {"GO:0000003", "GO:0000004"}
    )
    errors = term_errors(load(repo), adapter)
    assert len(errors) == 3
    assert any("should be 'other'" in e for e in errors)
    assert any("GO:0000003 is obsolete but not flagged" in e for e in errors)
    assert any("flagged obsolete but is live" in e for e in errors)


def test_cli_validate_and_build(repo: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["validate", "--root", str(repo)])
    assert result.exit_code == 0, result.output
    assert "records OK" in result.output
    _edit(repo, "XX/XX-2.md", title="Renamed")
    assert runner.invoke(app, ["validate", "--root", str(repo)]).exit_code == 1
    result = runner.invoke(app, ["build", "--root", str(repo)])
    assert "updated" in result.output
    assert runner.invoke(app, ["validate", "--root", str(repo)]).exit_code == 0


def _example(eid: str = "XX-1-E1", **extra: Any) -> Dict[str, Any]:
    ex: Dict[str, Any] = {
        "id": eid,
        "title": "A case",
        "verdict": "CONFORMANT",
        "subject": {
            "subject_kind": "annotation",
            "gene": {"gene_id": "UniProtKB:P00001", "symbol": "ABC1"},
            "term": {"term_id": "GO:0000001", "label": "right"},
            "qualifier": "enables",
            "evidence_code": "IDA",
            "reference": "PMID:1",
        },
        "explanation": "It follows the record.",
    }
    ex.update(extra)
    return ex


def _examples(root: Path, rid: str, examples: list, record: Optional[str] = None) -> None:
    path = root / RECORDS_DIR / rid.split("-")[0] / f"{rid}.examples.yaml"
    path.write_text(yaml.safe_dump({"record": record or rid, "examples": examples}, sort_keys=False))


def test_examples_render_and_validate(repo: Path) -> None:
    _examples(
        repo,
        "XX-1",
        [
            _example(),
            _example("XX-1-E2", verdict="NON_CONFORMANT", fix="Use GO:0000002.", see_also=["XX-2"]),
            _example("XX-1-E3", verdict="CONTESTED", discussion="https://github.com/o/r/issues/1"),
        ],
    )
    build(repo)
    assert validate(repo) == []
    text = (repo / RECORDS_DIR / "XX/XX-1.md").read_text()
    row = "| [XX-1-E1](XX-1.examples.yaml): A case | Conformant | ABC1 enables GO:0000001 right (IDA, PMID:1) |"
    assert row in text
    other = (repo / RECORDS_DIR / "XX/XX-2.md").read_text()
    assert "(from [XX-1](XX-1.md)) | Non-conformant |" in other
    records = {r["id"]: r for r in browser_data(load(repo))["records"]}
    assert [e["id"] for e in records["XX-1"]["examples"]] == ["XX-1-E1", "XX-1-E2", "XX-1-E3"]
    assert records["XX-1"]["examples"][0]["summary"] == "ABC1 enables GO:0000001 right (IDA, PMID:1)"
    assert records["XX-2"]["examples_from"] == [{"home": "XX-1", "id": "XX-1-E2"}]
    assert build(repo) == []


@pytest.mark.parametrize(
    "examples, record, expected",
    [
        ([_example(verdict="NON_CONFORMANT")], None, "needs a fix exactly when"),
        ([_example(fix="x")], None, "needs a fix exactly when"),
        ([_example(verdict="CONTESTED")], None, "needs a discussion URL or an open_question"),
        ([_example(discussion="https://x.org/1")], None, "is not CONTESTED"),
        ([_example(verdict="CONTESTED", open_question=3)], None, "XX-1 has 0"),
        ([_example("XX-2-E1")], None, "must start with XX-1-E"),
        ([_example(), _example()], None, "duplicate example id"),
        ([_example(see_also=["XX-1"])], None, "unknown or the home record"),
        ([_example(see_also=["ZZ-9"])], None, "unknown or the home record"),
        ([_example()], "XX-2", "does not match file name"),
        ([_example(verdict="MAYBE")], None, "MAYBE"),
        ([_example(subject={"subject_kind": "gocam", "description": "x"})], None, "needs model"),
        ([_example(subject={"subject_kind": "gocam", "model": "123"})], None, "does not match"),
        ([_example(subject={"subject_kind": "other"})], None, "needs description"),
        ([_example(sources=[{"kind": "repo", "title": "t", "path": "nope.md"}])], None, "source path nope.md"),
    ],
)
def test_validate_reports_example_problems(repo: Path, examples: list, record: Optional[str], expected: str) -> None:
    _examples(repo, "XX-1", examples, record)
    errors = validate(repo)
    assert any(expected in e for e in errors), errors


def test_examples_file_without_record(repo: Path) -> None:
    _examples(repo, "XX-9", [_example("XX-9-E1")])
    assert any("no record XX-9" in e for e in validate(repo))


def test_term_errors_cover_examples(repo: Path) -> None:
    _examples(repo, "XX-1", [_example()])
    errors = term_errors(load(repo), FakeAdapter({"GO:0000001": "other"}, set()))
    assert errors == ["records/XX/XX-1.examples.yaml: GO:0000001 label 'right' should be 'other'"]


AIGR_REVIEW = """id: P00001
gene_symbol: ABC1
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
existing_annotations:
- term:
    id: GO:0005515
    label: protein binding
  evidence_type: IPI
  original_reference_id: PMID:1
  qualifier: enables
  review:
    action: REMOVE
    reason: Uninformative.
- term:
    id: GO:0005739
    label: mitochondrion
  evidence_type: IBA
  original_reference_id: GO_REF:0000033
  qualifier: is_active_in
  extensions:
  - predicate: RO:0002233
    term:
      id: UniProtKB:Q1
      label: X
  review:
    action: ACCEPT
"""


def test_cli_aigr_example(tmp_path: Path) -> None:
    review = tmp_path / "genes/human/ABC1/ABC1-ai-review.yaml"
    review.parent.mkdir(parents=True)
    review.write_text(AIGR_REVIEW)
    runner = CliRunner()
    args = ["aigr-example", "genes/human/ABC1/ABC1-ai-review.yaml", "--aigr-root", str(tmp_path), "--commit", "abc"]
    listing = runner.invoke(app, args)
    assert listing.exit_code == 0, listing.output
    assert "1\tGO:0005739 mitochondrion\tIBA\tGO_REF:0000033\tACCEPT" in listing.output
    drafted = yaml.safe_load(runner.invoke(app, args + ["--index", "1"]).output)
    assert drafted["subject"] == {
        "subject_kind": "annotation",
        "gene": {"gene_id": "UniProtKB:P00001", "symbol": "ABC1"},
        "taxon": "NCBITaxon:9606",
        "term": {"term_id": "GO:0005739", "label": "mitochondrion"},
        "qualifier": "is_active_in",
        "evidence_code": "IBA",
        "reference": "GO_REF:0000033",
        "extension": "RO:0002233(UniProtKB:Q1)",
    }
    assert drafted["derived_from"] == [
        "https://github.com/monarch-initiative/ai-gene-review/blob/abc/genes/human/ABC1/ABC1-ai-review.yaml#L16"
    ]
    assert drafted["aigr_review"]["action"] == "ACCEPT"
