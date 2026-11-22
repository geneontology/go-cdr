---
id: BP-8
title: Give pleiotropic core machinery its core processes, not every process it affects
status: proposed
topic: BP
provenance: GOC
aspects:
- P
evidence_codes:
- IDA
- IMP
go_terms:
- term_id: GO:0006412
  label: translation
- term_id: GO:0000398
  label: mRNA splicing, via spliceosome
sources:
- kind: wiki
  title: Annotating downstream processes
  url: https://wiki.geneontology.org/index.php/Annotating_downstream_processes
- kind: drive
  title: FlyBase pathway curation guide
  url: https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI
- kind: paper
  title: PMID:32875947
  url: https://europepmc.org/article/MED/32875947
- kind: issue
  title: go-annotation#1396
  url: https://github.com/geneontology/go-annotation/issues/1396
date: '2026-11-15'
---

# BP-8. Give pleiotropic core machinery its core processes, not every process it affects

## Decision

**Statement.** Some gene products have a central role whose loss disturbs many processes: RNA polymerase, spliceosome, ribosome, proteasome, general chaperones, general chromatin modifiers, Mediator. Annotate them to the processes their activity is part of. Do not annotate the downstream processes that fail when they are removed. Remove such downstream rows, or demote them in review, once the core activity is known.

## Context

[wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) gives two examples. Yeast RPB2 should be annotated to transcription, not to the many processes transcription feeds. Yeast spliceosome mutants had been annotated to translation because of translation defects, and those rows were removed once their role in mRNA splicing was established, since many ribosomal transcripts are spliced in yeast. FlyBase pathway guidance treats NuRD and Mediator as non-specific and keeps them off pathway terms ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)). The Term Matrix QC system finds such errors by flagging co-annotation to processes that rarely share genes ([PMID:32875947](https://europepmc.org/article/MED/32875947), Term Matrix; [go-annotation#1396](https://github.com/geneontology/go-annotation/issues/1396)).

## Application

**Worked example.** A spliceosomal protein with IMP rows to GO:0006412 translation and IDA rows to GO:0000398 mRNA splicing, via spliceosome: keep splicing as core. For translation, use `REMOVE` if the paper's own data attribute the defect to splicing. Otherwise use `MARK_AS_OVER_ANNOTATED`.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | IDA, IMP |
| GO terms | `GO:0006412` translation; `GO:0000398` mRNA splicing, via spliceosome |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [BP-8-E1](BP-8.examples.yaml): A proteasome subunit's spermatogenesis row demoted to non-core | Conformant | rpn-10 involved_in GO:0007283 spermatogenesis (IGI, PMID:17050737) |
| [BP-8-E2](BP-8.examples.yaml): A ribosome-biogenesis ATPase annotated to positive regulation of translation | Non-conformant | ruvb-1 involved_in GO:0045727 positive regulation of translation (IMP, PMID:18804378) |

## Sources

- wiki: [Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)
- drive: [FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)
- paper: [PMID:32875947](https://europepmc.org/article/MED/32875947)
- issue: [go-annotation#1396](https://github.com/geneontology/go-annotation/issues/1396)

<!-- END GENERATED -->
