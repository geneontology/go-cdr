---
id: BP-1
title: Use `involved in` only when the gene product's activity is a step of the process
status: proposed
topic: BP
provenance: GOC_PLUS
provenance_note: '[GOC+]. GOC defines the relation. The requirement to name the step is our sharpening.'
aspects:
- P
go_terms:
- term_id: GO:0004708
  label: MAP kinase kinase activity
- term_id: GO:0000165
  label: MAPK cascade
- term_id: GO:0006913
  label: nucleocytoplasmic transport
- term_id: GO:0006998
  label: nuclear envelope organization
- term_id: GO:0055088
  label: lipid homeostasis
related:
- BP-4
differences:
- prior_source: '[Drive: Regulation and causality & legacy qualifiers, 2017](https://drive.google.com/open?id=1fmgRMOPel-8_7iIuMAkVDNGuxurUWTxJRdsZTgSeNRM)'
  prior_said: Legacy BP annotations should be read as "causally upstream of or within".
  we_recommend: Do not assume any legacy `involved_in` is a participation claim. Test each one against
    BP-1 in review.
  why: Sharpening. Legacy rows now carry `involved_in` in GAF/GPAD output, and the qualifier alone does
    not show that the relation was assessed.
sources:
- kind: wiki
  title: Annotation Relations
  url: https://wiki.geneontology.org/index.php/Annotation_Relations
- kind: drive
  title: Annotation relations – Guidelines for P2GO
  url: https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc
- kind: wiki
  title: Annotating from phenotypes
  url: https://wiki.geneontology.org/index.php/Annotating_from_phenotypes
- kind: drive
  title: Case studies annotating from mutant phenotypes
  url: https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0
- kind: issue
  title: go-annotation#2456
  url: https://github.com/geneontology/go-annotation/issues/2456
date: '2026-11-15'
---

# BP-1. Use `involved in` only when the gene product's activity is a step of the process

## Decision

**Statement.** Annotate `involved_in` P only if you can name the activity of the gene product that is part of P. That activity may be catalysis, binding that performs a step, a structural or scaffolding contribution the step depends on, or transport. If you cannot name it, use an upstream relation (BP-4) or do not annotate.

## Context

The relation means "enables some f, and f is part_of P" ([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations); [Drive: Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)). The wiki asks curators to "think of the Molecular Functions that make up that process" and check whether the gene product enables one ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). We make that test mandatory and operational: write the step down, at least in the review reason or the curator's notes.

## Application

**Worked examples.**

- Human MAP2K1 enables GO:0004708 MAP kinase kinase activity and phosphorylates ERK1/2. That activity is a step of GO:0000165 MAPK cascade, so `involved_in` GO:0000165 is correct.
- Yeast Brr6 is an essential nuclear envelope membrane protein whose mutants show nucleocytoplasmic transport defects. The later paper attributes the defect to lipid homeostasis at the NE-ER membrane and NPC assembly. Brr6 performs no transport step, so it is not `involved_in` GO:0006913 nucleocytoplasmic transport. The GOC case study discusses `acts upstream of or within` GO:0006998 nuclear envelope organization or GO:0055088 lipid homeostasis instead ([Drive: Case studies annotating from mutant phenotypes](https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0)). The same lesson appears in [go-annotation#2456](https://github.com/geneontology/go-annotation/issues/2456): nuclear retention caused by a processing defect does not make the processing factor a transport factor.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. GOC defines the relation. The requirement to name the step is our sharpening. |
| Date | 2026-11-15 |
| Related | [BP-4](BP-4.md) |
| GO terms | `GO:0004708` MAP kinase kinase activity; `GO:0000165` MAPK cascade; `GO:0006913` nucleocytoplasmic transport; `GO:0006998` nuclear envelope organization; `GO:0055088` lipid homeostasis |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [BP-1-E1](BP-1.examples.yaml): MEK1 involved in the MAPK cascade through its own kinase step | Conformant | MAP2K1 involved_in GO:0000165 MAPK cascade (IBA, GO_REF:0000033) |
| [BP-1-E2](BP-1.examples.yaml): INSIG1 annotated as involved in cholesterol biosynthesis it only restrains | Non-conformant | INSIG1 involved_in GO:0006695 cholesterol biosynthetic process (IDA, PMID:32322062) |
| [BP-12-E1](BP-12.examples.yaml): MEK1 annotated to the ERK1 and ERK2 cascade step (from [BP-12](BP-12.md)) | Conformant | MAP2K1 involved_in GO:0070371 ERK1 and ERK2 cascade (TAS, Reactome:R-HSA-110056) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: Regulation and causality & legacy qualifiers, 2017](https://drive.google.com/open?id=1fmgRMOPel-8_7iIuMAkVDNGuxurUWTxJRdsZTgSeNRM) | Legacy BP annotations should be read as "causally upstream of or within". | Do not assume any legacy `involved_in` is a participation claim. Test each one against BP-1 in review. | Sharpening. Legacy rows now carry `involved_in` in GAF/GPAD output, and the qualifier alone does not show that the relation was assessed. |

## Sources

- wiki: [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- drive: [Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- wiki: [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
- drive: [Case studies annotating from mutant phenotypes](https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0)
- issue: [go-annotation#2456](https://github.com/geneontology/go-annotation/issues/2456)

<!-- END GENERATED -->
