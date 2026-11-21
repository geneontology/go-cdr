---
id: EV-4
title: Use IMP when the inference rests on comparing alleles, or perturbed and unperturbed states, of
  one gene.
status: proposed
topic: EV
provenance: GOC_PLUS
provenance_note: '[GOC] [wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29);
  [GOC+] for the MF restriction.'
evidence_codes:
- IDA
- IMP
- IGI
related:
- LIT-8
sources:
- kind: issue
  title: go-annotation#1407
  url: https://github.com/geneontology/go-annotation/issues/1407
- kind: issue
  title: go-annotation#4697
  url: https://github.com/geneontology/go-annotation/issues/4697
- kind: wiki
  title: IMP
  url: https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29
date: '2026-11-15'
---

# EV-4. Use IMP when the inference rests on comparing alleles, or perturbed and unperturbed states, of one gene.

## Decision

Use IMP when the inference rests on comparing alleles, or perturbed and unperturbed states, of one gene.

## Context

IMP (ECO:0000315) covers mutations, natural variants, RNAi, morpholinos, CRISPR
alleles, antibody depletion, and inhibitors or conditions that perturb the gene
product, including overexpression when the resulting phenotype is used to infer
normal function. siRNA knockdown is IMP; the more specific ECO:0000019 (RNAi
evidence) maps to it ([go-annotation#1407](https://github.com/geneontology/go-annotation/issues/1407)).
Rescue of a mutant by the same gene strengthens the IMP; it is not IGI. Put the
allele or reagent identifier in WITH/FROM when one exists.

Two cautions apply. Gain-of-function alleles seldom reveal normal function. And
small-molecule inhibitors are only as specific as the drug: the wiki's own
example, baicalein inhibiting 12-LOX and reducing proliferation, supports at most a
non-core `acts_upstream_of_or_within` process row, because the readout is a
convergent phenotype ([from-paper-to-annotation LIT-8](../LIT/LIT-8.md)).

IMP may support an MF only with supporting molecular evidence. A loss of activity
in a knockout lysate shows the gene is necessary for the activity, not that its
product carries it; an active-site point mutant that abolishes activity in
purified protein is a different and much stronger observation (it is also IDA).
The PAINT review of TMX3 ([go-annotation#4697](https://github.com/geneontology/go-annotation/issues/4697))
records the consensus that an MF "shouldn't be MF by IMP unless there is
additional supporting evidence", and that IDA is over-used by curators who are
persuaded by a paper whatever its method.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] [wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29); [GOC+] for the MF restriction. |
| Date | 2026-11-15 |
| Related | [LIT-8](../LIT/LIT-8.md) |
| Evidence codes | IDA, IMP, IGI |

## Sources

- issue: [go-annotation#1407](https://github.com/geneontology/go-annotation/issues/1407)
- issue: [go-annotation#4697](https://github.com/geneontology/go-annotation/issues/4697)
- wiki: [IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29)

<!-- END GENERATED -->
