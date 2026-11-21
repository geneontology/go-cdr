---
id: LIT-14
title: Record provenance so the next reader can check the inference without rereading the paper.
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC] for AI-assisted associations; [GOC+] for the provenance fields.'
sources:
- kind: repo
  title: reference curation
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/reference_curation.md
- kind: repo
  title: source defects
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md
date: '2026-11-15'
---

# LIT-14. Record provenance so the next reader can check the inference without rereading the paper.

## Decision

Record provenance so the next reader can check the inference without rereading the paper.

## Context

For each annotation made or reviewed, record: the reference; the figure, table or
section; a verbatim quote of the result; the gene product and species assayed;
and, for inferential codes, the WITH/FROM. For each reference, record whether it
was checked (`reference_review.correctness`) and its relevance. Errors that live in
a source database go in `source_defects` with the responsible resource, so they can
be reported upstream; errors in this repository's own review are fixed in place
([reference curation](https://github.com/ai4curation/ai-gene-review/blob/main/docs/reference_curation.md);
[source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)).

AI-assisted extraction follows the same rule: the GOC accepts an association
suggested by an AI tool once a trained curator has confirmed it against the
experimental data, and it then takes the experimental code (Tips page, 2025). The
verbatim quote is how this repository shows that confirmation happened.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for AI-assisted associations; [GOC+] for the provenance fields. |
| Date | 2026-11-15 |

## Sources

- repo: [reference curation](https://github.com/ai4curation/ai-gene-review/blob/main/docs/reference_curation.md)
- repo: [source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)

<!-- END GENERATED -->
