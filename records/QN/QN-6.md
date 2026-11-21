---
id: QN-6
title: Judge the relation together with the term. Positive annotations entail ancestors only through relations
  that carry up.
status: proposed
topic: QN
provenance: GOC_PLUS
provenance_note: '[GOC+]. The property chains are GOC''s; using them for review consistency is the repo''s
  addition. [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md);
  [wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in).'
go_terms:
- term_id: GO:0008177
  label: succinate dehydrogenase (quinone) activity
- term_id: GO:0000104
  label: succinate dehydrogenase activity
- term_id: GO:0006303
  label: double-strand break repair via nonhomologous end joining
- term_id: GO:0006281
  label: DNA repair
sources:
- kind: repo
  title: action consistency
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md
- kind: wiki
  title: Is active in
  url: https://wiki.geneontology.org/index.php/Is_active_in
date: '2026-11-15'
---

# QN-6. Judge the relation together with the term. Positive annotations entail ancestors only through relations that carry up.

## Decision

Judge the relation together with the term. Positive annotations entail ancestors only through relations that carry up.

## Context

Positive claims propagate up the ontology with their relation, and some relations entail weaker ones. A consistency check that ignores relations reports false conflicts, such as `ACCEPT located_in` the axoneme next to `REMOVE is_active_in` the cilium, and misses real ones.

**Entailment table** (from the repo's `action_consistency.py`, which encodes GO's property chains):

| A positive row with... | ...also asserts, for the same or an ancestor term |
|---|---|
| `is_active_in` | `located_in` |
| `part_of` (complex) | `located_in` |
| `enables` or `contributes_to` an MF that is `part_of` a BP | `involved_in` (hence `acts_upstream_of_or_within`) that BP |
| `involved_in` | `acts_upstream_of_or_within` |
| `acts_upstream_of, positive effect` | `acts_upstream_of`; `acts_upstream_of_or_within, positive effect`; `acts_upstream_of_or_within` |
| `acts_upstream_of, negative effect` | the negative-effect analogues |
| `contributes_to` | not `enables` |

## Application

**Example.** An ACCEPTed `contributes_to` GO:0008177 row does not support `enables` GO:0000104. An ACCEPTed `involved_in` GO:0006303 double-strand break repair via nonhomologous end joining row does entail `involved_in` GO:0006281 DNA repair, so a REMOVE of a GO:0006281 row on the same gene needs an argument that the NHEJ row is also wrong.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The property chains are GOC's; using them for review consistency is the repo's addition. [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md); [wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in). |
| Date | 2026-11-15 |
| GO terms | `GO:0008177` succinate dehydrogenase (quinone) activity; `GO:0000104` succinate dehydrogenase activity; `GO:0006303` double-strand break repair via nonhomologous end joining; `GO:0006281` DNA repair |

## Sources

- repo: [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)
- wiki: [Is active in](https://wiki.geneontology.org/index.php/Is_active_in)

<!-- END GENERATED -->
