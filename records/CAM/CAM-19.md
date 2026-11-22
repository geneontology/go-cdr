---
id: CAM-19
title: When reviewing, check each activity against the gene review, and treat a model as one curator's
  assertion, not as evidence.
status: proposed
topic: CAM
provenance: NEW
sources:
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: web
  title: INVOLVED_IN_PRECOMPOSITION
  url: https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html
- kind: repo
  title: gocam-curation skill
  url: https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/SKILL.md
- kind: repo
  title: qc-and-consistency reference
  url: https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/qc-and-consistency.md
date: '2026-11-15'
---

# CAM-19. When reviewing, check each activity against the gene review, and treat a model as one curator's assertion, not as evidence.

## Decision

When reviewing, check each activity against the gene review, and treat a model as one curator's assertion, not as evidence.

## Context

For each activity in a `GoCamReview`, record a verdict (`OK`, `UNCERTAIN`,
`WRONG`), any QC flags, and consistency with the gene's review
(`CONSISTENT`, `MORE_SPECIFIC`, `MORE_GENERAL`, `RELATED`, `CONFLICT`,
`NOT_IN_REVIEW`, `NO_GENE_REVIEW`). Consistency judges the function: a correct
function with a wrong edge is `CONSISTENT` plus `WRONG_CAUSAL_SIGN`, not
`CONFLICT`. Anchor every non-trivial verdict in verbatim text from the cited
paper.

The converse applies in gene reviews. A GO-CAM activity is not a reason to
accept a GAF row, and absence of a gene from a model is not a reason to remove
one. But a curator who modelled a pathway, included the gene, and gave it a
different role than a proposed `NEW` term made a decision to argue with
explicitly; check `gocams/index.tsv` before proposing a process term (see the
AGT example in [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)). When a review decomposes a
precomposed "X involved in Y" term, record a GO-CAM that models Y in
`decomposed_into: gocam_associations`
([INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CAM-19-E1](CAM-19.examples.yaml): A TOLLIP adaptor activity consistent with its gene review but carrying the wrong edge sign | Conformant | gomodel:59cc772c00000000 |
| [CAM-19-E2](CAM-19.examples.yaml): A GO-CAM enabler checked against the gene review that removes the same claims | Conformant | gomodel:6796b94c00004996 |
| [CAM-19-E3](CAM-19.examples.yaml): A precomposed CMA targeting term decomposed with a pointer to the GO-CAM that models the context | Conformant | HSPA8 involved_in GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy (IDA, PMID:11559757) |
| [CAM-8-E3](CAM-8.examples.yaml): A cholesterol-esterifying enzyme drawn as directly inhibiting a viral fusion protein (from [CAM-8](CAM-8.md)) | Non-conformant | gomodel:6796b94c00004996 |

## Sources

- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- web: [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)
- repo: [gocam-curation skill](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/SKILL.md)
- repo: [qc-and-consistency reference](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/qc-and-consistency.md)

<!-- END GENERATED -->
