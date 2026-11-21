---
id: CC-7
title: Examine every root organelle row that comes from synthesis (IBA, ISS, ISO, IEA, IC, RCA); keep
  it only if the organelle claim survives the check.
status: proposed
topic: CC
provenance: NEW
aspects:
- C
evidence_codes:
- IBA
- ISS
- ISO
- IEA
open_questions:
- '**Validation.** Should the repo warn on ACCEPTed root-only synthesis rows whose `reason` records no
  check (CC-7)?'
sources:
- kind: issue
  title: go-annotation#5546
  url: https://github.com/geneontology/go-annotation/issues/5546
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# CC-7. Examine every root organelle row that comes from synthesis (IBA, ISS, ISO, IEA, IC, RCA); keep it only if the organelle claim survives the check.

## Decision

Examine every root organelle row that comes from synthesis (IBA, ISS, ISO, IEA, IC, RCA); keep it only if the organelle claim survives the check.

## Context

A propagated or inferred row has no assay limit to excuse a coarse term. Either the source knew
the sub-compartment and the propagation lost it, or the source did not know the location.
Check the source:

- **IBA:** read the PAINT node's experimental descendants. Is the target inside the clade that
  shares the location, or does the node mix cytosolic and organellar paralogs? GO's own advice
  for mixed trees is not to propagate CC at all
  ([go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546), alanyl-tRNA
  synthetases); see [phylogenetic-propagation.md](../PH/README.md).
- **IEA:** check the mapping (UniProt subcellular-location keyword, InterPro2GO, ARBA) and
  whether the gene has the feature the mapping assumes. Read the evidence tag on each location
  item of a UniProt SUBCELLULAR LOCATION line separately.
- **ISS/ISO and Ensembl projections:** trace to the donor paper; several rest on an unmarked
  staining pattern or "data not shown".

If the organelle claim holds, `ACCEPT` (or `KEEP_AS_NON_CORE`) and record the check in
`reason`. If not, `MARK_AS_OVER_ANNOTATED`, or `REMOVE` for a demonstrably wrong mapping or
over-propagation.

## Application

*Example.* CEPT1's IBA Golgi row comes from a PAINT node seeded only by the CHPT1 lineage;
brefeldin A moves CPT1 but not CEPT1, which sits in the ER and nuclear membranes. The row is
`MARK_AS_OVER_ANNOTATED` ([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html), Golgi batch 1).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| Evidence codes | IBA, ISS, ISO, IEA |

## Open questions

1. **Validation.** Should the repo warn on ACCEPTed root-only synthesis rows whose `reason` records no check (CC-7)?

## Sources

- issue: [go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546)
- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
