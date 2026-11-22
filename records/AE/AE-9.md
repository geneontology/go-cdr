---
id: AE-9
title: Do not use `part_of(Y)` to rebuild a precomposed "X involved in Y" term that GO has obsoleted for
  GO-CAM.
status: proposed
topic: AE
provenance: NEW
provenance_note: '[NEW]. GOC guidance (AE-8) permits `part_of`(BP) in general. The restriction comes from
  the obsoletion comments and the repo decision.'
go_terms:
- term_id: GO:0061740
  label: protein targeting to lysosome involved in chaperone-mediated autophagy
- term_id: GO:0006622
  label: protein targeting to lysosome
- term_id: GO:0061684
  label: chaperone-mediated autophagy
related:
- AE-8
differences:
- prior_source: '[wiki: Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions)'
  prior_said: '`part_of`(BP) on an MF is the standard way to link function and process'
  we_recommend: Still allowed, but never to rebuild a precomposition GO retired for GO-CAM
  why: GO's obsoletion comments ask for a model, and `part_of`(Y) restates the retired class
sources:
- kind: web
  title: INVOLVED_IN_PRECOMPOSITION
  url: https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# AE-9. Do not use `part_of(Y)` to rebuild a precomposed "X involved in Y" term that GO has obsoleted for GO-CAM.

## Decision

Do not use `part_of(Y)` to rebuild a precomposed "X involved in Y" term that GO has obsoleted for GO-CAM.

## Context

`involved_in` X with `part_of`(Y) is exactly GO's logical definition of the retired class. GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy is defined as GO:0006622 protein targeting to lysosome `and part_of some` GO:0061684 chaperone-mediated autophagy. GO has obsoleted more than 1,200 such terms, 883 with a comment saying the term should be captured as a GO-CAM model. Writing the same class as an extension undoes the obsoletion in different syntax ([INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)).

**What to do instead.** When you MODIFY a precomposed term to its genus X, record where Y went in `review.decomposed_into` ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)): `gocam_associations` or `module_associations` when Y is a mechanism with a model, `in_core_functions` when Y is central to the gene, or `context_dropped: true` when Y is peripheral or was itself the over-annotation. The repo briefly had a `proposed_replacement_extensions` slot for X plus `part_of`(Y). It was removed on 2026-10-25 because it restated the retired class, duplicated the model link and fed nothing downstream.

**Boundary.** [AE-8](AE-8.md) still applies to an activity `part_of` a process that GO has not retired and that is an ordinary BP. The rule targets the precompositions GO itself sent to GO-CAM.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW]. GOC guidance (AE-8) permits `part_of`(BP) in general. The restriction comes from the obsoletion comments and the repo decision. |
| Date | 2026-11-15 |
| Related | [AE-8](AE-8.md) |
| GO terms | `GO:0061740` protein targeting to lysosome involved in chaperone-mediated autophagy; `GO:0006622` protein targeting to lysosome; `GO:0061684` chaperone-mediated autophagy |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [AE-9-E1](AE-9.examples.yaml): The record's own CMA example decomposed into a GO-CAM and a module, with no extension | Conformant | HSPA8 involved_in GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy (IDA, PMID:11559757) |
| [AE-9-E2](AE-9.examples.yaml): canonical Wnt signaling part_of neural crest cell differentiation, rebuilding an obsoleted term | Non-conformant | LRP6 involved_in GO:0060070 canonical Wnt signaling pathway (IMP, PMID:11029007) |
| [BP-11-E1](../BP/BP-11.examples.yaml): HSPA8 protein targeting to lysosome involved in chaperone-mediated autophagy, decomposed to a module (from [BP-11](../BP/BP-11.md)) | Non-conformant | HSPA8 involved_in GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy (IDA, PMID:11559757) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions) | `part_of`(BP) on an MF is the standard way to link function and process | Still allowed, but never to rebuild a precomposition GO retired for GO-CAM | GO's obsoletion comments ask for a model, and `part_of`(Y) restates the retired class |

## Sources

- web: [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
