---
id: CAM-18
title: In pathway imports, the enabler is the active unit, not the catalyst entity as drawn.
status: proposed
topic: CAM
provenance: GOC_PLUS
sources:
- kind: drive
  title: Complex active units notes, 2025-07
  url: https://drive.google.com/open?id=19GdhwjKWXGzkxBIL0eVxrdDvgzunW542DGkbD9W-1c8
- kind: drive
  title: molecular binding cleanup notes
  url: https://drive.google.com/open?id=1ns86kSOMZsL84SLFQ60Bobl3t-0WNDa59oAhhc-JLsI
- kind: drive
  title: Conversion rules for manuscript
  url: https://drive.google.com/open?id=1SEj8BCjKa6ZFp4xEhRlGvCAEhZjlq880
- kind: web
  title: REACTOME
  url: https://ai4curation.io/ai-gene-review/pages/projects/REACTOME.html
date: '2026-11-15'
---

# CAM-18. In pathway imports, the enabler is the active unit, not the catalyst entity as drawn.

## Decision

In pathway imports, the enabler is the active unit, not the catalyst entity as drawn.

## Context

Reactome-derived models must map each catalyst to the gene product that
performs the reaction. When Reactome's catalyst is a set or complex of
modified forms of one gene product (cleavage fragments of a caspase, for
example), the active unit is the parent gene product from which all forms
derive. Reactome binding and dissociation events are not activities; they hide
an enabler (the adaptor or regulator that organises the complex) or a
consequence (the activation the binding causes). Black-box events that
associate a TF with expression of a target map to a gene-expression process,
not to an MF.

## Application

*Example.* For Reactome complex R-HSA-350870 (caspase-3), the active unit is
CASP3 1-277, the precursor of the active fragments; fixing this repaired 42
converted reactions (2025 notes).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |

## Sources

- drive: [Complex active units notes, 2025-07](https://drive.google.com/open?id=19GdhwjKWXGzkxBIL0eVxrdDvgzunW542DGkbD9W-1c8)
- drive: [molecular binding cleanup notes](https://drive.google.com/open?id=1ns86kSOMZsL84SLFQ60Bobl3t-0WNDa59oAhhc-JLsI)
- drive: [Conversion rules for manuscript](https://drive.google.com/open?id=1SEj8BCjKa6ZFp4xEhRlGvCAEhZjlq880)
- web: [REACTOME](https://ai4curation.io/ai-gene-review/pages/projects/REACTOME.html)

<!-- END GENERATED -->
