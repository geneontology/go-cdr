---
id: LIT-2
title: Let the readout's proximity to the gene product set the aspect and the depth of the term.
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC+] — the GOC phenotype guideline warns against read-outs; the proximity rule, its
  MF exclusion and the machinery test come from [ASSAY_TO_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION.html).'
go_terms:
- term_id: GO:0003700
  label: DNA-binding transcription factor activity
- term_id: GO:0003713
  label: transcription coactivator activity
- term_id: GO:0072126
  label: positive regulation of glomerular mesangial cell proliferation
- term_id: GO:0043066
  label: negative regulation of apoptotic process
sources:
- kind: web
  title: ASSAY_TO_FUNCTION rubric
  url: https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION/RUBRIC.html
- kind: web
  title: ASSAY_TO_FUNCTION/EDITS
  url: https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION/EDITS.html
- kind: web
  title: ASSAY_TO_FUNCTION
  url: https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION.html
date: '2026-11-15'
---

# LIT-2. Let the readout's proximity to the gene product set the aspect and the depth of the term.

## Decision

Let the readout's proximity to the gene product set the aspect and the depth of the term.

## Context

Classify the readout before choosing the term
([ASSAY_TO_FUNCTION rubric](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION/RUBRIC.html)):

- **Molecular readouts** measure the product's own activity: enzyme kinetics,
  in vitro kinase or ubiquitination assays, GTPase assays, electrophysiology of
  the pore-forming subunit, EMSA and ChIP for DNA binding, direct binding assays.
  They can support an MF term at the depth of what was measured.
- **Phenotypic hub readouts** report the state of a process that many inputs
  feed: ROS probes, caspase activity, viability and proliferation, autophagy
  flux, UPR reporters, calcium imaging, mitochondrial membrane potential,
  migration assays. A positive result after perturbing the gene supports at most
  a BP term ("regulation of P", "response to P") at the level the readout
  reports, defaults to non-core, and never supports a regulatory or process-like
  MF.

Two exceptions mark the boundaries. A luciferase reporter for a sequence-specific
DNA-binding transcription factor legitimately supports `GO:0003700` DNA-binding
transcription factor activity or its RNA polymerase II-specific children,
because the reporter reads that activity. The same reporter for a coregulator
that does not bind DNA does not support `GO:0003713` transcription coactivator
activity unless other evidence places the protein in the transcriptional
machinery (AIP was over-annotated this way; β-catenin and NICD were not). And a
binding or catalytic MF measured directly in the same paper is unaffected by the
paper also using hub readouts.

Promote a hub-derived process term to core only when independent evidence puts
the gene in the recognised machinery for that process: BCL2-family proteins for
apoptosis, ATG proteins for autophagy, IRE1/PERK/ATF6 for the UPR. PDGFB's
`GO:0072126` positive regulation of glomerular mesangial cell proliferation and
VEGFA's `GO:0043066` negative regulation of apoptotic process were moved to
non-core for this reason; VEGFA's endothelial proliferation, the ligand's
signature output, stayed core ([ASSAY_TO_FUNCTION/EDITS](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION/EDITS.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] — the GOC phenotype guideline warns against read-outs; the proximity rule, its MF exclusion and the machinery test come from [ASSAY_TO_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION.html). |
| Date | 2026-11-15 |
| GO terms | `GO:0003700` DNA-binding transcription factor activity; `GO:0003713` transcription coactivator activity; `GO:0072126` positive regulation of glomerular mesangial cell proliferation; `GO:0043066` negative regulation of apoptotic process |

## Sources

- web: [ASSAY_TO_FUNCTION rubric](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION/RUBRIC.html)
- web: [ASSAY_TO_FUNCTION/EDITS](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION/EDITS.html)
- web: [ASSAY_TO_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION.html)

<!-- END GENERATED -->
