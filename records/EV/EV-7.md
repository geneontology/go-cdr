---
id: EV-7
title: Classify a paper as high-throughput by how it was done, not by how many genes it names; then hold
  its annotations to the low-throughput standard.
status: proposed
topic: EV
provenance: GOC_PLUS
provenance_note: '[GOC] for the definitions and criteria; [GOC+] for the use-based review table ([OMICS_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html)).'
evidence_codes:
- EXP
- IDA
- IPI
- IMP
- IGI
- IEP
- HTP
- HDA
- HMP
- HGI
- HEP
go_terms:
- term_id: GO:0070062
  label: extracellular exosome
- term_id: GO:0016020
  label: membrane
- term_id: GO:0045296
  label: cadherin binding
sources:
- kind: issue
  title: go-annotation#1390
  url: https://github.com/geneontology/go-annotation/issues/1390
- kind: issue
  title: go-annotation#1774
  url: https://github.com/geneontology/go-annotation/issues/1774
- kind: wiki
  title: HTP
  url: https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Experiment_%28HTP%29
- kind: paper
  title: PMID:30715275
  url: https://europepmc.org/article/MED/30715275
- kind: wiki
  title: HDA
  url: https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Direct_Assay_%28HDA%29
- kind: issue
  title: go-annotation#1382
  url: https://github.com/geneontology/go-annotation/issues/1382
- kind: web
  title: omics project
  url: https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html
- kind: issue
  title: go-annotation#1839
  url: https://github.com/geneontology/go-annotation/issues/1839
date: '2026-11-15'
---

# EV-7. Classify a paper as high-throughput by how it was done, not by how many genes it names; then hold its annotations to the low-throughput standard.

## Decision

Classify a paper as high-throughput by how it was done, not by how many genes it names; then hold its annotations to the low-throughput standard.

## Context

The HTP family (HTP ECO:0006056; HDA ECO:0007005; HMP ECO:0007001; HGI
ECO:0007003; HEP ECO:0007007) maps one-to-one onto EXP, IDA, IMP, IGI and IEP.
There is no HTP equivalent of IPI; large interaction datasets go to IntAct. A study
is HTP when it applies one workflow to many genes in parallel, without explicit
target selection, produces tabular datasets expected to contain false positives,
and assigns the same property to everything above a threshold. There is no minimum
size, and a large hypothesis-driven screen that dissects one process may warrant
IMP/IGI ([go-annotation#1390](https://github.com/geneontology/go-annotation/issues/1390),
[go-annotation#1774](https://github.com/geneontology/go-annotation/issues/1774)).
Use HDA/HMP/HGI/HEP rather than the parent HTP.

The same rules apply as at low throughput, so most HTP papers should not be
curated ([wiki: HTP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Experiment_%28HTP%29);
[PMID:30715275](https://europepmc.org/article/MED/30715275)). Operational criteria:

- **Proteomics (HDA):** peptide FDR below 1%, at least two unique peptides
  (razor peptides do not count), and a purification, not an enrichment, judged by
  multi-step protocols, contaminant assays or multivariate methods such as LOPIT
  ([wiki: HDA](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Direct_Assay_%28HDA%29);
  [go-annotation#1382](https://github.com/geneontology/go-annotation/issues/1382)).
- **Localisation screens (HDA):** annotate; tagged-protein screens are among the
  most reliable HTP sources (63-89% accepted in the [omics project](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html)).
- **RNAi and mutant screens (HMP/HGI):** never annotate the primary screen. Annotate
  validated hits; hits confirmed by low-throughput work in the same paper get IMP
  as well as HMP ([go-annotation#1839](https://github.com/geneontology/go-annotation/issues/1839)).
- **Expression profiling (HEP):** as for IEP, BP only and rarely.

**Our sharpening: judge the use, not the code.** The [omics project](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html)
shows that what predicts whether an omics row holds up is how the data were used:

| Use of the data | Verdict |
|---|---|
| fraction or tagged localisation → location | usually sound |
| vesicle or body-fluid proteome → `GO:0070062` extracellular exosome | true but almost never informative; keep as non-core unless the protein is a vesicle component |
| membrane-fraction proteome → `GO:0016020` membrane | soluble contaminants plus an uninformative term; prefer a specific membrane or none |
| assay of the activity itself (RNA crosslinking, activity probes) → MF | sound; check abundant-protein carry-over |
| co-location or proximity labelling → MF ("found with X, so binds X") | unreliable: E-cadherin proximity labelling produced `GO:0045296` cadherin binding for 255 genes, 2 of 50 accepted |
| differential abundance → process, coded HDA | wrong code (it is HEP at most) and wrong inference: 0 of 9 accepted |

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the definitions and criteria; [GOC+] for the use-based review table ([OMICS_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html)). |
| Date | 2026-11-15 |
| Evidence codes | EXP, IDA, IPI, IMP, IGI, IEP, HTP, HDA, HMP, HGI, HEP |
| GO terms | `GO:0070062` extracellular exosome; `GO:0016020` membrane; `GO:0045296` cadherin binding |

## Sources

- issue: [go-annotation#1390](https://github.com/geneontology/go-annotation/issues/1390)
- issue: [go-annotation#1774](https://github.com/geneontology/go-annotation/issues/1774)
- wiki: [HTP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Experiment_%28HTP%29)
- paper: [PMID:30715275](https://europepmc.org/article/MED/30715275)
- wiki: [HDA](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Direct_Assay_%28HDA%29)
- issue: [go-annotation#1382](https://github.com/geneontology/go-annotation/issues/1382)
- web: [omics project](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html)
- issue: [go-annotation#1839](https://github.com/geneontology/go-annotation/issues/1839)

<!-- END GENERATED -->
