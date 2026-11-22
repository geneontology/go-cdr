---
id: IEA-7
title: Use only exact reaction mappings, and only for physiological reactions
status: proposed
topic: IEA
provenance: GOC
go_terms:
- term_id: GO:0044024
  label: histone H2AS1 kinase activity
sources:
- kind: issue
  title: go-annotation#5432
  url: https://github.com/geneontology/go-annotation/issues/5432
- kind: issue
  title: go-annotation#1519
  url: https://github.com/geneontology/go-annotation/issues/1519
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: web
  title: ENZYME_SPECIFICITY
  url: https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html
- kind: web
  title: RHEA
  url: https://ai4curation.io/ai-gene-review/pages/projects/RHEA.html
date: '2026-11-15'
---

# IEA-7. Use only exact reaction mappings, and only for physiological reactions

## Decision

EC2GO and Rhea2GO may drive annotation only through `exactMatch` cross-references. A
`broadMatch` or `narrowMatch` xref documents a relation and must never generate annotations. An EC
number applied to a protein for a non-physiological or assay-only reaction should not produce a GO
term, even if the EC assignment is kept.

## Context

broad-match EC xrefs leaked into the mapping export and annotated 82 *S. pombe* kinases
to `GO:0044024` histone H2AS1 kinase activity from EC 2.7.11.1; the GO position is that broadMatch
xrefs must not feed pipelines ([go-annotation#5432](https://github.com/geneontology/go-annotation/issues/5432)).
GO annotation concerns physiologically relevant reactions, so a mapping for a non-physiological EC
use should be removed while the EC number stays ([go-annotation#1519](https://github.com/geneontology/go-annotation/issues/1519)).
For weak or promiscuous activities, apply the same tiers as for experimental rows
([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), "Measured activity is not automatically function";
[ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html)).

## Application

Worked example: the repo's Rhea audit found that 88% of reactions carrying an EC number map to the
same GO term EC2GO already supplies, so most `GO_REF:0000116` rows are redundant, and that the real
gap is reactions with no GO target at all (36% of enzymatic reactions), not mis-propagation
([RHEA](https://ai4curation.io/ai-gene-review/pages/projects/RHEA.html)). A reviewer seeing a Rhea2GO row should expect an EC2GO twin and judge the
pair together.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0044024` histone H2AS1 kinase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-7-E1](IEA-7.examples.yaml): Rhea2GO acyl-CoA hydrolase term from a non-physiological substrate | Non-conformant | OLAH enables GO:0052816 long-chain fatty acyl-CoA hydrolase activity (IEA, GO_REF:0000116) |

## Sources

- issue: [go-annotation#5432](https://github.com/geneontology/go-annotation/issues/5432)
- issue: [go-annotation#1519](https://github.com/geneontology/go-annotation/issues/1519)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- web: [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html)
- web: [RHEA](https://ai4curation.io/ai-gene-review/pages/projects/RHEA.html)

<!-- END GENERATED -->
