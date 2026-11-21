---
id: ONT-7
title: Migrate an obsolete term in a review with `MODIFY`, everywhere it occurs
status: proposed
topic: ONT
provenance: NEW
evidence_codes:
- IDA
- IBA
go_terms:
- term_id: GO:0030943
  obsolete: true
- term_id: GO:0140436
  label: mitochondrial signal sequence receptor activity
sources:
- kind: repo
  title: ontology changes
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: web
  title: MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.html
- kind: web
  title: INVOLVED_IN_PRECOMPOSITION
  url: https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html
date: '2026-11-15'
---

# ONT-7. Migrate an obsolete term in a review with `MODIFY`, everywhere it occurs

## Decision

In a review, an existing annotation on an obsolete term is `MODIFY` with the replacement
(when the claim is sound and only the term is wrong), `REMOVE` (when the obsolete term was
the only thing making a wrong claim look right), or `UNDECIDED`. It is never `ACCEPT`. Move
the term out of core functions, modules and notes as well, and do not rewrite the GOA-sourced
term id itself.

## Context

`ACCEPT` means the term is a core function, which contradicts its obsoletion; the
ontology-change checks flag an obsoletion request beside an `ACCEPT` on the same term
([ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)). GOA-sourced
`existing_annotations[].term.id` values are not hard-validated, precisely because GOA lags or
leads the ontology; changing them to satisfy validation destroys provenance. Author-supplied
ids (core functions, NEW rows, module terms) are strictly validated and must move
([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).

## Application

*Example.* After `GO:0030943` was obsoleted, human TOMM20's IBA and IDA rows moved from
`ACCEPT` to `MODIFY` with `GO:0140436` as replacement, and the core molecular function moved
with them ([MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.html)).
A retired term's footprint usually reaches beyond the obvious file: gene reviews, modules,
evidence statements, project notes and cached enumerations. Search for the id across all of
them.

When a review decomposes a precomposed "X involved in Y" term, it says where Y went
(`decomposed_into`); see [biological-process.md](../BP/README.md) and
[INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| Evidence codes | IDA, IBA |
| GO terms | `GO:0030943`  (obsolete); `GO:0140436` mitochondrial signal sequence receptor activity |

## Sources

- repo: [ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- web: [MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.html)
- web: [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)

<!-- END GENERATED -->
