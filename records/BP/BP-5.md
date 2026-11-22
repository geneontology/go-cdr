---
id: BP-5
title: Use `acts upstream of` (without "or within") only when the mechanism is known and the activity
  is outside the process and does not regulate it
status: proposed
topic: BP
provenance: GOC
aspects:
- P
go_terms:
- term_id: GO:0097722
  label: sperm motility
- term_id: GO:0009566
  label: fertilization
differences:
- prior_source: Repository schema, `AnnotationQualifierEnum`
  prior_said: '`acts_upstream_of` described as "acts upstream of or within".'
  we_recommend: '`acts_upstream_of` is the mechanism-known, outside-the-process relation (BP-5).'
  why: Error in the repository's own enum description, not in GO guidance.
sources:
- kind: drive
  title: Annotation relations – Guidelines for P2GO
  url: https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc
- kind: wiki
  title: Annotation Relations
  url: https://wiki.geneontology.org/index.php/Annotation_Relations
- kind: wiki
  title: Annotating from phenotypes
  url: https://wiki.geneontology.org/index.php/Annotating_from_phenotypes
- kind: issue
  title: go-annotation#2417
  url: https://github.com/geneontology/go-annotation/issues/2417
- kind: issue
  title: go-annotation#1532
  url: https://github.com/geneontology/go-annotation/issues/1532
- kind: issue
  title: go-annotation#1450
  url: https://github.com/geneontology/go-annotation/issues/1450
date: '2026-11-15'
---

# BP-5. Use `acts upstream of` (without "or within") only when the mechanism is known and the activity is outside the process and does not regulate it

## Decision

**Statement.** `acts upstream of` and its signed children mean three things: the mechanism linking the activity to the process is known; the activity occurs before the process; and the activity is neither part of the process nor a regulator of it. Use them rarely. When the upstream process has its own GO term, annotate that term with `involved_in`. Use `acts upstream of` only when downstream users would lose real information without it.

## Context

Definitions are from the P2GO table and the wiki ([Drive: Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc); [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)). The phenotype guideline asks curators to "think about how relevant and informative the resulting *acts upstream of* annotation would be" ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). PomBase's policy is to avoid causal relations of this kind entirely, and its boundaries remain debated ([go-annotation#2417](https://github.com/geneontology/go-annotation/issues/2417); [go-annotation#1532](https://github.com/geneontology/go-annotation/issues/1532)).

## Application

**Worked example.** A sperm motility protein is `involved_in` GO:0097722 sperm motility. It is not `involved_in` GO:0009566 fertilization. If a curator wants the fertilization link visible, the honest relation is `acts upstream of, positive effect` GO:0009566 ([go-annotation#1450](https://github.com/geneontology/go-annotation/issues/1450) records that `causally_upstream_of` can express this). In most cases the motility annotation suffices, because a user can follow the ontology from motility to its role.

**Repository note.** The schema's `AnnotationQualifierEnum` currently describes `acts_upstream_of` as "acts upstream of or within". That conflates two different RO relations and should be corrected (see Open questions).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0097722` sperm motility; `GO:0009566` fertilization |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [BP-5-E1](BP-5.examples.yaml): RDR6 acts upstream of siRNA-mediated translational repression by making the dsRNA precursor | Conformant | RDR6 acts_upstream_of_positive_effect GO:0070549 siRNA-mediated gene silencing by inhibition of translation (IMP, PMID:32376953) |
| [BP-5-E2](BP-5.examples.yaml): acts_upstream_of on a regulation term for a transcription factor that induces NOS3 | Contested | Klf2 acts_upstream_of GO:0045429 positive regulation of nitric oxide biosynthetic process (ISO, GO_REF:0000121) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| Repository schema, `AnnotationQualifierEnum` | `acts_upstream_of` described as "acts upstream of or within". | `acts_upstream_of` is the mechanism-known, outside-the-process relation (BP-5). | Error in the repository's own enum description, not in GO guidance. |

## Sources

- drive: [Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- wiki: [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- wiki: [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
- issue: [go-annotation#2417](https://github.com/geneontology/go-annotation/issues/2417)
- issue: [go-annotation#1532](https://github.com/geneontology/go-annotation/issues/1532)
- issue: [go-annotation#1450](https://github.com/geneontology/go-annotation/issues/1450)

<!-- END GENERATED -->
