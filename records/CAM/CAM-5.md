---
id: CAM-5
title: '`has input` names what the activity acts on; the ligand of a receptor is upstream, not input.'
status: proposed
topic: CAM
provenance: GOC
go_terms:
- term_id: GO:0004396
  label: hexokinase activity
- term_id: GO:0005009
  label: insulin receptor activity
sources:
- kind: wiki
  title: Has input
  url: https://wiki.geneontology.org/index.php/Has_input
- kind: drive
  title: MF guidelines for GO-CAM
  url: https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4
- kind: repo
  title: gocam-curation has-input reference
  url: https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/has-input.md
date: '2026-11-15'
---

# CAM-5. `has input` names what the activity acts on; the ligand of a receptor is upstream, not input.

## Decision

`has input` names what the activity acts on; the ligand of a receptor is upstream, not input.

## Context

Correct fillers: the substrate of an enzyme; the target gene of a
transcription factor (the gene identifier, not "DNA" or a promoter region); the
effector a receptor activates; the molecules an adaptor bridges; the molecule a
sequestering protein holds; the cargo of a transporter. A ligand `has input`
its receptor. More than one input on one node means several substrates of one
reaction; an enzyme with alternative substrates gets one node per substrate
when the distinction matters.

Do not capture: an input already stated by the term (`GO:0004396` hexokinase
activity does not need `has input` D-hexose); currency metabolites (ATP for a
kinase); cofactors and metal ions; chemical analogues or other assay
conditions; the activating molecule of an "X-dependent" activity (calcium for
a calcium-dependent kinase). Direct physical interaction need not be shown
separately; an enzyme assay implies it.

A small-molecule ligand has no MF, because chemicals are not annotated. Link
it to the receptor activity with `is small molecule activator of` (RO:0012005)
or `is small molecule inhibitor of` (RO:0012006), not as the receptor's input.

*Rationale.* Putting the ligand on the receptor's input reverses the causal
flow: the ligand acts on the receptor. The linter rule `receptor_ligand_input`
found nine such models.

## Application

*Example.* Insulin enables receptor ligand activity, `has input` INSR, and
directly positively regulates INSR `GO:0005009` insulin receptor activity,
whose own input is the downstream effector it phosphorylates, not insulin
(the insulin signalling example in the MF guidelines). For a GPCR
activated by succinate, succinate `is small molecule activator of` the
receptor activity.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0004396` hexokinase activity; `GO:0005009` insulin receptor activity |

## Sources

- wiki: [Has input](https://wiki.geneontology.org/index.php/Has_input)
- drive: [MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)
- repo: [gocam-curation has-input reference](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/has-input.md)

<!-- END GENERATED -->
