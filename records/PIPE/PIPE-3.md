---
id: PIPE-3
title: 'Conformance: follow all GO rules'
status: proposed
topic: PIPE
provenance: NEW
provenance_note: '[NEW] Proposed at the GOC meeting, Cambridge 2025; not yet adopted.'
enforced_by:
- https://github.com/geneontology/go-site/tree/master/metadata/rules
related:
- IEA-4
sources:
- kind: drive
  title: GO annotation pipeline proposed rubrics and MOU (GOC meeting, Cambridge 2025)
  url: https://docs.google.com/presentation/d/1YudLhxPskOiptyhBkUo5sN6GkMjQWB4PIdM0_dNSZkw/edit
date: '2026-11-21'
---

# PIPE-3. Conformance: follow all GO rules

## Decision

A pipeline's output passes all GO rules, including do-not-annotate terms, taxon constraints and existing NOT annotations.

## Context

Rules violations are cheaper to prevent in the pipeline than to filter after release.

## Application

*Examples.* InterPro2GO and PAINT applying taxon constraints prospectively.


<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] Proposed at the GOC meeting, Cambridge 2025; not yet adopted. |
| Date | 2026-11-21 |
| Related | [IEA-4](../IEA/IEA-4.md) |
| Enforced by | <https://github.com/geneontology/go-site/tree/master/metadata/rules> |

## Sources

- drive: [GO annotation pipeline proposed rubrics and MOU (GOC meeting, Cambridge 2025)](https://docs.google.com/presentation/d/1YudLhxPskOiptyhBkUo5sN6GkMjQWB4PIdM0_dNSZkw/edit)

<!-- END GENERATED -->
