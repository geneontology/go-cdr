---
id: BP-7
title: Organism-level and other "high-level" processes need a mechanism
status: proposed
topic: BP
provenance: GOC_PLUS
provenance_note: '[GOC+]. The list is GOC''s. The subset and obsoletion checks, the extension requirement
  and the behaviour rubric are sharpenings.'
aspects:
- P
evidence_codes:
- IMP
go_terms:
- term_id: GO:0007610
  label: behavior
- term_id: GO:0048856
  label: anatomical structure development
- term_id: GO:0008219
  label: cell death
- term_id: GO:0040007
  label: growth
- term_id: GO:0007568
  obsolete: true
- term_id: GO:0000003
  obsolete: true
- term_id: GO:0008283
  label: cell population proliferation
- term_id: GO:0050673
  label: epithelial cell proliferation
- term_id: GO:0008284
  label: positive regulation of cell population proliferation
- term_id: GO:0007626
  label: locomotory behavior
- term_id: GO:0048512
  label: circadian behavior
related:
- BP-14
differences:
- prior_source: '[wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
    (list of high-level processes)'
  prior_said: Lists aging and reproduction among high-level processes to treat with caution.
  we_recommend: GO:0007568 aging and GO:0000003 reproduction are now obsolete; behavior, anatomical structure
    development, cell death and growth are do-not-annotate (BP-7).
  why: The ontology has changed since the 2018 review of the page.
- prior_source: '[go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204), [go-annotation#2469](https://github.com/geneontology/go-annotation/issues/2469)'
  prior_said: Proposed making cell population proliferation do-not-annotate, then a mandatory-extension
    rule. A later thread says positive regulation of cell population proliferation "is not for direct
    annotation".
  we_recommend: Neither term carries the flag. Require a cell type (child term or extension) for both
    (BP-7).
  why: The decision was never enforced in the ontology. We state the practice explicitly so reviewers
    apply it consistently.
sources:
- kind: issue
  title: go-annotation#2204
  url: https://github.com/geneontology/go-annotation/issues/2204
- kind: issue
  title: go-annotation#2469
  url: https://github.com/geneontology/go-annotation/issues/2469
- kind: wiki
  title: Annotating from phenotypes
  url: https://wiki.geneontology.org/index.php/Annotating_from_phenotypes
- kind: web
  title: BEHAVIOR
  url: https://ai4curation.io/ai-gene-review/pages/projects/BEHAVIOR.html
- kind: issue
  title: go-annotation#2820
  url: https://github.com/geneontology/go-annotation/issues/2820
date: '2026-11-15'
---

# BP-7. Organism-level and other "high-level" processes need a mechanism

## Decision

**Statement.** The following processes are reached by almost any perturbation: behaviour, development (embryonic, larval, organ), lifespan, growth, locomotion, cell proliferation, cell death, cell migration, protein localization and reproduction. Annotate a gene product to them only when the mechanism links its activity to the process. In practice that means the gene product acts in the circuit, signalling pathway or cell-level step that makes up the process. Without a mechanism, do not annotate. In review of an existing row, apply BP-14.

## Context

Term-specific constraints, checked against the current ontology:

