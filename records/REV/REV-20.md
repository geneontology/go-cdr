---
id: REV-20
title: An obsoletion-driven review ticket is a review of claims, not a find-and-replace
status: proposed
topic: REV
provenance: GOC
related:
- ONT-3
sources:
- kind: repo
  title: go-annotation issue template
  url: https://github.com/geneontology/go-annotation/blob/master/.github/ISSUE_TEMPLATE/annotation-review-for-obsoletion.md
- kind: wiki
  title: Obsoleting an Existing Ontology Term
  url: https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term
- kind: issue
  title: go-annotation#1940
  url: https://github.com/geneontology/go-annotation/issues/1940
- kind: issue
  title: go-annotation#2584
  url: https://github.com/geneontology/go-annotation/issues/2584
date: '2026-11-15'
---

# REV-20. An obsoletion-driven review ticket is a review of claims, not a find-and-replace

## Decision

When a `go-annotation` review ticket lists your group's annotations to a term being
obsoleted, decide each row on its biology: some move to the suggested term, some to a different
term, and some are deleted because the obsolete term was the only thing making them look right.

## Context

The standard ticket names the obsoletion reason, links the ontology ticket, attaches a
spreadsheet of experimental annotations by group and lists the mappings (InterPro2GO, UniProt
keywords, UniRule) to review
([go-annotation issue template](https://github.com/geneontology/go-annotation/blob/master/.github/ISSUE_TEMPLATE/annotation-review-for-obsoletion.md)).
Groups get at least seven days after notification, longer for large re-annotation
([wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)).
Precedents show the range of outcomes: `colocalizes_with` on complex terms became complex
binding or was removed when no interaction evidence existed
([go-annotation#1940](https://github.com/geneontology/go-annotation/issues/1940)); `occurs_at`
extensions were moved per pattern, and Pfam targets dropped
([go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584)). How to
choose among the obsolete term's `replaced_by` and `consider` targets is in
[ontology-change-and-taxa.md](../ONT/ONT-3.md).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Related | [ONT-3](../ONT/ONT-3.md) |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [REV-20-E1](REV-20.examples.yaml): An obsolete unfolded protein binding IDA on an sHSP mapped to a holdase NTR | Conformant | HSP17.7 enables GO:0051082 unfolded protein binding (IDA, PMID:11576425) |
| [REV-20-E2](REV-20.examples.yaml): Bovine alpha-crystallin moved to protein folding chaperone while it lacks refolding activity | Contested | CRYAA enables GO:0051082 unfolded protein binding (IBA, GO_REF:0000033) |

## Sources

- repo: [go-annotation issue template](https://github.com/geneontology/go-annotation/blob/master/.github/ISSUE_TEMPLATE/annotation-review-for-obsoletion.md)
- wiki: [Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)
- issue: [go-annotation#1940](https://github.com/geneontology/go-annotation/issues/1940)
- issue: [go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584)

<!-- END GENERATED -->
