---
id: ONT-13
title: In a review, propose a missing term with an NTR placeholder, never an ill-fitting id
status: proposed
topic: ONT
provenance: NEW
go_terms:
- term_id: GO:0051082
  obsolete: true
- term_id: GO:0044183
  label: protein folding chaperone
- term_id: GO:0140309
  label: unfolded protein holdase activity
- term_id: GO:7770062
  label: vesicle membrane tethering activity
related:
- ONT-1
differences:
- prior_source: This repository's earlier practice (`proposed_new_terms` with stand-in ids)
  prior_said: Core functions sometimes held an obsolete or nearly-right id while a term was missing
  we_recommend: NTR placeholder with a named proposal; no stand-in ids
  why: A wrong id is a false machine-readable claim ([ONT-13](ONT-13.md))
sources:
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: web
  title: UNFOLDED_PROTEIN_BINDING
  url: https://ai4curation.io/ai-gene-review/pages/projects/UNFOLDED_PROTEIN_BINDING.html
- kind: web
  title: VESICLE_TETHERING_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/VESICLE_TETHERING_OBSOLETION.html
date: '2026-11-15'
---

# ONT-13. In a review, propose a missing term with an NTR placeholder, never an ill-fitting id

## Decision

When a gene's core activity has no GO term, record a `proposed_new_terms` entry, point the
core function at it by name, and use `{id: NTR, label: ...}` as the replacement in any
`MODIFY`. Do not put an obsolete or nearly-right term id in a core function to fill the slot.

## Context

A wrong id says something false in a machine-readable field; an NTR placeholder says "not yet
expressible". In this repository a core function with no fitting term sets
`proposed_molecular_function` to the `proposed_name` of a top-level `proposed_new_terms` entry
and leaves `molecular_function` unset; validation checks that the names match and that the
proposal has its own support ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)). When GO creates the term, swap
its id in and drop the proposal.

## Application

*Example.* `GO:0051082` unfolded protein binding is obsolete; its comment offers `GO:0044183`
protein folding chaperone (which requires assisting folding) or `GO:0140309` (carrier-specific,
[ONT-1](ONT-1.md)). Neither fits an in-situ holdase. Reviews of small heat shock proteins record
`MODIFY` with `{id: NTR, label: holdase chaperone activity}` and a matching proposal, pending a
GO term ([UNFOLDED_PROTEIN_BINDING](https://ai4curation.io/ai-gene-review/pages/projects/UNFOLDED_PROTEIN_BINDING.html)).

*Example.* Once GO minted `GO:7770062`, the TMF1 review moved its core MF from a stand-in term
to the new id and dropped its "vesicle tethering activity" proposal
([VESICLE_TETHERING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/VESICLE_TETHERING_OBSOLETION.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| Related | [ONT-1](ONT-1.md) |
| GO terms | `GO:0051082`  (obsolete); `GO:0044183` protein folding chaperone; `GO:0140309` unfolded protein holdase activity; `GO:7770062` vesicle membrane tethering activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| This repository's earlier practice (`proposed_new_terms` with stand-in ids) | Core functions sometimes held an obsolete or nearly-right id while a term was missing | NTR placeholder with a named proposal; no stand-in ids | A wrong id is a false machine-readable claim ([ONT-13](ONT-13.md)) |

## Sources

- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- web: [UNFOLDED_PROTEIN_BINDING](https://ai4curation.io/ai-gene-review/pages/projects/UNFOLDED_PROTEIN_BINDING.html)
- web: [VESICLE_TETHERING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/VESICLE_TETHERING_OBSOLETION.html)

<!-- END GENERATED -->
