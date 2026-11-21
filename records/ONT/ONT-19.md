---
id: ONT-19
title: Propose a taxon constraint only with evidence of absence and a measured payoff
status: proposed
topic: ONT
provenance: NEW
provenance_note: '[NEW], consistent with the 2021 GOC proposal.'
go_terms:
- term_id: GO:0005118
  label: sevenless binding
differences:
- prior_source: '[Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)
    (proposal)'
  prior_said: Constraints should be global evolutionary statements; curators propose local tests with
    a suggested global constraint
  we_recommend: Adopt, and require evidence of absence plus a measured payoff
  why: A proposal without counts cannot be weighed against what it would wrongly block ([ONT-19](ONT-19.md))
sources:
- kind: web
  title: TAXON_PATHWAY_VARIANCE
  url: https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html
- kind: drive
  title: Taxon constraints 2021
  url: https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c
date: '2026-11-15'
---

# ONT-19. Propose a taxon constraint only with evidence of absence and a measured payoff

## Decision

A constraint proposal must name a term that presupposes a component, cite evidence that the
component is absent from the lineage, confirm that GO does not already have the constraint
(directly or by inheritance), and list the annotations it would block and any it would block
wrongly.

## Context

"Absence of evidence" is not enough: cite a primary source stating that the genome lacks the
component, or a reproducible bioinformatics check. A process the lineage merely does
differently does not qualify. Choose the taxon by the evolutionary event, at the highest
defensible rank; GO took the JAK-STAT constraint at Nematoda rather than the *Caenorhabditis*
fallback ([TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html),
[Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)).

## Application

*Example of a proposal with a measured payoff.* `GO:0005118` sevenless binding has no
constraint, while the sevenless signaling pathway is constrained to Arthropoda. 195
InterPro2GO IEAs from one signature carry it, 172 of them on vertebrate proteins (170 in the
GPRC5 family), none of which bind sevenless. The proposal pairs `only_in` Arthropoda with a
curated rule narrowing the mapping. Less certain proposals say so: `never_in` Aves for
cerebral cortex development is flagged as debated because avian pallium homology is contested
([TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW], consistent with the 2021 GOC proposal. |
| Date | 2026-11-15 |
| GO terms | `GO:0005118` sevenless binding |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c) (proposal) | Constraints should be global evolutionary statements; curators propose local tests with a suggested global constraint | Adopt, and require evidence of absence plus a measured payoff | A proposal without counts cannot be weighed against what it would wrongly block ([ONT-19](ONT-19.md)) |

## Sources

- web: [TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)
- drive: [Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)

<!-- END GENERATED -->
