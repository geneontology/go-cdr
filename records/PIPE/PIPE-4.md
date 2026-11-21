---
id: PIPE-4
title: 'Provenance: supply the complete inference chain'
status: proposed
topic: PIPE
provenance: NEW
provenance_note: '[NEW] Proposed at the GOC meeting, Cambridge 2025; not yet adopted.'
related:
- IEA-5
sources:
- kind: drive
  title: GO annotation pipeline proposed rubrics and MOU (GOC meeting, Cambridge 2025)
  url: https://docs.google.com/presentation/d/1YudLhxPskOiptyhBkUo5sN6GkMjQWB4PIdM0_dNSZkw/edit
date: '2026-11-21'
---

# PIPE-4. Provenance: supply the complete inference chain

## Decision

A pipeline supplies the complete inference chain behind each annotation, or enough information to retrieve it.

## Context

A curator who disputes an annotation must be able to see which premise was wrong.

## Application

*Examples.* All one-hop inferences. InterPro2GO: the provenance of the InterPro assignment is on the InterPro site. EC2GO for a Swiss-Prot entry, if PMIDs are supplied for the EC.

*Counter-examples.* EC2GO for a Swiss-Prot entry as currently supplied; KW2GO, where the provenance of the keyword assignment is not given; TrEMBL plus a mapping pipeline.


<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] Proposed at the GOC meeting, Cambridge 2025; not yet adopted. |
| Date | 2026-11-21 |
| Related | [IEA-5](../IEA/IEA-5.md) |

## Sources

- drive: [GO annotation pipeline proposed rubrics and MOU (GOC meeting, Cambridge 2025)](https://docs.google.com/presentation/d/1YudLhxPskOiptyhBkUo5sN6GkMjQWB4PIdM0_dNSZkw/edit)

<!-- END GENERATED -->
