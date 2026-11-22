---
id: LIT-11
title: Make one annotation per claim per method, each traceable to a result; do not harvest every term
  a paper touches.
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC] for one row per method; [GOC+] for the batch tests.'
evidence_codes:
- IEP
- TAS
- NAS
go_terms:
- term_id: GO:0009410
  label: response to xenobiotic stimulus
- term_id: GO:0030855
  label: epithelial cell differentiation
sources:
- kind: web
  title: IEP
  url: https://ai4curation.io/ai-gene-review/pages/projects/IEP.html
date: '2026-11-15'
---

# LIT-11. Make one annotation per claim per method, each traceable to a result; do not harvest every term a paper touches.

## Decision

Make one annotation per claim per method, each traceable to a result; do not harvest every term a paper touches.

## Context

One row records one gene product, one term, one evidence code and one reference.
If two methods in a paper support the same term, make two rows; if a result
supports a term and its regulation, consider which is the claim and make only that
one. The Tips page asks curators to "favor quality over quantity" and capture the
core function; "response to" and protein-binding terms are named as uninformative
when better terms exist.

Two batch patterns inflate annotation sets without adding information:

- **Many terms, one gene.** rat/Gstt1 carries four `response to X` terms from four
  induction papers; one `GO:0009410` response to xenobiotic stimulus says more. A
  paper that tests one perturbation under five conditions has one finding.
- **One term, many genes.** PMID:21492153 put `GO:0030855` epithelial cell
  differentiation on every protein that changed in a Caco-2 proteome; GOA has
  references producing 72 to 291 annotations each this way ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)).

In this repository, a row's support is a verbatim `supporting_text` with its
`reference_section_type` (RESULTS, a figure legend) where known. A quote from the
introduction or discussion supports TAS or NAS at most.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for one row per method; [GOC+] for the batch tests. |
| Date | 2026-11-15 |
| Evidence codes | IEP, TAS, NAS |
| GO terms | `GO:0009410` response to xenobiotic stimulus; `GO:0030855` epithelial cell differentiation |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [LIT-11-E1](LIT-11.examples.yaml): One of four response-to rows on a glutathione transferase | Non-conformant | Gstt1 involved_in GO:0010269 response to selenium ion (IEP, PMID:9331086) |
| [LIT-11-E2](LIT-11.examples.yaml): Epithelial cell differentiation from a Caco-2 differentiation proteome | Non-conformant | ACADVL involved_in GO:0030855 epithelial cell differentiation (IEP, PMID:21492153) |

## Sources

- web: [IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)

<!-- END GENERATED -->
