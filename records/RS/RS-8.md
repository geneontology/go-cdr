---
id: RS-8
title: Protein ligands are part of the pathway they start; annotate them with receptor ligand activity,
  not receptor-specific binding terms
status: proposed
topic: RS
provenance: GOC_PLUS
provenance_note: '[GOC+]. This departs from older advice that factors limiting ligand availability regulate
  the pathway, and from PomBase''s local convention (see Differences).'
aspects:
- P
go_terms:
- term_id: GO:0048018
  label: receptor ligand activity
- term_id: GO:0005112
  label: Notch binding
- term_id: GO:0005109
  label: frizzled binding
- term_id: GO:0005113
  label: patched binding
- term_id: GO:0048495
  label: Roundabout binding
- term_id: GO:0061355
  label: Wnt protein secretion
- term_id: GO:0007225
  label: patched ligand maturation
- term_id: GO:0038109
  label: Kit signaling pathway
- term_id: GO:0005173
  label: stem cell factor receptor binding
- term_id: GO:0090263
  label: positive regulation of canonical Wnt signaling pathway
- term_id: GO:0038034
  label: signal transduction in absence of ligand
differences:
- prior_source: '[wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)'
  prior_said: '"A factor which limits or increases the availability of a ligand to a receptor should be
    annotated as regulating the ligand/receptor pathway."'
  we_recommend: Ligand biogenesis, processing and secretion go to their own terms. Only factors that specifically
    change ligand–receptor engagement (antagonists, sequestering proteins, modulating co-receptors) get
    regulation of the pathway (RS-8).
  why: FlyBase's more recent rules exclude upstream biogenesis and secretion, and dedicated terms now
    exist. The wiki page is itself flagged "to be reviewed".
sources:
- kind: issue
  title: go-annotation#1691
  url: https://github.com/geneontology/go-annotation/issues/1691
- kind: issue
  title: go-annotation#1712
  url: https://github.com/geneontology/go-annotation/issues/1712
- kind: drive
  title: Signaling receptor activity (archived; moved to MF guidelines for GO-CAM)
  url: https://drive.google.com/open?id=1dZKucnM45V05MYJUkpuf3Epje6mZRxRv3-62Y5JwAHw
- kind: web
  title: LIGANDS_IN_SIGNALING
  url: https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html
- kind: drive
  title: FlyBase pathway curation guide
  url: https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI
- kind: wiki
  title: Signaling Curation Manual
  url: https://wiki.geneontology.org/index.php/Signaling_Curation_Manual
date: '2026-11-15'
---

# RS-8. Protein ligands are part of the pathway they start; annotate them with receptor ligand activity, not receptor-specific binding terms

## Decision

**Statement.** A protein ligand that activates a receptor is annotated as follows:

## Context

- MF: GO:0048018 receptor ligand activity, or a child.
- BP: `involved_in` the pathway it initiates, not "positive regulation of" that pathway.

Receptor-specific binding terms (GO:0005112 Notch binding, GO:0005109 frizzled binding, GO:0005113 patched binding, GO:0048495 Roundabout binding) are not the ligand's MF. In review, MODIFY them to the ligand activity term when the row's evidence shows ligand action. Ligand biogenesis, processing and secretion have their own process terms (GO:0061355 Wnt protein secretion, GO:0007225 patched ligand maturation). Annotate them there, not to the pathway or its regulation. Reserve "regulation of" the pathway for extracellular factors that specifically change ligand–receptor engagement: antagonists, sequestering proteins, co-receptors acting as modulators.

**Rationale.** Since 2017, GOC has treated ligands as pathway participants ([go-annotation#1691](https://github.com/geneontology/go-annotation/issues/1691); [go-annotation#1712](https://github.com/geneontology/go-annotation/issues/1712)), and the GO-CAM signalling-receptor guideline gives ligands receptor ligand activity, `part_of` the ligand's process ([Drive: Signaling receptor activity (archived; moved to MF guidelines for GO-CAM)](https://drive.google.com/open?id=1dZKucnM45V05MYJUkpuf3Epje6mZRxRv3-62Y5JwAHw)). A survey in this repository found 23 of 24 human and all 14 fly textbook ligands annotated `involved_in` their pathway ([LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html)). In January 2026 GO changed receptor ligand activity from a kind of signaling receptor binding to a term with signaling receptor binding as a part. A ligand annotated only to "Roundabout binding" therefore no longer counts as a ligand (same page; go-ontology#31015). FlyBase keeps ligand biogenesis and secretion out of the pathway and its regulation ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)).

## Application

**Worked examples.**

- Human KITLG has no GO:0038109 Kit signaling pathway annotation. It is the one exception in the ligand survey and a real gap: GO:0005173 stem cell factor receptor binding alone does not make it a ligand in GO ([LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html)).
- A Wnt secretion factor such as Wntless belongs on GO:0061355 Wnt protein secretion, not on GO:0090263 positive regulation of canonical Wnt signaling pathway.
- Ligand withdrawal that triggers signalling (dependence receptors) is GO:0038034 signal transduction in absence of ligand or a child. The withdrawn ligand is annotated to regulation of that pathway ([wiki: Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. This departs from older advice that factors limiting ligand availability regulate the pathway, and from PomBase's local convention (see Differences). |
| Date | 2026-11-15 |
| GO terms | `GO:0048018` receptor ligand activity; `GO:0005112` Notch binding; `GO:0005109` frizzled binding; `GO:0005113` patched binding; `GO:0048495` Roundabout binding; `GO:0061355` Wnt protein secretion; `GO:0007225` patched ligand maturation; `GO:0038109` Kit signaling pathway; `GO:0005173` stem cell factor receptor binding; `GO:0090263` positive regulation of canonical Wnt signaling pathway; `GO:0038034` signal transduction in absence of ligand |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) | "A factor which limits or increases the availability of a ligand to a receptor should be annotated as regulating the ligand/receptor pathway." | Ligand biogenesis, processing and secretion go to their own terms. Only factors that specifically change ligand–receptor engagement (antagonists, sequestering proteins, modulating co-receptors) get regulation of the pathway (RS-8). | FlyBase's more recent rules exclude upstream biogenesis and secretion, and dedicated terms now exist. The wiki page is itself flagged "to be reviewed". |

## Sources

- issue: [go-annotation#1691](https://github.com/geneontology/go-annotation/issues/1691)
- issue: [go-annotation#1712](https://github.com/geneontology/go-annotation/issues/1712)
- drive: [Signaling receptor activity (archived; moved to MF guidelines for GO-CAM)](https://drive.google.com/open?id=1dZKucnM45V05MYJUkpuf3Epje6mZRxRv3-62Y5JwAHw)
- web: [LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html)
- drive: [FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)
- wiki: [Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual)

<!-- END GENERATED -->
