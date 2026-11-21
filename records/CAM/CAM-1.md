---
id: CAM-1
title: 'Model activities, not genes: each activity unit has one function, one enabler, one location chain
  and one process chain.'
status: proposed
topic: CAM
provenance: GOC
go_terms:
- term_id: GO:0004707
  label: MAP kinase activity
- term_id: GO:0005829
  label: cytosol
- term_id: GO:0140367
  label: antibacterial innate immune response
- term_id: GO:0000981
  label: DNA-binding transcription factor activity, RNA polymerase II-specific
- term_id: GO:0005634
  label: nucleus
sources:
- kind: drive
  title: GO-CAM modeling guidelines
  url: https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA
- kind: drive
  title: GO-CAM Curation Documentation
  url: https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4
date: '2026-11-15'
---

# CAM-1. Model activities, not genes: each activity unit has one function, one enabler, one location chain and one process chain.

## Decision

Model activities, not genes: each activity unit has one function, one enabler, one location chain and one process chain.

## Context

An activity unit is an instance of a GO molecular function class, linked to:
the gene product that carries it out (`enabled by`, RO:0002333); where it
happens (`occurs in`, BFO:0000066, one GO cellular component term, optionally
nested `part of` a cell type and an anatomical structure); the process it
contributes to (`part of`, BFO:0000050, one biological process, which may
itself be nested `part of` a larger process); optionally what it acts on
(`has input`, RO:0002233) and what it produces (`has output`, RO:0002234); and
optionally when it happens (`happens during`, RO:0002092, with a GO
biological phase or a developmental stage term).

Each level holds one term. If an activity seems to be part of two unrelated
processes, it is two activities, or one of the processes is a context of the
other and belongs in the nesting.

*Rationale.* This is the shape all consortium specifications share, from the
2016 curation documentation to the 2025 workshop decks. It is what makes the
model decomposable into standard annotations.

## Application

*Example.* In the *C. elegans* intestinal immunity model `568b0f9600000284`,
PMK-1 enables `GO:0004707` MAP kinase activity, occurs in `GO:0005829`
cytosol, and is part of `GO:0140367` antibacterial innate immune response;
ATF-7 enables `GO:0000981` DNA-binding transcription factor activity, RNA
polymerase II-specific, occurring in `GO:0005634` nucleus, in the same process.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0004707` MAP kinase activity; `GO:0005829` cytosol; `GO:0140367` antibacterial innate immune response; `GO:0000981` DNA-binding transcription factor activity, RNA polymerase II-specific; `GO:0005634` nucleus |

## Sources

- drive: [GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)
- drive: [GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4)

<!-- END GENERATED -->
