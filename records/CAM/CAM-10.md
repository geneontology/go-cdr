---
id: CAM-10
title: Use `constitutively upstream of` for required housekeeping steps, not regulation.
status: proposed
topic: CAM
provenance: GOC
go_terms:
- term_id: GO:0019706
  label: protein-cysteine S-palmitoyltransferase activity
- term_id: GO:0003925
  label: G protein activity
sources:
- kind: wiki
  title: Constitutively upstream of
  url: https://wiki.geneontology.org/index.php/Constitutively_upstream_of
- kind: drive
  title: Regulation Notes, 2020 GO-CAM Jamboree
  url: https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40
date: '2026-11-15'
---

# CAM-10. Use `constitutively upstream of` for required housekeeping steps, not regulation.

## Decision

Use `constitutively upstream of` for required housekeeping steps, not regulation.

## Context

When an upstream activity is needed for a downstream one but runs at an
approximately constant rate and is not how the cell controls the downstream
activity, use `constitutively upstream of`. Typical cases: maturation
processing, lipid modification, folding or trafficking steps that every copy of
the downstream protein needs. An enzyme that modifies a protein as part of its
trafficking is not a regulator of that protein's activity: it acts in a
different place and does not set the amount or activity of its target.

## Application

*Example.* ZDHHC9 palmitoylates NRAS (`GO:0019706` protein-cysteine
S-palmitoyltransferase activity); palmitoylation is needed for NRAS
`GO:0003925` G protein activity at the membrane, but is not the switch, so the
edge is `constitutively upstream of` (model `635b1e3e00001677`, PMID:26493479).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0019706` protein-cysteine S-palmitoyltransferase activity; `GO:0003925` G protein activity |

## Sources

- wiki: [Constitutively upstream of](https://wiki.geneontology.org/index.php/Constitutively_upstream_of)
- drive: [Regulation Notes, 2020 GO-CAM Jamboree](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)

<!-- END GENERATED -->
