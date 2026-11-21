---
id: AE-5
title: Use `occurs_in` for the place where an MF happens, or where *every* step of a BP happens. Choose
  a location that places the activity unambiguously, and do not restate the term.
status: proposed
topic: AE
provenance: GOC_PLUS
provenance_note: '[GOC+]. The compartment-resolution and cell-line points sharpen existing guidance using
  repo findings.'
evidence_codes:
- IDA
go_terms:
- term_id: GO:0003909
  label: DNA ligase activity
- term_id: GO:0005739
  label: mitochondrion
- term_id: GO:0050852
  label: T cell receptor signaling pathway
- term_id: GO:0000785
  label: chromatin
- term_id: GO:0000228
  label: nuclear chromosome
sources:
- kind: wiki
  title: Occurs in
  url: https://wiki.geneontology.org/index.php/Occurs_in
- kind: web
  title: GOCAM_COMPARTMENTS
  url: https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html
- kind: wiki
  title: 'Annotation Extension: Capturing cell and tissue types'
  url: https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types
- kind: wiki
  title: Is active in
  url: https://wiki.geneontology.org/index.php/Is_active_in
- kind: issue
  title: go-annotation#1487
  url: https://github.com/geneontology/go-annotation/issues/1487
date: '2026-11-15'
---

# AE-5. Use `occurs_in` for the place where an MF happens, or where *every* step of a BP happens. Choose a location that places the activity unambiguously, and do not restate the term.

## Decision

Use `occurs_in` for the place where an MF happens, or where *every* step of a BP happens. Choose a location that places the activity unambiguously, and do not restate the term.

## Context

**Rule detail.**

- MF: the compartment, cell or tissue where the activity was observed. Human LIG3 isoform 1 `enables` GO:0003909 DNA ligase activity `occurs_in`(GO:0005739 mitochondrion), IDA, PMID:24674627.
- BP: only if every MF that is part of the process occurs in that location ([wiki: Occurs in](https://wiki.geneontology.org/index.php/Occurs_in)). A signalling pathway that starts at the plasma membrane and ends in the nucleus does not `occurs_in` the nucleus.
- Do not restate the term. GO:0050852 T cell receptor signaling pathway already `occurs_in` CL:0000084 T cell in the ontology.
- Prefer a location that resolves to one compartment. GO:0000785 chromatin is not `part_of` the nucleus in GO, because prokaryotes have chromatin too, so `occurs_in` chromatin does not say "nuclear". GO:0000228 nuclear chromosome does ([GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)).
- Do not infer a cell type from an immortalised cell line. Treat the line as an experimental tool ([wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types)). A HEK293 experiment does not support `occurs_in` kidney epithelial cell.
- An `occurs_in`(GO CC) on an MF is evidence for `is_active_in` that CC, by the property chain `enables o occurs_in` ([wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in)). Make the CC annotation too. Inferences GOC-OWL drew from BP `occurs_in` turned out unreliable, because curators had written `occurs_in` where `regulates_o_occurs_in` was meant ([go-annotation#1487](https://github.com/geneontology/go-annotation/issues/1487)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The compartment-resolution and cell-line points sharpen existing guidance using repo findings. |
| Date | 2026-11-15 |
| Evidence codes | IDA |
| GO terms | `GO:0003909` DNA ligase activity; `GO:0005739` mitochondrion; `GO:0050852` T cell receptor signaling pathway; `GO:0000785` chromatin; `GO:0000228` nuclear chromosome |

## Sources

- wiki: [Occurs in](https://wiki.geneontology.org/index.php/Occurs_in)
- web: [GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)
- wiki: [Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types)
- wiki: [Is active in](https://wiki.geneontology.org/index.php/Is_active_in)
- issue: [go-annotation#1487](https://github.com/geneontology/go-annotation/issues/1487)

<!-- END GENERATED -->
