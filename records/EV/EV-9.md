---
id: EV-9
title: Treat the phylogenetic codes as a PAINT curator's node judgement; challenge the node placement,
  not the donor count.
status: proposed
topic: EV
provenance: GOC_PLUS
provenance_note: '[GOC] ([PMID:21873635](https://europepmc.org/article/MED/21873635)); [GOC+] for the
  review stance ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)).'
evidence_codes:
- IBA
- IBD
- IKR
- IRD
sources:
- kind: web
  title: IRD_EVIDENCE
  url: https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html
- kind: paper
  title: PMID:21873635
  url: https://europepmc.org/article/MED/21873635
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: web
  title: IBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html
date: '2026-11-15'
---

# EV-9. Treat the phylogenetic codes as a PAINT curator's node judgement; challenge the node placement, not the donor count.

## Decision

Treat the phylogenetic codes as a PAINT curator's node judgement; challenge the node placement, not the donor count.

## Context

IBA (ECO:0000318) rows follow mechanically from a PAINT curator's IBD
(ECO:0000319) placed on an ancestral PANTHER node after reading the family's
experimental annotations. IKR (ECO:0000320) records loss of key residues and
produces NOT rows; IRD (ECO:0000321) records rapid divergence, sits only on
internal nodes, and blocks descent without producing any gene-level NOT
([IRD_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html)). A short donor list is not weak support,
and a target that appears among the sources of its own IBA has experimental
grounding of its own; neither is circularity. Full treatment, including a 2018
GOC thread that called such rows "self-referential", is in
[phylogenetic-propagation.md](../PH/README.md).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] ([PMID:21873635](https://europepmc.org/article/MED/21873635)); [GOC+] for the review stance ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)). |
| Date | 2026-11-15 |
| Evidence codes | IBA, IBD, IKR, IRD |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [EV-9-E1](EV-9.examples.yaml): A nucleus IBA seeded by the target alone | Conformant | ADIRF is_active_in GO:0005634 nucleus (IBA, GO_REF:0000033) |
| [EV-9-E2](EV-9.examples.yaml): A ribosome binding IBA carried across a subfamily boundary | Non-conformant | orb enables GO:0043022 ribosome binding (IBA, GO_REF:0000033) |

## Sources

- web: [IRD_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html)
- paper: [PMID:21873635](https://europepmc.org/article/MED/21873635)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- web: [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)

<!-- END GENERATED -->
