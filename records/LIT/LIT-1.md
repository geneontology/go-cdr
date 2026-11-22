---
id: LIT-1
title: Annotate the conclusion the experiment supports, not the assay's name or the authors' framing.
status: proposed
topic: LIT
provenance: GOC
provenance_note: '[GOC] [wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations).'
go_terms:
- term_id: GO:0048870
  label: cell motility
- term_id: GO:0042060
  label: wound healing
- term_id: GO:0006309
  label: apoptotic DNA fragmentation
- term_id: GO:0004531
  label: deoxyribonuclease II activity
sources:
- kind: issue
  title: go-annotation#1005
  url: https://github.com/geneontology/go-annotation/issues/1005
- kind: paper
  title: PMID:16500043
  url: https://europepmc.org/article/MED/16500043
- kind: wiki
  title: Tips
  url: https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations
date: '2026-11-15'
---

# LIT-1. Annotate the conclusion the experiment supports, not the assay's name or the authors' framing.

## Decision

Annotate the conclusion the experiment supports, not the assay's name or the authors' framing.

## Context

Some assays share a name with a GO term but measure something else. The Tips page
lists them: a scratch "wound-healing assay" measures `GO:0048870` cell motility,
not `GO:0042060` wound healing; DNA fragmentation and caspase activation measure
whether apoptosis happened, not whether the gene product does
`GO:0006309` apoptotic DNA fragmentation. Likewise, "expressed during" or
"activated during" a stage is not involvement in the process that defines the
stage: a yeast spore-wall protein induced during meiosis is not involved in
meiotic division ([go-annotation#1005](https://github.com/geneontology/go-annotation/issues/1005)).

Some assay conditions test general properties of the protein rather than its
function. The Tips page's example: DNase II is less active when tunicamycin blocks
its glycosylation ([PMID:16500043](https://europepmc.org/article/MED/16500043)).
The figure supports `GO:0004531` deoxyribonuclease II activity and nothing about
regulation, because tunicamycin is not shown to bind DNase II and glycosylation is
not a known regulatory switch for it.

*How to apply.* For each candidate term, write the one-sentence result it rests
on, in your own words, without the term's label. If the sentence describes a
readout ("migration into the scratch was reduced"), annotate the process the
readout measures, or nothing.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] [wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations). |
| Date | 2026-11-15 |
| GO terms | `GO:0048870` cell motility; `GO:0042060` wound healing; `GO:0006309` apoptotic DNA fragmentation; `GO:0004531` deoxyribonuclease II activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [LIT-1-E1](LIT-1.examples.yaml): Negative regulation of wound healing from a scratch-migration assay | Non-conformant | FGF2 involved_in GO:0061045 negative regulation of wound healing (IDA, PMID:19577615) |

## Sources

- issue: [go-annotation#1005](https://github.com/geneontology/go-annotation/issues/1005)
- paper: [PMID:16500043](https://europepmc.org/article/MED/16500043)
- wiki: [Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)

<!-- END GENERATED -->
