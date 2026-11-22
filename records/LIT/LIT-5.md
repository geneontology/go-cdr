---
id: LIT-5
title: In overexpression and heterologous systems, separate the assay from the phenotype, and annotate
  the gene that was expressed.
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC] for the IDA/IMP boundary (#6468); [GOC+] for the dose check.'
evidence_codes:
- IDA
- IMP
- IGI
related:
- LIT-8
- EV-5
sources:
- kind: wiki
  title: IMP
  url: https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29
- kind: issue
  title: go-annotation#6468
  url: https://github.com/geneontology/go-annotation/issues/6468
- kind: paper
  title: PMID:31206516
  url: https://europepmc.org/article/MED/31206516
date: '2026-11-15'
---

# LIT-5. In overexpression and heterologous systems, separate the assay from the phenotype, and annotate the gene that was expressed.

## Decision

In overexpression and heterologous systems, separate the assay from the phenotype, and annotate the gene that was expressed.

## Context

Expression systems are legitimate vehicles. A protein expressed in COS cells,
insect cells or E. coli and assayed for its activity is a direct assay of that
protein. A phenotype caused by expressing it is something else: a gain-of-function
or dosage effect, which seldom reveals normal function
([wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29);
[go-annotation#6468](https://github.com/geneontology/go-annotation/issues/6468)).
Three checks:

- **Is the readout the product's own activity or location?** Then annotate the
  MF or CC (IDA). If it is a cellular phenotype, annotate a process only by the
  rules for phenotypes ([LIT-8](LIT-8.md)), as IMP.
- **Does dose change the answer?** Fission yeast Epe1 at single copy removes
  ectopic heterochromatin only partly, while overexpressed Epe1 erases it
  completely ([PMID:31206516](https://europepmc.org/article/MED/31206516), cited
  in the Epe1 review). A result seen only on overexpression describes capacity,
  not normal function.
- **Whose gene is it?** The annotation goes to the expressed gene in its own
  species, not to the host. Mouse cDNA expressed in human HEK293 cells annotates
  the mouse gene. A human gene complementing a yeast mutant annotates the human
  gene by IGI, with the yeast gene in WITH/FROM
  ([evidence-codes EV-5](../EV/EV-5.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the IDA/IMP boundary (#6468); [GOC+] for the dose check. |
| Date | 2026-11-15 |
| Related | [LIT-8](LIT-8.md), [EV-5](../EV/EV-5.md) |
| Evidence codes | IDA, IMP, IGI |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [LIT-5-E1](LIT-5.examples.yaml): Epe1's boundary function annotated from the deletion, not the overexpression | Conformant | Epe1 involved_in GO:0033696 heterochromatin boundary formation (IMP, PMID:31206516) |
| [EV-5-E1](../EV/EV-5.examples.yaml): A plant arginase annotated by IGI from complementation of yeast (from [EV-5](../EV/EV-5.md)) | Conformant | ARGAH1 enables GO:0004053 arginase activity (IGI, PMID:7770544) |

## Sources

- wiki: [IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29)
- issue: [go-annotation#6468](https://github.com/geneontology/go-annotation/issues/6468)
- paper: [PMID:31206516](https://europepmc.org/article/MED/31206516)

<!-- END GENERATED -->
