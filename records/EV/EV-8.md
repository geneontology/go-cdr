---
id: EV-8
title: Use ISS, ISO, ISA or ISM only after a curator has reviewed the inference; name the experimentally
  supported donor or the model in WITH/FROM.
status: proposed
topic: EV
provenance: GOC_PLUS
provenance_note: '[GOC] ([wiki: ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29),
  [wiki: ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29), [wiki:
  ISA](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29), [wiki: ISM](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29));
  [GOC+] for the donor-chain restriction and the three-question review.'
evidence_codes:
- ISS
- ISO
- ISA
- ISM
- IC
- IEA
go_terms:
- term_id: GO:0005515
  label: protein binding
sources:
- kind: issue
  title: go-annotation#1775
  url: https://github.com/geneontology/go-annotation/issues/1775
- kind: issue
  title: go-annotation#11
  url: https://github.com/geneontology/go-annotation/issues/11
- kind: web
  title: ISO
  url: https://ai4curation.io/ai-gene-review/pages/projects/ISO.html
- kind: wiki
  title: ISS
  url: https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29
- kind: wiki
  title: ISO
  url: https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29
- kind: wiki
  title: ISA
  url: https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29
- kind: wiki
  title: ISM
  url: https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29
date: '2026-11-15'
---

# EV-8. Use ISS, ISO, ISA or ISM only after a curator has reviewed the inference; name the experimentally supported donor or the model in WITH/FROM.

## Decision

Use ISS, ISO, ISA or ISM only after a curator has reviewed the inference; name the experimentally supported donor or the model in WITH/FROM.

## Context

The similarity codes record manual sequence-based inference. ISS (ECO:0000250) is
the umbrella when several methods were combined; ISO (ECO:0000266) when the donor
is an established ortholog; ISA (ECO:0000247) for a reviewed alignment; ISM
(ECO:0000255) for a match to a sequence model (Pfam, TIGRFAM, Rfam, TMHMM). If any
step of a bulk transfer is unreviewed, the code is IEA. WITH/FROM is mandatory for
ISS, ISO and ISA; for ISM it holds the model accession when one exists.

Donor requirements:

- A gene-product donor must carry the same or a more specific term with
  experimental evidence (GORULE:0000038). The wiki also accepts IC on the donor; we
  accept it only when that IC itself rests on an experimental annotation of the
  donor, so that no chain is a transfer of a transfer.
- For ISO, list every paralog when the target is co-orthologous to several genes,
  and revisit the annotation when orthology calls change.
- HTP-supported donors are allowed, with case-by-case review
  ([go-annotation#1775](https://github.com/geneontology/go-annotation/issues/1775)).
- Antibody cross-reactivity is not sequence similarity
  ([go-annotation#11](https://github.com/geneontology/go-annotation/issues/11)).
- No ISS-family annotation to `GO:0005515` protein binding (GORULE:0000005).

When reviewing an ISO row, ask three separate questions ([ISO](https://ai4curation.io/ai-gene-review/pages/projects/ISO.html)): is
the donor annotation still present and experimental; is the donor the target's
ortholog rather than a paralog or one of a one-to-many set; and is the term safe
to move (conserved biochemistry usually is; tissue, developmental and regulatory
context often is not)? Record the answer in `review.propagation_review`. Mouse Ang2
shows the paralog failure: all its ISO rows come from human ANG, but Ang2 is a
divergent member of an expanded family, and 41 of 46 rows were removed.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] ([wiki: ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29), [wiki: ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29), [wiki: ISA](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29), [wiki: ISM](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29)); [GOC+] for the donor-chain restriction and the three-question review. |
| Date | 2026-11-15 |
| Evidence codes | ISS, ISO, ISA, ISM, IC, IEA |
| GO terms | `GO:0005515` protein binding |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [EV-8-E1](EV-8.examples.yaml): Angiogenesis transferred from human ANG to a non-angiogenic paralog | Non-conformant | Ang2 involved_in GO:0001525 angiogenesis (ISO, GO_REF:0000119) |
| [EV-8-E2](EV-8.examples.yaml): A response to yeast row whose donor annotation has gone | Non-conformant | Ang2 involved_in GO:0001878 response to yeast (ISO, GO_REF:0000119) |

## Sources

- issue: [go-annotation#1775](https://github.com/geneontology/go-annotation/issues/1775)
- issue: [go-annotation#11](https://github.com/geneontology/go-annotation/issues/11)
- web: [ISO](https://ai4curation.io/ai-gene-review/pages/projects/ISO.html)
- wiki: [ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29)
- wiki: [ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29)
- wiki: [ISA](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29)
- wiki: [ISM](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29)

<!-- END GENERATED -->
