---
id: PH-2
title: Seed an IBD only from experimental annotations that make the claim the term makes
status: proposed
topic: PH
provenance: GOC_PLUS
provenance_note: '[GOC+]. The aspect check is our addition to the GOC seed rule.'
evidence_codes:
- EXP
- IDA
- IPI
- IMP
- IGI
- IEP
- HTP
- IBD
- IEA
go_terms:
- term_id: GO:0004096
  label: catalase activity
- term_id: GO:0098869
  label: cellular oxidant detoxification
related:
- PH-3
differences:
- prior_source: '[wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)'
  prior_said: Only experimental annotations may seed an IBD.
  we_recommend: Also check that the seed's evidence type supports the aspect (IMP does not support MF)
    (PH-2).
  why: Experimental-code seeds have carried phenotype-derived MFs to whole families (ccmC).
sources:
- kind: wiki
  title: PAINT annotation guidelines
  url: https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines
- kind: web
  title: IBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html
- kind: issue
  title: go-annotation#4697
  url: https://github.com/geneontology/go-annotation/issues/4697
date: '2026-11-15'
---

# PH-2. Seed an IBD only from experimental annotations that make the claim the term makes

## Decision

An IBD must rest on experimental annotations (IDA, IMP, IGI, IPI, IEP, EXP and their HTP
counterparts under PH-3) on descendant gene products. Before using a seed, check that its
evidence type can support the aspect: an IMP phenotype grounds "needed for" a process, not a
molecular function.

## Context

only experimental annotations may support ancestral inference
([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)).
That rule says nothing about whether the experiment supports the aspect, and the repo found
IBDs whose sole seed was a molecular-function row derived from a pleiotropic mutant phenotype
([IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html), pattern 16). The cheap diagnostic is to read the seed's
sibling rows from the same reference: a block of IMP rows spanning unrelated processes is a
phenotype list, and the MF row inside it cannot stand. The 2023 PAINT tracker discussion of
TMX3 (PTHR46426) reached the same place: do not propagate an MF from a single IMP when a human
IDA in the family points to a different activity ([go-annotation#4697](https://github.com/geneontology/go-annotation/issues/4697)).

## Application

Worked example: the IBD for `GO:0004096` catalase activity on PANTHER node PTN001247822
(PTHR30071, CcmC) has one seed, *P. aeruginosa* CcmC, whose catalase row is an IMP from a
paper that also yields IMP rows for pyoverdine biosynthesis and several motility processes.
That set is the phenotype of a strain with no mature c-type cytochromes. Every CcmC leaf
inherits catalase activity, and the inter-ontology rule then adds `GO:0098869` cellular
oxidant detoxification as IEA. Withdrawing the seed must withdraw both
([IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html), §ccmC). Record such a case as
`root_cause: SOURCE_BAD` with `failure_modes: [SOURCE_EVIDENCE_WEAK]`.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The aspect check is our addition to the GOC seed rule. |
| Date | 2026-11-15 |
| Related | [PH-3](PH-3.md) |
| Evidence codes | EXP, IDA, IPI, IMP, IGI, IEP, HTP, IBD, IEA |
| GO terms | `GO:0004096` catalase activity; `GO:0098869` cellular oxidant detoxification |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) | Only experimental annotations may seed an IBD. | Also check that the seed's evidence type supports the aspect (IMP does not support MF) (PH-2). | Experimental-code seeds have carried phenotype-derived MFs to whole families (ccmC). |

## Sources

- wiki: [PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)
- web: [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)
- issue: [go-annotation#4697](https://github.com/geneontology/go-annotation/issues/4697)

<!-- END GENERATED -->
