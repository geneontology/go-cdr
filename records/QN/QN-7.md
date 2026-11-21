---
id: QN-7
title: When reviewing, correct a wrong relation as a structured relation change. Do not REMOVE a right
  term because its relation is wrong.
status: proposed
topic: QN
provenance: NEW
provenance_note: '[NEW]. GO has no review procedure for relation-only corrections. [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html);
  [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md).'
go_terms:
- term_id: GO:0008177
  label: succinate dehydrogenase (quinone) activity
differences:
- prior_source: None (gap)
  prior_said: No procedure for relation-only corrections
  we_recommend: MODIFY plus NEW with the corrected qualifier
  why: Keeps the true claim and makes the correction machine-readable
sources:
- kind: issue
  title: 'PR #3223'
  url: https://github.com/ai4curation/ai-gene-review/pull/3223
- kind: web
  title: SDH_GP2TERM_CONTRIBUTES_TO
  url: https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# QN-7. When reviewing, correct a wrong relation as a structured relation change. Do not REMOVE a right term because its relation is wrong.

## Decision

When reviewing, correct a wrong relation as a structured relation change. Do not REMOVE a right term because its relation is wrong.

## Context

A review judges claims. "SDHB enables GO:0008177" is false and "SDHB contributes_to GO:0008177" is true. The term is sound, so removing the row loses the true claim. Correcting it only in prose leaves the file asserting the false one: the repo's SDH audit found five reviews arguing for `contributes_to` in prose while only two rows carried it in the structured field.

**Procedure (repo).** Mark the existing row `MODIFY`, say in `reason` that only the relation changes, and add one `NEW` row with the same term and the corrected `qualifier`. Validation accepts this relation-only pattern, which [PR #3223](https://github.com/ai4curation/ai-gene-review/pull/3223) established for SDHB and SDHD. Apply the same pattern to `involved_in` → `acts_upstream_of_or_within, positive effect`, to `colocalizes_with` → `located_in`, and to `enables` → `contributes_to`.

### NOT annotations

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW]. GO has no review procedure for relation-only corrections. [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html); [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md). |
| Date | 2026-11-15 |
| GO terms | `GO:0008177` succinate dehydrogenase (quinone) activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| None (gap) | No procedure for relation-only corrections | MODIFY plus NEW with the corrected qualifier | Keeps the true claim and makes the correction machine-readable |

## Sources

- issue: [PR #3223](https://github.com/ai4curation/ai-gene-review/pull/3223)
- web: [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
