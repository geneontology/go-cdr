---
id: REV-10
title: Necessity is not participation
status: proposed
topic: REV
provenance: NEW
provenance_note: '[NEW], sharpening the GOC''s downstream-process and cargo guidance.'
go_terms:
- term_id: GO:0002003
  label: angiotensin maturation
- term_id: GO:0016486
  label: peptide hormone processing
sources:
- kind: wiki
  title: QCQA call 2018-03-20
  url: https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# REV-10. Necessity is not participation

## Decision

A gene product is involved in a process only if it does some of the work: catalyses a step,
or supplies structure or chemistry that a step depends on. Being required for the process,
consumed by it, or the thing it acts on is not participation.

## Context

Knockout abolishes the outcome; rescue restores it. Both are equally true of a substrate. A GAF
row cannot distinguish necessity evidence from participation evidence, so ask explicitly which
entity performs the step. The 2018 QC call listed "annotating a cargo or target to a process"
among the recurring error classes
([wiki: QCQA call 2018-03-20](https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20)).

## Application

*Example.* `GO:0002003` angiotensin maturation is a subclass of `GO:0016486` peptide hormone
processing (verified). It is annotated to the proteases (REN, ACE, ACE2 and others) and to no
angiotensinogen in human, mouse or rat. A review that proposed it for AGT as a missing
annotation was wrong: AGT supplies no residue beyond the cleaved bond and catalyses nothing.
The convention has principled exceptions where the substrate does work: thyroglobulin is a
scaffold for thyroid hormone generation, fibrin a cofactor in fibrinolysis, C3 the chemistry
of complement activation ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), worked example from
`genes/human/AGT`).

Apply the same test to existing rows: a `REMOVE` or `MARK_AS_OVER_ANNOTATED` is due when the
only evidence is necessity and the gene is the cargo, substrate or target.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW], sharpening the GOC's downstream-process and cargo guidance. |
| Date | 2026-11-15 |
| GO terms | `GO:0002003` angiotensin maturation; `GO:0016486` peptide hormone processing |

## Sources

- wiki: [QCQA call 2018-03-20](https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
