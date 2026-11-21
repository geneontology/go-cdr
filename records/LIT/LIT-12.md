---
id: LIT-12
title: 'Judge a paper against the rest of the literature: contested, superseded and retracted findings
  need explicit handling.'
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC] for representing current knowledge; [GOC+] for the retraction procedure.'
go_terms:
- term_id: GO:0032454
  label: histone H3K9 demethylase activity
related:
- LIT-8
sources:
- kind: web
  title: CONTESTED_FUNCTION
  url: https://ai4curation.io/ai-gene-review/pages/projects/CONTESTED_FUNCTION.html
- kind: web
  title: RETRACTIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/RETRACTIONS.html
date: '2026-11-15'
---

# LIT-12. Judge a paper against the rest of the literature: contested, superseded and retracted findings need explicit handling.

## Decision

Judge a paper against the rest of the literature: contested, superseded and retracted findings need explicit handling.

## Context

The Tips page says GO "is not an archive of all findings published on a protein"
and asks curators to remove annotations based on invalidated hypotheses. That
requires reading beyond the paper in hand.

- **Contested.** When good papers disagree, keep both visible and say so. Epe1's
  two experimental H3K9 demethylase rows (`GO:0032454`) are UNDECIDED: no assay has
  detected the activity, but genetic data do not rule it out. Its four electronic
  demethylase and oxidoreductase rows are removed as pseudo-enzyme propagations
  ([CONTESTED_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/CONTESTED_FUNCTION.html)).
- **Superseded.** When later work explains an earlier phenotype (yeast
  spliceosome and translation, [LIT-8](LIT-8.md)), the earlier process annotation
  goes. Record the later paper in `finding_review.superseded_by`.
- **Retracted.** A retraction is a fact about the source, not the biology. Flag the
  reference (`is_invalid: true`, `correctness: DISPUTED`), cite the notice, and ask
  what rests on it. If the retracted paper is the sole support, the row becomes
  UNDECIDED or a proposed REMOVE sent upstream; if other evidence supports it,
  keep it and say so. Do not remove every annotation on the gene
  ([RETRACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/RETRACTIONS.html); worked example human/TNFRSF21).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for representing current knowledge; [GOC+] for the retraction procedure. |
| Date | 2026-11-15 |
| Related | [LIT-8](LIT-8.md) |
| GO terms | `GO:0032454` histone H3K9 demethylase activity |

## Sources

- web: [CONTESTED_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/CONTESTED_FUNCTION.html)
- web: [RETRACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/RETRACTIONS.html)

<!-- END GENERATED -->
