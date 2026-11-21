---
id: LIT-13
title: When reviewing someone else's literature annotation, read what they read before overruling it;
  an abstract can confirm, but only the full text can refute.
status: proposed
topic: LIT
provenance: NEW
provenance_note: '[NEW], from the repository''s review experience.'
sources:
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: web
  title: WRONG_GENE_LEADS
  url: https://ai4curation.io/ai-gene-review/pages/projects/WRONG_GENE_LEADS.html
- kind: web
  title: EVIDENCE_SOURCE_SUFFICIENCY
  url: https://ai4curation.io/ai-gene-review/pages/projects/EVIDENCE_SOURCE_SUFFICIENCY.html
- kind: web
  title: FUNCTION_REQUIREMENT_RULES
  url: https://ai4curation.io/ai-gene-review/pages/projects/FUNCTION_REQUIREMENT_RULES.html
date: '2026-11-15'
---

# LIT-13. When reviewing someone else's literature annotation, read what they read before overruling it; an abstract can confirm, but only the full text can refute.

## Decision

When reviewing someone else's literature annotation, read what they read before overruling it; an abstract can confirm, but only the full text can refute.

## Context

The curator who made an experimental annotation read the full text. Many cached
papers in this repository are abstract-only, and a title that foregrounds a
paralog often hides an assay of the gene being annotated. So:

- Do not REMOVE an experimental row, or call it a wrong-gene attribution, because
  the cached title or abstract is about something else. Use UNDECIDED if you cannot
  verify it, or ACCEPT if the function is independently established
  ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), "Do not overrule curators from incomplete
  evidence").
- Reserve a confident "this paper is about X" for cases where the abstract says
  so. FLNC, SOCS3 and NLRP3 leads whose abstracts never named the gene stayed as
  queries; PAPSS1, whose abstract named PAPSS2, was confirmed
  ([WRONG_GENE_LEADS](https://ai4curation.io/ai-gene-review/pages/projects/WRONG_GENE_LEADS.html)).
- An abstract is usually enough to confirm. In a blinded pilot the abstract alone
  supported ACCEPT for 18 of 21 annotations, while REMOVE support in the corpus is
  93% primary research ([EVIDENCE_SOURCE_SUFFICIENCY](https://ai4curation.io/ai-gene-review/pages/projects/EVIDENCE_SOURCE_SUFFICIENCY.html)).
  Read the full text before REMOVE or MODIFY.
- Automated flags are leads. A function-requirement rule ("a protein that enables
  T has one of these domains") or a wrong-gene score never by itself justifies
  changing an annotation ([FUNCTION_REQUIREMENT_RULES](https://ai4curation.io/ai-gene-review/pages/projects/FUNCTION_REQUIREMENT_RULES.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW], from the repository's review experience. |
| Date | 2026-11-15 |

## Sources

- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- web: [WRONG_GENE_LEADS](https://ai4curation.io/ai-gene-review/pages/projects/WRONG_GENE_LEADS.html)
- web: [EVIDENCE_SOURCE_SUFFICIENCY](https://ai4curation.io/ai-gene-review/pages/projects/EVIDENCE_SOURCE_SUFFICIENCY.html)
- web: [FUNCTION_REQUIREMENT_RULES](https://ai4curation.io/ai-gene-review/pages/projects/FUNCTION_REQUIREMENT_RULES.html)

<!-- END GENERATED -->
