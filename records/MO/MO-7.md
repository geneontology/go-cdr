---
id: MO-7
title: Locate symbiont products in host compartments with host CC terms, and virion proteins with virion
  terms.
status: proposed
topic: MO
provenance: GOC
go_terms:
- term_id: GO:0018995
  label: host cellular component
- term_id: GO:0030430
  label: host cell cytoplasm
- term_id: GO:0042025
  label: host cell nucleus
- term_id: GO:0020002
  label: host cell plasma membrane
- term_id: GO:0033644
  label: host cell membrane
- term_id: GO:0044423
  label: virion component
- term_id: GO:0019028
  label: viral capsid
- term_id: GO:0055036
  label: virion membrane
- term_id: GO:0019031
  label: viral envelope
sources:
- kind: drive
  title: host_symbiont_annotation
  url: https://drive.google.com/open?id=1NiJfYB4JmClhbsr4G3Xwwr-6Bw4GWXGJ
- kind: web
  title: GOCAM_COMPARTMENTS
  url: https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html
- kind: drive
  title: Multi-species terms - documentation to review
  url: https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU
date: '2026-11-15'
---

# MO-7. Locate symbiont products in host compartments with host CC terms, and virion proteins with virion terms.

## Decision

Locate symbiont products in host compartments with host CC terms, and virion proteins with virion terms.

## Context

A symbiont protein that acts inside or on a host cell takes a term under
`GO:0018995` host cellular component (`GO:0030430` host cell cytoplasm,
`GO:0042025` host cell nucleus, `GO:0020002` host cell plasma membrane,
`GO:0033644` host cell membrane), not the plain cellular term. A structural
protein of the virus particle takes a term under `GO:0044423` virion component
(`GO:0019028` viral capsid, `GO:0055036` virion membrane, `GO:0019031` viral
envelope). Host proteins that are incorporated into virions are not annotated to
virion terms. The plain cellular terms (cytoplasm, nucleus) are for gene
products located in the organism that makes them under normal conditions.

*Rationale.* The host branch exists to keep pathological localisations out of
the normal CC annotations
([Drive: host_symbiont_annotation](https://drive.google.com/open?id=1NiJfYB4JmClhbsr4G3Xwwr-6Bw4GWXGJ)).
For GO-CAM, host CC terms do not resolve to a compartment in the repository's
spatial model; edges into them cross organisms
([GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0018995` host cellular component; `GO:0030430` host cell cytoplasm; `GO:0042025` host cell nucleus; `GO:0020002` host cell plasma membrane; `GO:0033644` host cell membrane; `GO:0044423` virion component; `GO:0019028` viral capsid; `GO:0055036` virion membrane; `GO:0019031` viral envelope |

## Sources

- drive: [host_symbiont_annotation](https://drive.google.com/open?id=1NiJfYB4JmClhbsr4G3Xwwr-6Bw4GWXGJ)
- web: [GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)
- drive: [Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU)

<!-- END GENERATED -->
