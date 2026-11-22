---
id: CC-1
title: Use `located_in` by default, `is_active_in` only when the activity is shown at that location, and
  `part_of` only for complex terms.
status: proposed
topic: CC
provenance: GOC
aspects:
- C
evidence_codes:
- HTP
go_terms:
- term_id: GO:0032991
  label: protein-containing complex
- term_id: GO:0005829
  label: cytosol
sources:
- kind: wiki
  title: Is active in
  url: https://wiki.geneontology.org/index.php/Is_active_in
- kind: wiki
  title: Part of relation
  url: https://wiki.geneontology.org/index.php/Part_of_relation
- kind: drive
  title: Guidelines for P2GO
  url: https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc
- kind: issue
  title: go-annotation#3595
  url: https://github.com/geneontology/go-annotation/issues/3595
- kind: wiki
  title: Annotation Relations
  url: https://wiki.geneontology.org/index.php/Annotation_Relations
- kind: wiki
  title: Located in
  url: https://wiki.geneontology.org/index.php/Located_in
- kind: wiki
  title: Annotation Conf. Call 2023-05-30
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-30
date: '2026-11-15'
---

# CC-1. Use `located_in` by default, `is_active_in` only when the activity is shown at that location, and `part_of` only for complex terms.

## Decision

Use `located_in` by default, `is_active_in` only when the activity is shown at that location, and `part_of` only for complex terms.

## Context

`located_in` links a gene product to a cellular anatomical entity where it has been detected.
`is_active_in` says the gene product enables its molecular function there; it follows from
`enables` some MF that `occurs_in` the location
([wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in)). `part_of` links a
gene product to a protein-containing complex (`GO:0032991` or a descendant) and is not used for
cellular anatomical entities
([wiki: Part of relation](https://wiki.geneontology.org/index.php/Part_of_relation);
[Drive: Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)).

Choose `is_active_in` only when the paper (or the combined literature) shows the MF happening
in that compartment: an activity assay on the purified compartment, a substrate that exists
only there, or a function that requires that side of a membrane. A fractionation or
immunofluorescence result alone is `located_in`.

## Application

*Example.* Mouse Tent2 (a cytoplasmic poly(A) polymerase) was annotated to nucleus from a
fractionation figure. The 2021 review agreed the protein is found in both fractions but that
the nucleus is not where its activity has been shown, so the nuclear row should be
`located_in`, not `is_active_in`
([go-annotation#3595](https://github.com/geneontology/go-annotation/issues/3595)).

*Example.* *C. elegans* CED-3 `is_active_in` `GO:0005829` cytosol: the caspase cleaves its
substrates there ([wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | HTP |
| GO terms | `GO:0032991` protein-containing complex; `GO:0005829` cytosol |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CC-1-E1](CC-1.examples.yaml): An is_active_in lysosomal membrane row backed by an activity measured there | Conformant | ATXN3 is_active_in GO:0005765 lysosomal membrane (IDA, PMID:33157014) |
| [CC-1-E2](CC-1.examples.yaml): An is_active_in nucleus row from a tagged-protein screen of a mitochondrial enzyme | Non-conformant | hem14 is_active_in GO:0005634 nucleus (HDA, PMID:16823372) |

## Sources

- wiki: [Is active in](https://wiki.geneontology.org/index.php/Is_active_in)
- wiki: [Part of relation](https://wiki.geneontology.org/index.php/Part_of_relation)
- drive: [Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- issue: [go-annotation#3595](https://github.com/geneontology/go-annotation/issues/3595)
- wiki: [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- wiki: [Located in](https://wiki.geneontology.org/index.php/Located_in)
- wiki: [Annotation Conf. Call 2023-05-30](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-30)

<!-- END GENERATED -->
