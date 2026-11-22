---
id: AE-1
title: An extension must narrow the term, so that the annotation stays true without it. Do not use extensions
  for conditions, negation or exclusivity.
status: proposed
topic: AE
provenance: GOC
provenance_note: '[GOC]. [wiki: Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of);
  [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation).'
go_terms:
- term_id: GO:0034504
  label: protein localization to nucleus
related:
- QN-12
sources:
- kind: wiki
  title: Happens during
  url: https://wiki.geneontology.org/index.php/Happens_during
- kind: wiki
  title: Annotation Extension Relation:independent of
  url: https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of
- kind: wiki
  title: Elements of an annotation
  url: https://wiki.geneontology.org/index.php/Elements_of_an_annotation
date: '2026-11-15'
---

# AE-1. An extension must narrow the term, so that the annotation stays true without it. Do not use extensions for conditions, negation or exclusivity.

## Decision

An extension must narrow the term, so that the annotation stays true without it. Do not use extensions for conditions, negation or exclusivity.

## Context

Folding works only if term plus extension is a subclass of the term. "Protein localization to nucleus `happens_during` mitotic anaphase" folds to a term that would be a child of GO:0034504 protein localization to nucleus ([wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during)). "Positive regulation of NF-kappaB signaling `independent_of` peptidase activity" folds to nothing.

**Test.** Delete the extension. If the remaining annotation is false, the extension was carrying the claim. Usually that means a NOT or condition was hidden in it, and the row is wrong. If the annotation is true but now says less, the extension is legitimate.

**Corollary.** Never combine an extension with NOT ([QN-12](../QN/QN-12.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC]. [wiki: Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of); [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation). |
| Date | 2026-11-15 |
| Related | [QN-12](../QN/QN-12.md) |
| GO terms | `GO:0034504` protein localization to nucleus |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [AE-1-E1](AE-1.examples.yaml): A neuronal occurs_in on an enzyme activity, which survives the delete-the-extension test | Conformant | GBA1 enables GO:0004348 glucosylceramidase activity (IMP, PMID:21700325) |
| [AE-1-E2](AE-1.examples.yaml): A cofactor-dependent Cdc42 arm kept as a bare annotation rather than given a condition extension | Conformant | ARHGEF16 involved_in GO:0032489 regulation of Cdc42 protein signal transduction (IDA, PMID:21139582) |

## Sources

- wiki: [Happens during](https://wiki.geneontology.org/index.php/Happens_during)
- wiki: [Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of)
- wiki: [Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)

<!-- END GENERATED -->
