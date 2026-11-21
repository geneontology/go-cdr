---
id: MO-6
title: Use a single-organism process term only for a process within the organism that encodes the gene
  product.
status: proposed
topic: MO
provenance: GOC
go_terms:
- term_id: GO:0046929
  label: negative regulation of neurotransmitter secretion
- term_id: GO:0044762
  label: symbiont-mediated suppression of host neurotransmitter secretion
sources:
- kind: issue
  title: go-annotation#4582
  url: https://github.com/geneontology/go-annotation/issues/4582
- kind: drive
  title: Multi-species terms - documentation to review
  url: https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU
date: '2026-11-15'
---

# MO-6. Use a single-organism process term only for a process within the organism that encodes the gene product.

## Decision

Use a single-organism process term only for a process within the organism that encodes the gene product.

## Context

A toxin that blocks neurotransmitter release in its victim is not annotated
to `GO:0046929` negative regulation of neurotransmitter secretion; that term
describes a process within a metazoan. Use the symbiont or venom term,
`GO:0044762` symbiont-mediated suppression of host neurotransmitter secretion.
Taxon constraints on single-organism terms are correct and should not be
relaxed to admit toxin or viral annotations.

## Application

*Example.* A botulinum neurotoxin encoded by a *Clostridium botulinum* phage
triggered a taxon violation on `GO:0046929`; the fix was the symbiont term
([go-annotation#4582](https://github.com/geneontology/go-annotation/issues/4582)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0046929` negative regulation of neurotransmitter secretion; `GO:0044762` symbiont-mediated suppression of host neurotransmitter secretion |

## Sources

- issue: [go-annotation#4582](https://github.com/geneontology/go-annotation/issues/4582)
- drive: [Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU)

<!-- END GENERATED -->
