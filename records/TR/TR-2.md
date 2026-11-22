---
id: TR-2
title: Annotate dbTF activity only when the protein's own sequence-specific DNA binding and its regulation
  of targets are both supported
status: proposed
topic: TR
provenance: GOC
aspects:
- F
- P
evidence_codes:
- IDA
- IMP
go_terms:
- term_id: GO:0003700
  label: DNA-binding transcription factor activity
- term_id: GO:0003714
  label: transcription corepressor activity
- term_id: GO:0000976
  label: transcription cis-regulatory region binding
- term_id: GO:0003713
  label: transcription coactivator activity
sources:
- kind: drive
  title: TF annotation guidelines
  url: https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs
- kind: issue
  title: go-annotation#3231
  url: https://github.com/geneontology/go-annotation/issues/3231
- kind: issue
  title: go-annotation#3125
  url: https://github.com/geneontology/go-annotation/issues/3125
- kind: web
  title: TRANSCRIPTION_FACTORS
  url: https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html
- kind: issue
  title: go-annotation#3168
  url: https://github.com/geneontology/go-annotation/issues/3168
- kind: paper
  title: PMID:23981286
  url: https://europepmc.org/article/MED/23981286
date: '2026-11-15'
---

# TR-2. Annotate dbTF activity only when the protein's own sequence-specific DNA binding and its regulation of targets are both supported

## Decision

Annotate `GO:0003700` or a descendant when (a) the protein itself binds a specific
double-stranded DNA sequence in a cis-regulatory region and (b) that binding regulates
transcription of a limited set of target genes. The strength of evidence needed for (a)
depends on the protein's family:

## Context

| Prior | Evidence needed for DNA binding |
|---|---|
| Member of a well-characterised dbTF family (homeodomain, GATA, bHLH with basic region, bZIP, nuclear receptor) or a 1:1 ortholog of a demonstrated dbTF | ChIP or nuclear-extract EMSA at a known motif may suffice, together with regulation of the target |
| Domain family with mixed members (C2H2 zinc finger, Myb/SANT, ARID, HMG, single zinc finger) | direct binding with purified protein (EMSA, footprinting, SELEX, structure) at a defined motif |
| No family precedent | purified-protein sequence-specific binding plus regulation of transcription through the cognate motif in a cis-regulatory module |

Rationale. The archived guideline sets the two-part requirement and the family-graded
standard, and warns that "the presence of a DNA binding domain in a protein does not
always imply the protein functions as a dbTF"
([Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)).
The term's usage note singles out zinc finger, Myb/SANT and ARID proteins, "since only a
subset of proteins containing these domains directly and selectively bind to regulatory
DNA motifs". A protein with one zinc finger and weak binding evidence is not classed as
a dbTF ([go-annotation#3231](https://github.com/geneontology/go-annotation/issues/3231)).
Each THAP family member needs its own direct evidence
([go-annotation#3125](https://github.com/geneontology/go-annotation/issues/3125)).

## Application

Worked examples. HDAC4 carries IDA/IMP rows to dbTF activator activity; it has no
DNA-binding domain and acts through MEF2, so the rows were `MODIFY` to `GO:0003714`
transcription corepressor activity and its DNA-binding row to `GO:0000976`
(`genes/human/HDAC4`; [TRANSCRIPTION_FACTORS](https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html)). MACC1
had an IDA dbTF activator row from a nuclear-extract EMSA; GOC curators found no
paper showing direct binding and changed it to `GO:0003713` transcription coactivator
activity ([go-annotation#3168](https://github.com/geneontology/go-annotation/issues/3168)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | IDA, IMP |
| GO terms | `GO:0003700` DNA-binding transcription factor activity; `GO:0003714` transcription corepressor activity; `GO:0000976` transcription cis-regulatory region binding; `GO:0003713` transcription coactivator activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [TR-2-E1](TR-2.examples.yaml): An ETS repressor shown to act through its binding site in a reporter | Conformant | ERF enables GO:0001227 DNA-binding transcription repressor activity, RNA polymerase II-specific (IDA, PMID:7588608) |
| [TR-2-E2](TR-2.examples.yaml): A dbTF row from an author calling the protein a transcription factor | Non-conformant | dac enables GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific (TAS, PMID:38528987) |

## Sources

- drive: [TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)
- issue: [go-annotation#3231](https://github.com/geneontology/go-annotation/issues/3231)
- issue: [go-annotation#3125](https://github.com/geneontology/go-annotation/issues/3125)
- web: [TRANSCRIPTION_FACTORS](https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html)
- issue: [go-annotation#3168](https://github.com/geneontology/go-annotation/issues/3168)
- paper: [PMID:23981286](https://europepmc.org/article/MED/23981286)

<!-- END GENERATED -->
