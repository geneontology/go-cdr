---
id: RS-7
title: Intracellular signalling cassettes are part of pathways; cassette members may carry both terms
status: proposed
topic: RS
provenance: GOC_PLUS
provenance_note: '[GOC+]. The cassette document is a draft with open comments, so we state its rules as
  recommended practice.'
aspects:
- P
go_terms:
- term_id: GO:0141124
  label: intracellular signaling cassette
- term_id: GO:0000165
  label: MAPK cascade
- term_id: GO:0043491
  label: phosphatidylinositol 3-kinase/protein kinase B signal transduction
- term_id: GO:0005078
  label: MAP kinase scaffold activity
- term_id: GO:0007173
  label: epidermal growth factor receptor signaling pathway
- term_id: GO:0043410
  label: positive regulation of MAPK cascade
differences:
- prior_source: '[Drive: Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4)
    vs [go-annotation#1712](https://github.com/geneontology/go-annotation/issues/1712)'
  prior_said: 'The cassette draft puts ligand and receptor in "positive regulation of" the cassette. #1712
    puts ligands in the pathway, not its regulation.'
  we_recommend: 'Both hold, at different levels: the ligand is `involved_in` the receptor pathway and
    acts upstream of the cassette it triggers (RS-7).'
  why: 'Apparent conflict. The cassette document regulates the cassette, and #1712 concerns the receptor
    pathway.'
sources:
- kind: drive
  title: Intracellular signaling guidelines
  url: https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4
- kind: drive
  title: PAINT signaling annotation – meeting minutes, 2025
  url: https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM
- kind: issue
  title: go-annotation#1592
  url: https://github.com/geneontology/go-annotation/issues/1592
- kind: web
  title: MAPK_CASCADES
  url: https://ai4curation.io/ai-gene-review/pages/projects/MAPK_CASCADES.html
date: '2026-11-15'
---

# RS-7. Intracellular signalling cassettes are part of pathways; cassette members may carry both terms

## Decision

**Statement.** A cassette, a child of GO:0141124 intracellular signaling cassette such as GO:0000165 MAPK cascade or GO:0043491 phosphatidylinositol 3-kinase/protein kinase B signal transduction, starts with activation of its first component and runs to a predictable output. Annotate:

## Context

- cassette members to the cassette term, and also to the receptor pathway it serves when the evidence places them there;
- the ligand, the receptor and the components between the receptor and the first cassette member to the receptor pathway. Annotate them to "positive regulation of" the cassette only when the cassette term is used without its pathway context;
- the targets of the cassette's last kinase to the receptor pathway, not to the cassette.

A pathway-specific scaffold that tethers cassette components is part of the cassette. If it also directly activates a component, add the regulator MF separately.

**Rationale.** These are the draft intracellular signalling guidelines ([Drive: Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4)). The 2025 PAINT signalling work applied them to the cassette children of GO:0141124 ([Drive: PAINT signaling annotation – meeting minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM)). The scaffold ruling comes from the 2017 MAPK review: FlyBase chose "part of", to separate scaffolds from proteins that merely modulate the cascade. PomBase proposed GO:0005078 MAP kinase scaffold activity together with a separate enzyme regulator MF where the scaffold also allosterically activates a kinase ([go-annotation#1592](https://github.com/geneontology/go-annotation/issues/1592)). The 2023–2024 cascade review implemented these conclusions, and GO:0000165 MAPK cascade is not being obsoleted (same thread).

## Application

**Worked example.** In an RTK pathway, GRB2, SOS1 and RAS lie between the receptor and the first cassette member, RAF. They are `involved_in` the receptor pathway (for example GO:0007173), and, with only the cassette in view, in GO:0043410 positive regulation of MAPK cascade. RAF, MEK1/2 and ERK1/2 are `involved_in` GO:0000165, and in GO:0007173 where the evidence places them there. An ERK substrate transcription factor is `involved_in` GO:0007173 but not GO:0000165 ([MAPK_CASCADES](https://ai4curation.io/ai-gene-review/pages/projects/MAPK_CASCADES.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The cassette document is a draft with open comments, so we state its rules as recommended practice. |
| Date | 2026-11-15 |
| GO terms | `GO:0141124` intracellular signaling cassette; `GO:0000165` MAPK cascade; `GO:0043491` phosphatidylinositol 3-kinase/protein kinase B signal transduction; `GO:0005078` MAP kinase scaffold activity; `GO:0007173` epidermal growth factor receptor signaling pathway; `GO:0043410` positive regulation of MAPK cascade |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4) vs [go-annotation#1712](https://github.com/geneontology/go-annotation/issues/1712) | The cassette draft puts ligand and receptor in "positive regulation of" the cassette. #1712 puts ligands in the pathway, not its regulation. | Both hold, at different levels: the ligand is `involved_in` the receptor pathway and acts upstream of the cassette it triggers (RS-7). | Apparent conflict. The cassette document regulates the cassette, and #1712 concerns the receptor pathway. |

## Sources

- drive: [Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4)
- drive: [PAINT signaling annotation – meeting minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM)
- issue: [go-annotation#1592](https://github.com/geneontology/go-annotation/issues/1592)
- web: [MAPK_CASCADES](https://ai4curation.io/ai-gene-review/pages/projects/MAPK_CASCADES.html)

<!-- END GENERATED -->
