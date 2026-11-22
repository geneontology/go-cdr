---
id: LIT-10
title: Know which findings are not annotatable, and leave them out.
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC] for most rows; [GOC+] for the readout and vesicle rows.'
evidence_codes:
- IEP
- HMP
- ISS
- IC
- ND
go_terms:
- term_id: GO:0005515
  label: protein binding
related:
- EV-3
sources:
- kind: wiki
  title: ND
  url: https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code
- kind: web
  title: IEP
  url: https://ai4curation.io/ai-gene-review/pages/projects/IEP.html
- kind: wiki
  title: HMP
  url: https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_%28HMP%29
- kind: web
  title: OMICS_EVIDENCE
  url: https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html
- kind: issue
  title: go-annotation#2521
  url: https://github.com/geneontology/go-annotation/issues/2521
- kind: wiki
  title: Tips
  url: https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations
- kind: issue
  title: go-annotation#1381
  url: https://github.com/geneontology/go-annotation/issues/1381
- kind: issue
  title: go-annotation#5160
  url: https://github.com/geneontology/go-annotation/issues/5160
- kind: issue
  title: go-annotation#1626
  url: https://github.com/geneontology/go-annotation/issues/1626
- kind: web
  title: NO_DATA
  url: https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html
date: '2026-11-15'
---

# LIT-10. Know which findings are not annotatable, and leave them out.

## Decision

Know which findings are not annotatable, and leave them out.

## Context

The following do not support a GO annotation by themselves:

| Finding | Why not | Sources |
|---|---|---|
| Cloning, sequence, chromosomal location | no function shown | [wiki: ND](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code) |
| Disease association, biomarker use, GWAS hit | no function shown | wiki: ND |
| Expression atlas, tissue distribution | expression is not function | [IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html) |
| Primary hits of a genome-wide screen | false-positive rate; validate first | [wiki: HMP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_%28HMP%29) |
| Membership of a regulon or co-expression cluster | a property of the promoter | [IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html) |
| A protein found in a vesicle or body-fluid proteome | true but uninformative, usually non-core | [OMICS_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html) |
| Oligomeric state, stoichiometry | out of GO scope | [go-annotation#2521](https://github.com/geneontology/go-annotation/issues/2521) |
| Effect of a chemical that alters the cellular environment | not regulation of the protein | [wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) |
| A PTM required for activity, absent a regulatory role | a property, not a function | wiki: Tips |
| Speculation in the discussion | not a result | [go-annotation#1381](https://github.com/geneontology/go-annotation/issues/1381) |
| Lipid profiles, metabolite levels or expression changes in a mutant | readouts, not the gene's role | [go-annotation#5160](https://github.com/geneontology/go-annotation/issues/5160) |
| A computational prediction in a paper | IC and experimental codes do not apply; use ISS family or nothing | [go-annotation#1626](https://github.com/geneontology/go-annotation/issues/1626) |
| A bare interaction with no functional consequence | `GO:0005515` is removed by policy | [evidence-codes EV-3](../EV/EV-3.md) |

"Not annotatable in GO" does not mean worthless. Phenotypes, interactions and
expression data have their own resources, which is why GO can be selective. If a
gene has no annotatable data in an aspect, the honest record is ND, and the
absence may be a knowledge gap ([NO_DATA](https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for most rows; [GOC+] for the readout and vesicle rows. |
| Date | 2026-11-15 |
| Related | [EV-3](../EV/EV-3.md) |
| Evidence codes | IEP, HMP, ISS, IC, ND |
| GO terms | `GO:0005515` protein binding |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [LIT-10-E1](LIT-10.examples.yaml): Immune response projected from a SNP association with bacteremia | Non-conformant | TGFBR3 involved_in GO:0006955 immune response (IEA, GO_REF:0000107) |
| [LIT-10-E2](LIT-10.examples.yaml): Protein homodimerization activity from a monomer-dimer mixture | Non-conformant | lipA enables GO:0042803 protein homodimerization activity (IDA, PMID:11106496) |
| [EV-11-E1](../EV/EV-11.examples.yaml): A cell-cell adhesion NAS row from a speculative discussion (from [EV-11](../EV/EV-11.md)) | Non-conformant | ADGRV1 involved_in GO:0098609 cell-cell adhesion (NAS, PMID:11606593) |

## Sources

- wiki: [ND](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code)
- web: [IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)
- wiki: [HMP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_%28HMP%29)
- web: [OMICS_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html)
- issue: [go-annotation#2521](https://github.com/geneontology/go-annotation/issues/2521)
- wiki: [Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
- issue: [go-annotation#1381](https://github.com/geneontology/go-annotation/issues/1381)
- issue: [go-annotation#5160](https://github.com/geneontology/go-annotation/issues/5160)
- issue: [go-annotation#1626](https://github.com/geneontology/go-annotation/issues/1626)
- web: [NO_DATA](https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html)

<!-- END GENERATED -->
