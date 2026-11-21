---
id: PH-5
title: Do not propagate binding-only, redundant, indirect or contextual terms
status: proposed
topic: PH
provenance: GOC_PLUS
provenance_note: '[GOC], with the localization clause [GOC+] (a 2025 tracker consensus, not yet in the
  written guideline).'
evidence_codes:
- IBA
- IBD
go_terms:
- term_id: GO:0005515
  label: protein binding
- term_id: GO:0042802
  label: identical protein binding
- term_id: GO:0042803
  label: protein homodimerization activity
- term_id: GO:0048254
  label: snoRNA localization
- term_id: GO:0006979
  label: response to oxidative stress
differences:
- prior_source: '[wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)'
  prior_said: Do not propagate protein binding, redundant MF/BP, indirect downstream processes.
  we_recommend: Add "response to" terms, phenotype-like localization processes and do-not-annotate terms
    (PH-5).
  why: Tracker consensus in 2018-2025 ([#2171](https://github.com/geneontology/go-annotation/issues/2171),
    [#2250](https://github.com/geneontology/go-annotation/issues/2250), [#5691](https://github.com/geneontology/go-annotation/issues/5691))
    and the 2024 do-not-annotate clean-up are not in the written guideline.
sources:
- kind: wiki
  title: PAINT annotation guidelines
  url: https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines
- kind: issue
  title: go-annotation#2097
  url: https://github.com/geneontology/go-annotation/issues/2097
- kind: issue
  title: go-annotation#2171
  url: https://github.com/geneontology/go-annotation/issues/2171
- kind: issue
  title: go-annotation#2250
  url: https://github.com/geneontology/go-annotation/issues/2250
- kind: issue
  title: go-annotation#5691
  url: https://github.com/geneontology/go-annotation/issues/5691
- kind: wiki
  title: 10 July 2024 PAINT call
  url: https://wiki.geneontology.org/index.php/10_July_2024_PAINT_Conference_Call
date: '2026-11-15'
---

# PH-5. Do not propagate binding-only, redundant, indirect or contextual terms

## Decision

Never place an IBD on: `GO:0005515` protein binding or its uninformative children such as
`GO:0042802` identical protein binding and `GO:0042803` protein homodimerization activity; a
partial MF already entailed by a placed MF (ligand binding under receptor activity, DNA
binding under a DNA-binding transcription factor activity); a one-step BP that restates a
placed MF; a downstream process the protein does not directly carry out; a "response to"
term; a localization process that reads as a mutant phenotype; any term in
`gocheck_do_not_annotate`.

## Context

the first four are in the PAINT guideline
([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines);
[go-annotation#2097](https://github.com/geneontology/go-annotation/issues/2097) for protein
binding). "Response to" terms are usually not propagated, with narrow exceptions such as
starvation for autophagy proteins ([go-annotation#2171](https://github.com/geneontology/go-annotation/issues/2171),
[go-annotation#2250](https://github.com/geneontology/go-annotation/issues/2250)). Localization
processes such as `GO:0048254` snoRNA localization, when the protein assembles the particle
and mislocalisation is the mutant readout, are phenotypes
([go-annotation#5691](https://github.com/geneontology/go-annotation/issues/5691)). PAINT
re-curated 505 families to remove do-not-annotate IBDs and now filters those terms from the
curation matrix ([wiki: 10 July 2024 PAINT call](https://wiki.geneontology.org/index.php/10_July_2024_PAINT_Conference_Call)).

## Application

Worked example: *S. pombe* sdh7 received `GO:0006979` response to oxidative stress and
regulation of gluconeogenesis by IBA from PTN000320077. The family's direct role is
mitochondrial complex II assembly; the other terms were removed from the node
([go-annotation#2171](https://github.com/geneontology/go-annotation/issues/2171)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC], with the localization clause [GOC+] (a 2025 tracker consensus, not yet in the written guideline). |
| Date | 2026-11-15 |
| Evidence codes | IBA, IBD |
| GO terms | `GO:0005515` protein binding; `GO:0042802` identical protein binding; `GO:0042803` protein homodimerization activity; `GO:0048254` snoRNA localization; `GO:0006979` response to oxidative stress |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) | Do not propagate protein binding, redundant MF/BP, indirect downstream processes. | Add "response to" terms, phenotype-like localization processes and do-not-annotate terms (PH-5). | Tracker consensus in 2018-2025 ([#2171](https://github.com/geneontology/go-annotation/issues/2171), [#2250](https://github.com/geneontology/go-annotation/issues/2250), [#5691](https://github.com/geneontology/go-annotation/issues/5691)) and the 2024 do-not-annotate clean-up are not in the written guideline. |

## Sources

- wiki: [PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)
- issue: [go-annotation#2097](https://github.com/geneontology/go-annotation/issues/2097)
- issue: [go-annotation#2171](https://github.com/geneontology/go-annotation/issues/2171)
- issue: [go-annotation#2250](https://github.com/geneontology/go-annotation/issues/2250)
- issue: [go-annotation#5691](https://github.com/geneontology/go-annotation/issues/5691)
- wiki: [10 July 2024 PAINT call](https://wiki.geneontology.org/index.php/10_July_2024_PAINT_Conference_Call)

<!-- END GENERATED -->
