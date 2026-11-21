---
id: PC-4
title: Do not infer a molecular function from complex membership, co-purification or loss of complex activity
  on knockout.
status: proposed
topic: PC
provenance: GOC_PLUS
provenance_note: '[GOC+] GOC states the membership rule; the loss-of-function rubric is the repo''s.'
aspects:
- C
- F
evidence_codes:
- IMP
go_terms:
- term_id: GO:0008137
  label: NADH dehydrogenase (ubiquinone) activity
related:
- PC-6
- PC-7
sources:
- kind: wiki
  title: Contributes to
  url: https://wiki.geneontology.org/index.php/Contributes_to
- kind: wiki
  title: Protein complexes
  url: https://wiki.geneontology.org/index.php/Protein_complexes
- kind: web
  title: PROTEIN_COMPLEX_FUNCTIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html
date: '2026-11-15'
---

# PC-4. Do not infer a molecular function from complex membership, co-purification or loss of complex activity on knockout.

## Decision

Do not infer a molecular function from complex membership, co-purification or loss of complex activity on knockout.

## Context

A subunit can be required for a complex's activity without carrying it out. The
Contributes_to checklist asks: can the activity occur without this subunit; can the protein be
annotated to another MF; is the annotation still acceptable without the qualifier
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). A complex's
link to its MF through `capable_of` cannot be used to annotate subunits, because it does not
say which subunit is active
([wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)).

Loss-of-function data distinguish poorly. Use the repo's attribution rubric
([PROTEIN_COMPLEX_FUNCTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html)):

| Evidence pattern | Handling |
|---|---|
| Purified subunit has the activity | `enables` on the subunit |
| Active site or cofactor centre lies in the subunit | `enables`, or `contributes_to` if it acts only in the complex (PC-6) |
| Activity requires a stable subcomplex | `contributes_to` for the subcomplex members only |
| Knockout lowers complex activity by destabilising assembly | assembly, stability or structural terms, not the activity |
| Subunit changes rate, specificity or inhibitor response | regulator terms (PC-7) |
| Only membership or co-purification | CC and BP only |

## Application

*Example of the error.* The repo's NDUFS4 review ACCEPTs an IMP `enables GO:0008137` NADH
dehydrogenase (ubiquinone) activity row and names `GO:0008137` as NDUFS4's core
`molecular_function`, while its own reason says NDUFS4 is a supernumerary subunit that "supports
the complex-level activity through assembly/stability rather than direct catalysis". Under
this rule the `enables` row is `MODIFY` (or `MARK_AS_OVER_ANNOTATED`), the core function
names complex I membership and assembly, and no `contributes_to` is given unless NDUFS4 is
shown to be in the electron-transfer mechanism.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] GOC states the membership rule; the loss-of-function rubric is the repo's. |
| Date | 2026-11-15 |
| Related | [PC-6](PC-6.md), [PC-7](PC-7.md) |
| Evidence codes | IMP |
| GO terms | `GO:0008137` NADH dehydrogenase (ubiquinone) activity |

## Sources

- wiki: [Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)
- wiki: [Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)
- web: [PROTEIN_COMPLEX_FUNCTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html)

<!-- END GENERATED -->
