---
id: CAM-9
title: Control through gene expression is always indirect; the regulator's input is the target gene and
  its process names the mechanism.
status: proposed
topic: CAM
provenance: GOC
go_terms:
- term_id: GO:0006357
  label: regulation of transcription by RNA polymerase II
- term_id: GO:0045944
  label: positive regulation of transcription by RNA polymerase II
- term_id: GO:0005634
  label: nucleus
related:
- CAM-13
sources:
- kind: drive
  title: MF guidelines for GO-CAM, TF section
  url: https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4
- kind: drive
  title: Regulation Notes, 2020 GO-CAM Jamboree
  url: https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40
- kind: repo
  title: gocam_lint
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/gocam_lint.md
date: '2026-11-15'
---

# CAM-9. Control through gene expression is always indirect; the regulator's input is the target gene and its process names the mechanism.

## Decision

Control through gene expression is always indirect; the regulator's input is the target gene and its process names the mechanism.

## Context

A DNA-binding transcription factor, a transcription coregulator, a miRNA or a
substrate-specific splicing factor controls the amount of the downstream gene
product. Its edge to the target's activity is `indirectly positively
regulates` or `indirectly negatively regulates`, because transcription,
processing and translation lie in between. Its `has input` is the target gene,
and its `part of` process is the regulation term that names the mechanism, for
most eukaryotic TFs a child of `GO:0006357` regulation of transcription by RNA
polymerase II, such as `GO:0045944` positive regulation of transcription by RNA
polymerase II. Its location is `GO:0005634` nucleus, or better a resolvable
nuclear sub-compartment (CAM-13).

*Rationale.* A direct edge from a TF to a cytoplasmic enzyme says the TF acts
on the enzyme protein. `gocam-lint` flags these (`transcription_direct_edge`)
and the compartment check flags the ones that cross the nuclear envelope.

## Application

*Example.* Two of the six compartment-crossing ERRORs in the cached corpus are
transcriptional repressors that "directly" regulate secreted proteins
(`568b0f9600000284`, `632cf60a00000169`); both edges should be indirect.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Related | [CAM-13](CAM-13.md) |
| GO terms | `GO:0006357` regulation of transcription by RNA polymerase II; `GO:0045944` positive regulation of transcription by RNA polymerase II; `GO:0005634` nucleus |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CAM-9-E1](CAM-9.examples.yaml): ATF4 with its target gene as input and an indirect edge to the target's activity | Conformant | gomodel:66b5638000001589 |
| [CAM-9-E2](CAM-9.examples.yaml): A bacterial response regulator whose input is a protein, not its target operon | Non-conformant | gomodel:671ae02600002832 |

## Sources

- drive: [MF guidelines for GO-CAM, TF section](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)
- drive: [Regulation Notes, 2020 GO-CAM Jamboree](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)
- repo: [gocam_lint](https://github.com/ai4curation/ai-gene-review/blob/main/docs/gocam_lint.md)

<!-- END GENERATED -->
