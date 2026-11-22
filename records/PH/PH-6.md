---
id: PH-6
title: Propagate substrate and cargo specificity only within a duplication-free clade
status: proposed
topic: PH
provenance: GOC_PLUS
evidence_codes:
- IDA
go_terms:
- term_id: GO:0003955
  label: NAD(P)H dehydrogenase (quinone) activity
- term_id: GO:0001512
  label: dihydronicotinamide riboside quinone reductase activity
- term_id: GO:0001729
  label: ceramide kinase activity
differences:
- prior_source: '[wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)'
  prior_said: Be cautious with substrates.
  we_recommend: Substrate terms only within duplication-free clades; general parent across duplications
    (PH-6).
  why: Turns a caution into a rule that can be checked on the tree.
sources:
- kind: wiki
  title: PAINT annotation guidelines
  url: https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines
- kind: issue
  title: go-annotation#2033
  url: https://github.com/geneontology/go-annotation/issues/2033
- kind: web
  title: IBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html
- kind: web
  title: ENZYME_SPECIFICITY
  url: https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html
date: '2026-11-15'
---

# PH-6. Propagate substrate and cargo specificity only within a duplication-free clade

## Decision

A substrate-specific MF (enzyme or transporter) may descend only to members that share the
seed's specificity without an intervening duplication that could have changed it. Across
duplications, place the general parent term on the deep node and the specific term on the
subclade with direct evidence.

## Context

the PAINT guideline asks for caution with substrates
([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)).
We make it operational. A PAPS transporter term propagated over an ancient duplication into a
fungal UDP-GlcNAc transporter was fixed by restricting the term to the animal-only node
([go-annotation#2033](https://github.com/geneontology/go-annotation/issues/2033)). The repo's
substrate cases fail the same way: the family node lumps specificities, and the leak can be in
the cleaved substrate or the co-substrate ([IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html), pattern 11;
[ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html)).

## Application

Worked example: human NQO2 inherits `GO:0003955` NAD(P)H dehydrogenase (quinone) activity from
the NQO1/NQO2 node (PTHR10204), but NQO2 uses dihydronicotinamide riboside, not NAD(P)H. The
correct term, `GO:0001512` dihydronicotinamide riboside quinone reductase activity, is already
supported by IDA. Because `GO:0001512` is not a descendant of `GO:0003955`, the review action is
a lateral MODIFY, and the PAINT fix is to restrict `GO:0003955` to the NQO1 clade. Human AGK
carries `GO:0001729` ceramide kinase activity from a node lumping acylglycerol and sphingosine
kinases; two direct assays found no ceramide phosphorylation ([IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Evidence codes | IDA |
| GO terms | `GO:0003955` NAD(P)H dehydrogenase (quinone) activity; `GO:0001512` dihydronicotinamide riboside quinone reductase activity; `GO:0001729` ceramide kinase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [PH-6-E1](PH-6.examples.yaml): A ceramide kinase activity inherited by AGK from a node that lumps lipid kinases | Conformant | AGK enables GO:0001729 ceramide kinase activity (IBA, GO_REF:0000033) |
| [PH-6-E2](PH-6.examples.yaml): NQO2 keeps the inherited NAD(P)H quinone reductase activity as non-core | Contested | NQO2 enables GO:0003955 NAD(P)H dehydrogenase (quinone) activity (IBA, GO_REF:0000033) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) | Be cautious with substrates. | Substrate terms only within duplication-free clades; general parent across duplications (PH-6). | Turns a caution into a rule that can be checked on the tree. |

## Sources

- wiki: [PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)
- issue: [go-annotation#2033](https://github.com/geneontology/go-annotation/issues/2033)
- web: [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)
- web: [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html)

<!-- END GENERATED -->
