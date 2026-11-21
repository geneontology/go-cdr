---
id: CAM-6
title: Link metabolic steps through the ChEBI product; use `provides input for` only when the intermediate
  is a macromolecule or has no ChEBI entry.
status: proposed
topic: CAM
provenance: GOC
provenance_note: '[GOC]. This reverses older documentation that named `provides input for` as the metabolic-pathway
  relation (see Differences).'
go_terms:
- term_id: GO:0061621
  label: canonical glycolysis
- term_id: GO:0004347
  label: glucose-6-phosphate isomerase activity
related:
- CAM-14
differences:
- prior_source: '[Drive: GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4)
    (c. 2016)'
  prior_said: '`provides input for` is the relation for metabolic pathways, where one activity makes a
    small molecule for the next.'
  we_recommend: Link through the ChEBI product with `has output`/`has input`; reserve `provides input
    for` for macromolecular or non-ChEBI intermediates (CAM-6).
  why: Follows the 2023 relation page; explicit molecules are checkable.
sources:
- kind: wiki
  title: Provides input for (reviewed 2023)
  url: https://wiki.geneontology.org/index.php/Provides_input_for
- kind: drive
  title: GO-CAM Curation Documentation
  url: https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4
date: '2026-11-15'
---

# CAM-6. Link metabolic steps through the ChEBI product; use `provides input for` only when the intermediate is a macromolecule or has no ChEBI entry.

## Decision

Link metabolic steps through the ChEBI product; use `provides input for` only when the intermediate is a macromolecule or has no ChEBI entry.

## Context

When an upstream activity's product is the next activity's substrate and the
product is in ChEBI, write `[upstream] has output [ChEBI]` and `[downstream]
has input [ChEBI]`. The reasoner derives the causal link. Use `provides input
for` (RO:0002413) only when the intermediate is a modified protein or RNA, or a
chemical with no ChEBI identifier.

*Rationale.* Explicit molecules make the model checkable against Rhea and
Reactome reactions and make transport steps visible. A bare `provides input
for` hides what moves between the steps, and hence whether it crosses a
membrane (CAM-14).

## Application

*Example.* In canonical glycolysis (`GO:0061621`), hexokinase `has output`
CHEBI:61548 D-glucopyranose 6-phosphate(2-), which is the `has input` of
`GO:0004347` glucose-6-phosphate isomerase activity. In contrast, AKT1
phosphorylates RAC1, and phosphorylated RAC1 (no ChEBI entry) is the input of
FBXL19's substrate-adaptor activity, so AKT1's activity `provides input for`
FBXL19's (model `63d320cd00001536`, PMID:23512198).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC]. This reverses older documentation that named `provides input for` as the metabolic-pathway relation (see Differences). |
| Date | 2026-11-15 |
| Related | [CAM-14](CAM-14.md) |
| GO terms | `GO:0061621` canonical glycolysis; `GO:0004347` glucose-6-phosphate isomerase activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4) (c. 2016) | `provides input for` is the relation for metabolic pathways, where one activity makes a small molecule for the next. | Link through the ChEBI product with `has output`/`has input`; reserve `provides input for` for macromolecular or non-ChEBI intermediates (CAM-6). | Follows the 2023 relation page; explicit molecules are checkable. |

## Sources

- wiki: [Provides input for (reviewed 2023)](https://wiki.geneontology.org/index.php/Provides_input_for)
- drive: [GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4)

<!-- END GENERATED -->
