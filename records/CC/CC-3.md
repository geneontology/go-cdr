---
id: CC-3
title: Treat an `is_active_in` row from IBA, a root-term ND, or a pipeline default as no stronger than
  `located_in` until the activity location is checked.
status: proposed
topic: CC
provenance: NEW
provenance_note: '[NEW] GOC sets the PAINT default but has no guidance on reading it. We treat the relation
  on a default-emitting pipeline row as uninformative.'
aspects:
- C
evidence_codes:
- IBA
- IBD
go_terms:
- term_id: GO:0005739
  label: mitochondrion
differences:
- prior_source: '[Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
    (CC default `located_in`) vs [Manager Call 2020-11-04](https://wiki.geneontology.org/index.php/Manager_Call_2020-11-04)
    and [PAINT call 2020-05-05](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)
    (`is_active_in` default for root CC and IBA)'
  prior_said: Two defaults for the same aspect
  we_recommend: '`located_in` is the default; read pipeline `is_active_in` as `located_in` until checked
    (CC-3)'
  why: PAINT ignores seed qualifiers, so the IBA relation carries no information about activity
open_questions:
- '**`is_active_in` from PAINT.** Should PAINT emit `located_in` for CC IBDs whose seeds are all `located_in`?
  This would make CC-3 unnecessary.'
sources:
- kind: wiki
  title: 5 May 2020 PAINT Conference Call
  url: https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call
- kind: wiki
  title: Manager Call 2020-11-04
  url: https://wiki.geneontology.org/index.php/Manager_Call_2020-11-04
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
date: '2026-11-15'
---

# CC-3. Treat an `is_active_in` row from IBA, a root-term ND, or a pipeline default as no stronger than `located_in` until the activity location is checked.

## Decision

Treat an `is_active_in` row from IBA, a root-term ND, or a pipeline default as no stronger than `located_in` until the activity location is checked.

## Context

Several pipelines emit `is_active_in` by default. PAINT uses `is_active_in` for all CC IBA rows
and ignores the qualifiers of the experimental seed annotations when placing an IBD
([wiki: 5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)).
GAF 2.2 also set `is_active_in` as the relation for root CC annotations
([wiki: Manager Call 2020-11-04](https://wiki.geneontology.org/index.php/Manager_Call_2020-11-04)),
while the Annotation Relations page names `located_in` as the CC default. So an IBA
`is_active_in GO:0005739` may rest entirely on `located_in` seeds from proteomics.

A reviewer should not ACCEPT an `is_active_in` row on the strength of its relation. Judge the
location; then, if the activity is not shown there, say in `reason` that the row is accepted
as a location claim only.

## Application

*Example.* In the repo's mitochondrion survey, IBA `is_active_in GO:0005739` rows on ADO and
BRAF sit beside reviews arguing that ADO's N-degron oxidation is cytosolic and that BRAF's
mitochondrial pool has no assigned activity
([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html), open question on `is_active_in`).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] GOC sets the PAINT default but has no guidance on reading it. We treat the relation on a default-emitting pipeline row as uninformative. |
| Date | 2026-11-15 |
| Evidence codes | IBA, IBD |
| GO terms | `GO:0005739` mitochondrion |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CC-3-E1](CC-3.examples.yaml): An IBA is_active_in nucleus row kept as a location claim only | Conformant | ACTL7B is_active_in GO:0005634 nucleus (IBA, GO_REF:0000033) |
| [CC-3-E2](CC-3.examples.yaml): An IBA is_active_in cytoplasm row marked over-annotated for its qualifier alone | Contested | ACTR5 is_active_in GO:0005737 cytoplasm (IBA, GO_REF:0000033) |
| [CC-17-E1](CC-17.examples.yaml): A Golgi IBA row propagated from the cholinephosphotransferase paralog (from [CC-17](CC-17.md)) | Non-conformant | CEPT1 is_active_in GO:0005794 Golgi apparatus (IBA, GO_REF:0000033) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) (CC default `located_in`) vs [Manager Call 2020-11-04](https://wiki.geneontology.org/index.php/Manager_Call_2020-11-04) and [PAINT call 2020-05-05](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call) (`is_active_in` default for root CC and IBA) | Two defaults for the same aspect | `located_in` is the default; read pipeline `is_active_in` as `located_in` until checked (CC-3) | PAINT ignores seed qualifiers, so the IBA relation carries no information about activity |

## Open questions

1. **`is_active_in` from PAINT.** Should PAINT emit `located_in` for CC IBDs whose seeds are all `located_in`? This would make CC-3 unnecessary.

## Sources

- wiki: [5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)
- wiki: [Manager Call 2020-11-04](https://wiki.geneontology.org/index.php/Manager_Call_2020-11-04)
- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)

<!-- END GENERATED -->
