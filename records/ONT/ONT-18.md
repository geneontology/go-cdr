---
id: ONT-18
title: A pathway named for a component does not exist where the component is absent
status: proposed
topic: ONT
provenance: GOC_PLUS
evidence_codes:
- IBA
- IRD
go_terms:
- term_id: GO:0007259
  label: cell surface receptor signaling pathway via JAK-STAT
- term_id: GO:0097696
  label: cell surface receptor signaling pathway via STAT
- term_id: GO:0046425
  label: regulation of receptor signaling pathway via JAK-STAT
- term_id: GO:0007260
  label: tyrosine phosphorylation of STAT protein
- term_id: GO:0009274
  label: peptidoglycan-based cell wall
- term_id: GO:0009505
  label: plant-type cell wall
- term_id: GO:0009277
  label: fungal-type cell wall
- term_id: GO:0005618
  label: cell wall
sources:
- kind: web
  title: TAXON_PATHWAY_VARIANCE
  url: https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html
- kind: wiki
  title: Species-Specific Terms
  url: https://wiki.geneontology.org/index.php/Species-Specific_Terms
date: '2026-11-15'
---

# ONT-18. A pathway named for a component does not exist where the component is absent

## Decision

When a lineage runs a pathway without a component that a GO term presupposes, annotate its
genes to the generic sibling that does not presuppose it, and remove inherited rows to the
component-specific term.

## Application

*Example.* *C. elegans* has two STATs and no JAK; *Dictyostelium* has four STATs and no animal
tyrosine kinases. Both inherit `GO:0007259` cell surface receptor signaling pathway via
JAK-STAT by IBA from a STAT family node at the unikont level, because the term was placed where
the STAT family arose while the pathway arose later with the JAK family. The *Dictyostelium*
statA and statC reviews `MODIFY` the row to `GO:0097696` cell surface receptor signaling pathway
via STAT, which presupposes no JAK; the worm rows are `REMOVE`. GO accepted `never_in`
Nematoda on `GO:0007259` and `GO:0046425`, and `only_in` Metazoa on `GO:0007259`, in November
2026 ([TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)).

The constraint fixed the class at once, which is why a constraint on the term is often more
durable than an IRD on each node. Note the knock-on effect: `GO:0007260` tyrosine
phosphorylation of STAT protein now inherits the Metazoa constraint through `part_of`, because
GO applied the constraint without the re-parenting under `GO:0097696` that the proposal had
listed as a prerequisite; the term is already listed for obsoletion upstream.

The same reasoning covers lineage-specific structures: GO distinguishes `GO:0009274`
peptidoglycan-based cell wall, `GO:0009505` plant-type cell wall and `GO:0009277` fungal-type
cell wall under `GO:0005618` cell wall by composition, not by taxon, and the "sensu" style of
naming is deprecated ([wiki: Species-Specific Terms](https://wiki.geneontology.org/index.php/Species-Specific_Terms)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Evidence codes | IBA, IRD |
| GO terms | `GO:0007259` cell surface receptor signaling pathway via JAK-STAT; `GO:0097696` cell surface receptor signaling pathway via STAT; `GO:0046425` regulation of receptor signaling pathway via JAK-STAT; `GO:0007260` tyrosine phosphorylation of STAT protein; `GO:0009274` peptidoglycan-based cell wall; `GO:0009505` plant-type cell wall; `GO:0009277` fungal-type cell wall; `GO:0005618` cell wall |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [ONT-18-E1](ONT-18.examples.yaml): A Dictyostelium STAT's JAK-STAT pathway row moved to the STAT-only sibling | Conformant | statC involved_in GO:0007259 cell surface receptor signaling pathway via JAK-STAT (IBA, GO_REF:0000033) |
| [ONT-18-E2](ONT-18.examples.yaml): A worm STAT's JAK-STAT pathway row removed | Conformant | sta-1 involved_in GO:0007259 cell surface receptor signaling pathway via JAK-STAT (IBA, GO_REF:0000033) |
| [PH-4-E1](../PH/PH-4.examples.yaml): A JAK-STAT pathway term inherited by a Dictyostelium STAT, moved to the STAT-only term (from [PH-4](../PH/PH-4.md)) | Conformant | statA involved_in GO:0007259 cell surface receptor signaling pathway via JAK-STAT (IBA, GO_REF:0000033) |
| [PH-14-E1](../PH/PH-14.examples.yaml): A JAK-STAT negative regulation IBA on worm GEI-17 removed, with the fix routed to the node (from [PH-14](../PH/PH-14.md)) | Conformant | gei-17 involved_in GO:0046426 negative regulation of receptor signaling pathway via JAK-STAT (IBA, GO_REF:0000033) |

## Sources

- web: [TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)
- wiki: [Species-Specific Terms](https://wiki.geneontology.org/index.php/Species-Specific_Terms)

<!-- END GENERATED -->
