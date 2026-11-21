---
id: CC-8
title: Add the sub-compartment as a separate row when at least two independent lines agree; do not substitute
  it for the root.
status: proposed
topic: CC
provenance: NEW
aspects:
- C
evidence_codes:
- IC
- IEA
go_terms:
- term_id: GO:0005759
  label: mitochondrial matrix
- term_id: GO:0005789
  label: endoplasmic reticulum membrane
- term_id: GO:0005788
  label: endoplasmic reticulum lumen
- term_id: GO:0070971
  label: endoplasmic reticulum exit site
- term_id: GO:0016020
  label: membrane
sources:
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
date: '2026-11-15'
---

# CC-8. Add the sub-compartment as a separate row when at least two independent lines agree; do not substitute it for the root.

## Decision

Add the sub-compartment as a separate row when at least two independent lines agree; do not substitute it for the root.

## Context

Lines of evidence: a predicted TM segment or tail anchor; a cleavable matrix presequence, PTS1
or PTS2; an ER signal peptide with or without a retention motif; a sub-organelle assay
(protease protection, sub-fractionation with markers, immuno-EM); a function that only makes
sense on one side (a matrix TCA enzyme, an inner-membrane carrier). With two agreeing lines,
add the matrix, membrane or lumen term as a `NEW` row (usually IC) beside the root rows, and
list the lines in `reason`. With one line, or lines that disagree, stay at the root and say why.

Keeping the root rows follows GO's own practice: DARS2 and MMUT carry `GO:0005759`
mitochondrial matrix and keep their `mitochondrion` rows. It also keeps rows on one term
consistent, so no exception to the action-consistency check is needed. The lasting fix for an
IEA root row is upstream: UniProt keyword SL-0170 (Mitochondrion matrix) maps to the matrix
term where SL-0173 (Mitochondrion) maps to the root.

For ER rows, a `NEW` `GO:0005789` endoplasmic reticulum membrane row needs a TM or tail anchor
plus an ER-specific assay on the endogenous protein; a `NEW` `GO:0005788` endoplasmic reticulum
lumen row needs a soluble signal-peptide protein shown to be retained (a KDEL-type motif, or
protease protection). `GO:0070971` endoplasmic reticulum exit site needs a marker of
transitional ER. Microsomes are not ER without an ER marker, and a "mitochondrial" fraction not
checked for an ER marker cannot separate mitochondria from mitochondria-associated membranes.

When a new sub-compartment row is added, the gene's generic `GO:0016020` membrane rows become
`MODIFY` to it, all rows on that term alike.

## Application

*Example.* The 2026-10 pilot added `NEW` IC `GO:0005759` matrix rows to AARS2, CLYBL and
MMADHC, each from a predicted presequence with no TM segment plus matrix-only substrates or
partners. None rested on a direct sub-mitochondrial assay. PYCR2 stayed at the root: its
N-terminus has been sequenced and carries no presequence, it has a cytoplasmic pool, and the
only fractionation was two-way, so there was one functional hint and nothing else
([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html), pilot note).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| Evidence codes | IC, IEA |
| GO terms | `GO:0005759` mitochondrial matrix; `GO:0005789` endoplasmic reticulum membrane; `GO:0005788` endoplasmic reticulum lumen; `GO:0070971` endoplasmic reticulum exit site; `GO:0016020` membrane |

## Sources

- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)

<!-- END GENERATED -->
