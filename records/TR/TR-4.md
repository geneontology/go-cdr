---
id: TR-4
title: 'Require a genomic address: non-specific, structure-specific and modification-specific DNA binders
  are not dbTFs'
status: proposed
topic: TR
provenance: GOC
aspects:
- F
- P
go_terms:
- term_id: GO:0003680
  label: minor groove of adenine-thymine-rich DNA binding
- term_id: GO:0008327
  label: methyl-CpG binding
- term_id: GO:0032448
  label: DNA hairpin binding
- term_id: GO:0003697
  label: single-stranded DNA binding
- term_id: GO:0051880
  label: G-quadruplex DNA binding
- term_id: GO:0003713
  label: transcription coactivator activity
sources:
- kind: drive
  title: human TF catalogue talk
  url: https://drive.google.com/open?id=11wth1xVtY8S5U93KHsiklVWWaa_ORs_CkbRHLV2ewNE
- kind: issue
  title: go-annotation#3110
  url: https://github.com/geneontology/go-annotation/issues/3110
- kind: issue
  title: go-annotation#3086
  url: https://github.com/geneontology/go-annotation/issues/3086
- kind: issue
  title: go-annotation#3135
  url: https://github.com/geneontology/go-annotation/issues/3135
- kind: web
  title: TRANSCRIPTION_FACTORS
  url: https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html
date: '2026-11-15'
---

# TR-4. Require a genomic address: non-specific, structure-specific and modification-specific DNA binders are not dbTFs

## Decision

Binding that cannot select a limited set of genes does not support dbTF activity.
Annotate it with the specific binding term and, if the protein regulates transcription
through a dbTF, a coregulator term: AT-hook and other minor-groove binders
(`GO:0003680` minor groove of adenine-thymine-rich DNA binding); methyl-CpG binders
(`GO:0008327` methyl-CpG binding); hairpin and single-strand binders (`GO:0032448` DNA
hairpin binding, `GO:0003697` single-stranded DNA binding); G-quadruplex binders
(`GO:0051880` G-quadruplex DNA binding).

## Context

"All dbTFs should bind double-stranded DNA specifically. The binding will
provide a genomic address to allow condition-specific gene regulation"
([Drive: human TF catalogue talk](https://drive.google.com/open?id=11wth1xVtY8S5U93KHsiklVWWaa_ORs_CkbRHLV2ewNE)).
AT-hook proteins bind a sequence too short to address a gene and act with dbTFs
([go-annotation#3110](https://github.com/geneontology/go-annotation/issues/3110)).
MeCP2 binds methyl-CpG, so its location is specified by methylation rather than
sequence; its dbTF rows were removed in favour of methyl-CpG binding
([go-annotation#3086](https://github.com/geneontology/go-annotation/issues/3086)).
Hairpin or single-strand binding is not dbTF evidence, "we really do double strand DNA
binding for the dbTFs" ([go-annotation#3135](https://github.com/geneontology/go-annotation/issues/3135)).

## Application

Worked examples. Mouse ARID3A and ARID3B dbTF rows: `GO:0003680` plus
`GO:0003713` transcription coactivator activity where the paper supports it. NR0B1
(DAX1) hairpin binding: `GO:0032448`, coregulator rather than dbTF. Human NME2, which
binds a G-quadruplex promoter element of MYC, was kept as a non-core, non-canonical
promoter regulator rather than a dbTF ([TRANSCRIPTION_FACTORS](https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0003680` minor groove of adenine-thymine-rich DNA binding; `GO:0008327` methyl-CpG binding; `GO:0032448` DNA hairpin binding; `GO:0003697` single-stranded DNA binding; `GO:0051880` G-quadruplex DNA binding; `GO:0003713` transcription coactivator activity |

## Sources

- drive: [human TF catalogue talk](https://drive.google.com/open?id=11wth1xVtY8S5U93KHsiklVWWaa_ORs_CkbRHLV2ewNE)
- issue: [go-annotation#3110](https://github.com/geneontology/go-annotation/issues/3110)
- issue: [go-annotation#3086](https://github.com/geneontology/go-annotation/issues/3086)
- issue: [go-annotation#3135](https://github.com/geneontology/go-annotation/issues/3135)
- web: [TRANSCRIPTION_FACTORS](https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html)

<!-- END GENERATED -->
