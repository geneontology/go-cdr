---
id: CC-9
title: A soluble protein stably tethered to an organelle by a named integral partner gets the cytoplasmic-side
  term; brief or regulated recruitment stays at the root.
status: proposed
topic: CC
provenance: NEW
aspects:
- C
evidence_codes:
- IC
go_terms:
- term_id: GO:0098554
  label: cytoplasmic side of endoplasmic reticulum membrane
- term_id: GO:0005789
  label: endoplasmic reticulum membrane
- term_id: GO:0099617
  label: matrix side of mitochondrial inner membrane
- term_id: GO:0032473
  label: cytoplasmic side of mitochondrial outer membrane
- term_id: GO:0098574
  label: cytoplasmic side of lysosomal membrane
- term_id: GO:0160281
  label: cytoplasmic side of trans-Golgi network membrane
- term_id: GO:0042406
  label: extrinsic component of endoplasmic reticulum membrane
related:
- CC-10
differences:
- prior_source: '[#5694](https://github.com/geneontology/go-annotation/issues/5694) (2025, open)'
  prior_said: Cytoplasmic side and extrinsic component are separate hierarchies; a protein may carry both
  we_recommend: Use the cytoplasmic-side term for stably tethered soluble proteins, only under the four-part
    test (CC-9)
  why: Gives a decision rule where the thread gave a structure; avoids terms slated for obsoletion
open_questions:
- '**Side-of-membrane terms for every organelle.** GO lacks cytoplasmic-side terms for the Golgi stack
  and the peroxisome (CC-9). Should GO add them, or retire side terms in favour of UniProt topology as
  it did for integral terms?'
sources:
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
- kind: issue
  title: go-annotation#5694
  url: https://github.com/geneontology/go-annotation/issues/5694
date: '2026-11-15'
---

# CC-9. A soluble protein stably tethered to an organelle by a named integral partner gets the cytoplasmic-side term; brief or regulated recruitment stays at the root.

## Decision

A soluble protein stably tethered to an organelle by a named integral partner gets the cytoplasmic-side term; brief or regulated recruitment stays at the root.

## Context

GO's intrinsic and extrinsic component terms do not say which side a protein is on. The
"cytoplasmic side of X membrane" terms do, and are defined to include proteins "peripherally
associated" with that leaflet. `GO:0098554` cytoplasmic side of endoplasmic reticulum membrane
is `part_of` `GO:0005789`, so it refines the membrane term rather than avoiding it. The route
needs all four of: (a) direct evidence the endogenous protein is at the organelle; (b) a named
integral membrane protein of the organelle that binds it; (c) dependence on that partner
(knockout or a binding mutant releases or destabilises the protein); (d) cytosolic synthesis
with no signal peptide or targeting sequence, checked in the literature as well as UniProt
features. A protein failing (d), such as a matrix protein held by an inner-membrane partner,
gets the side term for its own compartment (`GO:0099617` matrix side of mitochondrial inner
membrane).

Other side terms exist for the mitochondrial outer membrane (`GO:0032473`), lysosome
(`GO:0098574`) and trans-Golgi network (`GO:0160281`), but none for the Golgi stack or the
peroxisome; a case there becomes a `proposed_new_terms` entry, not a forced narrower term.
Signalling, stress or autophagy recruitment, Rab-dependent docking, and cycling complexes such
as SRP are not tethering.

## Application

*Example.* UFSP2 has no TM or signal peptide; endogenous UFSP2 is lost in ODR4-knockout cells;
ODR4 is a transmembrane ER protein. UFSP2 gains a `NEW` IC `GO:0098554` row beside its ACCEPTed
ER root rows. UFL1 and CDK5RAP3, held by DDRGK1, keep their direct-evidence `GO:0005789` rows
([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html), 2026-11-11 note).

GO's answer to the question of when to use `GO:0042406` extrinsic component of endoplasmic
reticulum membrane versus `GO:0098554` is that the two hierarchies classify different things
(loosely bound versus leaflet) and a protein may carry both
([go-annotation#5694](https://github.com/geneontology/go-annotation/issues/5694)). We prefer the
side term because it says more and because the extrinsic terms were slated for obsoletion
(CC-10).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| Related | [CC-10](CC-10.md) |
| Evidence codes | IC |
| GO terms | `GO:0098554` cytoplasmic side of endoplasmic reticulum membrane; `GO:0005789` endoplasmic reticulum membrane; `GO:0099617` matrix side of mitochondrial inner membrane; `GO:0032473` cytoplasmic side of mitochondrial outer membrane; `GO:0098574` cytoplasmic side of lysosomal membrane; `GO:0160281` cytoplasmic side of trans-Golgi network membrane; `GO:0042406` extrinsic component of endoplasmic reticulum membrane |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CC-9-E1](CC-9.examples.yaml): A NEW cytoplasmic side of ER membrane row for a partner-tethered protease | Conformant | UFSP2 located_in GO:0098554 cytoplasmic side of endoplasmic reticulum membrane (IC, PMID:35926457) |
| [CC-9-E2](CC-9.examples.yaml): A cytoplasmic side of Golgi membrane row where the record says no such term exists | Contested | HID1 located_in GO:0098548 cytoplasmic side of Golgi membrane (IDA, PMID:21337012) |
| [CC-10-E1](CC-10.examples.yaml): A generic membrane IBA row refined to the leaflet and the TGN membrane (from [CC-10](CC-10.md)) | Conformant | HID1 is_active_in GO:0016020 membrane (IBA, GO_REF:0000033) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [#5694](https://github.com/geneontology/go-annotation/issues/5694) (2025, open) | Cytoplasmic side and extrinsic component are separate hierarchies; a protein may carry both | Use the cytoplasmic-side term for stably tethered soluble proteins, only under the four-part test (CC-9) | Gives a decision rule where the thread gave a structure; avoids terms slated for obsoletion |

## Open questions

1. **Side-of-membrane terms for every organelle.** GO lacks cytoplasmic-side terms for the Golgi stack and the peroxisome (CC-9). Should GO add them, or retire side terms in favour of UniProt topology as it did for integral terms?

## Sources

- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)
- issue: [go-annotation#5694](https://github.com/geneontology/go-annotation/issues/5694)

<!-- END GENERATED -->
