---
id: AE-4
title: Use `has_output` only for a specific product the term does not already name, and only for a single
  reaction.
status: proposed
topic: AE
provenance: GOC_PLUS
provenance_note: '[GOC+] (the semantics-over-label reading is ours).'
sources:
- kind: wiki
  title: Has output
  url: https://wiki.geneontology.org/index.php/Has_output
- kind: drive
  title: Harmonizing use of input/output relations in GO (Fall 2024 GOC)
  url: https://drive.google.com/open?id=1GUfrZgxeal3L99v3BCRs4yyrsq_D8yGwq8RwNuQ6OMs
- kind: drive
  title: Review & update Noctua documentation
  url: https://drive.google.com/open?id=13MWyxdfcS78dYz9hg61R4ZS4ydp3OY8Y16LAb3xD3Ug
date: '2026-11-15'
---

# AE-4. Use `has_output` only for a specific product the term does not already name, and only for a single reaction.

## Decision

Use `has_output` only for a specific product the term does not already name, and only for a single reaction.

## Context

**Rationale and example.** DGKA's product in PMID:22627129 is captured together with its input in one annotation. Multiple outputs are allowed only when they belong to the same reaction ([wiki: Has output](https://wiki.geneontology.org/index.php/Has_output)). The same exclusions as for `has_input` apply: no currency metabolites, no products named in the term.

**Primary input and output.** GO has discussed moving annotations to `has_primary_input` (RO:0004009) and `has_primary_output` (RO:0004008) ([Drive: Harmonizing use of input/output relations in GO (Fall 2024 GOC)](https://drive.google.com/open?id=1GUfrZgxeal3L99v3BCRs4yyrsq_D8yGwq8RwNuQ6OMs)). A separate documentation review decided "for now" to keep only `has_input` and `has_output`, used for the primary entity ([Drive: Review & update Noctua documentation](https://drive.google.com/open?id=13MWyxdfcS78dYz9hg61R4ZS4ydp3OY8Y16LAb3xD3Ug)). Whichever label is used, the semantics are the same: capture only the primary participant.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] (the semantics-over-label reading is ours). |
| Date | 2026-11-15 |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [AE-4-E1](AE-4.examples.yaml): A specific vitamin K epoxide recorded as the output of gamma-carboxylation | Conformant | GGCX enables GO:0008488 gamma-glutamyl carboxylase activity (IDA, PMID:17073445) |
| [AE-4-E2](AE-4.examples.yaml): Water recorded as an output of a peroxidase | Non-conformant | LPO enables GO:0004601 peroxidase activity (IDA, PMID:6295491) |
| [AE-3-E3](AE-3.examples.yaml): Substrate and products that the enzyme term's definition already names (from [AE-3](AE-3.md)) | Non-conformant | GALC enables GO:0004336 galactosylceramidase activity (IDA, PMID:8281145) |

## Sources

- wiki: [Has output](https://wiki.geneontology.org/index.php/Has_output)
- drive: [Harmonizing use of input/output relations in GO (Fall 2024 GOC)](https://drive.google.com/open?id=1GUfrZgxeal3L99v3BCRs4yyrsq_D8yGwq8RwNuQ6OMs)
- drive: [Review & update Noctua documentation](https://drive.google.com/open?id=13MWyxdfcS78dYz9hg61R4ZS4ydp3OY8Y16LAb3xD3Ug)

<!-- END GENERATED -->
