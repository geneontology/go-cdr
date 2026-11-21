---
id: REV-5
title: The conclusion, not the assay; the direct role, not its downstream effects
status: proposed
topic: REV
provenance: GOC
go_terms:
- term_id: GO:0048870
  label: cell motility
- term_id: GO:0042060
  label: wound healing
differences:
- prior_source: '[wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)
    (flagged "to be reviewed")'
  prior_said: Annotate to the experimental evidence, using judgement about core genes; request "X involved
    in Y" terms for downstream effects
  we_recommend: Downstream rows are over-annotation unless the evidence shows participation; do not request
    precomposed terms
  why: GO has obsoleted 1,265 "X involved in Y" terms, 883 with a comment pointing to GO-CAM ([INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html))
    ([REV-5](REV-5.md), [ONT-12](../ONT/ONT-12.md))
sources:
- kind: wiki
  title: Tips
  url: https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations
- kind: wiki
  title: Annotating downstream processes
  url: https://wiki.geneontology.org/index.php/Annotating_downstream_processes
- kind: web
  title: OVER_ANNOTATION_PATTERNS
  url: https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html
date: '2026-11-15'
---

# REV-5. The conclusion, not the assay; the direct role, not its downstream effects

## Decision

A row whose term names the assay readout, or a downstream consequence of the core
activity, is over-annotation. Mark it `MARK_AS_OVER_ANNOTATED`, or `REMOVE` it when direct
evidence later showed the gene acts elsewhere.

## Context

GOC examples: a scratch "wound healing" assay measures `GO:0048870` cell motility, not
`GO:0042060` wound healing; DNA fragmentation and caspase activation are readouts of
apoptosis, not evidence of a direct role in it
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).
The downstream-process guideline gives the canonical removal: yeast spliceosome components
had been annotated to translation from mutant phenotypes, and those rows were removed once the
splicing role was shown, because translation defects are expected when ribosomal transcripts
are spliced ([wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)).

The pattern "gene affects X, X affects Y, gene annotated to Y" is the commonest source of
pleiotropic over-annotation ([OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html),
pattern 4). For a hub gene, expect most developmental and disease-adjacent process rows to
fall here. Do not remove them merely for being downstream; ask whether the row's evidence
shows the gene acting in the process. The rules for phenotype-derived process rows are in
[biological-process.md](../BP/README.md).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0048870` cell motility; `GO:0042060` wound healing |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) (flagged "to be reviewed") | Annotate to the experimental evidence, using judgement about core genes; request "X involved in Y" terms for downstream effects | Downstream rows are over-annotation unless the evidence shows participation; do not request precomposed terms | GO has obsoleted 1,265 "X involved in Y" terms, 883 with a comment pointing to GO-CAM ([INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)) ([REV-5](REV-5.md), [ONT-12](../ONT/ONT-12.md)) |

## Sources

- wiki: [Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
- wiki: [Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)
- web: [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)

<!-- END GENERATED -->
