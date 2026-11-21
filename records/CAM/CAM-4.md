---
id: CAM-4
title: Type each activity by the role it plays in the flow; a bare binding term is not an activity.
status: proposed
topic: CAM
provenance: GOC_PLUS
provenance_note: '[GOC] for the role table; [GOC+] for the rule that a binding term may not carry a causal
  edge.'
go_terms:
- term_id: GO:0048018
  label: receptor ligand activity
- term_id: GO:0038023
  label: signaling receptor activity
- term_id: GO:0015026
  label: coreceptor activity
- term_id: GO:0060090
  label: molecular adaptor activity
- term_id: GO:0140313
  label: molecular sequestering activity
- term_id: GO:0140311
  label: protein sequestering activity
- term_id: GO:0000981
  label: DNA-binding transcription factor activity, RNA polymerase II-specific
- term_id: GO:0001228
  label: DNA-binding transcription activator activity, RNA polymerase II-specific
- term_id: GO:0001227
  label: DNA-binding transcription repressor activity, RNA polymerase II-specific
- term_id: GO:0005515
  label: protein binding
- term_id: GO:0005488
  label: binding
related:
- CAM-9
- CAM-5
differences:
- prior_source: '[Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4),
    adaptor section'
  prior_said: The adaptor's outgoing edge is "directly positively regulates or constitutively upstream
    of"; a second example uses `provides input for`.
  we_recommend: 'All three, chosen by mechanism: control (direct regulation), required scaffold (constitutively
    upstream), enzyme brought to substrate (provides input for) (CAM-4).'
  why: The section states two options and illustrates a third; the decision rule makes the choice explicit.
- prior_source: '[wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19)'
  prior_said: Re-annotate `activated by`/`inhibited by` extensions as a binding annotation that directly
    regulates the activity; a decoy receptor "enables protein binding, directly negatively regulates receptor
    activity".
  we_recommend: Use the role term (`GO:0140311` protein sequestering activity for decoys, an activator
    or inhibitor term for direct regulators), not bare binding (CAM-4).
  why: Sequestering and regulator terms now exist; binding terms cannot carry causal meaning.
sources:
- kind: drive
  title: MF guidelines for GO-CAM (copy, reviewed 2026-03)
  url: https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4
- kind: drive
  title: GO-CAM Curation Documentation
  url: https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4
- kind: wiki
  title: Annotation Conf. Call 2019-11-19
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19
date: '2026-11-15'
---

# CAM-4. Type each activity by the role it plays in the flow; a bare binding term is not an activity.

## Decision

Type each activity by the role it plays in the flow; a bare binding term is not an activity.

## Context

The MF term must say what the gene product does to the next step. Use these
role terms, each with its standard context:

| Role | MF term | `has input` | Outgoing edge |
|---|---|---|---|
| Protein ligand | `GO:0048018` receptor ligand activity or a child | its receptor | directly positively regulates the receptor activity |
| Receptor | `GO:0038023` signaling receptor activity or a child | the effector it acts on, not the ligand | directly positively regulates the effector |
| Coreceptor | `GO:0015026` coreceptor activity | the protein it acts on | as for receptor |
| Adaptor | `GO:0060090` molecular adaptor activity or a child | the two or more molecules it brings together | directly positively regulates, or constitutively upstream of, the downstream activity; provides input for when it brings an enzyme to its substrate |
| Sequestering protein | `GO:0140313` molecular sequestering activity, usually `GO:0140311` protein sequestering activity | the sequestered molecule | directly negatively regulates the sequestered molecule's activity; BP is part of negative regulation of that molecule's process |
| DNA-binding TF | a child of `GO:0000981`, e.g. `GO:0001228` or `GO:0001227` | the target gene | indirectly positively or negatively regulates the target's activity (CAM-9) |
| Enzyme | the catalytic activity | the substrate (CAM-5) | as the mechanism requires |

A binding term (`GO:0005515` protein binding, `GO:0005488` binding) has no
causal consequence, so it cannot carry an outgoing regulatory edge with any
meaning. If the binding is the mechanism, find the role: adaptor,
sequestering, inhibitor or activator, receptor, ligand. If no role term fits,
the binding belongs in a standard annotation, not in the model. An adaptor
with a single input is a warning sign that adaptor is the wrong term.

*Rationale.* `gocam-lint` found 56 binding-MF and 521 generic-MF warnings over
2,037 cached models (November 2026). Most are activities whose role the paper
does establish.

## Application

*Example.* CAV1 enables `GO:0140311` protein sequestering activity with `has
input` TLR4, directly negatively regulates TLR4 receptor activity, and is part
of negative regulation of the TLR4 pathway (MF guidelines, 2026 revision).
TYROBP enables molecular adaptor activity, bridging the virion receptor SIGLEC1 and the downstream PTPN11, whose scaffolding activity it activates.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the role table; [GOC+] for the rule that a binding term may not carry a causal edge. |
| Date | 2026-11-15 |
| Related | [CAM-9](CAM-9.md), [CAM-5](CAM-5.md) |
| GO terms | `GO:0048018` receptor ligand activity; `GO:0038023` signaling receptor activity; `GO:0015026` coreceptor activity; `GO:0060090` molecular adaptor activity; `GO:0140313` molecular sequestering activity; `GO:0140311` protein sequestering activity; `GO:0000981` DNA-binding transcription factor activity, RNA polymerase II-specific; `GO:0001228` DNA-binding transcription activator activity, RNA polymerase II-specific; `GO:0001227` DNA-binding transcription repressor activity, RNA polymerase II-specific; `GO:0005515` protein binding; `GO:0005488` binding |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4), adaptor section | The adaptor's outgoing edge is "directly positively regulates or constitutively upstream of"; a second example uses `provides input for`. | All three, chosen by mechanism: control (direct regulation), required scaffold (constitutively upstream), enzyme brought to substrate (provides input for) (CAM-4). | The section states two options and illustrates a third; the decision rule makes the choice explicit. |
| [wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19) | Re-annotate `activated by`/`inhibited by` extensions as a binding annotation that directly regulates the activity; a decoy receptor "enables protein binding, directly negatively regulates receptor activity". | Use the role term (`GO:0140311` protein sequestering activity for decoys, an activator or inhibitor term for direct regulators), not bare binding (CAM-4). | Sequestering and regulator terms now exist; binding terms cannot carry causal meaning. |

## Sources

- drive: [MF guidelines for GO-CAM (copy, reviewed 2026-03)](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)
- drive: [GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4)
- wiki: [Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19)

<!-- END GENERATED -->
