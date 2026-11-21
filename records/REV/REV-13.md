---
id: REV-13
title: Remove bare protein binding; look for the informative function behind it
status: proposed
topic: REV
provenance: GOC_PLUS
evidence_codes:
- ISS
- IEA
go_terms:
- term_id: GO:0005515
  label: protein binding
differences:
- prior_source: '[OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html),
    pattern 1'
  prior_said: Remove protein binding "when more specific functional annotations exist or when interactions
    are from HTP screens"
  we_recommend: Remove bare `GO:0005515` regardless; look for the informative MF; project-specific exceptions
    documented
  why: Policy now term-level rather than conditional ([REV-13](REV-13.md))
sources:
- kind: wiki
  title: Tips
  url: https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations
- kind: issue
  title: go-annotation#2097
  url: https://github.com/geneontology/go-annotation/issues/2097
- kind: drive
  title: GO rules 2024
  url: https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM
date: '2026-11-15'
---

# REV-13. Remove bare protein binding; look for the informative function behind it

## Decision

A row on `GO:0005515` protein binding identifies no function. Remove it under the
protein-binding policy, and where the interaction evidence supports something informative (an
adaptor, a ligase-binding, a receptor-binding or a complex-binding term), propose that instead.

## Context

The GOC recommends avoiding protein binding when more precise annotations can be made
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)),
decided that protein binding should not be propagated by PAINT
([go-annotation#2097](https://github.com/geneontology/go-annotation/issues/2097)), filters NOT
annotations to binding and protein binding (GORULE:0000002), and was implementing a filter for
ISS and IEA binding rows in 2024 (GORULE:0000005)
([Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)).
Descendants such as enzyme binding are informative and follow the normal rules. Projects with
their own standing instructions (the ClinGen Mendelian project) may keep supported generic
binding as non-core when nothing more specific is evidenced. Details:
[molecular-function.md](../MF/README.md).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Evidence codes | ISS, IEA |
| GO terms | `GO:0005515` protein binding |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html), pattern 1 | Remove protein binding "when more specific functional annotations exist or when interactions are from HTP screens" | Remove bare `GO:0005515` regardless; look for the informative MF; project-specific exceptions documented | Policy now term-level rather than conditional ([REV-13](REV-13.md)) |

## Sources

- wiki: [Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
- issue: [go-annotation#2097](https://github.com/geneontology/go-annotation/issues/2097)
- drive: [GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)

<!-- END GENERATED -->
