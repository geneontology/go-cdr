---
id: EV-5
title: Use IGI when the inference depends on perturbing two or more genes; put the other gene in WITH/FROM;
  annotate only the gene whose role the experiment informs.
status: proposed
topic: EV
provenance: GOC_PLUS
provenance_note: '[GOC] [wiki: IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29);
  [GOC+] for resolving the A/B contradiction.'
evidence_codes:
- IDA
- IMP
- IGI
go_terms:
- term_id: GO:1900181
  label: negative regulation of protein localization to nucleus
differences:
- prior_source: '[wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29)
    vs [wiki: IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29)'
  prior_said: 'IMP page: gene A''s mutation informing gene B is IGI; IGI page: it is IMP on A with an
    extension'
  we_recommend: A single perturbation of A never annotates B; annotate A (IMP + extension) or, if B was
    also perturbed, B by IGI (EV-5)
  why: 'The two pages contradict each other; #1327 shows curators split'
sources:
- kind: wiki
  title: IGI
  url: https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29
- kind: issue
  title: go-annotation#1327
  url: https://github.com/geneontology/go-annotation/issues/1327
date: '2026-11-15'
---

# EV-5. Use IGI when the inference depends on perturbing two or more genes; put the other gene in WITH/FROM; annotate only the gene whose role the experiment informs.

## Decision

Use IGI when the inference depends on perturbing two or more genes; put the other gene in WITH/FROM; annotate only the gene whose role the experiment informs.

## Context

IGI (ECO:0000316) covers suppression, enhancement and synthetic interactions,
co-transfection of two gene products to test their joint function, and
complementation of a mutation in one gene by expression of another, including
cross-species complementation. The deciding question is the point of reference:
one perturbation against control is IMP; the effect of a second perturbation is IGI
([wiki: IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29)).
For complementation, WITH/FROM holds the endogenous gene that was complemented,
which may be in another species (lgg-1 complementing yeast atg8Δ).

Three cases are not IGI. Rescue by the same gene is IMP. A miRNA repressing a
3′UTR reporter is IDA, because the target's expression is read without perturbing
it. A mutation in gene A that changes gene B's localisation or activity is an IMP
annotation **to gene A**, with gene B in an extension
(`transports_or_maintains_localization_of`, `has_input`).

The wiki IMP page also says that when "a mutation in gene A provides information
about gene B being annotated", IGI is used. That sentence contradicts the IGI
page, and the 2015 discussion in [go-annotation#1327](https://github.com/geneontology/go-annotation/issues/1327)
shows curators reading the two pages in opposite directions. We resolve it this
way: a single perturbation of gene A never supports an annotation to gene B.
Either gene B was also perturbed (IGI, B annotated with A in WITH/FROM) or it was
not, and then gene A is annotated (IMP with an extension naming B).

## Application

*Example.* GSK3B antagonists cause nuclear accumulation of GATA6: GSK3B gets
`GO:1900181` negative regulation of protein localization to nucleus, IMP, with
GATA6 in the extension. GATA6 gets nothing from this experiment.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] [wiki: IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29); [GOC+] for resolving the A/B contradiction. |
| Date | 2026-11-15 |
| Evidence codes | IDA, IMP, IGI |
| GO terms | `GO:1900181` negative regulation of protein localization to nucleus |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [EV-5-E1](EV-5.examples.yaml): A plant arginase annotated by IGI from complementation of yeast | Conformant | ARGAH1 enables GO:0004053 arginase activity (IGI, PMID:7770544) |
| [EV-5-E2](EV-5.examples.yaml): A Golgi organization row for SERK1 from suppression of an ARF-GAP mutant | Non-conformant | SERK1 acts_upstream_of_or_within GO:0007030 Golgi organization (IGI, PMID:20230490) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29) vs [wiki: IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29) | IMP page: gene A's mutation informing gene B is IGI; IGI page: it is IMP on A with an extension | A single perturbation of A never annotates B; annotate A (IMP + extension) or, if B was also perturbed, B by IGI (EV-5) | The two pages contradict each other; #1327 shows curators split |

## Sources

- wiki: [IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29)
- issue: [go-annotation#1327](https://github.com/geneontology/go-annotation/issues/1327)

<!-- END GENERATED -->
