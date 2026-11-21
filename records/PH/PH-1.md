---
id: PH-1
title: Review an IBA by its node placement, not by its donor count
status: proposed
topic: PH
provenance: GOC_PLUS
provenance_note: '[GOC+]. Sharpens [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)
  and the repo rule in [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
  ("What an IBA asserts").'
evidence_codes:
- IBA
- IBD
go_terms:
- term_id: GO:0032452
  label: histone demethylase activity
- term_id: GO:0019782
  label: ISG15 activating enzyme activity
- term_id: GO:0008641
  label: ubiquitin-like modifier activating enzyme activity
related:
- PH-9
sources:
- kind: issue
  title: go-annotation#2382
  url: https://github.com/geneontology/go-annotation/issues/2382
- kind: web
  title: IBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html
- kind: wiki
  title: PAINT annotation guidelines
  url: https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# PH-1. Review an IBA by its node placement, not by its donor count

## Decision

An IBA asserts that the target descends from a node at which a curator judged the function
to have arisen. Challenge it by showing the target sits outside the clade that inherited the
function, or that the target lost or changed the function after the node.

## Context

the IBA row is a mechanical output; the judgement lives in the IBD. A node seeded
by one well-characterised MOD or human gene can be sound, because the curator made the call
with the whole tree and alignment in view. The 2019 PAINT tracker discussion between curators
who wanted a two-seed minimum and PAINT curators who did not ([go-annotation#2382](https://github.com/geneontology/go-annotation/issues/2382))
shows why donor count is a poor proxy: single-seed IBDs fail when the BP term is loosely tied
to the MF, not because they are single.

## Application

Worked example: *S. pombe* Epe1 receives `GO:0032452` histone demethylase activity by IBA from
JmjC-domain relatives. The argument against it is target-specific: Epe1's Fe(II)-binding triad
has Tyr in place of the third His ligand and no demethylase activity is detectable in vitro
([IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html), pattern 1). The node is right for KDM2A/KDM2B; the leaf
lost the activity. The correct fix is a loss below the node (PH-9), not removal of the IBD.

Counter-example: UBA7 receives `GO:0019782` ISG15 activating enzyme activity by IBA, while
the InterPro2GO row gives only `GO:0008641` ubiquitin-like modifier activating enzyme
activity. Here the IBA is the more precise and better-supported claim
([IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html), pattern 2).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. Sharpens [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) and the repo rule in [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) ("What an IBA asserts"). |
| Date | 2026-11-15 |
| Related | [PH-9](PH-9.md) |
| Evidence codes | IBA, IBD |
| GO terms | `GO:0032452` histone demethylase activity; `GO:0019782` ISG15 activating enzyme activity; `GO:0008641` ubiquitin-like modifier activating enzyme activity |

## Sources

- issue: [go-annotation#2382](https://github.com/geneontology/go-annotation/issues/2382)
- web: [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)
- wiki: [PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
