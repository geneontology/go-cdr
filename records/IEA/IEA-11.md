---
id: IEA-11
title: An inferred annotation falls with its premise
status: proposed
topic: IEA
provenance: GOC_PLUS
evidence_codes:
- ISO
- IEA
go_terms:
- term_id: GO:0004096
  label: catalase activity
- term_id: GO:0098869
  label: cellular oxidant detoxification
related:
- PH-2
sources:
- kind: wiki
  title: IEA
  url: https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29
- kind: web
  title: IBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html
- kind: web
  title: ISO
  url: https://ai4curation.io/ai-gene-review/pages/projects/ISO.html
date: '2026-11-15'
---

# IEA-11. An inferred annotation falls with its premise

## Decision

For a row made by GO's inter-ontology inference (`GO_REF:0000108`, with the premise term in
`WITH/FROM`), review the premise. If the premise annotation is removed, remove the inferred row
too, whatever its own plausibility.

## Context

GO derives annotations along transitive relations between aspects
([wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)).
A wrong MF therefore drags a BP behind it, and the BP survives the MF's removal unless someone
follows the link ([IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html), pattern 16).

## Application

Worked example: CcmC proteins inherit `GO:0004096` catalase activity from a phenotype-derived seed,
and `GO:0098869` cellular oxidant detoxification then arrives as IEA `GO_REF:0000108` with
`GO:0004096` in `WITH/FROM`. Both go together ([phylogenetic-propagation.md, PH-2](../PH/PH-2.md)).
Mouse Akt1's ER location was likewise inferred only from a flattened process row and was removed
with it ([ISO](https://ai4curation.io/ai-gene-review/pages/projects/ISO.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Related | [PH-2](../PH/PH-2.md) |
| Evidence codes | ISO, IEA |
| GO terms | `GO:0004096` catalase activity; `GO:0098869` cellular oxidant detoxification |

## Sources

- wiki: [IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)
- web: [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)
- web: [ISO](https://ai4curation.io/ai-gene-review/pages/projects/ISO.html)

<!-- END GENERATED -->
