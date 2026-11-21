---
id: LIT-8
title: A phenotype shows necessity; annotate the most proximal process and use the weakest relation the
  evidence allows.
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC] for the phenotype rules; [GOC+] for the performer test and the substrate convention
  ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).'
go_terms:
- term_id: GO:0006412
  label: translation
- term_id: GO:0002003
  label: angiotensin maturation
- term_id: GO:0090200
  label: positive regulation of release of cytochrome c from mitochondria
sources:
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: wiki
  title: Annotating from phenotypes
  url: https://wiki.geneontology.org/index.php/Annotating_from_phenotypes
- kind: drive
  title: Case studies, annotating from mutant phenotypes
  url: https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0
- kind: paper
  title: PMID:26666268
  url: https://europepmc.org/article/MED/26666268
date: '2026-11-15'
---

# LIT-8. A phenotype shows necessity; annotate the most proximal process and use the weakest relation the evidence allows.

## Decision

A phenotype shows necessity; annotate the most proximal process and use the weakest relation the evidence allows.

## Context

A knockout that abolishes a process shows the gene is needed for it, and the gene
product could be a step in the process, an upstream regulator, a supplier of a
substrate, or the substrate itself. Before writing `involved_in`, name the gene
product that performs the step ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), "Do not add what
curators deliberately declined to add"). The GOC phenotype guideline gives the
traps and the defaults
([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)):

- **Required for is not involved in.** `involved_in` asserts that the product's
  MF is part of the process. If that is not shown, use `acts_upstream_of_or_within`
  (or its positive or negative child) or do not annotate the process.
- **Work outward from the MF.** For a transcription factor, the most proximal
  process is regulation of transcription; next, the cell fate it specifies; the
  behaviour of the animal is a phenotype, not a GO process for the TF
  ([Drive: Case studies, annotating from mutant phenotypes](https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0)).
- **High-level phenotypes.** For lifespan, behaviour, growth, cell death,
  proliferation, migration, development and protein localisation, the guideline
  "strongly encourage[s]" curators not to annotate unless the mechanism is known.
- **Pleiotropy.** Yeast spliceosome mutants have translation defects because most
  yeast introns are in ribosomal protein genes; their `GO:0006412` translation rows
  were removed once splicing was established. Splicing factors are needed for
  cell-cycle progression without being part of it. Inviable mutants are a warning
  sign.
- **Regulation needs a mechanism.** A "regulation of P" annotation should be backed
  by evidence that the product's MF regulates an MF in P.
- **Substrates are not participants.** Angiotensinogen is necessary for
  `GO:0002003` angiotensin maturation and carries no annotation to it in human,
  mouse or rat; the proteases that cut it do.

## Application

*Example (not to annotate).* CHCHD10 mutant alleles inhibit apoptosis by
preventing cytochrome c release ([PMID:26666268](https://europepmc.org/article/MED/26666268)).
The guideline allows at most a causally-upstream annotation to apoptotic process and
explicitly rejects `GO:0090200` positive regulation of release of cytochrome c from
mitochondria.

Details on relations, regulation and causal distance are in
[biological-process.md](../BP/README.md) and
[regulation-and-signaling.md](../RS/README.md).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the phenotype rules; [GOC+] for the performer test and the substrate convention ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)). |
| Date | 2026-11-15 |
| GO terms | `GO:0006412` translation; `GO:0002003` angiotensin maturation; `GO:0090200` positive regulation of release of cytochrome c from mitochondria |

## Sources

- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- wiki: [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
- drive: [Case studies, annotating from mutant phenotypes](https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0)
- paper: [PMID:26666268](https://europepmc.org/article/MED/26666268)

<!-- END GENERATED -->
