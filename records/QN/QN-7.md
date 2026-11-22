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

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [QN-7-E1](QN-7.examples.yaml): A relation-only MODIFY on SDHD, paired with a contributes_to NEW row | Conformant | SDHD enables GO:0008177 succinate dehydrogenase (quinone) activity (IEA, GO_REF:0000107) |
| [QN-7-E2](QN-7.examples.yaml): A yeast SDH2 enables row accepted with the relation correction left in the summary | Non-conformant | SDH2 enables GO:0008177 succinate dehydrogenase (quinone) activity (IDA, PMID:13445213) |
| [QN-7-E3](QN-7.examples.yaml): A wrong is_active_in relation handled by marking the term over-annotated | Non-conformant | rho-1 is_active_in GO:0005829 cytosol (IBA, GO_REF:0000033) |
| [QN-1-E1](QN-1.examples.yaml): An is_active_in relation kept on a protein-complex term (from [QN-1](QN-1.md)) | Non-conformant | EXT1 is_active_in GO:1902494 catalytic complex (IDA, PMID:36593275) |
| [QN-2-E1](QN-2.examples.yaml): SDHB contributes to the whole-complex succinate:quinone activity (from [QN-2](QN-2.md)) | Conformant | SDHB contributes_to GO:0008177 succinate dehydrogenase (quinone) activity (IDA, PMID:37098072) |
| [QN-2-E3](QN-2.examples.yaml): An enables row for a single SDH subunit accepted while its own text calls for contributes_to (from [QN-2](QN-2.md)) | Non-conformant | sdh2 enables GO:0008177 succinate dehydrogenase (quinone) activity (IEA, GO_REF:0000120) |
| [QN-4-E2](QN-4.examples.yaml): An ortholog-transferred is_active_in kept although the review says it overstates the evidence (from [QN-4](QN-4.md)) | Non-conformant | vms1 is_active_in GO:0005789 endoplasmic reticulum membrane (ISO, GO_REF:0000024) |
| [QN-5-E1](QN-5.examples.yaml): A colocalizes_with cytosol row accepted as the core location of a cytosolic enzyme (from [QN-5](QN-5.md)) | Non-conformant | HPR2 colocalizes_with GO:0005829 cytosol (IDA, PMID:30233632) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| None (gap) | No procedure for relation-only corrections | MODIFY plus NEW with the corrected qualifier | Keeps the true claim and makes the correction machine-readable |

## Sources

- issue: [PR #3223](https://github.com/ai4curation/ai-gene-review/pull/3223)
- web: [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
