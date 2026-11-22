---
id: RS-3
title: Limiting quantities, constitutive prerequisites and substrate supply are not regulation
status: proposed
topic: RS
provenance: GOC_PLUS
provenance_note: '[GOC]. Item 3 is [GOC+]: GOC raised it without resolving it, and we state the default.'
aspects:
- P
sources:
- kind: wiki
  title: Annotating regulation
  url: https://wiki.geneontology.org/index.php/Annotating_regulation
- kind: issue
  title: go-annotation#1955
  url: https://github.com/geneontology/go-annotation/issues/1955
- kind: issue
  title: go-annotation#2431
  url: https://github.com/geneontology/go-annotation/issues/2431
- kind: wiki
  title: Guidelines for checkpoints
  url: https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints
- kind: wiki
  title: Annotation Relations
  url: https://wiki.geneontology.org/index.php/Annotation_Relations
- kind: wiki
  title: Constitutively upstream of
  url: https://wiki.geneontology.org/index.php/Constitutively_upstream_of
date: '2026-11-15'
---

# RS-3. Limiting quantities, constitutive prerequisites and substrate supply are not regulation

## Decision

**Statement.** Do not annotate a gene product to regulation of X only because X slows or stops without it. In particular:

## Context

1. a pathway member whose abundance limits flux, such as receptor number at the surface;
2. a constitutive step that is rate-limiting but not modulated, such as nuclear transport of a signalling component;
3. a process that supplies a substrate or cofactor (folate, ATP, lipids) consumed by X;
4. a gene whose mutation creates a problem that a checkpoint or stress pathway then detects.

**Rationale.** [wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation), Guideline 6, gives the receptor example. In [go-annotation#1955](https://github.com/geneontology/go-annotation/issues/1955), translocation into the nucleus is rate-limiting in the G2/M pathway, but the nuclear pore "isn't doing anything mechanistically" to modulate it. Generic perturbation phenotypes such as cell cycle delay do not justify a regulation term. Folate-generating processes are causally upstream of nucleotide and amino acid metabolism but do not regulate them. When to annotate such dependencies at all remains unsettled ([go-annotation#2431](https://github.com/geneontology/go-annotation/issues/2431)). Mutations that activate a checkpoint show that the checkpoint works, not that the gene is in it ([wiki: Guidelines for checkpoints](https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints)). GO-CAM gives constitutive requirements their own relation, `constitutively upstream of`, separate from regulation ([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)).

## Application

**Worked example.** NRAS palmitoylation by ZDHHC9 is needed for NRAS signalling but is not regulated by the signal. In a GO-CAM it is `constitutively upstream of` the NRAS activity ([wiki: Constitutively upstream of](https://wiki.geneontology.org/index.php/Constitutively_upstream_of)). In a standard annotation, ZDHHC9 does not get "positive regulation of Ras protein signal transduction". It gets its palmitoyltransferase MF and the process that MF is part of.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC]. Item 3 is [GOC+]: GOC raised it without resolving it, and we state the default. |
| Date | 2026-11-15 |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [RS-3-E1](RS-3.examples.yaml): Positive regulation of triglyceride synthesis on GPAT1 moved to the process | Conformant | Gpam involved_in GO:0010867 positive regulation of triglyceride biosynthetic process (ISO, GO_REF:0000096) |
| [RS-3-E2](RS-3.examples.yaml): Positive regulation of fatty acid beta-oxidation on CPT1A marked over-annotated | Conformant | Cpt1a involved_in GO:0032000 positive regulation of fatty acid beta-oxidation (IMP, PMID:19302064) |
| [RS-2-E3](RS-2.examples.yaml): Positive regulation of cell division kept on the kinetochore subunit SPC24 (from [RS-2](RS-2.md)) | Non-conformant | SPC24 acts_upstream_of_or_within GO:0051781 positive regulation of cell division (IMP, PMID:29356153) |

## Sources

- wiki: [Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation)
- issue: [go-annotation#1955](https://github.com/geneontology/go-annotation/issues/1955)
- issue: [go-annotation#2431](https://github.com/geneontology/go-annotation/issues/2431)
- wiki: [Guidelines for checkpoints](https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints)
- wiki: [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- wiki: [Constitutively upstream of](https://wiki.geneontology.org/index.php/Constitutively_upstream_of)

<!-- END GENERATED -->
