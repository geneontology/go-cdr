---
id: IEA-3
title: Map a domain to what the domain does, not to what proteins containing it do
status: proposed
topic: IEA
provenance: GOC
go_terms:
- term_id: GO:0003677
  label: DNA binding
- term_id: GO:0003676
  label: nucleic acid binding
sources:
- kind: paper
  title: PMID:22301074
  url: https://europepmc.org/article/MED/22301074
- kind: issue
  title: go-annotation#2710
  url: https://github.com/geneontology/go-annotation/issues/2710
- kind: web
  title: INTERPRO
  url: https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html
date: '2026-11-15'
---

# IEA-3. Map a domain to what the domain does, not to what proteins containing it do

## Decision

A domain entry may carry only terms the domain itself performs or enables. Whole-protein
functions (transcription factor activity, a complex's catalytic activity, a process) belong on
family entries whose membership is functionally uniform. Do not map GO terms to InterPro
homologous-superfamily entries.

## Context

this is InterPro's revised protocol ([PMID:22301074](https://europepmc.org/article/MED/22301074))
and its stated convention for homologous superfamilies ([go-annotation#2710](https://github.com/geneontology/go-annotation/issues/2710)).
The repo still finds domain entries carrying whole-protein or neighbouring-domain functions
([INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html)).

## Application

Worked examples: `IPR042371` (Z-binding domain) maps dsRNA adenosine deaminase activity, so ZBP1,
which has Z-binding domains but no deaminase domain, inherits ADAR1's catalytic activity; the
deaminase belongs to `IPR002466`. `IPR006935` (Helicase/UvrB, N-terminal) maps `GO:0003677` DNA
binding, which RIG-I-like receptors such as IFIH1 inherit although they sense RNA; the proposed fix
is `GO:0003676` nucleic acid binding, as on the sibling helicase entries `IPR011545` and
`IPR006555`. The MADS-box domain supports DNA binding and dimerisation, not DNA-binding
transcription factor activity ([INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0003677` DNA binding; `GO:0003676` nucleic acid binding |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-3-E1](IEA-3.examples.yaml): Z-binding domain entry carries ADAR1's deaminase activity to ZBP1 | Non-conformant | ZBP1 enables GO:0003726 double-stranded RNA adenosine deaminase activity (IEA, GO_REF:0000002) |
| [IEA-3-E2](IEA-3.examples.yaml): Helicase/UvrB N-terminal entry gives an RNA sensor DNA binding | Non-conformant | IFIH1 enables GO:0003677 DNA binding (IEA, GO_REF:0000002) |

## Sources

- paper: [PMID:22301074](https://europepmc.org/article/MED/22301074)
- issue: [go-annotation#2710](https://github.com/geneontology/go-annotation/issues/2710)
- web: [INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html)

<!-- END GENERATED -->
