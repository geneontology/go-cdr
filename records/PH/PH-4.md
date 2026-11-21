---
id: PH-4
title: Place the IBD at the deepest node the evidence supports, and no deeper
status: proposed
topic: PH
provenance: GOC_PLUS
provenance_note: '[GOC] for the A/B/C logic and HGT blocking; [GOC+] for the prerequisite test.'
evidence_codes:
- IBD
go_terms:
- term_id: GO:0007259
  label: cell surface receptor signaling pathway via JAK-STAT
- term_id: GO:0046426
  label: negative regulation of receptor signaling pathway via JAK-STAT
differences:
- prior_source: '[wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)'
  prior_said: Choose MRCA, older or younger node by curator judgement.
  we_recommend: 'Add an explicit test: never above the taxon where the term''s prerequisite exists (PH-4).'
  why: JAK-STAT terms placed where STATs arose rather than where JAKs arose reached worms and amoebae.
sources:
- kind: wiki
  title: PAINT annotation guidelines
  url: https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines
- kind: wiki
  title: 13 March 2024 PAINT call
  url: https://wiki.geneontology.org/index.php/13_March_2024_PAINT_Conference_Call
- kind: wiki
  title: 11 Feb 2026 PAINT call
  url: https://wiki.geneontology.org/index.php/11_Feb_2026_PAINT_Conference_Call
- kind: web
  title: PAINT
  url: https://ai4curation.io/ai-gene-review/pages/projects/PAINT.html
- kind: web
  title: IBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html
- kind: web
  title: TAXON_PATHWAY_VARIANCE
  url: https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html
date: '2026-11-15'
---

# PH-4. Place the IBD at the deepest node the evidence supports, and no deeper

## Decision

Start from the most recent common ancestor of the experimentally annotated sequences. Move
the node deeper only when orthology, active-site conservation, consistent annotations in other
aspects, and the absence of contradicting well-studied members support it. Move it shallower,
or annotate twice, when the function plausibly arose more than once. Never place a term above
the taxon in which its prerequisite exists.

## Context

this is the PAINT A/B/C decision: the MRCA is right, the function is older, or it
is younger and convergent ([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)).
We add an explicit prerequisite test, because the cleanest repo failures are terms placed where
the protein family arose rather than where the pathway arose. Taxon-constraint violations in
PAINT come from three sources: old IBDs above an `only_in_taxon` limit, propagation through a
`never_in_taxon` clade, and horizontal transfer nodes
([wiki: 13 March 2024 PAINT call](https://wiki.geneontology.org/index.php/13_March_2024_PAINT_Conference_Call)).
PAINT now blocks CC and BP propagation below horizontal-transfer nodes
([wiki: 11 Feb 2026 PAINT call](https://wiki.geneontology.org/index.php/11_Feb_2026_PAINT_Conference_Call)).

## Application

Worked example: the STAT family IBD for `GO:0007259` cell surface receptor signaling pathway
via JAK-STAT sits on PTN000927860, the Unikonts node, though its seeds support only Bilateria.
JAKs are animal-only, so worm STA-1 and STA-2 and *Dictyostelium* STATs inherit a pathway their
lineage lacks. The PIAS node PTN000845825 likewise passes `GO:0046426` negative regulation of
receptor signaling pathway via JAK-STAT to worm GEI-17. The class-level fix is a taxon
constraint on the pathway term, which GO accepted; the node-level fix is a move of the IBD
(`TOO_DEEP`) or IRDs on the nematode and amoebozoan branches ([PAINT](https://ai4curation.io/ai-gene-review/pages/projects/PAINT.html),
[IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html), pattern 14, [TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the A/B/C logic and HGT blocking; [GOC+] for the prerequisite test. |
| Date | 2026-11-15 |
| Evidence codes | IBD |
| GO terms | `GO:0007259` cell surface receptor signaling pathway via JAK-STAT; `GO:0046426` negative regulation of receptor signaling pathway via JAK-STAT |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) | Choose MRCA, older or younger node by curator judgement. | Add an explicit test: never above the taxon where the term's prerequisite exists (PH-4). | JAK-STAT terms placed where STATs arose rather than where JAKs arose reached worms and amoebae. |

## Sources

- wiki: [PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)
- wiki: [13 March 2024 PAINT call](https://wiki.geneontology.org/index.php/13_March_2024_PAINT_Conference_Call)
- wiki: [11 Feb 2026 PAINT call](https://wiki.geneontology.org/index.php/11_Feb_2026_PAINT_Conference_Call)
- web: [PAINT](https://ai4curation.io/ai-gene-review/pages/projects/PAINT.html)
- web: [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)
- web: [TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)

<!-- END GENERATED -->
