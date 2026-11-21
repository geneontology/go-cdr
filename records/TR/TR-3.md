---
id: TR-3
title: 'Read each DNA-binding assay for what it shows: location, binding, or direct sequence-specific
  binding'
status: proposed
topic: TR
provenance: GOC
aspects:
- F
- P
evidence_codes:
- ISM
go_terms:
- term_id: GO:0000785
  label: chromatin
related:
- TR-2
sources:
- kind: wiki
  title: 'Annotation consistency: ChIP experiments'
  url: https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments
- kind: issue
  title: go-annotation#943
  url: https://github.com/geneontology/go-annotation/issues/943
- kind: issue
  title: go-annotation#3235
  url: https://github.com/geneontology/go-annotation/issues/3235
- kind: issue
  title: go-annotation#2985
  url: https://github.com/geneontology/go-annotation/issues/2985
- kind: web
  title: TRANSCRIPTION_FACTORS
  url: https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html
date: '2026-11-15'
---

# TR-3. Read each DNA-binding assay for what it shows: location, binding, or direct sequence-specific binding

## Decision

ChIP and nuclear-extract EMSA (including supershift) show that a protein is at a
region or in a complex that binds it; they do not show that the protein binds DNA. Use
them for `GO:0000785` chromatin (CC) and, for an established dbTF, to identify targets.
Use purified-protein assays (EMSA, footprinting, SELEX, crystal structure) for DNA-binding
MF terms. HT-SELEX shows sequence recognition but not regulation. An InterPro mapping
supports DNA binding only if the InterPro entry itself maps to a DNA-binding term.

## Context

"In vivo ChIP experiments do not usually provide sufficient evidence for a
protein-DNA interaction because it does not demonstrate whether the interaction is
direct" ([wiki: Annotation consistency: ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments),
reviewed 2023; [go-annotation#943](https://github.com/geneontology/go-annotation/issues/943)).
The exception on that page, studies premised on direct binding through a known motif,
is the family prior of [TR-2](TR-2.md). Nuclear extracts identify transcription complexes,
so a shift "is not sufficient to attribute direct DNA binding because binding may be
indirect, through another DNA binding protein"
([go-annotation#3235](https://github.com/geneontology/go-annotation/issues/3235)).
ISM annotations of dbTF activity from InterPro entries that carry no DNA-binding mapping
were removed as unsupported
([go-annotation#2985](https://github.com/geneontology/go-annotation/issues/2985)).
The guideline's high-throughput notes say HT-SELEX supports DNA binding but not dbTF
activity without functional evidence, and ChIP-seq is inconclusive alone
([TRANSCRIPTION_FACTORS](https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html), summarising the 2023 PDF).

## Application

Worked example. LYAR was reported to bind rDNA in a supershift assay with nuclear
extract. The antibody supershift does not show direct binding, and other papers show it
regulates rDNA transcription without binding DNA, so the evidence does not support a
dbTF annotation ([go-annotation#3235](https://github.com/geneontology/go-annotation/issues/3235)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Related | [TR-2](TR-2.md) |
| Evidence codes | ISM |
| GO terms | `GO:0000785` chromatin |

## Sources

- wiki: [Annotation consistency: ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments)
- issue: [go-annotation#943](https://github.com/geneontology/go-annotation/issues/943)
- issue: [go-annotation#3235](https://github.com/geneontology/go-annotation/issues/3235)
- issue: [go-annotation#2985](https://github.com/geneontology/go-annotation/issues/2985)
- web: [TRANSCRIPTION_FACTORS](https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html)

<!-- END GENERATED -->
