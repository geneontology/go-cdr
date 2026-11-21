---
id: REV-1
title: Judge the claim, not the row; rows sharing a term get consistent actions
status: proposed
topic: REV
provenance: GOC_PLUS
provenance_note: '[GOC+]. The GOC asks curators to look at existing annotations for consistency ([wiki:
  Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)); the claim-level
  framing and the formal consistency table are ours ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md),
  [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)).'
evidence_codes:
- IDA
- IBA
- NAS
- IEA
go_terms:
- term_id: GO:0005929
  label: cilium
- term_id: GO:0005515
  label: protein binding
related:
- REV-13
differences:
- prior_source: GOC evidence-code documentation (2007 onward)
  prior_said: Evidence codes are not quality measures
  we_recommend: 'Agree, and extend: rows sharing a term are one claim and get one verdict'
  why: The code-agnostic view has to reach the review actions, or reviewers remove IEAs to "clean up"
    ([REV-1](REV-1.md))
sources:
- kind: repo
  title: action consistency
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md
- kind: web
  title: OVER_ANNOTATION_PATTERNS
  url: https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html
- kind: wiki
  title: Tips
  url: https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# REV-1. Judge the claim, not the row; rows sharing a term get consistent actions

## Decision

Rows with the same GO term (and compatible qualifiers) are one claim. Their actions may
differ in emphasis but must not contradict each other, and `REMOVE` must not be used to keep
the "best" evidence code and discard the rest.

## Context

GOA often carries one term from several sources, for example IBA, IEA and NAS for one
complex membership. These are independent lines of evidence for one claim. `REMOVE` asserts
that the claim is unlikely to be true, so removing the IEA while accepting the IDA says the
claim is both true and false. The machine-checkable version of this rule is the action
consistency table ([action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)), which also
handles hierarchy: keeping a positive annotation to `GO:0005929` cilium while keeping a NOT on
an ancestor of it is a contradiction, because a positive annotation entails its ancestors and
a NOT entails its descendants.

## Application

*Example.* Fission yeast Gaa1 carries `GPI-anchor transamidase complex` from more than one
source (IBA, IEA and NAS; see `genes/SCHPO/gaa1`). A review that accepts the
IBA and removes the IEA "as redundant" fails consistency; the right record accepts (or keeps) all three, with one
argument. The redundancy itself is not an error
([OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html), pattern 5).

The one sanctioned exception is bare `GO:0005515` protein binding, which the protein-binding
policy removes as uninformative even beside accepted rows ([REV-13](REV-13.md)).

When GOA holds a positive row and a NOT row for the same term from different papers, decide:
`REMOVE` or `UNDECIDED` one side, or, if both hold in different contexts (NOT in roots,
positive in shoots), record a per-annotation `consistency_exception` with the reason.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The GOC asks curators to look at existing annotations for consistency ([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)); the claim-level framing and the formal consistency table are ours ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)). |
| Date | 2026-11-15 |
| Related | [REV-13](REV-13.md) |
| Evidence codes | IDA, IBA, NAS, IEA |
| GO terms | `GO:0005929` cilium; `GO:0005515` protein binding |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| GOC evidence-code documentation (2007 onward) | Evidence codes are not quality measures | Agree, and extend: rows sharing a term are one claim and get one verdict | The code-agnostic view has to reach the review actions, or reviewers remove IEAs to "clean up" ([REV-1](REV-1.md)) |

## Sources

- repo: [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)
- web: [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)
- wiki: [Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
