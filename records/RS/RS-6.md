---
id: RS-6
title: A signalling pathway runs from ligand–receptor engagement to the last effector; annotate its members,
  not its targets
status: proposed
topic: RS
provenance: GOC
provenance_note: '[GOC]. The Signaling Curation Manual is flagged as under construction (2018) and cites
  some obsolete terms; its boundary rules are the part we adopt.'
aspects:
- P
go_terms:
- term_id: GO:0007165
  label: signal transduction
- term_id: GO:0001228
  label: DNA-binding transcription activator activity, RNA polymerase II-specific
- term_id: GO:0007173
  label: epidermal growth factor receptor signaling pathway
- term_id: GO:0045944
  label: positive regulation of transcription by RNA polymerase II
- term_id: GO:0008286
  label: insulin receptor signaling pathway
- term_id: GO:2000767
  label: positive regulation of cytoplasmic translation
differences:
- prior_source: '[Drive: Kimberly & Pascale minutes](https://drive.google.com/open?id=1PTb0-s9LE8IhsStqhdc25Hb5prdlxBGWbOr8oLfIWNA)
    vs [Drive: Breakout use cases, 2022](https://drive.google.com/open?id=1nSVZ-LoPOnnWf_2e9ZOLAxbBjnTT9QKVq_Vb0448yGw)'
  prior_said: 'Minutes (GO-CAM standardisation): curators would not annotate +/- regulation of transcription,
    only the "larger" BP. FlyBase: the pathway TF is `involved_in` both the pathway and positive regulation
    of transcription by RNA Pol II.'
  we_recommend: 'For standard annotation of a pathway''s terminal TF, follow FlyBase: pathway term plus
    the regulation-of-transcription term, with `has_input` the targets (RS-6). The GO-CAM convention is
    left to [gocam-modeling.md](../CAM/README.md).'
  why: The two sources address different products. In a GAF, the transcription term is the only place
    the TF's regulatory role appears.
sources:
- kind: wiki
  title: Signaling Curation Manual
  url: https://wiki.geneontology.org/index.php/Signaling_Curation_Manual
- kind: drive
  title: Intracellular signaling guidelines
  url: https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4
- kind: drive
  title: FlyBase pathway curation guide
  url: https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI
- kind: wiki
  title: 2017 Cambridge GOC Signalling Workshop
  url: https://wiki.geneontology.org/index.php/2017_Cambridge_GOC_Signalling_Workshop
- kind: drive
  title: Breakout use cases, 2022
  url: https://drive.google.com/open?id=1nSVZ-LoPOnnWf_2e9ZOLAxbBjnTT9QKVq_Vb0448yGw
date: '2026-11-15'
---

# RS-6. A signalling pathway runs from ligand–receptor engagement to the last effector; annotate its members, not its targets

## Decision

**Statement.** Annotate to a signalling pathway term:

## Context

- the ligand (for protein ligands), the receptor, co-receptors and adaptors;
- the transducers and second-messenger enzymes that relay the signal;
- the last effector that hands the signal to the downstream process. This is often a DNA-binding transcription factor, or a kinase acting on the translation or metabolic machinery.

Do not annotate to the pathway:

- target genes whose expression the pathway changes;
- the machinery of the downstream process (RNA polymerase, ribosome, glycogen synthase);
- general factors that every pathway needs, such as Mediator, NuRD or ESCRT.

Avoid direct annotation to GO:0007165 signal transduction when a receptor- or ligand-specific pathway term exists.

**Rationale.** The Signaling Curation Manual sets the end of a pathway at "the transfer of information to gene products carrying out a downstream cellular process". The downstream process itself is not part of signalling. S6K is the last effector of PI3K signalling, SREBP1 is the last effector of EGFR-to-AKT signalling, and glycogen synthase is outside the pathway ([wiki: Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual)). The draft cassette guidelines add that "the very downstream targets of the pathway – such as the genes whose levels are regulated by the pathway – are not annotated to the pathway" ([Drive: Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4)). FlyBase's rules give the same boundary and exclude general chromatin and Mediator factors, and the endocytic machinery as opposed to the ubiquitin ligase that targets the receptor ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)). The 2017 Cambridge signalling workshop agreed that every signalling term should have a defined start and end ([wiki: 2017 Cambridge GOC Signalling Workshop](https://wiki.geneontology.org/index.php/2017_Cambridge_GOC_Signalling_Workshop)).

## Application

**Worked examples**, from the FlyBase pattern presented at the 2022 GOC breakout ([Drive: Breakout use cases, 2022](https://drive.google.com/open?id=1nSVZ-LoPOnnWf_2e9ZOLAxbBjnTT9QKVq_Vb0448yGw)):

- Drosophila pnt enables GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific (with `has_input` its target gene). It is `involved_in` GO:0007173 epidermal growth factor receptor signaling pathway and `involved_in` GO:0045944 positive regulation of transcription by RNA polymerase II. The ligand is not annotated to the transcription regulation term.
- Drosophila S6k is `involved_in` GO:0008286 insulin receptor signaling pathway and GO:2000767 positive regulation of cytoplasmic translation. RpS6 is not annotated to the pathway.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC]. The Signaling Curation Manual is flagged as under construction (2018) and cites some obsolete terms; its boundary rules are the part we adopt. |
| Date | 2026-11-15 |
| GO terms | `GO:0007165` signal transduction; `GO:0001228` DNA-binding transcription activator activity, RNA polymerase II-specific; `GO:0007173` epidermal growth factor receptor signaling pathway; `GO:0045944` positive regulation of transcription by RNA polymerase II; `GO:0008286` insulin receptor signaling pathway; `GO:2000767` positive regulation of cytoplasmic translation |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: Kimberly & Pascale minutes](https://drive.google.com/open?id=1PTb0-s9LE8IhsStqhdc25Hb5prdlxBGWbOr8oLfIWNA) vs [Drive: Breakout use cases, 2022](https://drive.google.com/open?id=1nSVZ-LoPOnnWf_2e9ZOLAxbBjnTT9QKVq_Vb0448yGw) | Minutes (GO-CAM standardisation): curators would not annotate +/- regulation of transcription, only the "larger" BP. FlyBase: the pathway TF is `involved_in` both the pathway and positive regulation of transcription by RNA Pol II. | For standard annotation of a pathway's terminal TF, follow FlyBase: pathway term plus the regulation-of-transcription term, with `has_input` the targets (RS-6). The GO-CAM convention is left to [gocam-modeling.md](../CAM/README.md). | The two sources address different products. In a GAF, the transcription term is the only place the TF's regulatory role appears. |

## Sources

- wiki: [Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual)
- drive: [Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4)
- drive: [FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)
- wiki: [2017 Cambridge GOC Signalling Workshop](https://wiki.geneontology.org/index.php/2017_Cambridge_GOC_Signalling_Workshop)
- drive: [Breakout use cases, 2022](https://drive.google.com/open?id=1nSVZ-LoPOnnWf_2e9ZOLAxbBjnTT9QKVq_Vb0448yGw)

<!-- END GENERATED -->
