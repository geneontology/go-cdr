---
id: PIPE-5
title: 'Biological explainability: explain each inference in known terms'
status: proposed
topic: PIPE
provenance: NEW
provenance_note: '[NEW] Proposed at the GOC meeting, Cambridge 2025; not yet adopted.'
sources:
- kind: drive
  title: GO annotation pipeline proposed rubrics and MOU (GOC meeting, Cambridge 2025)
  url: https://docs.google.com/presentation/d/1YudLhxPskOiptyhBkUo5sN6GkMjQWB4PIdM0_dNSZkw/edit
date: '2026-11-21'
---

# PIPE-5. Biological explainability: explain each inference in known terms

## Decision

Each inference can be explained as a composition of known, named entities and terms.

## Context

An explanation in biological terms lets curators judge an annotation and lets users trust it.

## Application

*Examples.* EC2GO from a Swiss-Prot entry whose EC comes from a paper with a clear assay and a clear EC-to-GO mapping; UniRules and other biologically meaningful rules, such as homeobox plus zinc finger implies transcription factor.

*Borderline.* InterPro-N2GO: the first step embeds the sequence in an opaque vector, but the vector corresponds to a known family or domain and the mapping is explainable. A pipeline that uses a protein language model to predict DNA binding and maps that to transcription factor activity. A reasoning model distilled from an opaque protein language model. ARBA.

*Counter-example.* An end-to-end deep-learning pipeline of the CAFA5 kind.


<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] Proposed at the GOC meeting, Cambridge 2025; not yet adopted. |
| Date | 2026-11-21 |

## Sources

- drive: [GO annotation pipeline proposed rubrics and MOU (GOC meeting, Cambridge 2025)](https://docs.google.com/presentation/d/1YudLhxPskOiptyhBkUo5sN6GkMjQWB4PIdM0_dNSZkw/edit)

<!-- END GENERATED -->
