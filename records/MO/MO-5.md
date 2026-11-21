---
id: MO-5
title: Give an effector its molecular function, its host target and its host location, not only a process
  term.
status: proposed
topic: MO
provenance: GOC_PLUS
go_terms:
- term_id: GO:0008061
  label: chitin binding
related:
- MO-1
sources:
- kind: web
  title: PLANT_FUNGAL_INTERACTIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/PLANT_FUNGAL_INTERACTIONS.html
date: '2026-11-15'
---

# MO-5. Give an effector its molecular function, its host target and its host location, not only a process term.

## Decision

Give an effector its molecular function, its host target and its host location, not only a process term.

## Context

An effector annotation set is complete when it has: the MF the effector
performs (a catalytic activity, an inhibitor activity, a sequestering
activity, a binding term with a specific ligand), with `has input` the host
target; a host CC term for where it acts; and the symbiont-mediated or
effector-mediated BP. A process term alone hides the mechanism and makes it
impossible to tell effectors apart.

## Application

*Example.* OspC3 (MO-1) has all four parts. In the plant-fungal reviews, the
LysM effector Slp1 lacked chitin binding (`GO:0008061`) and PWL2 had locations
only; each of the four chitin-binding proteins (ECP6, AVR4, Slp1 and the
receptors) now carries its own mechanism.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Related | [MO-1](MO-1.md) |
| GO terms | `GO:0008061` chitin binding |

## Sources

- web: [PLANT_FUNGAL_INTERACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PLANT_FUNGAL_INTERACTIONS.html)

<!-- END GENERATED -->
