---
id: REV-15
title: A retraction is a source failure; scope the response to the evidence line
status: proposed
topic: REV
provenance: GOC_PLUS
provenance_note: '[GOC+]. The GOC discussed handling retractions in December 2023 and specified GORULE:0000022
  to filter annotations to retracted publications; its implementation was on hold pending a way to query
  external sources during the pipeline run ([wiki: Annotation Conf. Call 2023-12-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-12-12),
  [wiki: Ontology meeting 2023-12-11](https://wiki.geneontology.org/index.php/Ontology_meeting_2023-12-11),
  [Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)).
  We recommend against a blanket filter; see Differences.'
evidence_codes:
- IPI
go_terms:
- term_id: GO:0005515
  label: protein binding
differences:
- prior_source: '[Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)
    (GORULE:0000022)'
  prior_said: Filter annotations to retracted publications
  we_recommend: Flag the citation; act only on rows whose sole evidence is the retracted paper; `UNDECIDED`
    or a proposed `REMOVE` sent upstream
  why: None of the four retraction-backed annotations found here was a core function, and notices often
    affirm part of a paper ([REV-15](REV-15.md))
sources:
- kind: web
  title: RETRACTIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/RETRACTIONS.html
- kind: wiki
  title: Annotation Conf. Call 2023-12-12
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-12-12
- kind: wiki
  title: Ontology meeting 2023-12-11
  url: https://wiki.geneontology.org/index.php/Ontology_meeting_2023-12-11
- kind: drive
  title: GO rules 2024
  url: https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM
date: '2026-11-15'
---

# REV-15. A retraction is a source failure; scope the response to the evidence line

## Decision

Flag a retracted reference, cite the notice, and then ask what rests on it. If the retracted
paper is the sole evidence for an annotation, the row becomes `UNDECIDED` or a proposed
`REMOVE` with the retraction cited and sent upstream. Do not mass-remove a gene's annotations
because one paper was retracted.

## Context

Retractions are issued for image duplication, statistics, misconduct and honest error, and a
notice often affirms part of the work. An expression of concern questions a record without
withdrawing it; an erratum is usually benign. The first full scan of this repository (25,088
distinct PMIDs) found 7 retracted papers, 4 of them under a GO annotation, and none supporting
an accepted core function: the recorded actions were `REMOVE` (TP53, a `GO:0005515` IPI),
`KEEP_AS_NON_CORE` (mouse Mtor, BACE1) and `UNDECIDED` (STAT3), each reached on biological
grounds before the retraction was known ([RETRACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/RETRACTIONS.html)).

Procedure: set `is_invalid: true` with `correctness: DISPUTED` and the notice in
`review_notes`; add the notice as its own reference; then sort citation sites. A citation in
the reference list only is bibliographic cleanup. A `supporting_text` quote from a retracted
paper must not be load-bearing; find independent support. An `original_reference_id` is the
real case: look for independent corroboration and say so in the reason if it exists.
Retraction status changes after a review is written, so the check must be re-run, not done once.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The GOC discussed handling retractions in December 2023 and specified GORULE:0000022 to filter annotations to retracted publications; its implementation was on hold pending a way to query external sources during the pipeline run ([wiki: Annotation Conf. Call 2023-12-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-12-12), [wiki: Ontology meeting 2023-12-11](https://wiki.geneontology.org/index.php/Ontology_meeting_2023-12-11), [Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)). We recommend against a blanket filter; see Differences. |
| Date | 2026-11-15 |
| Evidence codes | IPI |
| GO terms | `GO:0005515` protein binding |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM) (GORULE:0000022) | Filter annotations to retracted publications | Flag the citation; act only on rows whose sole evidence is the retracted paper; `UNDECIDED` or a proposed `REMOVE` sent upstream | None of the four retraction-backed annotations found here was a core function, and notices often affirm part of a paper ([REV-15](REV-15.md)) |

## Sources

- web: [RETRACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/RETRACTIONS.html)
- wiki: [Annotation Conf. Call 2023-12-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-12-12)
- wiki: [Ontology meeting 2023-12-11](https://wiki.geneontology.org/index.php/Ontology_meeting_2023-12-11)
- drive: [GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)

<!-- END GENERATED -->
