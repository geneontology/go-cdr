---
id: LIT-3
title: An in vitro activity supports a molecular function only at the depth that was tested; decide whether
  the protein evolved to perform it.
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC+]. GO documentation has no promiscuity rule; the tiers follow de Crécy-Lagard et
  al. 2025 (PMID:40703034) as adopted in [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html).'
evidence_codes:
- IDA
- IBA
- IC
- IEA
go_terms:
- term_id: GO:0061710
  label: L-threonylcarbamoyladenylate synthase activity
- term_id: GO:0047400
  label: phosphonoacetate hydrolase activity
- term_id: GO:0004358
  label: L-glutamate N-acetyltransferase activity, acting on acetyl-L-ornithine as donor
- term_id: GO:0004042
  label: L-glutamate N-acetyltransferase activity, acting on acetyl-CoA as donor
related:
- EV-12
sources:
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: web
  title: ENZYME_SPECIFICITY
  url: https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html
- kind: issue
  title: go-annotation#5845
  url: https://github.com/geneontology/go-annotation/issues/5845
date: '2026-11-15'
---

# LIT-3. An in vitro activity supports a molecular function only at the depth that was tested; decide whether the protein evolved to perform it.

## Decision

An in vitro activity supports a molecular function only at the depth that was tested; decide whether the protein evolved to perform it.

## Context

An enzyme assay supports the reaction that was assayed, with the substrate that
was used. Do not climb to a narrower term (a specific substrate the paper did not
test) or jump to a pathway: an activity on a pathway intermediate supports the MF,
and a BP annotation to the pathway needs in vivo evidence or an IC that states the
step ([evidence-codes EV-12](../EV/EV-12.md)).

Measured activity is not automatically function
([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md); [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html)).
State the judgement in `reason`:

| Tier | Action | When |
|---|---|---|
| Genuine secondary activity | KEEP_AS_NON_CORE | respectable efficiency; plausible physiological substrate or in vivo phenotype; no other enzyme owns the reaction |
| Real in vitro activity, relevance unknown | MARK_AS_OVER_ANNOTATED | activity is real, nothing shows it is used |
| Promiscuous noise | REMOVE, even on IDA | a dedicated enzyme for the reaction exists in the organism; the activity is orders of magnitude lower; the protein lacks the specificity determinants |

## Application

*Examples.* ECOLI/yciO, `GO:0061710` L-threonylcarbamoyladenylate synthase
activity: REMOVE. TsaC is the essential dedicated enzyme, YciO's rate is about
10⁴-fold lower, and YciO lacks the KRSN tetrad. ECOLI/yjdM, `GO:0047400`
phosphonoacetate hydrolase activity: MARK_AS_OVER_ANNOTATED, because E. coli has
no dedicated enzyme to assign the reaction to. Fission yeast aga1 (ArgJ) carries
both `GO:0004358` (acetyl-L-ornithine donor) and `GO:0004042` (acetyl-CoA donor);
the acetyl-CoA activity was measured in an overexpression study at about 0.3% of
the ornithine-donor rate, and PomBase had not annotated it experimentally
([go-annotation#5845](https://github.com/geneontology/go-annotation/issues/5845)).
The review keeps the IBA and IEA rows for it as non-core.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. GO documentation has no promiscuity rule; the tiers follow de Crécy-Lagard et al. 2025 (PMID:40703034) as adopted in [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html). |
| Date | 2026-11-15 |
| Related | [EV-12](../EV/EV-12.md) |
| Evidence codes | IDA, IBA, IC, IEA |
| GO terms | `GO:0061710` L-threonylcarbamoyladenylate synthase activity; `GO:0047400` phosphonoacetate hydrolase activity; `GO:0004358` L-glutamate N-acetyltransferase activity, acting on acetyl-L-ornithine as donor; `GO:0004042` L-glutamate N-acetyltransferase activity, acting on acetyl-CoA as donor |

## Sources

- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- web: [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html)
- issue: [go-annotation#5845](https://github.com/geneontology/go-annotation/issues/5845)

<!-- END GENERATED -->
