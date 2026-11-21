---
id: ONT-16
title: Know what a taxon constraint says and how it propagates
status: proposed
topic: ONT
provenance: GOC
evidence_codes:
- IEA
go_terms:
- term_id: GO:0007595
  label: lactation
- term_id: GO:0046425
  label: regulation of receptor signaling pathway via JAK-STAT
- term_id: GO:0007259
  label: cell surface receptor signaling pathway via JAK-STAT
differences:
- prior_source: '[wiki: GAF Taxonomy Reasoning](https://wiki.geneontology.org/index.php/GAF_Taxonomy_Reasoning)'
  prior_said: Constraints do not propagate over `regulates` because inter-species regulation may be valid
  we_recommend: Same; therefore request constraints on regulation terms explicitly when they are needed
  why: The JAK-STAT request needed a separate constraint on the regulation term ([ONT-16](ONT-16.md))
sources:
- kind: wiki
  title: GAF Taxonomy Reasoning
  url: https://wiki.geneontology.org/index.php/GAF_Taxonomy_Reasoning
- kind: drive
  title: Taxon constraints 2021
  url: https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c
- kind: wiki
  title: Adding, Editing, Deleting Taxon Restrictions
  url: https://wiki.geneontology.org/index.php/Adding%2C_Editing%2C_Deleting_Taxon_Restrictions
- kind: web
  title: TAXON_PATHWAY_VARIANCE
  url: https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html
date: '2026-11-15'
---

# ONT-16. Know what a taxon constraint says and how it propagates

## Decision

`only_in_taxon T` means an annotation is valid only for organisms in T; `never_in_taxon T`
means it is valid everywhere except T. Constraints propagate from a term to its `is_a` and
`part_of` descendants and combine by intersection. They are not propagated over `regulates`.

## Application

*Example.* `GO:0007595` lactation is `only_in` Mammalia; an InterPro2GO IEA that gave it to a
chicken protein was flagged invalid by exactly this reasoning
([wiki: GAF Taxonomy Reasoning](https://wiki.geneontology.org/index.php/GAF_Taxonomy_Reasoning)).
An immune-response term restricted to animals, fungi and plants and a T-cell term restricted to
vertebrates combine to vertebrates for a T-cell-mediated immune response
([Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)).

Constraints also arrive from imported ontologies: a term defined by reference to an Uberon or
CL class inherits that class's constraint. Before asking for a constraint, check whether it is
already entailed; editors do this with a DL query on `'in taxon' some T`
([wiki: Adding, Editing, Deleting Taxon Restrictions](https://wiki.geneontology.org/index.php/Adding%2C_Editing%2C_Deleting_Taxon_Restrictions)).
Because propagation stops at `regulates`, a regulation term needs its own constraint: the JAK-STAT
proposal requested one on `GO:0046425` separately from `GO:0007259` for that reason
([TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)).

The 2021 proposal distinguishes global constraints (the term's evolutionary distribution) from
local ones added at a group's request, and recommends that curators propose a local test
together with the global constraint it implies
([Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | IEA |
| GO terms | `GO:0007595` lactation; `GO:0046425` regulation of receptor signaling pathway via JAK-STAT; `GO:0007259` cell surface receptor signaling pathway via JAK-STAT |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: GAF Taxonomy Reasoning](https://wiki.geneontology.org/index.php/GAF_Taxonomy_Reasoning) | Constraints do not propagate over `regulates` because inter-species regulation may be valid | Same; therefore request constraints on regulation terms explicitly when they are needed | The JAK-STAT request needed a separate constraint on the regulation term ([ONT-16](ONT-16.md)) |

## Sources

- wiki: [GAF Taxonomy Reasoning](https://wiki.geneontology.org/index.php/GAF_Taxonomy_Reasoning)
- drive: [Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)
- wiki: [Adding, Editing, Deleting Taxon Restrictions](https://wiki.geneontology.org/index.php/Adding%2C_Editing%2C_Deleting_Taxon_Restrictions)
- web: [TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)

<!-- END GENERATED -->
