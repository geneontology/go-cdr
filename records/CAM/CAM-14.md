---
id: CAM-14
title: A material-flow edge must not cross a membrane without the activity that crosses it; a regulation
  edge may join compartments only if the regulated protein moves.
status: proposed
topic: CAM
provenance: NEW
provenance_note: '[NEW]. The GOC documents say nothing about compartment adjacency; the rule comes from
  this repository''s spatial model.'
go_terms:
- term_id: GO:0004197
  label: cysteine-type endopeptidase activity
- term_id: GO:0005829
  label: cytosol
- term_id: GO:0005125
  label: cytokine activity
- term_id: GO:0005576
  label: extracellular region
- term_id: GO:0022829
  label: wide pore channel activity
differences:
- prior_source: None (GOC documents silent)
  prior_said: No rule about compartments joined by an edge.
  we_recommend: Material-flow edges may not skip a membrane; direct regulation may join compartments only
    if the target moves (CAM-14).
  why: The repo compartment model found 54 unexplained direct edges, mostly missing transporters.
sources:
- kind: web
  title: GOCAM_COMPARTMENTS
  url: https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html
- kind: repo
  title: gocam_lint, compartment topology
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/gocam_lint.md
date: '2026-11-15'
---

# CAM-14. A material-flow edge must not cross a membrane without the activity that crosses it; a regulation edge may join compartments only if the regulated protein moves.

## Decision

A material-flow edge must not cross a membrane without the activity that crosses it; a regulation edge may join compartments only if the regulated protein moves.

## Context

Classify each edge by the distance between its two locations. Two activities
in the same or adjacent compartments (sharing a boundary) can be linked
directly. For anything farther apart:

- A **material-flow edge** (`provides input for`, or a shared `has output` /
  `has input` molecule) means the molecule itself moves. Add the transporter,
  channel, translocon or secretion step, or say why it is absent.
- A **direct regulation edge** means the two proteins touch. It may join
  distant compartments only when the downstream protein is known to occupy a
  compartment next to the regulator and then moves (JAK1 touches STAT3 at the
  membrane; STAT3 then acts in the nucleus).
- A direct edge from an interior space to the exterior (cytosol to
  extracellular region) is an error unless one of these applies.

## Application

*Example.* In the IL-1β model `59cc772c00000000`, CASP1 cysteine-type
endopeptidase activity (`GO:0004197`) in `GO:0005829` cytosol directly
positively regulates IL1B `GO:0005125` cytokine activity in `GO:0005576`
extracellular region. The cleavage is direct, but the release step (gasdermin
D pore, `GO:0022829` wide pore channel activity) is missing; the model should
route the cytokine through it.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW]. The GOC documents say nothing about compartment adjacency; the rule comes from this repository's spatial model. |
| Date | 2026-11-15 |
| GO terms | `GO:0004197` cysteine-type endopeptidase activity; `GO:0005829` cytosol; `GO:0005125` cytokine activity; `GO:0005576` extracellular region; `GO:0022829` wide pore channel activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| None (GOC documents silent) | No rule about compartments joined by an edge. | Material-flow edges may not skip a membrane; direct regulation may join compartments only if the target moves (CAM-14). | The repo compartment model found 54 unexplained direct edges, mostly missing transporters. |

## Sources

- web: [GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)
- repo: [gocam_lint, compartment topology](https://github.com/ai4curation/ai-gene-review/blob/main/docs/gocam_lint.md)

<!-- END GENERATED -->
