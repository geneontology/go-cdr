---
id: PH-7
title: Do not propagate a cellular component across a node whose members live in different compartments
status: proposed
topic: PH
provenance: GOC_PLUS
evidence_codes:
- IDA
- IBA
go_terms:
- term_id: GO:0005739
  label: mitochondrion
- term_id: GO:0005634
  label: nucleus
- term_id: GO:0005737
  label: cytoplasm
differences:
- prior_source: '[go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546)'
  prior_said: (tracker consensus) Not propagating a CC is right for mixed families.
  we_recommend: Formalised as PH-7, with the mutually-exclusive versus subsuming test for reviewers.
  why: Not in any written guideline; reviewers over-removed subsuming terms.
sources:
- kind: issue
  title: go-annotation#5546
  url: https://github.com/geneontology/go-annotation/issues/5546
- kind: web
  title: IBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
date: '2026-11-15'
---

# PH-7. Do not propagate a cellular component across a node whose members live in different compartments

## Decision

When paralogs with different localisations interleave below a node, place no CC on that
node. Annotate compartments only on nodes whose descendants share them, and leave mixed nodes
without a CC.

## Context

compartment is not conserved across paralogs even when the fold and reaction are.
For alanyl-tRNA synthetases, where cytosolic and mitochondrial members are mixed in the tree,
the 2024 consensus was that saying nothing is better than a wrong compartment
([go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546)). The repo
found the same leak for nucleus onto cytoplasmic PIWI proteins, plasma membrane onto
ribosome-associated Hsp70s, and mitochondrion onto cytosolic ALDH1L1
([IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html), patterns 10 and 13).

## Application

Worked example: rat ALDH1L1 receives `GO:0005739` mitochondrion by IBA. UniProt names it the
cytosolic 10-formyltetrahydrofolate dehydrogenase and it has a cytosol IDA; the mitochondrial
paralog is ALDH1L2. When reviewing a localisation IBA, place both compartments in the GO
hierarchy first: `GO:0005634` nucleus versus `GO:0005737` cytoplasm is mutually exclusive and
a valid REMOVE; `GO:0005737` cytoplasm over a mitochondrial protein is not, because
`GO:0005739` mitochondrion is `part_of` cytoplasm. Root organelle terms follow
[cellular-component.md](../CC/README.md) and [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Evidence codes | IDA, IBA |
| GO terms | `GO:0005739` mitochondrion; `GO:0005634` nucleus; `GO:0005737` cytoplasm |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [PH-7-E1](PH-7.examples.yaml): A mitochondrion IBA on cytosolic rat ALDH1L1 from a node seeded by its mitochondrial paralog | Conformant | Aldh1l1 is_active_in GO:0005739 mitochondrion (IBA, GO_REF:0000033) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546) | (tracker consensus) Not propagating a CC is right for mixed families. | Formalised as PH-7, with the mutually-exclusive versus subsuming test for reviewers. | Not in any written guideline; reviewers over-removed subsuming terms. |

## Sources

- issue: [go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546)
- web: [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)
- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)

<!-- END GENERATED -->
