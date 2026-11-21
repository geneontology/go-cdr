---
id: REV-3
title: A correct but general term is `MODIFY` only when this row's evidence supports the specific term
status: proposed
topic: REV
provenance: NEW
provenance_note: '[NEW]. This is a maintainer ruling of 2026-11-14, made after two reviews in one batch
  read the action vocabulary two opposite ways for the same kind of row. It narrows `TOO_GENERAL` and
  does not retroactively condemn earlier reviews ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).
  It departs from the over-annotation catalogue, which recommends "REMOVE or MODIFY" for broad enzyme
  terms ([OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html),
  pattern 2); see the Differences table.'
go_terms:
- term_id: GO:0016498
  label: neuromedin K receptor activity
- term_id: GO:0004930
  label: G protein-coupled receptor activity
- term_id: GO:0016020
  label: membrane
- term_id: GO:0005886
  label: plasma membrane
- term_id: GO:0005739
  label: mitochondrion
differences:
- prior_source: '[OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html),
    pattern 2'
  prior_said: 'Broad enzyme terms: "REMOVE or MODIFY to more specific child terms"'
  we_recommend: '`MODIFY` only if this row''s evidence supports the child; otherwise keep; never `REMOVE`
    a true term'
  why: 2026-11-14 maintainer ruling; `REMOVE` asserts falsehood ([REV-3](REV-3.md))
sources:
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: web
  title: OVER_ANNOTATION_PATTERNS
  url: https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html
date: '2026-11-15'
---

# REV-3. A correct but general term is `MODIFY` only when this row's evidence supports the specific term

## Decision

If a row's term is true but less specific than the evidence allows, `MODIFY` it to the
specific descendant, and only when this row's own evidence supports that descendant. If the
row's evidence stops at the general term, keep the row. Reserve `TOO_GENERAL` for terms that
are imprecise on their own once a specific term is asserted elsewhere.

## Context

A paper that identifies tachykinin NK3 ligand binding supports `GO:0016498` neuromedin K
receptor activity; an InterPro2GO row from a generic GPCR signature supports only
`GO:0004930` G protein-coupled receptor activity. The InterPro row is not `MODIFY` (its
evidence cannot reach the descendant) and it is not `TOO_GENERAL` (GPCR activity is a
respectably specific term): keep it. `TOO_GENERAL` is for `GO:0016020` membrane beside an
accepted `GO:0005886` plasma membrane, where the broad term answers no question by itself.
When several descendants are supported, as for a pleiotropic gene, list all of them as
replacements rather than choosing one.

Root organelle terms are an exception: `GO:0005739` mitochondrion and the other four root
organelles stay as they are when supported, and the sub-compartment is added as a new row,
not substituted ([cellular-component.md](../CC/README.md),
[ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)).

Lateral corrections are a separate, older use of `MODIFY`: a sign error, or a BP that should
have been a different process, takes a replacement that is not a descendant.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW]. This is a maintainer ruling of 2026-11-14, made after two reviews in one batch read the action vocabulary two opposite ways for the same kind of row. It narrows `TOO_GENERAL` and does not retroactively condemn earlier reviews ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)). It departs from the over-annotation catalogue, which recommends "REMOVE or MODIFY" for broad enzyme terms ([OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html), pattern 2); see the Differences table. |
| Date | 2026-11-15 |
| GO terms | `GO:0016498` neuromedin K receptor activity; `GO:0004930` G protein-coupled receptor activity; `GO:0016020` membrane; `GO:0005886` plasma membrane; `GO:0005739` mitochondrion |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html), pattern 2 | Broad enzyme terms: "REMOVE or MODIFY to more specific child terms" | `MODIFY` only if this row's evidence supports the child; otherwise keep; never `REMOVE` a true term | 2026-11-14 maintainer ruling; `REMOVE` asserts falsehood ([REV-3](REV-3.md)) |

## Sources

- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- web: [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)

<!-- END GENERATED -->