- GO:0007610 behavior, GO:0048856 anatomical structure development, GO:0008219 cell death and GO:0040007 growth are in `gocheck_do_not_annotate`. Use a specific child or nothing.
- GO:0007568 aging and GO:0000003 reproduction are obsolete in the current release. Do not create new annotations to them.
- GO:0008283 cell population proliferation is not flagged do-not-annotate. The 2018 annotation review converged on requiring a cell-type extension rather than a flag ([go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204)). Use a cell-type-specific child, such as GO:0050673 epithelial cell proliferation, or add the cell type as an extension.
- The same reasoning covers GO:0008284 positive regulation of cell population proliferation, which a 2019 thread said should not be used directly ([go-annotation#2469](https://github.com/geneontology/go-annotation/issues/2469)). The term carries no flag, so this is practice rather than enforcement.

**Rationale.** The wiki lists these processes and strongly encourages curators not to annotate them when the mechanism is unknown ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). Behaviour is the cleanest test. In this repository's corpus, 86% of reviewer-adjudicated behaviour annotations were downgraded (197 adjudicated, September 2026). The rows accepted as core were mostly sensory receptors and channels acting in the relevant neurons, clock components and neuropeptides ([BEHAVIOR](https://ai4curation.io/ai-gene-review/pages/projects/BEHAVIOR.html)). [go-annotation#2820](https://github.com/geneontology/go-annotation/issues/2820) (open) questions human `adult behavior` annotations from autism-association papers on the same grounds.

## Application

**Worked examples.**

- Mouse Tuba1a carries five behaviour terms, all IMP, including GO:0007626 locomotory behavior. The behaviours are distal consequences of brain malformation, so all five are kept as non-core ([BEHAVIOR](https://ai4curation.io/ai-gene-review/pages/projects/BEHAVIOR.html)).
- *C. elegans* lov-1 and pkd-2 are the polycystin sensory channels of the male-mating circuit, so `mating behavior` is accepted as core. Drosophila CRY gets GO:0048512 circadian behavior because the behaviour is the clock's direct output ([BEHAVIOR](https://ai4curation.io/ai-gene-review/pages/projects/BEHAVIOR.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The list is GOC's. The subset and obsoletion checks, the extension requirement and the behaviour rubric are sharpenings. |
| Date | 2026-11-15 |
| Related | [BP-14](BP-14.md) |
| Evidence codes | IMP |
| GO terms | `GO:0007610` behavior; `GO:0048856` anatomical structure development; `GO:0008219` cell death; `GO:0040007` growth; `GO:0007568`  (obsolete); `GO:0000003`  (obsolete); `GO:0008283` cell population proliferation; `GO:0050673` epithelial cell proliferation; `GO:0008284` positive regulation of cell population proliferation; `GO:0007626` locomotory behavior; `GO:0048512` circadian behavior |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [BP-7-E1](BP-7.examples.yaml): The polycystin sensory channel LOV-1 kept in mating behavior | Conformant | lov-1 involved_in GO:0007617 mating behavior (IMP, PMID:10517638) |
| [BP-7-E2](BP-7.examples.yaml): An InterPro mapping to egg-laying behavior for a presenilin | Non-conformant | sel-12 involved_in GO:0018991 egg-laying behavior (IEA, GO_REF:0000002) |
| [BP-7-E3](BP-7.examples.yaml): HGF kept on the bare positive regulation of cell population proliferation | Contested | Hgf involved_in GO:0008284 positive regulation of cell population proliferation (TAS, PMID:12181355) |
| [BP-14-E2](BP-14.examples.yaml): Tuba1a locomotory behavior kept as a distal, non-core process (from [BP-14](BP-14.md)) | Conformant | Tuba1a involved_in GO:0007626 locomotory behavior (IMP, PMID:22101068) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) (list of high-level processes) | Lists aging and reproduction among high-level processes to treat with caution. | GO:0007568 aging and GO:0000003 reproduction are now obsolete; behavior, anatomical structure development, cell death and growth are do-not-annotate (BP-7). | The ontology has changed since the 2018 review of the page. |
| [go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204), [go-annotation#2469](https://github.com/geneontology/go-annotation/issues/2469) | Proposed making cell population proliferation do-not-annotate, then a mandatory-extension rule. A later thread says positive regulation of cell population proliferation "is not for direct annotation". | Neither term carries the flag. Require a cell type (child term or extension) for both (BP-7). | The decision was never enforced in the ontology. We state the practice explicitly so reviewers apply it consistently. |

## Sources

- issue: [go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204)
- issue: [go-annotation#2469](https://github.com/geneontology/go-annotation/issues/2469)
- wiki: [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
- web: [BEHAVIOR](https://ai4curation.io/ai-gene-review/pages/projects/BEHAVIOR.html)
- issue: [go-annotation#2820](https://github.com/geneontology/go-annotation/issues/2820)

<!-- END GENERATED -->
