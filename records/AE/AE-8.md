---
id: AE-8
title: Use `part_of`(BP) on an MF to say which process the activity serves. Make the matching BP annotation
  as a separate row, and do not add a `part_of` the ontology already entails.
status: proposed
topic: AE
provenance: GOC
go_terms:
- term_id: GO:0003924
  label: GTPase activity
- term_id: GO:0048011
  label: neurotrophin TRK receptor signaling pathway
- term_id: GO:0016301
  label: kinase activity
- term_id: GO:0016310
  label: phosphorylation
sources:
- kind: wiki
  title: 'Column 16: Function x Process x Component extensions'
  url: https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions
date: '2026-11-15'
---

# AE-8. Use `part_of`(BP) on an MF to say which process the activity serves. Make the matching BP annotation as a separate row, and do not add a `part_of` the ontology already entails.

## Decision

Use `part_of`(BP) on an MF to say which process the activity serves. Make the matching BP annotation as a separate row, and do not add a `part_of` the ontology already entails.

## Context

**Rule detail.** `enables` GO:0003924 GTPase activity `part_of`(GO:0048011 neurotrophin TRK receptor signaling pathway) should come with a separate `involved_in` GO:0048011 row, so users who ignore column 16 lose nothing. Not: GO:0016301 kinase activity `part_of`(GO:0016310 phosphorylation). It is harmless but adds nothing, because the ontology already links them ([wiki: Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0003924` GTPase activity; `GO:0048011` neurotrophin TRK receptor signaling pathway; `GO:0016301` kinase activity; `GO:0016310` phosphorylation |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [AE-8-E1](AE-8.examples.yaml): An activator activity part_of heme biosynthesis, with the matching BP row from the same paper | Conformant | FXN enables GO:0008047 enzyme activator activity (IDA, PMID:15123683) |
| [AE-8-E2](AE-8.examples.yaml): A part_of on reelin receptor activity that the ontology already entails | Non-conformant | LRP8 enables GO:0038025 reelin receptor activity (ISS, GO_REF:0000024) |

## Sources

- wiki: [Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions)

<!-- END GENERATED -->
