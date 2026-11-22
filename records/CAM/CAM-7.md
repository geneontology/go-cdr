---
id: CAM-7
title: Choose the causal relation by relationship type, then sign, then directness.
status: proposed
topic: CAM
provenance: GOC_PLUS
provenance_note: '[GOC] for the tree; [GOC+] for the ban on unsigned parents (the tree offers no path
  to them; older guidance and the repository skill still name `positively regulates` RO:0002213 as the
  indirect relation).'
related:
- CAM-6
- CAM-10
- CAM-11
- CAM-8
sources:
- kind: drive
  title: New Causal Relations Decision Tree for VPE (2022-12-20)
  url: https://drive.google.com/open?id=1ODFtV2aEeUeOUDs8dupre-3hUJchLFMMu-kChPKR1Oc
- kind: drive
  title: GO-CAM modeling guidelines
  url: https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA
date: '2026-11-15'
---

# CAM-7. Choose the causal relation by relationship type, then sign, then directness.

## Decision

Choose the causal relation by relationship type, then sign, then directness.

## Context

Use the 2022 decision tree. First decide what kind of relationship holds:

| Relationship | Test | Relation(s) |
|---|---|---|
| Regulation | The upstream activity conditionally controls the downstream one. | `directly positively regulates` RO:0002629; `directly negatively regulates` RO:0002630; `indirectly positively regulates` RO:0002407; `indirectly negatively regulates` RO:0002409 |
| Provides input | The upstream activity makes a molecule the downstream one uses (CAM-6). | `provides input for` RO:0002413 |
| Constitutively upstream | The upstream activity is normally present and required, and does not control (CAM-10). | `constitutively upstream of` RO:0012009 |
| Removes input | Both act on the same input; the upstream one makes it unavailable (CAM-11). | `removes input for` RO:0012010 |
| Undetermined | Too little data to name a mechanism. | `causally upstream of, positive effect` RO:0002304; `causally upstream of, negative effect` RO:0002305 |

For regulation, then choose the sign, then directness (CAM-8). Always state a
sign when the data show one. Do not use the unsigned parents (`regulates`
RO:0002211, `positively regulates` RO:0002213, `negatively regulates`
RO:0002212, `causally upstream of` RO:0002411) in new models.

Edges read subject to object: the subject is the activity whose output changes
the other's rate. A reversed edge is QC flag `INCORRECT_DIRECTIONALITY`; a
wrong sign is `WRONG_CAUSAL_SIGN`.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the tree; [GOC+] for the ban on unsigned parents (the tree offers no path to them; older guidance and the repository skill still name `positively regulates` RO:0002213 as the indirect relation). |
| Date | 2026-11-15 |
| Related | [CAM-6](CAM-6.md), [CAM-10](CAM-10.md), [CAM-11](CAM-11.md), [CAM-8](CAM-8.md) |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CAM-7-E1](CAM-7.examples.yaml): CaMKII to STAT1 left as causally upstream, positive effect, on pharmacological evidence | Conformant | gomodel:62b4ffe300004525 |
| [CAM-7-E2](CAM-7.examples.yaml): A GAP drawn as negatively regulating the GTPase activity it stimulates | Non-conformant | gomodel:693b3c0900004859 |
| [CAM-7-E3](CAM-7.examples.yaml): A receptor-to-phosphatase regulation drawn as provides input for | Non-conformant | gomodel:68d5ebd600001504 |
| [CAM-2-E2](CAM-2.examples.yaml): One PERK phosphorylation drawn as opposite-sign edges to two eIF2alpha nodes (from [CAM-2](CAM-2.md)) | Non-conformant | gomodel:66b5638000001589 |
| [CAM-8-E2](CAM-8.examples.yaml): Protein kinase D drawn as directly activating p38 with the mechanism unknown (from [CAM-8](CAM-8.md)) | Non-conformant | gomodel:568b0f9600000284 |
| [CAM-19-E1](CAM-19.examples.yaml): A TOLLIP adaptor activity consistent with its gene review but carrying the wrong edge sign (from [CAM-19](CAM-19.md)) | Conformant | gomodel:59cc772c00000000 |

## Sources

- drive: [New Causal Relations Decision Tree for VPE (2022-12-20)](https://drive.google.com/open?id=1ODFtV2aEeUeOUDs8dupre-3hUJchLFMMu-kChPKR1Oc)
- drive: [GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)

<!-- END GENERATED -->
