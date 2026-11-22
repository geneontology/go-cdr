---
id: AE-2
title: Use comma for facts that hold together and pipe for independent statements. Make separate annotations
  for alternative substrates or targets.
status: proposed
topic: AE
provenance: GOC
provenance_note: '[GOC]. [Drive: Noctua Standard Annotations evidence splitting](https://drive.google.com/open?id=1p2pwOCovVbX61bQspUcptSt2pkA3OSzDHulOpQhZElQ);
  [Drive: Annotation Extension Sept 2017](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk).'
evidence_codes:
- IMP
go_terms:
- term_id: GO:0140314
  label: calcium ion sequestering activity
- term_id: GO:0016529
  label: sarcoplasmic reticulum
sources:
- kind: wiki
  title: Has input
  url: https://wiki.geneontology.org/index.php/Has_input
- kind: wiki
  title: Occurs in
  url: https://wiki.geneontology.org/index.php/Occurs_in
- kind: drive
  title: Noctua Standard Annotations evidence splitting
  url: https://drive.google.com/open?id=1p2pwOCovVbX61bQspUcptSt2pkA3OSzDHulOpQhZElQ
- kind: drive
  title: Annotation Extension Sept 2017
  url: https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk
date: '2026-11-15'
---

# AE-2. Use comma for facts that hold together and pipe for independent statements. Make separate annotations for alternative substrates or targets.

## Decision

Use comma for facts that hold together and pipe for independent statements. Make separate annotations for alternative substrates or targets.

## Context

A comma group is one class: "calcium ion sequestering activity, `occurs_in` sarcoplasmic reticulum, `occurs_in` cardiac muscle cell". A pipe gives independent extensions on the same term. Several `has_input` fillers in one comma group mean several inputs *of one reaction*. An enzyme with alternative substrates, or a transcription factor with several targets, needs one annotation (or one pipe-separated group) per target ([wiki: Has input](https://wiki.geneontology.org/index.php/Has_input)).

## Application

**Example.** CASQ2 (O14958) `enables` GO:0140314 calcium ion sequestering activity, `occurs_in`(GO:0016529 sarcoplasmic reticulum), `occurs_in`(CL:0000746 cardiac muscle cell), IMP, PMID:16908766 ([wiki: Occurs in](https://wiki.geneontology.org/index.php/Occurs_in)). Nested locations go in one comma group. Distinct locations go in separate groups.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC]. [Drive: Noctua Standard Annotations evidence splitting](https://drive.google.com/open?id=1p2pwOCovVbX61bQspUcptSt2pkA3OSzDHulOpQhZElQ); [Drive: Annotation Extension Sept 2017](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk). |
| Date | 2026-11-15 |
| Evidence codes | IMP |
| GO terms | `GO:0140314` calcium ion sequestering activity; `GO:0016529` sarcoplasmic reticulum |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [AE-2-E1](AE-2.examples.yaml): One has_input group per target gene on a transcription factor activity | Conformant | LMX1B enables GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific (ISS, GO_REF:0000024) |
| [AE-2-E2](AE-2.examples.yaml): Two regulated genes placed in one comma group on a gene-expression row | Non-conformant | AGR2 involved_in GO:0010628 positive regulation of gene expression (IMP, PMID:22184114) |
| [AE-3-E1](AE-3.examples.yaml): Target genes named on the regulation-of-transcription BP row as well as on the MF row (from [AE-3](AE-3.md)) | Conformant | LMX1B involved_in GO:0045944 positive regulation of transcription by RNA polymerase II (ISS, GO_REF:0000024) |

## Sources

- wiki: [Has input](https://wiki.geneontology.org/index.php/Has_input)
- wiki: [Occurs in](https://wiki.geneontology.org/index.php/Occurs_in)
- drive: [Noctua Standard Annotations evidence splitting](https://drive.google.com/open?id=1p2pwOCovVbX61bQspUcptSt2pkA3OSzDHulOpQhZElQ)
- drive: [Annotation Extension Sept 2017](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk)

<!-- END GENERATED -->
