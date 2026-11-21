---
id: PC-5
title: The subunit that performs the activity `enables` it, with no qualifier, even when it works inside
  a complex; homomultimers also `enable`.
status: proposed
topic: PC
provenance: GOC
aspects:
- C
- F
go_terms:
- term_id: GO:0004579
  label: dolichyl-diphosphooligosaccharide-protein glycotransferase activity
- term_id: GO:0000030
  label: mannosyltransferase activity
- term_id: GO:0003924
  label: GTPase activity
- term_id: GO:0004298
  label: threonine-type endopeptidase activity
- term_id: GO:0008320
  label: transmembrane protein transporter activity
- term_id: GO:0140436
  label: mitochondrial signal sequence receptor activity
sources:
- kind: wiki
  title: Enables
  url: https://wiki.geneontology.org/index.php/Enables
- kind: drive
  title: GOC 2021-05 Contributes_to
  url: https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks
- kind: issue
  title: go-annotation#2664
  url: https://github.com/geneontology/go-annotation/issues/2664
- kind: web
  title: PROTEIN_COMPLEX_FUNCTIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html
- kind: issue
  title: go-annotation#6466
  url: https://github.com/geneontology/go-annotation/issues/6466
date: '2026-11-15'
---

# PC-5. The subunit that performs the activity `enables` it, with no qualifier, even when it works inside a complex; homomultimers also `enable`.

## Decision

The subunit that performs the activity `enables` it, with no qualifier, even when it works inside a complex; homomultimers also `enable`.

## Context

`enables` is used for a complex member when the activity is mediated by that gene product and
the other subunits are accessory
([wiki: Enables](https://wiki.geneontology.org/index.php/Enables)). The 2020 Complex Working
Group's "simple rule" is that MF is assigned to the subunit that performs it, and that the
catalytic subunit can be identified in most enzyme complexes: E3 ligases, HDAC and HAT
complexes, kinase complexes
([Drive: GOC 2021-05 Contributes_to](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks);
[go-annotation#2664](https://github.com/geneontology/go-annotation/issues/2664)).

## Application

*Examples* (from the GO wiki unless noted):
- STT3 `enables` `GO:0004579` dolichyl-diphosphooligosaccharide-protein glycotransferase
  activity; it is the catalytic subunit of the oligosaccharyltransferase.
- PIGM `enables` `GO:0000030` mannosyltransferase activity; the accessory PIGX is required but
  has no activity, and gets no annotation to it.
- eIF2 gamma `enables` `GO:0003924` GTPase activity; alpha and beta do not.
- PSMB5, whose Thr60 is the active-site nucleophile, `enables` `GO:0004298` threonine-type
  endopeptidase activity; the alpha-ring subunit PSMA1 does not
  ([PROTEIN_COMPLEX_FUNCTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html), proteasome pilot).
- TOM40 `enables` `GO:0008320` transmembrane protein transporter activity as the channel; TOM22
  and TOM20 enable `GO:0140436` mitochondrial signal sequence receptor activity, not a
  `contributes_to` transporter row
  ([go-annotation#6466](https://github.com/geneontology/go-annotation/issues/6466)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0004579` dolichyl-diphosphooligosaccharide-protein glycotransferase activity; `GO:0000030` mannosyltransferase activity; `GO:0003924` GTPase activity; `GO:0004298` threonine-type endopeptidase activity; `GO:0008320` transmembrane protein transporter activity; `GO:0140436` mitochondrial signal sequence receptor activity |

## Sources

- wiki: [Enables](https://wiki.geneontology.org/index.php/Enables)
- drive: [GOC 2021-05 Contributes_to](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks)
- issue: [go-annotation#2664](https://github.com/geneontology/go-annotation/issues/2664)
- web: [PROTEIN_COMPLEX_FUNCTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html)
- issue: [go-annotation#6466](https://github.com/geneontology/go-annotation/issues/6466)

<!-- END GENERATED -->
