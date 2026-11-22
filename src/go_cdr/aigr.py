"""Draft examples from AI Gene Review (ai-gene-review) annotation reviews.

The subject of a drafted example is copied from the review file, never typed,
so its identifiers are the ones GOA and the reviewer used. The verdict and the
explanation are left to whoever writes the example: an AI review's action is
evidence for a verdict, not a consensus ruling.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

AIGR_REPO = "https://github.com/ai4curation/ai-gene-review"


def gene_curie(gene_id: str) -> str:
    """CURIE for an AI Gene Review ``id``.

    >>> gene_curie("P01019")
    'UniProtKB:P01019'
    >>> gene_curie("URS0000759CF4_9606")
    'RNAcentral:URS0000759CF4_9606'
    >>> gene_curie("SGD:S000001")
    'SGD:S000001'
    """
    if ":" in gene_id:
        return gene_id
    if gene_id.startswith("URS"):
        return f"RNAcentral:{gene_id}"
    return f"UniProtKB:{gene_id}"


def extension_text(extensions: List[Dict[str, Any]]) -> str:
    """Extensions in GAF style, ``predicate(filler)``, comma-joined.

    >>> extension_text([{"predicate": "RO:0002233", "term": {"id": "UniProtKB:Q8N884", "label": "CGAS"}}])
    'RO:0002233(UniProtKB:Q8N884)'
    """
    return ",".join(f"{e['predicate']}({e['term']['id']})" for e in extensions)


def relative_review_path(aigr_root: Path, review_path: str) -> str:
    """The review path relative to the checkout, so that pinned links never hold local paths.

    >>> relative_review_path(Path("/x/aigr"), "/x/aigr/genes/human/A/A-ai-review.yaml")
    'genes/human/A/A-ai-review.yaml'
    >>> relative_review_path(Path("/x/aigr"), "genes/human/A/A-ai-review.yaml")
    'genes/human/A/A-ai-review.yaml'
    """
    path = Path(review_path)
    if path.is_absolute():
        path = path.resolve().relative_to(aigr_root.resolve())
    return path.as_posix()


def _annotation_lines(text: str) -> List[int]:
    """1-based line of each ``existing_annotations`` item, in order."""
    node = yaml.compose(text)
    if node is None:
        return []
    for key, value in node.value:
        if key.value == "existing_annotations":
            return [item.start_mark.line + 1 for item in value.value]
    return []


def draft_example(aigr_root: Path, review_path: str, index: int, commit: str) -> Dict[str, Any]:
    """An example skeleton for ``existing_annotations[index]`` of a review file.

    Returns the subject and provenance, plus the reviewer's ``action`` and
    ``reason`` under ``aigr_review`` for whoever writes the verdict (drop that
    key before saving).
    """
    review_path = relative_review_path(aigr_root, review_path)
    text = (aigr_root / review_path).read_text()
    doc = yaml.safe_load(text)
    row = doc["existing_annotations"][index]
    term = row["term"]
    subject: Dict[str, Any] = {
        "subject_kind": "annotation",
        "gene": {"gene_id": gene_curie(str(doc["id"])), "symbol": doc.get("gene_symbol")},
        "taxon": (doc.get("taxon") or {}).get("id"),
        "term": {"term_id": term["id"], "label": term.get("label")},
        "qualifier": row.get("qualifier"),
        "evidence_code": row.get("evidence_type"),
        "reference": row.get("original_reference_id"),
    }
    if row.get("negated"):
        subject["negated"] = True
    if row.get("extensions"):
        subject["extension"] = extension_text(row["extensions"])
    subject = {k: v for k, v in subject.items() if v is not None}
    line = _annotation_lines(text)[index]
    review = row.get("review") or {}
    replacements: Optional[List[Dict[str, Any]]] = review.get("proposed_replacement_terms")
    return {
        "subject": subject,
        "derived_from": [f"{AIGR_REPO}/blob/{commit}/{review_path}#L{line}"],
        "aigr_review": {
            "action": review.get("action"),
            "reason": review.get("reason"),
            "proposed_replacement_terms": replacements,
        },
    }


def find_rows(aigr_root: Path, review_path: str, term_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """Index, term, evidence and action of each annotation row (optionally one term)."""
    doc = yaml.safe_load((aigr_root / review_path).read_text())
    rows = []
    for i, row in enumerate(doc.get("existing_annotations") or []):
        if term_id and row["term"]["id"] != term_id:
            continue
        rows.append(
            {
                "index": i,
                "term": f"{row['term']['id']} {row['term'].get('label', '')}",
                "evidence": row.get("evidence_type"),
                "reference": row.get("original_reference_id"),
                "action": (row.get("review") or {}).get("action"),
            }
        )
    return rows
