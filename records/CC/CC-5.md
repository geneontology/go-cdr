---
id: CC-5
title: Record sequestration and regulated relocation with `located_in`; reserve `is_active_in` for the
  compartment where the protein works.
status: proposed
topic: CC
provenance: GOC_PLUS
provenance_note: '[GOC+] Resolves the 2014 PomBase-versus-location-of-action disagreement by relation
  choice.'
aspects:
- C
differences:
- prior_source: '[Ashburner et al. 2000](https://europepmc.org/article/MED/10802651) as quoted in the
    2017 GOC deck; [2017-05-09 call](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09)'
  prior_said: CC is where the gene product is active
  we_recommend: CC records presence (`located_in`) and activity (`is_active_in`) separately; sequestration
    pools are annotated (CC-5)
  why: Reconciles the location-of-action view with PomBase's practice ([#1226](https://github.com/geneontology/go-annotation/issues/1226))
sources:
- kind: issue
  title: go-annotation#1226
  url: https://github.com/geneontology/go-annotation/issues/1226
- kind: wiki
  title: Annotation Conf. Call 2017-05-09
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09
- kind: drive
  title: GOC 2017-10 Cellular_Component_Annotations
  url: https://drive.google.com/open?id=19QGQd6Ps0xQssV6LBPgPwVHNhuDmXFPgFDGjPRehUkM
- kind: issue
  title: go-annotation#4573
  url: https://github.com/geneontology/go-annotation/issues/4573
date: '2026-11-15'
---

# CC-5. Record sequestration and regulated relocation with `located_in`; reserve `is_active_in` for the compartment where the protein works.

## Decision

Record sequestration and regulated relocation with `located_in`; reserve `is_active_in` for the compartment where the protein works.

## Context

A transcription factor held in the cytoplasm until signalled, a recombination protein excluded
from the nucleus in interphase, or an ER-anchored SREBP precursor are all in a real place by a
specific mechanism. PomBase argued that such locations should be annotated because they
reflect purpose
([go-annotation#1226](https://github.com/geneontology/go-annotation/issues/1226)); the
GOC location-of-action view argued they should not
([Annotation Conf. Call 2017-05-09](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09)).
GAF 2.2's two relations let both views coexist: annotate the sequestering compartment with
`located_in`, the working compartment with `is_active_in`.

## Application

*Example.* DAF-16: `located_in` cytoplasm (sequestered, inactive), `is_active_in` nucleus
(transcription factor activity), the categories used in the 2017 GOC deck
([Drive: GOC 2017-10 Cellular_Component_Annotations](https://drive.google.com/open?id=19QGQd6Ps0xQssV6LBPgPwVHNhuDmXFPgFDGjPRehUkM)).
If the sequestering protein has its own activity there (a sequestering protein in the cytosol),
that protein `is_active_in` the cytosol and its target is the `has_input`
([go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573)).

Material released by cell lysis is not a location. Histones spilled from a lysed cell are not
`located_in` extracellular region; neutrophil extracellular traps, which are a physiological
structure, are a defensible exception
([go-annotation#1226](https://github.com/geneontology/go-annotation/issues/1226)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] Resolves the 2014 PomBase-versus-location-of-action disagreement by relation choice. |
| Date | 2026-11-15 |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Ashburner et al. 2000](https://europepmc.org/article/MED/10802651) as quoted in the 2017 GOC deck; [2017-05-09 call](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09) | CC is where the gene product is active | CC records presence (`located_in`) and activity (`is_active_in`) separately; sequestration pools are annotated (CC-5) | Reconciles the location-of-action view with PomBase's practice ([#1226](https://github.com/geneontology/go-annotation/issues/1226)) |

## Sources

- issue: [go-annotation#1226](https://github.com/geneontology/go-annotation/issues/1226)
- wiki: [Annotation Conf. Call 2017-05-09](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09)
- drive: [GOC 2017-10 Cellular_Component_Annotations](https://drive.google.com/open?id=19QGQd6Ps0xQssV6LBPgPwVHNhuDmXFPgFDGjPRehUkM)
- issue: [go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573)

<!-- END GENERATED -->
