---
id: AE-6
title: On CC annotations, use `part_of` with a cell or anatomy term for the cell or tissue in which the
  component sits, and an existence relation for the stage.
status: proposed
topic: AE
provenance: GOC_PLUS
provenance_note: '[GOC+] (the relation names are updated to the SAE list).'
go_terms:
- term_id: GO:0031966
  label: mitochondrial membrane
- term_id: GO:0051329
  label: mitotic interphase
sources:
- kind: wiki
  title: Supplying temporal location information
  url: https://wiki.geneontology.org/index.php/Annotation_Extension_field%3A_Supplying_temporal_location_information_to_a_GO_annotation
date: '2026-11-15'
---

# AE-6. On CC annotations, use `part_of` with a cell or anatomy term for the cell or tissue in which the component sits, and an existence relation for the stage.

## Decision

On CC annotations, use `part_of` with a cell or anatomy term for the cell or tissue in which the component sits, and an existence relation for the stage.

## Application

**Examples.** A gene product in GO:0031966 mitochondrial membrane of a spermatocyte: `part_of`(CL:0000017 spermatocyte). *S. pombe* Clp1 at the spindle pole body in interphase: the legacy form was `exists_during`(GO:0051329 mitotic interphase) ([wiki: Supplying temporal location information](https://wiki.geneontology.org/index.php/Annotation_Extension_field%3A_Supplying_temporal_location_information_to_a_GO_annotation)). `exists_during` is not in RO. Current tooling uses `existence_overlaps` (RO:0002490) or `existence_starts_and_ends_during` (RO:0002491).

**Not for complexes.** The SAE allows only existence relations on protein-containing-complex terms. A complex is not "part of" a cell type in this sense.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] (the relation names are updated to the SAE list). |
| Date | 2026-11-15 |
| GO terms | `GO:0031966` mitochondrial membrane; `GO:0051329` mitotic interphase |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [AE-6-E1](AE-6.examples.yaml): A telomere location limited to S phase with an existence relation | Conformant | H3-3A located_in GO:0000781 chromosome, telomeric region (IDA, PMID:20110566) |
| [AE-6-E2](AE-6.examples.yaml): A protein complex given part_of a kidney cell type and tissue | Non-conformant | FXYD2 part_of GO:0005890 sodium:potassium-exchanging ATPase complex (ISS, GO_REF:0000024) |
| [AE-6-E3](AE-6.examples.yaml): An existence relation filled with a signalling pathway, not a stage | Non-conformant | LRP6 located_in GO:0031410 cytoplasmic vesicle (IDA, PMID:20093472) |

## Sources

- wiki: [Supplying temporal location information](https://wiki.geneontology.org/index.php/Annotation_Extension_field%3A_Supplying_temporal_location_information_to_a_GO_annotation)

<!-- END GENERATED -->
