---
id: REV-19
title: Know what the gorules already enforce, and do not mistake passing them for review
status: proposed
topic: REV
provenance: GOC
evidence_codes:
- IPI
- ND
- IEA
go_terms:
- term_id: GO:0005488
  label: binding
- term_id: GO:0006810
  label: transport
- term_id: GO:0050896
  label: response to stimulus
sources:
- kind: wiki
  title: GO Central QC Procedure
  url: https://wiki.geneontology.org/index.php/GO_Central_%28GOC%29_QC_Procedure
- kind: drive
  title: GO rules update 2023
  url: https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI
- kind: wiki
  title: Annotation Conf. Call 2024-03-12
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12
date: '2026-11-15'
---

# REV-19. Know what the gorules already enforce, and do not mistake passing them for review

## Decision

Treat a gorule failure on a row as a prompt to review it; treat a gorule pass as no evidence
of correctness. Understand which rules filter and which only warn.

## Context

GO rules run when GAF or GPAD files are loaded. Errors are filtered from GO products; warnings
are reported and kept; some failures are repaired automatically, notably obsolete terms with a
`replaced_by` (GORULE:0000020) and aspect mismatches (GORULE:0000028)
([wiki: GO Central QC Procedure](https://wiki.geneontology.org/index.php/GO_Central_%28GOC%29_QC_Procedure),
[Drive: GO rules update 2023](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI)).
Rules a reviewer meets most often:

| Rule | Check | Outcome |
|---|---|---|
| GORULE:0000002 | NOT annotations to binding and protein binding | filter |
| GORULE:0000007 | IPI used for catalytic activity or its descendants | filter |
| GORULE:0000008 | annotation to a `gocheck_do_not_annotate` term | warning |
| GORULE:0000011 | ND only on root terms, roots only with ND | filter |
| GORULE:0000013 | taxon constraint violation | non-experimental filtered; experimental reported, kept |
| GORULE:0000020 | obsolete or merged term with `replaced_by` | repair |
| GORULE:0000029 | IEA older than one year (warning) or three years (filter) | warning/filter |
| GORULE:0000022 | reference retracted | specified; implementation on hold (2023-24) |

The `gocheck_do_not_annotate` subset absorbed the former do-not-manually-annotate subset in
2024 and holds terms that are not wrong but uninformative (`GO:0005488` binding,
`GO:0006810` transport, `GO:0050896` response to stimulus); an `obsoletion_candidate` subset
gives early warning of terms about to go ([wiki: Annotation Conf. Call 2024-03-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12)).
A row on a do-not-annotate term is usually `MODIFY` (if the evidence supports a specific term)
or `MARK_AS_OVER_ANNOTATED`.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | IPI, ND, IEA |
| GO terms | `GO:0005488` binding; `GO:0006810` transport; `GO:0050896` response to stimulus |

## Sources

- wiki: [GO Central QC Procedure](https://wiki.geneontology.org/index.php/GO_Central_%28GOC%29_QC_Procedure)
- drive: [GO rules update 2023](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI)
- wiki: [Annotation Conf. Call 2024-03-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12)

<!-- END GENERATED -->
