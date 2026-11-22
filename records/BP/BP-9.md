---
id: BP-9
title: 'Developmental processes: annotate the cell-level step, at the right grain, for genes that perform
  it'
status: proposed
topic: BP
provenance: GOC_PLUS
provenance_note: '[GOC+]. The term structure is GOC''s. Preferring cell-level terms and treating organ-level
  terms as non-core are our synthesis.'
aspects:
- P
evidence_codes:
- IEP
go_terms:
- term_id: GO:0045165
  label: cell fate commitment
- term_id: GO:0030154
  label: cell differentiation
- term_id: GO:0048663
  label: neuron fate commitment
differences:
- prior_source: '[Drive: BP refactoring 2022](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg);
    [Drive: Decomposition of macro BPs, 2023](https://drive.google.com/open?id=1q7PE8VGRGYWyohbLMwpiYpd6dnCJQVuomyzsK5dC9bc)'
  prior_said: Draft proposals to separate cell-level from organism-level development and to model macro
    processes as has-part of cell-level processes.
  we_recommend: Prefer cell-level developmental terms now; organ-level rows from phenotypes default to
    non-core (BP-9).
  why: Acts on the direction of both drafts without waiting for the ontology change.
sources:
- kind: wiki
  title: Development
  url: https://wiki.geneontology.org/index.php/Development
- kind: web
  title: NEURON_DEVELOPMENT
  url: https://ai4curation.io/ai-gene-review/pages/projects/NEURON_DEVELOPMENT.html
- kind: drive
  title: BP refactoring 2022 – developmental process
  url: https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg
- kind: drive
  title: Decomposition of macro biological processes
  url: https://drive.google.com/open?id=1q7PE8VGRGYWyohbLMwpiYpd6dnCJQVuomyzsK5dC9bc
- kind: web
  title: IEP
  url: https://ai4curation.io/ai-gene-review/pages/projects/IEP.html
date: '2026-11-15'
---

# BP-9. Developmental processes: annotate the cell-level step, at the right grain, for genes that perform it

## Decision

**Statement.** Annotate developmental processes when the gene product performs a defined step: a fate decision, a differentiation programme, a morphogenetic cell behaviour, or a signalling pathway acting in that tissue. Prefer the cell-level process (GO:0045165 cell fate commitment, GO:0030154 cell differentiation, cell-type-specific children) over organ development terms. Use the standard sub-process that matches the evidence: formation, morphogenesis, structural organization, differentiation, fate specification, determination, commitment or maturation. Organ- and organism-level development terms come from phenotypes far more often than from steps. Treat them as non-core unless the gene's activity defines that organ's development.

## Context

GO's development node has a fixed pattern. `x development` has parts: morphogenesis, which includes formation and structural organization; maturation; and differentiation of the cells that make up x. Cell differentiation has fate commitment (specification and determination) and cell development ([wiki: Development](https://wiki.geneontology.org/index.php/Development)). The pattern is precise, but the evidence for a given step often is not. Fate specification and determination differ in an assay (reversible or not in a neutral environment) that most papers do not perform ([NEURON_DEVELOPMENT](https://ai4curation.io/ai-gene-review/pages/projects/NEURON_DEVELOPMENT.html)). The 2022 BP refactoring proposal separates cell-level from organism-level development. It notes that "regulation of gross anatomical structure development" is doubtful, because regulation happens at the level of pathways and cells ([Drive: BP refactoring 2022 – developmental process](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg)). The 2023 draft on macro processes calls organ-level terms "laundry lists of genes" ([Drive: Decomposition of macro biological processes](https://drive.google.com/open?id=1q7PE8VGRGYWyohbLMwpiYpd6dnCJQVuomyzsK5dC9bc)).

## Application

**Worked examples.**

- Human NOTCH1 and ASCL1: GO:0048663 neuron fate commitment is kept as an exemplar term. Notch-mediated lateral inhibition is a genuine binary fate decision with strong experimental support ([NEURON_DEVELOPMENT](https://ai4curation.io/ai-gene-review/pages/projects/NEURON_DEVELOPMENT.html)).
- A specification term inferred from early transcriptional bias, with no test of plasticity, is over-precise. Use the commitment or differentiation parent the data support (`MODIFY`), as the NEURON_DEVELOPMENT framework recommends for glial specification rows.
- An IEP time-course in which a metabolic enzyme rises as a tissue matures, such as rat Ckmt2 in postnatal heart, does not show a role in building the tissue. `MARK_AS_OVER_ANNOTATED` ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html), pattern 2).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The term structure is GOC's. Preferring cell-level terms and treating organ-level terms as non-core are our synthesis. |
| Date | 2026-11-15 |
| Evidence codes | IEP |
| GO terms | `GO:0045165` cell fate commitment; `GO:0030154` cell differentiation; `GO:0048663` neuron fate commitment |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [BP-9-E1](BP-9.examples.yaml): ASCL1 kept in neuron fate commitment | Conformant | ASCL1 involved_in GO:0048663 neuron fate commitment (ISS, GO_REF:0000024) |
| [BP-9-E2](BP-9.examples.yaml): An IEP time-course read as a role in heart development | Non-conformant | Ckmt2 involved_in GO:0007507 heart development (IEP, PMID:8086475) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: BP refactoring 2022](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg); [Drive: Decomposition of macro BPs, 2023](https://drive.google.com/open?id=1q7PE8VGRGYWyohbLMwpiYpd6dnCJQVuomyzsK5dC9bc) | Draft proposals to separate cell-level from organism-level development and to model macro processes as has-part of cell-level processes. | Prefer cell-level developmental terms now; organ-level rows from phenotypes default to non-core (BP-9). | Acts on the direction of both drafts without waiting for the ontology change. |

## Sources

- wiki: [Development](https://wiki.geneontology.org/index.php/Development)
- web: [NEURON_DEVELOPMENT](https://ai4curation.io/ai-gene-review/pages/projects/NEURON_DEVELOPMENT.html)
- drive: [BP refactoring 2022 – developmental process](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg)
- drive: [Decomposition of macro biological processes](https://drive.google.com/open?id=1q7PE8VGRGYWyohbLMwpiYpd6dnCJQVuomyzsK5dC9bc)
- web: [IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)

<!-- END GENERATED -->
