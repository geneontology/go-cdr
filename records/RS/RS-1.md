---
id: RS-1
title: Decide between "part of X" and "regulation of X" by locating the gene product's activity relative
  to the process boundaries
status: proposed
topic: RS
provenance: GOC
aspects:
- P
sources:
- kind: wiki
  title: Annotating regulation
  url: https://wiki.geneontology.org/index.php/Annotating_regulation
- kind: drive
  title: Breakout – Annotating to a process or its regulation, 2022
  url: https://drive.google.com/open?id=1ii8kFkraHYYSGThmYZq9i6EyqNmY4v91hpGuuvIMunk
- kind: issue
  title: go-annotation#1687
  url: https://github.com/geneontology/go-annotation/issues/1687
date: '2026-11-15'
---

# RS-1. Decide between "part of X" and "regulation of X" by locating the gene product's activity relative to the process boundaries

## Decision

**Statement.** First establish where X starts and ends: from the term definition, a GO-CAM, or a current review of the pathway. If the gene product performs one of the activities between the start and the end, it is `involved_in` X. If it acts from outside X to start, stop or modulate it, it is `involved_in` regulation of X. If you cannot tell, annotate X with `acts upstream of or within` and a sign.

## Context

These are Guidelines 1 and 2 of [wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation), restated at the 2022 GOC breakout ([Drive: Breakout – Annotating to a process or its regulation, 2022](https://drive.google.com/open?id=1ii8kFkraHYYSGThmYZq9i6EyqNmY4v91hpGuuvIMunk)). The 2017 decision that "gene product involved_in X regulation" uses the plain `involved_in` relation, rather than a separate `regulates` relation, makes the term carry the regulation ([go-annotation#1687](https://github.com/geneontology/go-annotation/issues/1687)).

## Application

**Worked example.** Yeast Atg1 is a protein kinase needed to form autophagic vesicles. Authors' language could support either autophagosome formation or its regulation. SGD annotated Atg1 to the process because, once Atg1 is active, the decision to proceed with autophagy has already been taken. The genes upstream of that decision regulate the pathway ([wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |

## Sources

- wiki: [Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation)
- drive: [Breakout – Annotating to a process or its regulation, 2022](https://drive.google.com/open?id=1ii8kFkraHYYSGThmYZq9i6EyqNmY4v91hpGuuvIMunk)
- issue: [go-annotation#1687](https://github.com/geneontology/go-annotation/issues/1687)

<!-- END GENERATED -->
