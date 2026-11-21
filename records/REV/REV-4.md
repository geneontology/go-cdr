---
id: REV-4
title: Separate core from peripheral before deciding anything else
status: proposed
topic: REV
provenance: GOC_PLUS
provenance_note: '[GOC+]. Core-function focus is GOC guidance; the explicit core/non-core split per row
  is ours.'
sources:
- kind: wiki
  title: Tips
  url: https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations
- kind: drive
  title: Highly annotated genes, daf-16
  url: https://drive.google.com/open?id=1YhRirPCkc9Pl0gOC3Mhc5Zn0VK8SGHEOO-BeI6pwAGk
- kind: drive
  title: Highly annotated genes, MTOR
  url: https://drive.google.com/open?id=1Ha8AyFN9WndsT6UPPUnMYawzdn-dnqCG
date: '2026-11-15'
---

# REV-4. Separate core from peripheral before deciding anything else

## Decision

Write down the gene product's core activity, location and process first. `ACCEPT` is for
rows that state that core; true, precise rows outside it are `KEEP_AS_NON_CORE`.

## Context

A review that starts row by row drifts toward accepting everything that is not wrong. The GOC
recommends a gene-centric or pathway-centric pass rather than paper-by-paper curation, and
"less is more": select the terms that capture the essence of the function
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).
The Fall 2024 consortium sessions on highly annotated genes (mouse *Ctnnb1*, *C. elegans*
*daf-16*, human MTOR) made the same point from the other end: review the annotation set first,
then worry about how it is displayed
([Drive: Highly annotated genes, daf-16](https://drive.google.com/open?id=1YhRirPCkc9Pl0gOC3Mhc5Zn0VK8SGHEOO-BeI6pwAGk),
[Drive: Highly annotated genes, MTOR](https://drive.google.com/open?id=1Ha8AyFN9WndsT6UPPUnMYawzdn-dnqCG)).

## Application

*Example.* For DAF-16, a FOXO transcription factor that shuttles between cytoplasm and
nucleus, the review proposed removing the remaining cytoplasm and cytosol rows because the
cellular component is where the product is active, and DAF-16 is inactive in the cytoplasm
([Drive: daf-16](https://drive.google.com/open?id=1YhRirPCkc9Pl0gOC3Mhc5Zn0VK8SGHEOO-BeI6pwAGk)).
In this repository's vocabulary, those rows would be `MARK_AS_OVER_ANNOTATED` if the
localization is real but not where the function acts, and `KEEP_AS_NON_CORE` only if the
cytoplasmic pool does something.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. Core-function focus is GOC guidance; the explicit core/non-core split per row is ours. |
| Date | 2026-11-15 |

## Sources

- wiki: [Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
- drive: [Highly annotated genes, daf-16](https://drive.google.com/open?id=1YhRirPCkc9Pl0gOC3Mhc5Zn0VK8SGHEOO-BeI6pwAGk)
- drive: [Highly annotated genes, MTOR](https://drive.google.com/open?id=1Ha8AyFN9WndsT6UPPUnMYawzdn-dnqCG)

<!-- END GENERATED -->
