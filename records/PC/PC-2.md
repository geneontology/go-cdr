---
id: PC-2
title: Use the most specific complex term that the evidence supports; treat bare `GO:0032991` protein-containing
  complex as a placeholder to refine; record the organelle separately.
status: proposed
topic: PC
provenance: GOC_PLUS
provenance_note: '[GOC+] Point 3 and the MODIFY action are ours.'
aspects:
- C
- F
go_terms:
- term_id: GO:0032991
  label: protein-containing complex
- term_id: GO:0019773
  label: proteasome core complex, alpha-subunit complex
- term_id: GO:0045273
  label: respiratory chain complex II (succinate dehydrogenase)
sources:
- kind: wiki
  title: Protein complexes
  url: https://wiki.geneontology.org/index.php/Protein_complexes
- kind: drive
  title: Annotating activities of complexes and subcomplexes
  url: https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s
- kind: wiki
  title: Ontology meeting 2024-01-29
  url: https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-29
date: '2026-11-15'
---

# PC-2. Use the most specific complex term that the evidence supports; treat bare `GO:0032991` protein-containing complex as a placeholder to refine; record the organelle separately.

## Decision

Use the most specific complex term that the evidence supports; treat bare `GO:0032991` protein-containing complex as a placeholder to refine; record the organelle separately.

## Context

`GO:0032991` says only that the protein is in some complex. When the complex is known, a
`GO:0032991` row on the gene is `MODIFY` to the specific term. If GO has no term for a
physiological complex, request one rather than stopping at the root
([wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes), "How to
request").

Three properties of complex terms constrain the choice:

1. **Complex terms are classes, not instances.** GO does not make terms for a particular
   subunit composition in one species; those belong in Complex Portal or the Protein Ontology.
   Complexes differing only by cell type are out of scope.
2. **Subcomplexes and partial complexes are out of scope.** There is no GO term for the
   catalytic core of complex I or of complex IV
   ([Drive: Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s)).
   Named sectors that exist as terms (for example the ATP synthase F1 and Fo sectors, or
   `GO:0019773` proteasome core complex, alpha-subunit complex) may be used.
3. **Complex terms are species-agnostic and do not imply an organelle.** `GO:0045273`
   respiratory chain complex II (succinate dehydrogenase) has no `part_of` path to mitochondrion,
   because bacteria have it in the plasma membrane. A human SDHB review needs its mitochondrial
   inner membrane row in addition to its complex row; see
   [cellular-component.md](../CC/README.md).

The 2024 ontology meeting reaffirmed that complexes should not be split into cytoplasmic,
mitochondrial and plastid versions
([wiki: Ontology meeting 2024-01-29](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-29)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] Point 3 and the MODIFY action are ours. |
| Date | 2026-11-15 |
| GO terms | `GO:0032991` protein-containing complex; `GO:0019773` proteasome core complex, alpha-subunit complex; `GO:0045273` respiratory chain complex II (succinate dehydrogenase) |

## Sources

- wiki: [Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)
- drive: [Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s)
- wiki: [Ontology meeting 2024-01-29](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-29)

<!-- END GENERATED -->
