---
id: ONT-20
title: Do not annotate new rows to flagged terms, and read existing rows on them as review prompts
status: proposed
topic: ONT
provenance: GOC
sources:
- kind: wiki
  title: Annotation Conf. Call 2024-03-12
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12
- kind: drive
  title: GO rules 2024
  url: https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM
- kind: issue
  title: go-annotation#1452
  url: https://github.com/geneontology/go-annotation/issues/1452
date: '2026-11-15'
---

# ONT-20. Do not annotate new rows to flagged terms, and read existing rows on them as review prompts

## Decision

Do not make new annotations to terms in `gocheck_do_not_annotate` or `obsoletion_candidate`.
Existing rows on such terms are not wrong by that fact; review them for a specific replacement.

## Context

Since 2024 GO has one do-not-annotate subset, enforced as a warning (GORULE:0000008) in the GOC
pipeline and a filter in GOA's, with Noctua and PAINT blocking new use; its members are high
level or uninformative rather than wrong. The `obsoletion_candidate` subset warns curators at
least two months before a term goes
([wiki: Annotation Conf. Call 2024-03-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12),
[Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)).
Obsolete terms may remain in slims, but annotations to them should be filtered from products
([go-annotation#1452](https://github.com/geneontology/go-annotation/issues/1452)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |

## Sources

- wiki: [Annotation Conf. Call 2024-03-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12)
- drive: [GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)
- issue: [go-annotation#1452](https://github.com/geneontology/go-annotation/issues/1452)

<!-- END GENERATED -->
