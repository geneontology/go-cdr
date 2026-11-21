---
id: MO-8
title: Record the other organism for interspecies annotations, and only for physiological interactions.
status: proposed
topic: MO
provenance: GOC_PLUS
go_terms:
- term_id: GO:0044419
  label: biological process involved in interspecies interaction between organisms
differences:
- prior_source: '[go-annotation#3514](https://github.com/geneontology/go-annotation/issues/3514) (2020)'
  prior_said: Migrate the interacting species from the taxon field to a `has input` extension.
  we_recommend: Keep the interacting taxon field; add `has input` for a known host target (MO-8).
  why: GAF 2.2 and GPAD 2.0 kept the field; most groups making these annotations did not use extensions.
sources:
- kind: drive
  title: Multi-species terms - documentation to review
  url: https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU
- kind: issue
  title: go-annotation#3514
  url: https://github.com/geneontology/go-annotation/issues/3514
- kind: issue
  title: go-annotation#3314
  url: https://github.com/geneontology/go-annotation/issues/3314
- kind: drive
  title: host_symbiont_annotation
  url: https://drive.google.com/open?id=1NiJfYB4JmClhbsr4G3Xwwr-6Bw4GWXGJ
date: '2026-11-15'
---

# MO-8. Record the other organism for interspecies annotations, and only for physiological interactions.

## Decision

Record the other organism for interspecies annotations, and only for physiological interactions.

## Context

For an annotation to a term under `GO:0044419`, record the interacting
organism. The long-standing mechanism is a second taxon in GAF column 13
(gene product's taxon first, interacting taxon second; the same taxon twice for
an intraspecies interaction). A 2020 announcement recommended moving to a
`has input` extension naming the interacting organism or its gene product; GAF
2.2 and GPAD 2.0 kept the interacting-taxon field, and several groups do not
use extensions. Until the GOC decides, record the interacting taxon in the
taxon field and, where the host target gene product is known, add it as `has
input` on the MF.

Do not add a second taxon to annotations made by sequence similarity, and do
not create interspecies binding annotations from heterologous experiments
(a human protein screened against a mouse library, a protein expressed in COS
cells). An interspecies interaction annotation states that the two proteins
meet in nature. For a heterologous experiment, the partner identifier goes in
WITH/FROM, describing the experiment.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| GO terms | `GO:0044419` biological process involved in interspecies interaction between organisms |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [go-annotation#3514](https://github.com/geneontology/go-annotation/issues/3514) (2020) | Migrate the interacting species from the taxon field to a `has input` extension. | Keep the interacting taxon field; add `has input` for a known host target (MO-8). | GAF 2.2 and GPAD 2.0 kept the field; most groups making these annotations did not use extensions. |

## Sources

- drive: [Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU)
- issue: [go-annotation#3514](https://github.com/geneontology/go-annotation/issues/3514)
- issue: [go-annotation#3314](https://github.com/geneontology/go-annotation/issues/3314)
- drive: [host_symbiont_annotation](https://drive.google.com/open?id=1NiJfYB4JmClhbsr4G3Xwwr-6Bw4GWXGJ)

<!-- END GENERATED -->
