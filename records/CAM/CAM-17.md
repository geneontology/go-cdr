---
id: CAM-17
title: Know the standard annotations your model will export, and review exported rows against the model.
status: proposed
topic: CAM
provenance: GOC_PLUS
provenance_note: '[GOC] for the export behaviour; [GOC+] for the review practice.'
evidence_codes:
- ND
related:
- CAM-3
- CAM-8
sources:
- kind: drive
  title: GO-CAM to GPAD and GPAD to GO-CAM (2019)
  url: https://drive.google.com/open?id=1AgkJqA4-V0HG0SaDiNO9ENTxaQC_1HwsmwyhyHhuxog
- kind: drive
  title: Standard annotations from triples specification (draft)
  url: https://drive.google.com/open?id=1UwTDxUslfXEgdn4flcz1oBNKILtz3-alX5O_bcLtgLk
- kind: drive
  title: Standard annotation GO-CAM criteria notes
  url: https://drive.google.com/open?id=1vmP4fqTl4Sc2AaCTI2OG3WuKYBBs5dhItiYC9yloees
- kind: drive
  title: 2025 GO-CAM guidelines for protein-containing complexes
  url: https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE
date: '2026-11-15'
---

# CAM-17. Know the standard annotations your model will export, and review exported rows against the model.

## Decision

Know the standard annotations your model will export, and review exported rows against the model.

## Context

The export flattens the reasoned graph. The rules that matter to curators:

| Model content | Exported row |
|---|---|
| gene product `enabled by` an MF node | GP enables MF |
| complex enabler with `has part` members | each member contributes_to MF (not yet implemented, 2025) |
| complex enabler, no `has part` | no MF row |
| MF `part of` BP | GP involved_in BP, MF context as extension |
| MF `occurs in` CC | GP is_active_in CC |
| `has input`, `occurs in` on the MF | extensions on the MF row |
| root MF with a causal edge to a BP | GP acts_upstream_of_or_within (or a signed child) BP |
| MF-to-MF causal edge | not exported as an extension; may yield an inferred MF regulator row |
| root term | exported only with ND evidence |
| do-not-annotate term | filtered |

Nested context (a BP `part of` a BP that has its own context) is not
exportable as an extension; the export keeps the primary chain only. When a
reviewed GAF row comes from a Noctua model, judge the row as you would any
other, but look at the model to see what the curator asserted; a wrong row is
often a modelling shortcut (CAM-3, CAM-8) rather than a wrong claim.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the export behaviour; [GOC+] for the review practice. |
| Date | 2026-11-15 |
| Related | [CAM-3](CAM-3.md), [CAM-8](CAM-8.md) |
| Evidence codes | ND |

## Sources

- drive: [GO-CAM to GPAD and GPAD to GO-CAM (2019)](https://drive.google.com/open?id=1AgkJqA4-V0HG0SaDiNO9ENTxaQC_1HwsmwyhyHhuxog)
- drive: [Standard annotations from triples specification (draft)](https://drive.google.com/open?id=1UwTDxUslfXEgdn4flcz1oBNKILtz3-alX5O_bcLtgLk)
- drive: [Standard annotation GO-CAM criteria notes](https://drive.google.com/open?id=1vmP4fqTl4Sc2AaCTI2OG3WuKYBBs5dhItiYC9yloees)
- drive: [2025 GO-CAM guidelines for protein-containing complexes](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE)

<!-- END GENERATED -->
