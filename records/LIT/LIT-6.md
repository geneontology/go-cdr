---
id: LIT-6
title: Annotate the gene product and organism actually assayed; a paper about a paralog, ortholog or partner
  is not evidence for your gene.
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC] for annotating the organism assayed; [GOC+] for the paralog and collision checks.'
evidence_codes:
- IDA
- ISO
- TAS
- ND
sources:
- kind: wiki
  title: TAS
  url: https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: paper
  title: PMID:11514575
  url: https://europepmc.org/article/MED/11514575
- kind: web
  title: WRONG_GENE_LEADS
  url: https://ai4curation.io/ai-gene-review/pages/projects/WRONG_GENE_LEADS.html
- kind: web
  title: MISCITATIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html
- kind: web
  title: ISOFORMS
  url: https://ai4curation.io/ai-gene-review/pages/projects/ISOFORMS.html
- kind: issue
  title: go-annotation#11
  url: https://github.com/geneontology/go-annotation/issues/11
date: '2026-11-15'
---

# LIT-6. Annotate the gene product and organism actually assayed; a paper about a paralog, ortholog or partner is not evidence for your gene.

## Decision

Annotate the gene product and organism actually assayed; a paper about a paralog, ortholog or partner is not evidence for your gene.

## Context

Before writing a row, confirm from the paper that the protein assayed is the one
being annotated: the species, the gene, and where relevant the isoform.

- **Orthologs.** A mouse experiment annotates the mouse gene. The human ortholog
  gets the function by ISO from that annotation, not by IDA citing the mouse paper.
  The TAS page makes the same point about reviews: authors often cite
  experiments in other organisms ([wiki: TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29)).
  For ND review, a paper on an ortholog is not literature on the gene, however
  strong ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).
- **Paralogs.** CSGALNACT1 carried ten rows from [PMID:11514575](https://europepmc.org/article/MED/11514575),
  which cloned the paralog CHSY1. PAPSS1 carried `skeletal system development`
  (TAS) from a paper whose abstract names the mutated gene as PAPSS2. Both are now
  recorded as `WRONG_GENE_PRODUCT` source defects
  ([WRONG_GENE_LEADS](https://ai4curation.io/ai-gene-review/pages/projects/WRONG_GENE_LEADS.html)).
- **Name collisions.** "AP-2" is both a transcription factor family and a
  clathrin adaptor complex, and an early AP-2α splice product was called "AP-2B";
  both collisions reached GOA as rows on TFAP2A and TFAP2B. "ARH1" and "BACH1" are
  similar traps ([MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html)).
- **Isoforms.** Record the isoform tested (`isoform:`), without assuming the
  function is isoform-specific ([ISOFORMS](https://ai4curation.io/ai-gene-review/pages/projects/ISOFORMS.html)).
- **Antibodies.** A cross-reacting antibody against another species' protein is
  not evidence of orthology or identity
  ([go-annotation#11](https://github.com/geneontology/go-annotation/issues/11)).

Multi-gene papers are legitimate: a calmodulin-mutation paper about CALM1 may
assay all three identical CALM proteins. The test is whether the gene was assayed,
not whether it is in the title.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for annotating the organism assayed; [GOC+] for the paralog and collision checks. |
| Date | 2026-11-15 |
| Evidence codes | IDA, ISO, TAS, ND |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [LIT-6-E1](LIT-6.examples.yaml): A GalNAc transferase IDA row citing the cloning paper of the paralog CHSY1 | Non-conformant | CSGALNACT1 enables GO:0008376 acetylgalactosaminyltransferase activity (IDA, PMID:11514575) |
| [LIT-6-E2](LIT-6.examples.yaml): Skeletal system development on PAPSS1 from a paper about PAPSS2 | Non-conformant | PAPSS1 involved_in GO:0001501 skeletal system development (TAS, PMID:9771708) |

## Sources

- wiki: [TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- paper: [PMID:11514575](https://europepmc.org/article/MED/11514575)
- web: [WRONG_GENE_LEADS](https://ai4curation.io/ai-gene-review/pages/projects/WRONG_GENE_LEADS.html)
- web: [MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html)
- web: [ISOFORMS](https://ai4curation.io/ai-gene-review/pages/projects/ISOFORMS.html)
- issue: [go-annotation#11](https://github.com/geneontology/go-annotation/issues/11)

<!-- END GENERATED -->
