---
id: IEA-10
title: Automated orthology transfer must preserve relations and stop at context
status: proposed
topic: IEA
provenance: GOC_PLUS
evidence_codes:
- IDA
- IPI
- IMP
- IGI
- IEP
- IBA
- ISO
- IEA
differences:
- prior_source: '[wiki: Ensembl Compara annotation projection](https://wiki.geneontology.org/index.php/Ensembl_Compara_annotation_projection)'
  prior_said: Projects experimental rows between one-to-one orthologs; no limit on term type.
  we_recommend: Preserve relations; exclude context, development and response-to terms; treat as provisional
    pending a consortium decision (IEA-10).
  why: Relation upgrades ([#5411](https://github.com/geneontology/go-annotation/issues/5411)) and context
    transfer ([#1344](https://github.com/geneontology/go-annotation/issues/1344)); Ensembl stopped orthology
    calls in 2026.
sources:
- kind: wiki
  title: Ensembl Compara annotation projection
  url: https://wiki.geneontology.org/index.php/Ensembl_Compara_annotation_projection
- kind: drive
  title: Ensembl and ISO pipelines
  url: https://drive.google.com/open?id=1q9m9RbQqdpXMPrLq-jzTC-ouLJjUda_XAA93U8zTkNw
- kind: drive
  title: IEA WG Fall 2026
  url: https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I
- kind: issue
  title: go-annotation#5411
  url: https://github.com/geneontology/go-annotation/issues/5411
- kind: issue
  title: go-annotation#1344
  url: https://github.com/geneontology/go-annotation/issues/1344
- kind: issue
  title: go-annotation#1807
  url: https://github.com/geneontology/go-annotation/issues/1807
- kind: web
  title: HOMOLOGY_PROPAGATION
  url: https://ai4curation.io/ai-gene-review/pages/projects/HOMOLOGY_PROPAGATION.html
date: '2026-11-15'
---

# IEA-10. Automated orthology transfer must preserve relations and stop at context

## Decision

An automated ortholog projection must use one-to-one orthologs, experimental donor rows only, and
the donor's gene-product-to-term relation unchanged. It should not transfer tissue, developmental,
"response to", or organism-specific process terms. When reviewing a Compara row, treat it as a
transfer of the donor row and check the donor's relation first.

## Context

the Compara method uses one-to-one and apparent one-to-one orthologs and projects only
IDA, IEP, IGI, IMP and IPI rows ([wiki: Ensembl Compara annotation projection](https://wiki.geneontology.org/index.php/Ensembl_Compara_annotation_projection)).
In practice it copies annotations wholesale: the IEA working group called it boilerplating that
cannot tell conservation from divergence, inflated by many-to-many paralog mappings, and silent in
review because a dispute must target the original source
([Drive: Ensembl and ISO pipelines](https://drive.google.com/open?id=1q9m9RbQqdpXMPrLq-jzTC-ouLJjUda_XAA93U8zTkNw);
[Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).
A 2024 report showed a mouse `acts_upstream_of_or_within` row arriving in human as `involved_in`
([go-annotation#5411](https://github.com/geneontology/go-annotation/issues/5411)). Developmental and
response-to terms on human GART from Compara were an early example
([go-annotation#1344](https://github.com/geneontology/go-annotation/issues/1344)), and Ensembl Plants
once projected auxin-signalling terms onto yeast ([go-annotation#1807](https://github.com/geneontology/go-annotation/issues/1807)).
In the repo's statistics, 20% of reviewed Compara rows were downgraded against 9% of IBA
([HOMOLOGY_PROPAGATION](https://ai4curation.io/ai-gene-review/pages/projects/HOMOLOGY_PROPAGATION.html)).

## Application

Worked example: human GART carried brainstem, cerebellum and cerebral cortex development from a
mouse phenotype by Compara projection. GART is a purine biosynthetic enzyme; the developmental terms
are downstream phenotypes and should not have been projected
([go-annotation#1344](https://github.com/geneontology/go-annotation/issues/1344)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Evidence codes | IDA, IPI, IMP, IGI, IEP, IBA, ISO, IEA |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-10-E1](IEA-10.examples.yaml): Compara projects a nematode cuticle process onto mouse Duox1 | Non-conformant | Duox1 involved_in GO:0042335 cuticle development (IEA, GO_REF:0000107) |
| [IEA-10-E2](IEA-10.examples.yaml): A budding-yeast nitrogen-starvation response projected onto Candida Bcy1 | Non-conformant | BCY1 involved_in GO:0006995 cellular response to nitrogen starvation (IEA, GO_REF:0000107) |
| [IEA-10-E3](IEA-10.examples.yaml): Developmental terms projected onto mouse Wdpcp, true by the mouse's own IMP | Contested | Wdpcp involved_in GO:0042733 embryonic digit morphogenesis (IEA, GO_REF:0000107) |
| [PIPE-1-E2](../PIPE/PIPE-1.examples.yaml): Ensembl Compara answers a relation-upgrade report at once but changes output slowly (from [PIPE-1](../PIPE/PIPE-1.md)) | Contested | Ensembl Compara |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Ensembl Compara annotation projection](https://wiki.geneontology.org/index.php/Ensembl_Compara_annotation_projection) | Projects experimental rows between one-to-one orthologs; no limit on term type. | Preserve relations; exclude context, development and response-to terms; treat as provisional pending a consortium decision (IEA-10). | Relation upgrades ([#5411](https://github.com/geneontology/go-annotation/issues/5411)) and context transfer ([#1344](https://github.com/geneontology/go-annotation/issues/1344)); Ensembl stopped orthology calls in 2026. |

## Sources

- wiki: [Ensembl Compara annotation projection](https://wiki.geneontology.org/index.php/Ensembl_Compara_annotation_projection)
- drive: [Ensembl and ISO pipelines](https://drive.google.com/open?id=1q9m9RbQqdpXMPrLq-jzTC-ouLJjUda_XAA93U8zTkNw)
- drive: [IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)
- issue: [go-annotation#5411](https://github.com/geneontology/go-annotation/issues/5411)
- issue: [go-annotation#1344](https://github.com/geneontology/go-annotation/issues/1344)
- issue: [go-annotation#1807](https://github.com/geneontology/go-annotation/issues/1807)
- web: [HOMOLOGY_PROPAGATION](https://ai4curation.io/ai-gene-review/pages/projects/HOMOLOGY_PROPAGATION.html)

<!-- END GENERATED -->
