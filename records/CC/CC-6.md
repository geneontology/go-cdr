---
id: CC-6
title: 'A root organelle term is informative: never `TOO_GENERAL`, and never `MODIFY` it to a sub-compartment.'
status: proposed
topic: CC
provenance: NEW
aspects:
- C
evidence_codes:
- EXP
- IDA
- IMP
- HTP
- HDA
go_terms:
- term_id: GO:0005739
  label: mitochondrion
- term_id: GO:0005783
  label: endoplasmic reticulum
- term_id: GO:0005794
  label: Golgi apparatus
- term_id: GO:0005777
  label: peroxisome
- term_id: GO:0005764
  label: lysosome
- term_id: GO:0016020
  label: membrane
related:
- CC-10
- CC-16
sources:
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# CC-6. A root organelle term is informative: never `TOO_GENERAL`, and never `MODIFY` it to a sub-compartment.

## Decision

A root organelle term is informative: never `TOO_GENERAL`, and never `MODIFY` it to a sub-compartment.

## Context

This rule covers `GO:0005739` mitochondrion, `GO:0005783` endoplasmic reticulum, `GO:0005794`
Golgi apparatus, `GO:0005777` peroxisome and `GO:0005764` lysosome. Every protein in a
membrane-bounded organelle sits in a membrane or a lumen, but "in the mitochondrion" is still a
real claim, and many assays (organelle proteomics, whole-organelle co-staining, GFP-fusion
screens) cannot resolve further. Direct evidence (IDA, EXP, HDA, HTP, IMP) from such an assay
is `ACCEPT`, or `KEEP_AS_NON_CORE` if the location is peripheral to the function. The
exception to the general "correct but general is `MODIFY`" rule
([reviewing-annotations.md](../REV/README.md)) applies to these five terms only. A
generic term such as `GO:0016020` membrane is not a root organelle term and is still refined
(CC-10).

## Application

*Example.* In the repo's 2026-10 survey, 1,576 of 2,134 mitochondrion rows on genes that also
had a sub-compartment were `ACCEPT`, and no review had used `TOO_GENERAL` on a root organelle
row ([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)).

The nucleus, the series organelles (endosome, vacuole, autophagosome) and plastids are not yet
covered; for the nucleus see CC-16.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| Related | [CC-10](CC-10.md), [CC-16](CC-16.md) |
| Evidence codes | EXP, IDA, IMP, HTP, HDA |
| GO terms | `GO:0005739` mitochondrion; `GO:0005783` endoplasmic reticulum; `GO:0005794` Golgi apparatus; `GO:0005777` peroxisome; `GO:0005764` lysosome; `GO:0016020` membrane |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CC-6-E1](CC-6.examples.yaml): A MitoCoP mitochondrion row accepted although the matrix is known | Conformant | DARS2 located_in GO:0005739 mitochondrion (HTP, PMID:34800366) |
| [CC-6-E2](CC-6.examples.yaml): An HPA Golgi apparatus row refined to cisternae by MODIFY | Non-conformant | The HID1 review's `MODIFY` of the Human Protein Atlas IDA row `GO:0005794` Golgi apparatus (GO_REF:0000052) to Golgi trans cisterna, Golgi medial cisterna and trans-Golgi network membrane, terms the gene already carries from higher-resolution studies. |
| [CC-7-E1](CC-7.examples.yaml): An IBA mitochondrion row kept after checking its PAINT seed (from [CC-7](CC-7.md)) | Conformant | AARS2 is_active_in GO:0005739 mitochondrion (IBA, GO_REF:0000033) |
| [CC-8-E2](CC-8.examples.yaml): An HDA mitochondrion row replaced by the inner-membrane term (from [CC-8](CC-8.md)) | Non-conformant | The Drosophila MCU review's `MODIFY` of an HDA `GO:0005739` mitochondrion row (PMID:25294944, organelle proteomics) to `GO:0005743` mitochondrial inner membrane, a term the gene already carries. |
| [CC-14-E1](CC-14.examples.yaml): An HPA mitochondria call on an aminoacyl-tRNA synthetase accepted at the organelle (from [CC-14](CC-14.md)) | Conformant | DARS2 located_in GO:0005739 mitochondrion (IDA, GO_REF:0000052) |

## Sources

- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
