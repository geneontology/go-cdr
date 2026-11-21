---
id: IEA-15
title: Do not launder a prediction into manual evidence
status: proposed
topic: IEA
provenance: GOC
evidence_codes:
- ISS
- ISO
- ISA
- ISM
- IC
- IEA
go_terms:
- term_id: GO:0000981
  label: DNA-binding transcription factor activity, RNA polymerase II-specific
sources:
- kind: wiki
  title: IEA
  url: https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29
- kind: wiki
  title: ISM
  url: https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29
- kind: wiki
  title: 'Annotation consistency: IEA, ISS, IC'
  url: https://wiki.geneontology.org/index.php/Annotation_consistency%3A_IEA%2C_ISS%2C_IC_Usage_Discussion
- kind: issue
  title: go-annotation#3007
  url: https://github.com/geneontology/go-annotation/issues/3007
- kind: drive
  title: Draft AI policy statement
  url: https://drive.google.com/open?id=1leeuPb1WDgyORZHrxhapW9HKLTPrCi6xsMi-KaZNCIQ
date: '2026-11-15'
---

# IEA-15. Do not launder a prediction into manual evidence

## Decision

A curator who reviews an electronic prediction and agrees with it makes a new annotation with the
evidence they actually used: ISS, ISA or ISO for a reviewed similarity (with the match in
`WITH/FROM` and `GO_REF:0000024` or the paper), ISM for a reviewed sequence-model match. Do not copy
an IEA into a manual record, do not use an IEA as the evidence for a GO-CAM activity, and do not let
a computational prediction override experimental evidence in the same gene.

## Context

if sequence-based evidence has been reviewed by a curator, the code is ISS or a child,
not IEA ([wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29);
[wiki: ISM](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29)). Converting
an IEA to ISS makes sense for InterPro2GO and Compara, where sequence similarity is the basis, and
not for vocabulary mappings, where there is none ([wiki: Annotation consistency: IEA, ISS, IC](https://wiki.geneontology.org/index.php/Annotation_consistency%3A_IEA%2C_ISS%2C_IC_Usage_Discussion);
archived). Strong experimental evidence that a protein is a transcription coregulator overrides
computational evidence that it is a DNA-binding transcription factor, and the conflicting InterPro
mapping should be disputed; a mapping InterPro has already removed cannot support an annotation
([go-annotation#3007](https://github.com/geneontology/go-annotation/issues/3007)). For AI-generated
predictions, the IEA working group's draft position is that GO does not accept them without review by
a trained curator, and that training on IEA rows risks a loop that amplifies errors
([Drive: Draft AI policy statement](https://drive.google.com/open?id=1leeuPb1WDgyORZHrxhapW9HKLTPrCi6xsMi-KaZNCIQ);
draft, partly superseded).

## Application

Worked example: RCOR1, RCOR2, RCOR3 and MIDEAS carried `GO:0000981` DNA-binding transcription factor
activity, RNA polymerase II-specific by ISM from `IPR001005` and `IPR009057`, whose DNA-binding
mappings InterPro had already removed; they are corepressors and the rows were removed
([go-annotation#3007](https://github.com/geneontology/go-annotation/issues/3007)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | ISS, ISO, ISA, ISM, IC, IEA |
| GO terms | `GO:0000981` DNA-binding transcription factor activity, RNA polymerase II-specific |

## Sources

- wiki: [IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)
- wiki: [ISM](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29)
- wiki: [Annotation consistency: IEA, ISS, IC](https://wiki.geneontology.org/index.php/Annotation_consistency%3A_IEA%2C_ISS%2C_IC_Usage_Discussion)
- issue: [go-annotation#3007](https://github.com/geneontology/go-annotation/issues/3007)
- drive: [Draft AI policy statement](https://drive.google.com/open?id=1leeuPb1WDgyORZHrxhapW9HKLTPrCi6xsMi-KaZNCIQ)

<!-- END GENERATED -->
