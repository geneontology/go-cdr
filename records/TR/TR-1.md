---
id: TR-1
title: 'Classify the activity first: polymerase, GTF, dbTF, coTF, or regulator of a regulator'
status: proposed
topic: TR
provenance: GOC
aspects:
- F
- P
go_terms:
- term_id: GO:0003899
  label: DNA-directed RNA polymerase activity
- term_id: GO:0140223
  label: general transcription initiation factor activity
- term_id: GO:0016251
  label: RNA polymerase II general transcription initiation factor activity
- term_id: GO:0006366
  label: transcription by RNA polymerase II
- term_id: GO:0003700
  label: DNA-binding transcription factor activity
- term_id: GO:0000981
  label: DNA-binding transcription factor activity, RNA polymerase II-specific
- term_id: GO:0001228
  label: DNA-binding transcription activator activity, RNA polymerase II-specific
- term_id: GO:0001227
  label: DNA-binding transcription repressor activity, RNA polymerase II-specific
- term_id: GO:0004879
  label: nuclear receptor activity
- term_id: GO:0016987
  label: sigma factor activity
- term_id: GO:0003712
  label: transcription coregulator activity
- term_id: GO:0003713
  label: transcription coactivator activity
- term_id: GO:0003714
  label: transcription corepressor activity
- term_id: GO:0140416
  label: transcription regulator inhibitor activity
- term_id: GO:0140537
  label: transcription regulator activator activity
- term_id: GO:0140110
  label: transcription regulator activity
- term_id: GO:0006355
  label: regulation of DNA-templated transcription
- term_id: GO:0006351
  label: DNA-templated transcription
sources:
- kind: drive
  title: MF guidelines for GO-CAM
  url: https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4
- kind: issue
  title: go-annotation#2853
  url: https://github.com/geneontology/go-annotation/issues/2853
- kind: drive
  title: TF annotation guidelines
  url: https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs
date: '2026-11-15'
---

# TR-1. Classify the activity first: polymerase, GTF, dbTF, coTF, or regulator of a regulator

## Decision

Before choosing terms, decide which class of transcription activity the evidence shows
and use that class's terms:

## Context

| Class | MF (pick the most specific child) | BP relation |
|---|---|---|
| RNA polymerase core | `GO:0003899` DNA-directed RNA polymerase activity (catalytic-core subunits `contributes_to`) | part of transcription |
| GTF | `GO:0140223` general transcription initiation factor activity; `GO:0016251` for RNA polymerase II | part of transcription (`GO:0006366` for Pol II) |
| dbTF | `GO:0003700` DNA-binding transcription factor activity; `GO:0000981` (Pol II), `GO:0001228` activator / `GO:0001227` repressor (Pol II), `GO:0004879` nuclear receptor activity, `GO:0016987` sigma factor activity | part of regulation of transcription |
| coTF | `GO:0003712` transcription coregulator activity; `GO:0003713` coactivator / `GO:0003714` corepressor | part of regulation of transcription |
| Regulator of a transcription regulator, away from chromatin | `GO:0140416` transcription regulator inhibitor activity; `GO:0140537` transcription regulator activator activity | part of regulation of gene expression |

**A protein may have more than one class of activity when each is shown; do not assign
a second class to cover uncertainty.** Never annotate `GO:0140110` transcription
regulator activity, which is a do-not-annotate grouping term.

Rationale. The classes differ in what they act on: a dbTF's input is the target gene, a
coTF's input is the dbTF, a GTF acts at every promoter of its polymerase
([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
The ontology encodes the split: `GO:0003700` is part of `GO:0006355` regulation of
DNA-templated transcription, while `GO:0140223` is part of `GO:0006351` DNA-templated
transcription. GO:0140223's usage note: dbTFs "modulate the selection of which genes are
expressed under specific conditions, while general transcription factors are the
constitutive machinery required for transcription initiation"
([go-annotation#2853](https://github.com/geneontology/go-annotation/issues/2853)).
Dual function is allowed: the archived guideline lists "acts as a DNA-binding
transcription factor in certain contexts and as a cofactor in others" among legitimate
outcomes of a literature review.

## Application

Worked examples from the GOC workshop examples
([Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)):
GTF2H2, a TFIIH subunit, is a GTF; NKX6-3, a homeodomain protein shown by ChIP and
reporter assays to act through TAAT motifs, is a dbTF; SIN3A, recruited to the SOCS3
promoter through STAT3 and lacking a DNA-binding domain, is a corepressor, and its old
dbTF annotation was removed.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0003899` DNA-directed RNA polymerase activity; `GO:0140223` general transcription initiation factor activity; `GO:0016251` RNA polymerase II general transcription initiation factor activity; `GO:0006366` transcription by RNA polymerase II; `GO:0003700` DNA-binding transcription factor activity; `GO:0000981` DNA-binding transcription factor activity, RNA polymerase II-specific; `GO:0001228` DNA-binding transcription activator activity, RNA polymerase II-specific; `GO:0001227` DNA-binding transcription repressor activity, RNA polymerase II-specific; `GO:0004879` nuclear receptor activity; `GO:0016987` sigma factor activity; `GO:0003712` transcription coregulator activity; `GO:0003713` transcription coactivator activity; `GO:0003714` transcription corepressor activity; `GO:0140416` transcription regulator inhibitor activity; `GO:0140537` transcription regulator activator activity; `GO:0140110` transcription regulator activity; `GO:0006355` regulation of DNA-templated transcription; `GO:0006351` DNA-templated transcription |

## Sources

- drive: [MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)
- issue: [go-annotation#2853](https://github.com/geneontology/go-annotation/issues/2853)
- drive: [TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)

<!-- END GENERATED -->
