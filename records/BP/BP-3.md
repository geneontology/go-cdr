---
id: BP-3
title: Run the comparator check before treating an absence as a gap
status: proposed
topic: BP
provenance: NEW
aspects:
- P
go_terms:
- term_id: GO:0002003
  label: angiotensin maturation
differences:
- prior_source: '[CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)'
  prior_said: Comparator check before `NEW` process terms.
  we_recommend: Same, and also when judging whether an existing lone annotation is an outlier (BP-3).
  why: Extension of the same logic to review.
sources:
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# BP-3. Run the comparator check before treating an absence as a gap

## Decision

**Statement.** Before proposing a `NEW` process annotation because related genes carry the term and this one does not, name two or three gene products that stand in the same role (other substrates, other ligands, other assembly factors) for the same kind of process. Check whether they carry the term. A systematic absence across genes, species and MODs is a convention to identify, not an oversight to correct.

## Context

"Every other participant has this term" usually means the term describes something this gene does not do. The check turns an assumption into a prediction that one QuickGO query can falsify. Also check production GO-CAMs (in this repository `gocams/index.tsv`): a curator who modelled the pathway, included the gene, and gave it a different role made a decision. If you disagree, argue with it explicitly.

## Application

**Worked example.** The renin–angiotensin GO-CAM (`gocams/6246724f00000549/`) contains AGT twice, once as the hormone-activity node and once as the proteases' input. Both roles are represented without placing AGT in GO:0002003 ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| GO terms | `GO:0002003` angiotensin maturation |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [BP-3-E1](BP-3.examples.yaml): The renin-angiotensin GO-CAM represents angiotensinogen without placing it in angiotensin maturation | Conformant | gomodel:6246724f00000549 |
| [BP-3-E2](BP-3.examples.yaml): A new keratinization row for a wool KAP, after a same-role comparator check | Conformant | KRTAP3-1 involved_in GO:0031424 keratinization (TAS, PMID:27240405) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) | Comparator check before `NEW` process terms. | Same, and also when judging whether an existing lone annotation is an outlier (BP-3). | Extension of the same logic to review. |

## Sources

- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
