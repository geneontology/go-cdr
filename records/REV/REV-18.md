---
id: REV-18
title: Every row needs term-specific reasoning and independent, verbatim support
status: proposed
topic: REV
provenance: NEW
sources:
- kind: web
  title: REVIEW_QUALITY_AUDIT
  url: https://ai4curation.io/ai-gene-review/pages/projects/REVIEW_QUALITY_AUDIT.html
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# REV-18. Every row needs term-specific reasoning and independent, verbatim support

## Decision

Each row's `summary` and `reason` must be about that term, and each `supporting_text` must be
a verbatim quote from a source that independently supports the claim. Boilerplate reasons,
placeholder quotes, the gene's own GOA file and restated UniProt labels are not support.

## Context

A generation pass once filled every row of mouse Fyn, Egfr, Grb2, Cbl and Egf with a handful of
templated reasons and a placeholder quote ("deep research report reviewed for GO term
specificity..."). The action labels looked plausible and carried no curation; Fyn also held
contradictory `REMOVE`/`ACCEPT` pairs on its core terms. All were re-reviewed, and the detector
now runs as a smell test ([REVIEW_QUALITY_AUDIT](https://ai4curation.io/ai-gene-review/pages/projects/REVIEW_QUALITY_AUDIT.html)).

What does not count:

- the gene's `-goa.tsv` (it says what is annotated, never why it is true; citing it is a
  blocking error), or another gene's GOA file as comparator evidence (argue comparators in prose);
- UniProt protein names, EC numbers, keywords and `DR GO` lines, which restate annotations;
- UniProt statements whose only evidence is an ARBA rule, submitter import (`ECO:0000313`) or a
  machine-generated name, which repeat a prediction;
- the protein existence level, as support for `ACCEPT`, `NEW` or a core function;
- your own notes or a deep-research summary as if it were literature.

Curated UniProt text tied to a publication, family classification and sequence-analysis
features (signal peptides, TM helices) are valid support for what they say
([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).

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
| [REV-18-E1](REV-18.examples.yaml): An APP row accepted with an evidence-code template as its only reasoning | Non-conformant | APP involved_in GO:1904646 cellular response to amyloid-beta (IDA, PMID:29518356) |
| [REV-9-E2](REV-9.examples.yaml): A photosystem I assembly IBA on PsbP1 removed without examining its PAINT seed (from [REV-9](REV-9.md)) | Non-conformant | PSBP1 involved_in GO:0048564 photosystem I assembly (IBA, GO_REF:0000033) |
| [REV-11-E3](REV-11.examples.yaml): Melanin biosynthesis proposed for POMC with a boilerplate reason (from [REV-11](REV-11.md)) | Non-conformant | POMC GO:0042438 melanin biosynthetic process (NAS) |

## Sources

- web: [REVIEW_QUALITY_AUDIT](https://ai4curation.io/ai-gene-review/pages/projects/REVIEW_QUALITY_AUDIT.html)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
