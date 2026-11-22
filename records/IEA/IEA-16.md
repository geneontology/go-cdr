---
id: IEA-16
title: Hold new prediction pipelines to the rubric before they enter GO
status: proposed
topic: IEA
provenance: GOC_PLUS
evidence_codes:
- IEA
go_terms:
- term_id: GO:0010285
  label: L,L-diaminopimelate:2-oxoglutarate transaminase activity
- term_id: GO:0062045
  label: L-lysine:pyruvate alpha-transaminase activity
- term_id: GO:0004766
  label: spermidine synthase activity
- term_id: GO:0030750
  label: putrescine N-methyltransferase activity
sources:
- kind: drive
  title: IEA WG pipelines update GOC 2026
  url: https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y
- kind: drive
  title: IEA WG Fall 2026
  url: https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I
- kind: web
  title: ARBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/ARBA_REVIEW.html
- kind: web
  title: NCBIFam
  url: https://ai4curation.io/ai-gene-review/pages/projects/NCBIFam.html
date: '2026-11-15'
---

# IEA-16. Hold new prediction pipelines to the rubric before they enter GO

## Decision

A new electronic pipeline, or a revision of an existing one, should show: one-hop provenance to a
documented source; conformance to GO rules (taxon constraints, do-not-annotate terms, correct
relations, no "regulation of" for participants); explainable individual inferences; a named
maintainer who responds to disputes; regular rebuilds; measured accuracy on held-out, not in-sample,
data; and unique value over existing sources.

## Context

these are the IEA working group's rubric criteria and its recommendation that future
pipelines demonstrate value, need and compliance ([Drive: IEA WG pipelines update GOC 2026](https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y);
[Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).
We add the in-sample caveat: rules mined from Swiss-Prot and evaluated on the same well-studied
proteins measure training-set agreement, not accuracy on the poorly curated proteomes where the
pipeline matters ([ARBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/ARBA_REVIEW.html)). Groups whose curation is mapped directly to GO
(Rhea, subcellular location) should check that their SOP aligns with GO, or annotate GO separately
([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).

## Application

Worked example: the repo's NCBIfam audit found a large apparent gain from a proposed
`TIGR03542` to `GO:0010285` L,L-diaminopimelate:2-oxoglutarate transaminase activity mapping, but both
reviewed "gaps" were plant ALD1 proteins with `GO:0062045` L-lysine:pyruvate alpha-transaminase
activity, a cross-kingdom paralog; likewise the reviewed gain for `TIGR00417` to `GO:0004766`
spermidine synthase activity was tobacco PMT1, a `GO:0030750` putrescine N-methyltransferase. Scoping
the mapping to the model's lineage removed both errors ([NCBIFam](https://ai4curation.io/ai-gene-review/pages/projects/NCBIFam.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Evidence codes | IEA |
| GO terms | `GO:0010285` L,L-diaminopimelate:2-oxoglutarate transaminase activity; `GO:0062045` L-lysine:pyruvate alpha-transaminase activity; `GO:0004766` spermidine synthase activity; `GO:0030750` putrescine N-methyltransferase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-16-E1](IEA-16.examples.yaml): A proposed NCBIfam mapping whose reviewed gains were checked one by one | Conformant | ncbifam2go (proposed) |
| [IEA-16-E2](IEA-16.examples.yaml): A specific dGTPase mapping proposed for a substrate-heterogeneous family | Non-conformant | ncbifam2go (proposed) |
| [PIPE-7-E1](../PIPE/PIPE-7.examples.yaml): ARBA's training-set agreement read as a benchmark (from [PIPE-7](../PIPE/PIPE-7.md)) | Contested | ARBA |

## Sources

- drive: [IEA WG pipelines update GOC 2026](https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y)
- drive: [IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)
- web: [ARBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/ARBA_REVIEW.html)
- web: [NCBIFam](https://ai4curation.io/ai-gene-review/pages/projects/NCBIFam.html)

<!-- END GENERATED -->
