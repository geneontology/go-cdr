---
id: ONT-2
title: Establish a term's state against a named release, from two independent services
status: proposed
topic: ONT
provenance: NEW
go_terms:
- term_id: GO:0061753
  label: substrate localization to autophagosome
- term_id: GO:0140355
  label: cargo receptor ligand activity
sources:
- kind: repo
  title: action consistency
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md
- kind: web
  title: CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.html
- kind: repo
  title: ontology changes
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md
date: '2026-11-15'
---

# ONT-2. Establish a term's state against a named release, from two independent services

## Decision

When obsoletion, merging or childlessness is load-bearing for a decision, check it in two
independent services (for example OLS or the GO API, and the release file or local build your
validation uses), and record the date and release you checked.

## Context

Services disagree. QuickGO runs a snapshot ahead of the release PURL, and for a merged
identifier it can silently return the surviving term's record as "not obsolete", so a lookup
appears to confirm a term that has gone. Two endpoints of one service are one check. The
local build used for this document lists `GO:0061753` substrate localization to autophagosome
and `GO:0140355` cargo receptor ligand activity as live while GOA already treats the first
as obsolete and the second has an open obsoletion ticket
([action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md),
[CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.html)).
Two repository audits recorded terms as live after GO had retired them, both because the page
did not move when the ontology did ([ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)).

Attribute an obsoletion to the release that first carried it, and remember that negative
results from a lexical search are not evidence that no term exists: GO search is token-based,
so walk the branch before claiming a gap.

### Obsoletions and merges

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| GO terms | `GO:0061753` substrate localization to autophagosome; `GO:0140355` cargo receptor ligand activity |

## Sources

- repo: [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)
- web: [CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.html)
- repo: [ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)

<!-- END GENERATED -->
