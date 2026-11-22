---
id: ONT-14
title: An ontology gap is not a knowledge gap
status: proposed
topic: ONT
provenance: NEW
evidence_codes:
- ND
sources:
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# ONT-14. An ontology gap is not a knowledge gap

## Decision

A missing or ill-fitting GO term is an ontology gap: record it as a proposed term, a proposed
ontology change, or a suggested question. A knowledge gap is something nobody knows that only a
new experiment could resolve. Do not file one as the other.

## Context

The test is whether a wet-lab experiment would close the gap. "GO has no term for MHC-I
quality-control autophagy" is closed by an ontology editor; "which receptor delivers MHC-I to
the autophagosome" is closed by an experiment. In this repository a `knowledge_gaps` entry whose
only kind is `ONTOLOGY` or `CURATION` is not allowed; those kinds may appear only beside
`BIOLOGY`. The same separation applies to ND annotations: an ND that persists because no term
fits is `ONTOLOGY_BLOCKED`, not a true gap in knowledge ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md),
[reviewing-annotations.md](../REV/REV-12.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| Evidence codes | ND |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [ONT-14-E1](ONT-14.examples.yaml): A missing RhoA-specific GEF term filed as a knowledge gap | Non-conformant | A `knowledge_gaps` entry in the ARHGEF19 review with `gap_kind: [ONTOLOGY]`: the protein is a RhoA exchange factor, and not a Rac1 or Cdc42 one, but this "cannot be stated in a GO term". |
| [ONT-14-E2](ONT-14.examples.yaml): A missing CoQ synthome component term filed as a knowledge gap as well as a proposal | Non-conformant | A `knowledge_gaps` entry in the *C. |

## Sources

- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
