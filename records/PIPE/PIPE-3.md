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

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [PIPE-3-E1](PIPE-3.examples.yaml): A combined-pipeline row propagated from a donor set that contains a curated NOT | Non-conformant | UniProt combined automatic annotation (GO_REF:0000120) |
| [PIPE-3-E2](PIPE-3.examples.yaml): A curated rule checked against the taxon constraint of its process term | Conformant | curated rules (ai-gene-review rules/curated) |
| [IEA-11-E2](../IEA/IEA-11.examples.yaml): Viral entry inferred from a virus receptor row that contradicts its own donor (from [IEA-11](../IEA/IEA-11.md)) | Non-conformant | Hyal2 involved_in GO:0046718 symbiont entry into host cell (IEA, GO_REF:0000108) |

## Sources

- drive: [GO annotation pipeline proposed rubrics and MOU (GOC meeting, Cambridge 2025)](https://docs.google.com/presentation/d/1YudLhxPskOiptyhBkUo5sN6GkMjQWB4PIdM0_dNSZkw/edit)

<!-- END GENERATED -->
