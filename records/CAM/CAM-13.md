---
id: CAM-13
title: Give each activity one location that resolves to a distinct compartment.
status: proposed
topic: CAM
provenance: NEW
provenance_note: '[GOC] for one location and no complexes; [NEW] for the resolvability requirement and
  the nuclear-chromosome preference.'
go_terms:
- term_id: GO:0000228
  label: nuclear chromosome
- term_id: GO:0000785
  label: chromatin
- term_id: GO:0016020
  label: membrane
- term_id: GO:0005886
  label: plasma membrane
- term_id: GO:0030430
  label: host cell cytoplasm
- term_id: GO:0042025
  label: host cell nucleus
related:
- MO-7
differences:
- prior_source: '[Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)'
  prior_said: Location may be "transmembrane"; a reviewer comment points to GO:0044214.
  we_recommend: '`GO:0005886` plasma membrane for transmembrane receptors (CAM-13).'
  why: GO:0044214 "spanning component of plasma membrane" is obsolete.
- prior_source: '[Drive: GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4)'
  prior_said: 'Location: any GO CC term except complexes.'
  we_recommend: Location must resolve to a distinct compartment; chromatin becomes nuclear chromosome
    (CAM-13).
  why: GO's chromatin has no `part_of` path to nucleus; 293 activities in 104 models resolve nowhere.
open_questions:
- '**Chromatin.** Should GO add a `part_of` path from chromatin to nucleus for eukaryotes (via a taxon-specific
  class), or should curators be required to use nuclear chromosome? The repo rule (CAM-13) assumes the
  latter.'
sources:
- kind: drive
  title: GO-CAM modeling guidelines
  url: https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA
- kind: web
  title: GOCAM_COMPARTMENTS
  url: https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html
- kind: repo
  title: gocam-curation compartments reference
  url: https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/compartments.md
date: '2026-11-15'
---

# CAM-13. Give each activity one location that resolves to a distinct compartment.

## Decision

Give each activity one location that resolves to a distinct compartment.

## Context

`occurs in` takes a GO cellular component term that is not a protein-containing
complex (the complex belongs in the enabler). The term should resolve, through
`is_a`/`part_of`, to one compartment: cytosol, nuclear lumen, a membrane, a
lumen, the extracellular region. Prefer the precise term:

- Use `GO:0000228` nuclear chromosome rather than `GO:0000785` chromatin. In GO,
  chromatin is part of chromosome and chromosome is not part of nucleus
  (prokaryotes have chromosomes), so "chromatin" places the activity nowhere.
  This is the largest single source of unresolved locations: 293 activities in
  104 cached models.
- Name the membrane (plasma membrane, ER membrane), not `GO:0016020` membrane.
- For a transmembrane receptor, use `GO:0005886` plasma membrane, even though
  the catalytic domain faces one side.
- Add a cell type or anatomy only when the specificity is shown to matter, and
  never use a cell type term as the `occurs in` itself.
- For a symbiont activity inside a host, use the host term (`GO:0030430` host
  cell cytoplasm, `GO:0042025` host cell nucleus); see
  [MO-7](../MO/MO-7.md).

*Rationale.* A location that resolves nowhere cannot be checked against
anything, and coarse terms (`cytoplasm`, `nucleus`) hide whether an edge
crosses a membrane.

## Application

*Example.* In BMP9 signalling (`600ced8500002343`), SMAD1 transcription factor
activity occurs in chromatin; the location that says what is meant is nuclear
chromosome.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] [GOC] for one location and no complexes; [NEW] for the resolvability requirement and the nuclear-chromosome preference. |
| Date | 2026-11-15 |
| Related | [MO-7](../MO/MO-7.md) |
| GO terms | `GO:0000228` nuclear chromosome; `GO:0000785` chromatin; `GO:0016020` membrane; `GO:0005886` plasma membrane; `GO:0030430` host cell cytoplasm; `GO:0042025` host cell nucleus |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA) | Location may be "transmembrane"; a reviewer comment points to GO:0044214. | `GO:0005886` plasma membrane for transmembrane receptors (CAM-13). | GO:0044214 "spanning component of plasma membrane" is obsolete. |
| [Drive: GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4) | Location: any GO CC term except complexes. | Location must resolve to a distinct compartment; chromatin becomes nuclear chromosome (CAM-13). | GO's chromatin has no `part_of` path to nucleus; 293 activities in 104 models resolve nowhere. |

## Open questions

1. **Chromatin.** Should GO add a `part_of` path from chromatin to nucleus for eukaryotes (via a taxon-specific class), or should curators be required to use nuclear chromosome? The repo rule (CAM-13) assumes the latter.

## Sources

- drive: [GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)
- web: [GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)
- repo: [gocam-curation compartments reference](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/compartments.md)

<!-- END GENERATED -->
