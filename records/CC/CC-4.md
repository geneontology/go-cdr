---
id: CC-4
title: Annotate residence, not transit.
status: proposed
topic: CC
provenance: GOC_PLUS
provenance_note: '[GOC+] GOC stated the transit rule in minutes but never in a guideline page. The evidence
  tiers are ours.'
aspects:
- C
evidence_codes:
- IBA
- ISS
- IEA
go_terms:
- term_id: GO:0005789
  label: endoplasmic reticulum membrane
differences:
- prior_source: '[Manager Call 2017-04-19](https://wiki.geneontology.org/index.php/Manager_Call_2017-04-19);
    [#4573](https://github.com/geneontology/go-annotation/issues/4573)'
  prior_said: Secreted proteins not annotated to the secretory pathway; no documentation; UniProt keeps
    "real" retention
  we_recommend: Transit is not residence, with evidence tiers for keeping a resident pool (CC-4)
  why: The GOC rule was stated only in minutes and a ticket; curators need a test
sources:
- kind: wiki
  title: Manager Call 2017-04-19
  url: https://wiki.geneontology.org/index.php/Manager_Call_2017-04-19
- kind: wiki
  title: Annotation Conf. Call 2017-05-09
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09
- kind: issue
  title: go-annotation#4573
  url: https://github.com/geneontology/go-annotation/issues/4573
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
date: '2026-11-15'
---

# CC-4. Annotate residence, not transit.

## Decision

Annotate residence, not transit.

## Context

Every secreted, plasma-membrane and lysosomal protein passes through the ER and Golgi. That
passage is real, but the protein does not carry out its function there, and the GOC position
since 2017 is that secreted proteins are not annotated to the secretory pathway
([Manager Call 2017-04-19](https://wiki.geneontology.org/index.php/Manager_Call_2017-04-19);
[Annotation Conf. Call 2017-05-09](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09)).
The 2023 discussion of UniProt keyword mappings restated this: Golgi localization of a protein
destined for the plasma membrane is not where it acts and is inappropriate for GO; Swiss-Prot
likewise omits ER and Golgi locations seen only when secretion is blocked with drugs
([go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573)).

Operational tests (from the repo's ER and Golgi batches, [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html) rule 7):

| Evidence for an ER or Golgi row on a protein that acts elsewhere | Action |
|---|---|
| Direct evidence on the gene: endogenous protein in its native cell, marker-confirmed, without secretion block | keep, `KEEP_AS_NON_CORE` |
| Wild-type tagged protein showing a minor marker-confirmed pool beside the main location | keep, `KEEP_AS_NON_CORE` |
| Retention only of an overexpressed or disease-mutant protein, or only under brefeldin A or similar | `MARK_AS_OVER_ANNOTATED` |
| A synthesis row (IBA, ISS, IEA) whose source shows only transit | `MARK_AS_OVER_ANNOTATED` |
| Regulated retention as part of the protein's control (for example ER retention by modification) | keep; may be core if the regulation is the function |

Topology does not force a sub-compartment on a transit pool: a TM protein passing through the
ER gets no `GO:0005789` endoplasmic reticulum membrane row.

## Application

*Example.* ATP1A1's ISS Golgi row rests on a rat paper that measured ER-to-Golgi transit with
reporters; the alpha subunit was never shown in a marker-defined Golgi compartment. The row is
`MARK_AS_OVER_ANNOTATED`, matching the ER call for the same source
([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html), Golgi batch 1).

Three non-resident pools are distinct from biosynthetic transit and are real locations:
retrograde or ligand-driven pools reached from the plasma membrane (ADRB2 palmitoylation at the
Golgi), adaptor-dependent recycling stops, and internalized receptors that signal from
endosomes. Annotate these with `located_in` (or `is_active_in` when signalling from that
compartment is shown, as for endosomal GPCR signalling cited in the 2017 call), as non-core
unless the activity is core.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] GOC stated the transit rule in minutes but never in a guideline page. The evidence tiers are ours. |
| Date | 2026-11-15 |
| Evidence codes | IBA, ISS, IEA |
| GO terms | `GO:0005789` endoplasmic reticulum membrane |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Manager Call 2017-04-19](https://wiki.geneontology.org/index.php/Manager_Call_2017-04-19); [#4573](https://github.com/geneontology/go-annotation/issues/4573) | Secreted proteins not annotated to the secretory pathway; no documentation; UniProt keeps "real" retention | Transit is not residence, with evidence tiers for keeping a resident pool (CC-4) | The GOC rule was stated only in minutes and a ticket; curators need a test |

## Sources

- wiki: [Manager Call 2017-04-19](https://wiki.geneontology.org/index.php/Manager_Call_2017-04-19)
- wiki: [Annotation Conf. Call 2017-05-09](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09)
- issue: [go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573)
- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)

<!-- END GENERATED -->
