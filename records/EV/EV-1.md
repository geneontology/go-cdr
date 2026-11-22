---
id: EV-1
title: Use the most specific experimental code; do not use EXP when IDA, IPI, IMP, IGI or IEP applies.
status: proposed
topic: EV
provenance: GOC
provenance_note: '[GOC] [wiki: EXP](https://wiki.geneontology.org/index.php/Inferred_from_Experiment_%28EXP%29).'
evidence_codes:
- EXP
- IDA
go_terms:
- term_id: GO:0003841
  label: 1-acylglycerol-3-phosphate O-acyltransferase activity
sources:
- kind: wiki
  title: EXP wiki page
  url: https://wiki.geneontology.org/index.php/Inferred_from_Experiment_%28EXP%29
- kind: paper
  title: PMID:21878620
  url: https://europepmc.org/article/MED/21878620
- kind: web
  title: MISCITATIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html
date: '2026-11-15'
---

# EV-1. Use the most specific experimental code; do not use EXP when IDA, IPI, IMP, IGI or IEP applies.

## Decision

Use the most specific experimental code; do not use EXP when IDA, IPI, IMP, IGI or IEP applies.

## Context

EXP (ECO:0000269, experimental evidence used in manual assertion) is the parent of
the five low-throughput experimental codes. The [EXP wiki page](https://wiki.geneontology.org/index.php/Inferred_from_Experiment_%28EXP%29)
asks curators to use a child code and to leave WITH/FROM empty. A bare EXP hides the
inference a reviewer most needs to see. When reviewing an EXP row, read the paper and
judge the claim as though it carried the specific code the method warrants.

## Application

*Example.* PNPLA3 carries `GO:0003841` 1-acylglycerol-3-phosphate O-acyltransferase
activity as EXP from [PMID:21878620](https://europepmc.org/article/MED/21878620),
a paper that assayed the reaction and found no activity. Reading it as "IDA, enzyme
assay" makes the defect visible: the assay is a direct test of the term and the
result was negative, so the claim is a NOT, not a positive
([MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html); review in `genes/human/PNPLA3`).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] [wiki: EXP](https://wiki.geneontology.org/index.php/Inferred_from_Experiment_%28EXP%29). |
| Date | 2026-11-15 |
| Evidence codes | EXP, IDA |
| GO terms | `GO:0003841` 1-acylglycerol-3-phosphate O-acyltransferase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [EV-1-E1](EV-1.examples.yaml): An EXP helicase row read as the enzyme assay it is | Conformant | uvrD enables GO:0043138 3'-5' DNA helicase activity (EXP, PMID:8419285) |
| [EV-1-E2](EV-1.examples.yaml): An EXP outer membrane row whose experiment shows surface accessibility | Non-conformant | omcS located_in GO:0009279 cell outer membrane (EXP, PMID:16332857) |
| [LIT-9-E2](../LIT/LIT-9.examples.yaml): A positive acyltransferase row citing the paper that found no activity (from [LIT-9](../LIT/LIT-9.md)) | Non-conformant | PNPLA3 enables GO:0003841 1-acylglycerol-3-phosphate O-acyltransferase activity (EXP, PMID:21878620) |

## Sources

- wiki: [EXP wiki page](https://wiki.geneontology.org/index.php/Inferred_from_Experiment_%28EXP%29)
- paper: [PMID:21878620](https://europepmc.org/article/MED/21878620)
- web: [MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html)

<!-- END GENERATED -->
