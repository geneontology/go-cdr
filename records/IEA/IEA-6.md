---
id: IEA-6
title: Know the current status of each pipeline
status: proposed
topic: IEA
provenance: GOC
evidence_codes:
- IEA
go_terms:
- term_id: GO:0006915
  label: apoptotic process
differences:
- prior_source: '[wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)
    (last reviewed 2020, note added 2026)'
  prior_said: Lists EC, HAMAP, InterPro, Rhea, UniProt keywords and subcellular locations as the mappings
    in use.
  we_recommend: KW2GO is retired except for viruses; SubCell2GO, Rhea2GO and EC2GO are being replaced;
    UniPathway2GO is retired (IEA-6).
  why: The page is out of date relative to the IEA working group decisions; it should carry the status
    table.
sources:
- kind: drive
  title: IEA WG Fall 2026
  url: https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I
- kind: drive
  title: IEA WG pipelines update Sept 2026
  url: https://drive.google.com/open?id=1FQpXSPZdK78X3wX5UEQ9jkFk6Xex0NCi8NeDawOs7IE
- kind: web
  title: SPKW
  url: https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html
- kind: wiki
  title: IEA
  url: https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29
date: '2026-11-15'
---

# IEA-6. Know the current status of each pipeline

## Decision

Treat rows from retired pipelines as historical, rows from pipelines under replacement as
provisional, and rows from kept pipelines as disputable through the pipeline's tracker.

## Context

as of the IEA working group's Fall 2026 report
([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I);
[Drive: IEA WG pipelines update Sept 2026](https://drive.google.com/open?id=1FQpXSPZdK78X3wX5UEQ9jkFk6Xex0NCi8NeDawOs7IE)):

| Pipeline | GO_REF | Decision |
|---|---|---|
| KW2GO | `GO_REF:0000043` | Retired; kept for viruses only (ViralZone asked to align keyword use with GO) |
| SubCell2GO | `GO_REF:0000044` | Replace with direct annotations for Swiss-Prot; stop for TrEMBL |
| Rhea2GO | `GO_REF:0000116` | Replace with direct annotations for Swiss-Prot; stop for TrEMBL |
| EC2GO | `GO_REF:0000003` | Replace with direct annotations for Swiss-Prot; stop for TrEMBL |
| UniPathway2GO | `GO_REF:0000041` | Retire; loss files for groups to review |
| InterPro2GO | `GO_REF:0000002` | Keep; dispute through GitHub |
| Rfam2GO | | Keep; check mapped terms are current |
| GO inter-ontology inferences | `GO_REF:0000108` | Keep |
| ARBA, UniRule | `GO_REF:0000117` (ARBA) | Keep and improve; dispute through GitHub |
| TreeGrafter | `GO_REF:0000118` | Keep; update expected |
| Ensembl Compara | `GO_REF:0000107` | Revise or remove; Ensembl stopped orthology calls in January 2026 |

The repo verified that GOA had removed `GO_REF:0000043` rows for cellular organisms by about April
2026 ([SPKW](https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html)). The GO wiki's IEA page still lists keyword and subcellular-location
mappings as sanctioned, with a note that several are "under review and revision"
([wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)).
IEAs older than one year draw a warning and those older than three years are filtered
(GORULE:0000029, same page).

## Application

Worked example: a cached GOA file for a human gene may still carry `GO:0006915` apoptotic process
from KW2GO. Review it for the retrospective record, but do not cite the row as evidence elsewhere,
and do not expect it in the next release.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | IEA |
| GO terms | `GO:0006915` apoptotic process |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-6-E1](IEA-6.examples.yaml): A retired-keyword row reviewed for the record and recognised as historical | Conformant | GI GO:0009908 flower development (IEA, GO_REF:0000043) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29) (last reviewed 2020, note added 2026) | Lists EC, HAMAP, InterPro, Rhea, UniProt keywords and subcellular locations as the mappings in use. | KW2GO is retired except for viruses; SubCell2GO, Rhea2GO and EC2GO are being replaced; UniPathway2GO is retired (IEA-6). | The page is out of date relative to the IEA working group decisions; it should carry the status table. |

## Sources

- drive: [IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)
- drive: [IEA WG pipelines update Sept 2026](https://drive.google.com/open?id=1FQpXSPZdK78X3wX5UEQ9jkFk6Xex0NCi8NeDawOs7IE)
- web: [SPKW](https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html)
- wiki: [IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)

<!-- END GENERATED -->
