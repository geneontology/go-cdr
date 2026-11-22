---
id: REV-9
title: Challenge an electronic or phylogenetic row by arguing with its source
status: proposed
topic: REV
provenance: GOC_PLUS
provenance_note: '[GOC+]. GOC rules on IEA age (GORULE:0000029) and IBA provenance (GORULE:0000026) govern
  the pipeline ([Drive: GO rules update 2023](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI));
  the requirement to argue with the node or mapping is ours.'
evidence_codes:
- IBA
- IEA
go_terms:
- term_id: GO:0007259
  label: cell surface receptor signaling pathway via JAK-STAT
related:
- REV-17
- ONT-17
sources:
- kind: web
  title: IBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html
- kind: web
  title: TAXON_PATHWAY_VARIANCE
  url: https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html
- kind: drive
  title: GO rules update 2023
  url: https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI
date: '2026-11-15'
---

# REV-9. Challenge an electronic or phylogenetic row by arguing with its source

## Decision

An IEA or IBA row may be removed on biological grounds, but the argument must address what
produced it: the InterPro2GO mapping and the signature's scope, the UniRule or ARBA condition
set, or the PAINT node at which the function was placed.

## Context

For an IBA, the question is whether the target sits inside the clade that inherited the
function, and whether there is target-specific evidence of loss. Donor count is not strength:
a node seeded by one well-characterized gene can be sound, and the target appearing in its own
WITH/FROM is expected, not circular ([phylogenetic-propagation.md](../PH/README.md),
[IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)). For an InterPro2GO row, ask whether the mapped term holds for every
member of the signature; if not, the defect belongs to InterPro ([REV-17](REV-17.md)).

## Application

*Example.* *C. elegans* STA-1 and STA-2 inherit `GO:0007259` cell surface receptor signaling
pathway via JAK-STAT by IBA from a STAT node that spans unikonts, but the worm has no JAK. The
rows are `REMOVE`, and the durable fix was a taxon constraint on the term, which GO added in
November 2026 ([TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html),
[ONT-17](../ONT/ONT-17.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. GOC rules on IEA age (GORULE:0000029) and IBA provenance (GORULE:0000026) govern the pipeline ([Drive: GO rules update 2023](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI)); the requirement to argue with the node or mapping is ours. |
| Date | 2026-11-15 |
| Related | [REV-17](REV-17.md), [ONT-17](../ONT/ONT-17.md) |
| Evidence codes | IBA, IEA |
| GO terms | `GO:0007259` cell surface receptor signaling pathway via JAK-STAT |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [REV-9-E1](REV-9.examples.yaml): JAK-STAT IBA on worm STA-1 removed by arguing with the node | Conformant | sta-1 involved_in GO:0007259 cell surface receptor signaling pathway via JAK-STAT (IBA, GO_REF:0000033) |
| [REV-9-E2](REV-9.examples.yaml): A photosystem I assembly IBA on PsbP1 removed without examining its PAINT seed | Non-conformant | PSBP1 involved_in GO:0048564 photosystem I assembly (IBA, GO_REF:0000033) |

## Sources

- web: [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)
- web: [TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)
- drive: [GO rules update 2023](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI)

<!-- END GENERATED -->
