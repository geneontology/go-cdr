---
id: LIT-7
title: Cite the primary paper that contains the evidence, and verify that the identifier resolves to it.
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC] for citing primary work; [GOC+] for the identifier checks.'
evidence_codes:
- IDA
- IPI
- IEP
- TAS
go_terms:
- term_id: GO:0071260
  label: cellular response to mechanical stimulus
related:
- EV-10
- EV-3
sources:
- kind: paper
  title: PMID:37160800
  url: https://europepmc.org/article/MED/37160800
- kind: web
  title: MISCITATIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# LIT-7. Cite the primary paper that contains the evidence, and verify that the identifier resolves to it.

## Decision

Cite the primary paper that contains the evidence, and verify that the identifier resolves to it.

## Context

The reference is the paper whose results support the annotation. A review is the
right reference only for TAS, and TAS is the right code only when the primary
paper cannot be reached ([evidence-codes EV-10](../EV/EV-10.md)). Recent
reviews are still worth reading for context: the Tips page asks curators to work
gene by gene or pathway by pathway, not paper by paper.

Primary evidence means results. A meeting report is not: UniProt cites
[PMID:37160800](https://europepmc.org/article/MED/37160800), an 18-author
peroxisome meeting report with no abstract, with ECO:0000269 (experimental
evidence) for PEX39's function, two years before the primary paper. A paper in a
predatory journal deserves the same scepticism (Tips page).

Then check the identifier:

- **Digit errors.** NLRP3 carried IDA rows citing PMID:1189953, a 1975 psychiatry
  paper; a digit was dropped. PMID:22572157 (a platelet-antibody chip) stands in
  for PMID:22752157 (VRK2 anchoring KSR1-MEK1 to the ER) on 31 MGI rows.
- **Batch errors.** PMID:19593445, a paper on BAD in prostate cancer, supports
  `GO:0071260` cellular response to mechanical stimulus (IEP) on 36 human genes it
  never mentions. One wrong identifier is rarely wrong once; check the gene's
  neighbours in the complex or family
  ([MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html)).
- **Partner errors.** For IPI rows, check the WITH/FROM partner against the paper
  ([evidence-codes EV-3](../EV/EV-3.md)).

In this repository a `supporting_text` must be a verbatim substring of the cached
paper, and the reference title is checked against fetched metadata. These checks
catch a wrong PMID whose title no longer matches; they do not catch a right paper
used for a claim it does not make. That is what `reference_review.correctness:
MISCITED` records ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for citing primary work; [GOC+] for the identifier checks. |
| Date | 2026-11-15 |
| Related | [EV-10](../EV/EV-10.md), [EV-3](../EV/EV-3.md) |
| Evidence codes | IDA, IPI, IEP, TAS |
| GO terms | `GO:0071260` cellular response to mechanical stimulus |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [LIT-7-E1](LIT-7.examples.yaml): NLRP3 IDA rows citing a 1975 psychiatry abstract | Non-conformant | NLRP3 enables GO:0060090 molecular adaptor activity (IDA, PMID:1189953) |
| [EV-10-E2](../EV/EV-10.examples.yaml): A P2X7 plasma membrane row cited to a P2X1 Reactome event (from [EV-10](../EV/EV-10.md)) | Non-conformant | P2RX7 located_in GO:0005886 plasma membrane (TAS, Reactome:R-HSA-139855) |

## Sources

- paper: [PMID:37160800](https://europepmc.org/article/MED/37160800)
- web: [MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
