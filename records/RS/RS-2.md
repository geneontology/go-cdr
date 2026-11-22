---
id: RS-2
title: Annotate regulation of X only when the gene product modulates X, and name the target
status: proposed
topic: RS
provenance: GOC_PLUS
provenance_note: '[GOC+]. Requiring a named target, or the honest fallback to an upstream relation, is
  our sharpening.'
aspects:
- P
go_terms:
- term_id: GO:0061501
  label: 2',3'-cyclic GMP-AMP synthase activity
- term_id: GO:0140896
  label: cGAS/STING signaling pathway
- term_id: GO:0016032
  label: viral process
- term_id: GO:0005096
  label: GTPase activator activity
related:
- BP-4
differences:
- prior_source: '[wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation),
    Guideline 5'
  prior_said: IMP can support regulation terms when assay, allele type and gene identity are considered.
  we_recommend: IMP alone supports an upstream relation. A regulation term needs a named target or a known
    regulatory mechanism (RS-2).
  why: 'The 2022 PomBase breakdown and #2570 show that phenotype-based regulation rows are the main source
    of errors in this class.'
sources:
- kind: wiki
  title: Annotating from phenotypes
  url: https://wiki.geneontology.org/index.php/Annotating_from_phenotypes
- kind: issue
  title: go-annotation#2570
  url: https://github.com/geneontology/go-annotation/issues/2570
- kind: drive
  title: 2022 questions about regulation
  url: https://drive.google.com/open?id=1J_WpQPSyn4wvsMtxEAG4d7xA4SLmA0m2
- kind: drive
  title: GO-CAM Jamboree 2020 – Regulation notes
  url: https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40
- kind: issue
  title: go-annotation#2587
  url: https://github.com/geneontology/go-annotation/issues/2587
- kind: issue
  title: go-annotation#1979
  url: https://github.com/geneontology/go-annotation/issues/1979
- kind: issue
  title: go-annotation#1166
  url: https://github.com/geneontology/go-annotation/issues/1166
date: '2026-11-15'
---

# RS-2. Annotate regulation of X only when the gene product modulates X, and name the target

## Decision

**Statement.** A regulation annotation needs evidence that the gene product's activity changes the activity, amount or location of a specific participant of X, or changes when X starts or stops. Record the participant when known: `has_input` on the BP annotation, or the regulated gene product in a GO-CAM. A perturbation that changes the outcome of X, with no target, does not support a regulation term. It supports `acts upstream of or within, positive/negative effect` X (BP-4).

## Context

The phenotype guideline asks for MF-level evidence and says mutant phenotypes "more often provide supporting, rather than definitive" evidence for regulation ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). Curators in [go-annotation#2570](https://github.com/geneontology/go-annotation/issues/2570) argued that regulation terms should require mechanistic evidence of control. In the 2022 PomBase breakdown of 922 "regulation of biological process" annotations, nearly all valid cases fell into two mechanisms, signalling and regulation of gene expression. The remainder were mostly ontology or annotation errors ([Drive: 2022 questions about regulation](https://drive.google.com/open?id=1J_WpQPSyn4wvsMtxEAG4d7xA4SLmA0m2)). The 2020 GO-CAM jamboree gave three patterns for a regulatory link between activities. The first is a direct state change of a successive activity of another gene product (MAPKK to MAPK). The second is a binding activity that switches on another activity of the same product. The third is a specificity factor that controls the amount of the downstream product (a transcription factor and its target, a miRNA and its mRNA). Enzymes that modify a protein only as part of its trafficking were excluded ([Drive: GO-CAM Jamboree 2020 – Regulation notes](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)). The extension relation for the regulated entity is now `has_input`; `has_regulation_target` was retired for it, although PomBase keeps a local display label ([go-annotation#2587](https://github.com/geneontology/go-annotation/issues/2587)).

## Application

**Worked examples.**

- Human cGAS enables GO:0061501 2',3'-cyclic GMP-AMP synthase activity. Its product, cGAMP, activates STING1. The 2018 review found that cGAS should not be annotated as a regulator of the viral life cycle, because the cyclic nucleotide does the regulating and the enzyme acts upstream of it ([go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979)). With the current ontology, the second-messenger producer is a participant of the pathway it starts: GO:0140896 cGAS/STING signaling pathway. It is not a regulator of GO:0016032 viral process.
- Activity is more specific than outcome. A GEF does not alter the GTPase's catalytic rate, so it is not GO:0005096 GTPase activator activity ([go-annotation#1166](https://github.com/geneontology/go-annotation/issues/1166)). On the BP side, the GEF is part of the signalling pathway the GTPase transduces.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. Requiring a named target, or the honest fallback to an upstream relation, is our sharpening. |
| Date | 2026-11-15 |
| Related | [BP-4](../BP/BP-4.md) |
| GO terms | `GO:0061501` 2',3'-cyclic GMP-AMP synthase activity; `GO:0140896` cGAS/STING signaling pathway; `GO:0016032` viral process; `GO:0005096` GTPase activator activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [RS-2-E1](RS-2.examples.yaml): Regulation of beta-glucan biosynthesis on Cdc42 marked over-annotated | Conformant | cdc42 involved_in GO:0032951 regulation of beta-glucan biosynthetic process (IGI, PMID:8887550) |
| [RS-2-E2](RS-2.examples.yaml): Ebola VP35 negative regulation of gene expression replaced by its IRF3 mechanism | Conformant | VP35 involved_in GO:0010629 negative regulation of gene expression (IDA, PMID:12829834) |
| [RS-2-E3](RS-2.examples.yaml): Positive regulation of cell division kept on the kinetochore subunit SPC24 | Non-conformant | SPC24 acts_upstream_of_or_within GO:0051781 positive regulation of cell division (IMP, PMID:29356153) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation), Guideline 5 | IMP can support regulation terms when assay, allele type and gene identity are considered. | IMP alone supports an upstream relation. A regulation term needs a named target or a known regulatory mechanism (RS-2). | The 2022 PomBase breakdown and #2570 show that phenotype-based regulation rows are the main source of errors in this class. |

## Sources

- wiki: [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
- issue: [go-annotation#2570](https://github.com/geneontology/go-annotation/issues/2570)
- drive: [2022 questions about regulation](https://drive.google.com/open?id=1J_WpQPSyn4wvsMtxEAG4d7xA4SLmA0m2)
- drive: [GO-CAM Jamboree 2020 – Regulation notes](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)
- issue: [go-annotation#2587](https://github.com/geneontology/go-annotation/issues/2587)
- issue: [go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979)
- issue: [go-annotation#1166](https://github.com/geneontology/go-annotation/issues/1166)

<!-- END GENERATED -->
