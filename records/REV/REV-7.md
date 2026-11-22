---
id: REV-7
title: Measured activity is not automatically function
status: proposed
topic: REV
provenance: GOC_PLUS
provenance_note: '[GOC+]. The three tiers are ours ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md),
  [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html)).'
evidence_codes:
- IDA
open_questions:
- Is there a principled cutoff for "noise-level" promiscuous activity ([REV-7](REV-7.md)), or must it
  stay a stated judgement?
sources:
- kind: issue
  title: go-annotation#1519
  url: https://github.com/geneontology/go-annotation/issues/1519
- kind: issue
  title: go-annotation#1324
  url: https://github.com/geneontology/go-annotation/issues/1324
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: web
  title: ENZYME_SPECIFICITY
  url: https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html
date: '2026-11-15'
---

# REV-7. Measured activity is not automatically function

## Decision

For an enzyme activity that was assayed but is weak or promiscuous, decide whether the
protein evolved to catalyse it: a genuine secondary activity is `KEEP_AS_NON_CORE`; real in
vitro activity of unknown relevance is `MARK_AS_OVER_ANNOTATED`; noise-level activity of a
paralog, when a dedicated enzyme for the reaction exists in the organism, is `REMOVE`, even on
an IDA row.

## Context

There is no numeric cutoff. State the judgement in the reason: what the kcat/Km or relative
rate was, what the physiological enzyme is, and whether any in vivo evidence links the gene to
the reaction. GOC precedent agrees on the principle that only physiologically relevant
reactions are annotated: EC-to-GO mappings for non-physiological reactions were removed while
the EC number was kept, and transpeptidation by gamma-glutamyltransferase was treated as an
assay artefact of a hydrolase ([go-annotation#1519](https://github.com/geneontology/go-annotation/issues/1519),
[go-annotation#1324](https://github.com/geneontology/go-annotation/issues/1324)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The three tiers are ours ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html)). |
| Date | 2026-11-15 |
| Evidence codes | IDA |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [REV-7-E1](REV-7.examples.yaml): Noise-level GAPDH activity of the E. coli paralog Epd removed despite IDA | Conformant | epd enables GO:0004365 glyceraldehyde-3-phosphate dehydrogenase (NAD+) (phosphorylating) activity (IDA, PMID:9182530) |
| [REV-7-E2](REV-7.examples.yaml): Mannose isomerase activity of YihS marked over-annotated as unknown-relevance | Conformant | yihS enables GO:0050089 mannose isomerase activity (IDA, PMID:18328504) |
| [REV-7-E3](REV-7.examples.yaml): Glucokinase mannokinase activity: kinetically near glucose, relevance unknown | Contested | GCK enables GO:0019158 mannokinase activity (EXP, PMID:7742312) |

## Open questions

1. Is there a principled cutoff for "noise-level" promiscuous activity ([REV-7](REV-7.md)), or must it stay a stated judgement?

## Sources

- issue: [go-annotation#1519](https://github.com/geneontology/go-annotation/issues/1519)
- issue: [go-annotation#1324](https://github.com/geneontology/go-annotation/issues/1324)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- web: [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html)

<!-- END GENERATED -->
