---
id: ONT-10
title: Track upstream changes as inbound work, and argue disagreement in writing
status: proposed
topic: ONT
provenance: NEW
differences:
- prior_source: '[wiki: Manager 09Feb11](https://wiki.geneontology.org/index.php/Manager_09Feb11)'
  prior_said: Do not obsolete on definition edits that leave annotations correct; curators refine from
    reports
  we_recommend: Same, and record when a definition change was checked (`ontology_state_verified`)
  why: Undated statements about term state went stale twice in this repository ([ONT-10](ONT-10.md))
sources:
- kind: repo
  title: ontology changes
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md
date: '2026-11-15'
---

# ONT-10. Track upstream changes as inbound work, and argue disagreement in writing

## Decision

Distinguish a change you are asking the ontology to make from a change the ontology has made
or plans. For an upstream change, record whether you agree, when you last checked its state,
and whether your own content has been migrated. If you disagree, write the argument.

## Context

The failure that actually happens is that the ontology moves and the curated content keeps
citing the retired term. This repository records each change with an `origin`
(`SELF_PROPOSED`, `UPSTREAM_PROPOSED`, `UPSTREAM_COMPLETED`), a `stance` for upstream changes
(`AGREE`, `DISAGREE`, `PARTIALLY_AGREE`, `NEEDS_CONFIRMATION`), the date the term's state was
last verified, and an adoption status for its own affected files. A check fires when a change
has landed and the affected content is still unmigrated
([ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)). A `DISAGREE` with fewer than twenty
words of argument is flagged: asserting disagreement is not raising it.

### Requesting and proposing terms

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Manager 09Feb11](https://wiki.geneontology.org/index.php/Manager_09Feb11) | Do not obsolete on definition edits that leave annotations correct; curators refine from reports | Same, and record when a definition change was checked (`ontology_state_verified`) | Undated statements about term state went stale twice in this repository ([ONT-10](ONT-10.md)) |

## Sources

- repo: [ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)

<!-- END GENERATED -->
