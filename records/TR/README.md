---
id: TR
title: Transcription regulation
record_kind: guideline
applies_to:
- contributing_group
status: proposed
aspects:
- F
- P
differences:
- prior_source: '[Drive: TF annotation guidelines (archived 2023)](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)
    vs [wiki: ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments)
    and [go-annotation#3168](https://github.com/geneontology/go-annotation/issues/3168)'
  prior_said: 'Guideline: for well-characterised families "weaker evidence of DNA binding, such as ChIP
    experiments is sufficient". Wiki and issue: ChIP does not show binding'
  we_recommend: ChIP may complete a dbTF annotation for a well-characterised family member, but never
    supports a DNA-binding MF on its own, and never for a protein without a recognised DBD ([TR-2](TR-2.md),
    [TR-3](TR-3.md))
  why: The sources conflict; the reconciliation keeps both the family prior and the ChIP limitation
- prior_source: '[Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)'
  prior_said: dbTFs and coTFs "part of GO:0005667 transcription factor complex"
  we_recommend: '`GO:0005667` (now "transcription regulator complex") or `GO:0090575` only when the complex
    is shown'
  why: A dbTF is not by definition in a stable complex; the label has also changed
open_questions:
- '**Locus by modification.** MeCP2 binds methyl-CpG and recruits corepressors, doing for methylated sites
  what a dbTF does for motifs. One curator argued for a new "methyl-CpG-dependent" regulator term rather
  than methyl-CpG binding plus coTF ([go-annotation#3086](https://github.com/geneontology/go-annotation/issues/3086)).
  Should GO create one?'
- '**Definition of GO:0000976.** Should the definition be widened to match its comment (non-specific regulatory-region
  binding), or should a separate non-specific term be created?'
- '**Direction for coTFs.** Can a corepressor be inferred from deacetylase or H3K27 methyltransferase
  activity, or must direction always be shown at a target?'
- '**HT-SELEX plus domain.** SKI and SKIL were annotated as dbTFs by PAINT because the SKOR DNA-binding
  domain is present and SKOR proteins bind DNA in HT-SELEX, despite evidence that SKI binds DNA only in
  complex ([go-annotation#2985](https://github.com/geneontology/go-annotation/issues/2985)). When is domain-plus-relative
  evidence enough?'
- '**Identifier namespace for target genes.** The question raised when `regulates_transcription_of` was
  retired, whether `has_input` takes gene or gene-product identifiers, is unresolved ([go-annotation#2598](https://github.com/geneontology/go-annotation/issues/2598)).'
- '**Should `GO:0006351` become do-not-annotate?** Proposed in 2017 and still open ([go-annotation#1720](https://github.com/geneontology/go-annotation/issues/1720)).'
- '**Bacterial and plant guidance.** The GOC guidelines were written for eukaryotic Pol II. Should bacterial
  regulators (sigma factors, response regulators, nucleoid proteins such as H-NS) have their own documented
  conventions?'
date: '2026-11-15'
---

# Transcription regulation: GO annotation guidelines


**In brief:**

- Classify each transcription activity as one of four kinds before choosing terms: RNA
  polymerase, general transcription factor (GTF), DNA-binding transcription factor
  (dbTF), or transcription coregulator (coTF). Proteins that act on transcription
  regulators away from chromatin are a fifth, separate kind.
- A dbTF annotation needs two things shown for the protein itself: sequence-specific
  binding to double-stranded DNA that gives a genomic address, and regulation of target
  genes through that binding. A DNA-binding domain alone is not enough, and neither is a
  ChIP peak or a nuclear-extract gel shift.
- A coTF acts at a specific locus through a dbTF (or through a mark a dbTF caused to be
  laid down). Most coTFs do not bind DNA; those that bind DNA without sequence
  specificity stay coTFs.
- Chromatin enzymes, readers and chaperones get their own activity. They get a
  transcription-regulation annotation only when gene-specific recruitment and an effect
  on those genes are shown; a global chromatin defect is not regulation of transcription.
- Use RNA polymerase II-specific terms for eukaryotic protein-coding genes without
  waiting for the paper to say so. Name target genes with `has_input`, one target per
  annotation, direct targets only.

## Scope


This document covers molecular function (MF) and biological process (BP) annotation of
proteins that carry out or regulate DNA-templated transcription: RNA polymerases, GTFs,
dbTFs (including nuclear receptors, bacterial regulators and sigma factors), coTFs,
inhibitors and activators of transcription regulators, and chromatin proteins insofar as
they regulate transcription. It covers the DNA-binding evidence standard, polymerase
specificity, activator versus repressor, cis-regulatory binding terms and target-gene
extensions.

Covered elsewhere: general MF principles and the protein binding policy
([molecular-function.md](../MF/README.md)); evidence codes, including how to
code ChIP and EMSA ([evidence-codes.md](../EV/README.md)); extension syntax
([annotation-extensions.md](../AE/README.md)); signaling pathways ending in a
transcription factor ([regulation-and-signaling.md](../RS/README.md));
complexes such as Mediator and TFIID ([protein-complexes.md](../PC/README.md));
GO-CAM models of transcription ([gocam-modeling.md](../CAM/README.md)); ncRNA and
siRNA-mediated silencing ([multi-organism-and-ncrna.md](../MO/README.md)).

## Principles


**Transcription was refactored around what each class of protein does.** Between 2017
and 2021 the GO transcription working group and the GREEKC consortium replaced the old
terms with three activity classes: GTFs, "the molecular machine that assembles with the
RNA polymerase at the promoter"; dbTFs, which "provide genomic addresses and specify the
cell types and the conditions under which specific genes are expressed"; and coTFs,
which bridge GTFs and dbTFs, specify the dbTF's effect, or modify chromatin, "normally
... independent of high affinity binding to specific DNA sequences"
([Drive: TF annotation guidelines, archived 2023](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs);
[PMID:34461313](https://europepmc.org/article/MED/34461313), Gene Ontology
representation for transcription factor functions, 2021). The 2021 paper is the
canonical reference; the archived Drive guideline adds a four-question checklist,
worked examples and pitfalls, and remains useful.

**Author vocabulary is unreliable.** "Transcription factor" is used for all three
classes, and "coactivator" has been used for a dbTF's dimer partner. Read what the
experiments show, not what the protein is called
([Drive: human TF catalogue talk, 2020](https://drive.google.com/open?id=11wth1xVtY8S5U93KHsiklVWWaa_ORs_CkbRHLV2ewNE)).

**Curate the gene, not the paper.** The guideline asks curators to read the
literature on a gene before deciding between dbTF and coTF, because a single
experiment rarely settles it and earlier papers may be superseded
([Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)).

**Being required for expression is not regulating transcription.** Many proteins
change a gene's mRNA level without acting on its transcription. GO uses regulation of
gene expression for that, and keeps regulation of transcription for evidence that the
protein acts on transcription itself
([Drive: 2017 transcription guidelines](https://drive.google.com/open?id=0B_c5g4FezmhfNENjNk5RbjJwQUk)).

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [TR-1](TR-1.md) | Classify the activity first: polymerase, GTF, dbTF, coTF, or regulator of a regulator | proposed | [GOC] |
| [TR-2](TR-2.md) | Annotate dbTF activity only when the protein's own sequence-specific DNA binding and its regulation of targets are both supported | proposed | [GOC] |
| [TR-3](TR-3.md) | Read each DNA-binding assay for what it shows: location, binding, or direct sequence-specific binding | proposed | [GOC] |
| [TR-4](TR-4.md) | Require a genomic address: non-specific, structure-specific and modification-specific DNA binders are not dbTFs | proposed | [GOC] |
| [TR-5](TR-5.md) | Annotate coTF activity for locus-specific action through a dbTF, and protect proteins with a real DNA-binding domain from it | proposed | [GOC+] |
| [TR-6](TR-6.md) | Separate GTFs from coTFs by where they are recruited, and annotate GTFs to transcription itself | proposed | [GOC] |
| [TR-7](TR-7.md) | Proteins that act on transcription regulators away from chromatin are regulator-of-regulator, not coTFs | proposed | [GOC+] |
| [TR-8](TR-8.md) | Use RNA polymerase II terms for eukaryotic protein-coding genes; name Pol I or III only when shown | proposed | [GOC] |
| [TR-9](TR-9.md) | State activator or repressor when the direction at a target is shown; allow both when context changes it | proposed | [GOC+] |
| [TR-10](TR-10.md) | For dbTF DNA binding use the cis-regulatory sequence-specific terms; put region and motif in extensions | proposed | [GOC+] |
| [TR-11](TR-11.md) | Annotate regulation of transcription only from evidence of a transcriptional effect; use regulation of gene expression for mRNA-level changes | proposed | [GOC] |
| [TR-12](TR-12.md) | Give chromatin enzymes, readers and chaperones their own activity; add transcription regulation only on gene-specific evidence | proposed | [GOC+] |
| [TR-13](TR-13.md) | Treat an enzyme activity plus dbTF activity on one protein as a probable error | proposed | [GOC] |
| [TR-14](TR-14.md) | Name the direct target gene with `has_input`, one target per annotation; a coTF's input is the dbTF | proposed | [GOC+] |
| [TR-15](TR-15.md) | Bacterial and plant regulators follow the same evidence standard with their own terms | proposed | [NEW] |
| [TR-16](TR-16.md) | Review electronic and propagated dbTF rows against the family and the member | proposed | [GOC+] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


### Which class?

```
Does the protein assemble with RNA polymerase at core promoter elements of all/most genes?
  yes -> GTF (TR-6)
Does it bind double-stranded DNA itself, at a motif specific enough to select genes?   (TR-2, TR-3, TR-4)
  yes, and regulates targets through that binding -> dbTF (activator/repressor if shown, TR-9)
  binds DNA, but AT-rich minor groove / methyl-CpG / hairpin / ssDNA / G4 / non-specific -> specific binding term; go on
Is it recruited to specific genes by a dbTF, by a locally deposited mark, or by another coTF, and does it change their transcription?
  yes -> coTF (coactivator/corepressor if shown, TR-5); add its own enzymatic/reader activity (TR-12)
Does it bind a transcription regulator away from chromatin to block or enable it?
  yes -> GO:0140416 / GO:0140537 (TR-7)
Does it alter target mRNA levels with no evidence of acting at the gene?
  yes -> regulation of gene expression at most (TR-11), or the process it really performs
```

### Which evidence supports what?

| Evidence | DNA-binding MF | dbTF MF | CC chromatin | `has_input` target |
|---|---|---|---|---|
| Purified-protein EMSA, footprinting, SELEX, structure at a motif | yes | with regulation | no | with regulation |
| HT-SELEX motif only | yes (`GO:1990837`) | no | no | no |
| Nuclear-extract EMSA or supershift | no | only with a strong family prior | no | supports, for an established dbTF |
| ChIP / ChIP-seq | no | only with a strong family prior and regulation | yes | supports, if also regulated |
| Reporter or enhancer assay with motif mutation | no | yes, with binding | no | yes |
| qPCR / RNA-seq change only | no | no | no | no; BP regulation of gene expression |
| InterPro domain match | only if InterPro maps it | only via a dbTF-family signature | no | no |

### Chromatin protein: which BP?

| What was shown | BP |
|---|---|
| Recruited by a named dbTF to named genes; changes their transcription | regulation of transcription (with coTF MF) |
| Mark-dependent action at promoters of active genes | `GO:0045815` transcription initiation-coupled chromatin remodeling |
| Restores chromatin behind elongating polymerase; loss gives cryptic transcription | `GO:0140673` transcription elongation-coupled chromatin remodeling |
| Maintains silent domains | `GO:0140719` or `GO:0140718` heterochromatin formation |
| Genome-wide expression changes after deletion, mechanism unknown | none from this evidence; at most regulation of gene expression |

## Common errors


**DNA-binding domain read as dbTF.** Zinc finger, Myb/SANT, ARID and HMG proteins given
dbTF activity from domain or IBA alone. Fix: require the family-graded evidence of
[TR-2](TR-2.md); `MODIFY` to coTF or `REMOVE`.

**ChIP read as DNA binding.** IDA rows to `GO:0000978` from ChIP or nuclear-extract
EMSA. Fix: chromatin CC, and DNA binding only from purified-protein assays
([TR-3](TR-3.md)).

**Coactivator in a DNA-bound complex annotated as dbTF.** NOTCH1, RFXANK, RFXAP, MACC1.
Fix: `MODIFY` to `GO:0003713`; remove the DNA-binding row unless the protein contacts DNA
itself ([TR-5](TR-5.md)).

**dbTF annotated as coTF from a protein–protein interaction.** Cdx2 and Pou5f1. Fix:
keep dbTF unless the regulatory effect is shown not to use DNA binding ([TR-5](TR-5.md)).

**GTF subunit annotated as coactivator by propagation.** TFIID subunits. Fix: GTF
activity and transcription BP ([TR-6](TR-6.md)).

**Chromatin enzyme annotated to regulation of transcription from a deletion
phenotype.** Fix: the enzyme's activity and the chromatin process; coTF only with
gene-specific recruitment ([TR-12](TR-12.md)).

**Signaling protein annotated to regulation of transcription.** Receptors, kinases and
ligands whose pathway ends in gene induction. Fix: the pathway BP; regulation of
transcription is for proteins acting at the gene ([TR-11](TR-11.md)).

**Every differentially expressed gene in `has_input`.** Fix: direct targets only
([TR-14](TR-14.md)).

**Grouping terms.** `GO:0140110` transcription regulator activity is do-not-annotate;
bare `GO:0003677` DNA binding beside a specific dbTF or binding term is `TOO_GENERAL`.

## Reading list


**Papers**

- [PMID:34461313](https://europepmc.org/article/MED/34461313) Gene Ontology representation for transcription factor functions (2021; canonical)
- [PMID:23981286](https://europepmc.org/article/MED/23981286) GO annotation of sequence-specific DNA binding transcription factors (2013; partly superseded)
- [PMID:34673265](https://europepmc.org/article/MED/34673265) A GO catalogue of human DNA-binding transcription factors (2021)

**GO Consortium Drive**

- [Transcription Factors Annotation Guidelines (archived, last updated 2023-10-24)](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)
- [MF guidelines for GO-CAM (copy; reviewed 2026-03)](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)
- [Transcription coregulator activity (archived)](https://drive.google.com/open?id=1Wq-_3w6F2L_CGvneQT8n-pv-Ekk_i2_QpUZJeO_kvxI)
- [DNA-binding transcription factor activity annotation guidelines (archived)](https://drive.google.com/open?id=1o06rwrGwx8Fw_fqw3ldsrGlM0ot21Q137yQ95ySpasc)
- [2017 transcription working-group guidelines and decision tree](https://drive.google.com/open?id=0B_c5g4FezmhfNENjNk5RbjJwQUk)
- [UCL expression/transcription decision tree, 2016](https://drive.google.com/open?id=0B_c5g4FezmhfSzV5OERKcHJ1MUk)
- [2020 GO-CAM jamboree: transcription and its regulation](https://drive.google.com/open?id=1_T0d9BJAY7yC0iZ1aQ9l3bNeOHKL4TLx14Eddml-XHs)
- [2020 GOC meeting: human transcription factor catalogue](https://drive.google.com/open?id=11wth1xVtY8S5U93KHsiklVWWaa_ORs_CkbRHLV2ewNE)
- [2025 ontology group report (histone readers and writers)](https://drive.google.com/open?id=18n5uLIg0K2pnJ5e06E4Ssxn8zJ6anDdcOJ-k0Xft2W8)
- [2025 GO-CAM transcription: histone readers](https://drive.google.com/open?id=1L_5jlDwXazGGNZUOsz1r8kWYInYeEagk)
- [Managers' minutes (GO-CAM transcription conventions, 2026)](https://drive.google.com/open?id=1PTb0-s9LE8IhsStqhdc25Hb5prdlxBGWbOr8oLfIWNA)

**GO wiki**

- [Annotation consistency: ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments) (reviewed 2023)
- [Chromatin remodeling manual](https://wiki.geneontology.org/index.php/Chromatin_remodeling_manual) (reviewed 2025)
- [Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)
- [Transcription jamboree](https://wiki.geneontology.org/index.php/Transcription_jamboree) (archived)
- [Proposal to obsolete "promoter binding" and child terms](https://wiki.geneontology.org/index.php/Proposal_to_obsolete_%22promoter_binding%22_and_child_terms)
- [Ontology meeting 2018-09-24](https://wiki.geneontology.org/index.php/Ontology_meeting_2018-09-24)
- [Ontology meeting 2018-10-01](https://wiki.geneontology.org/index.php/Ontology_meeting_2018-10-01)
- [GO-CAM Working Group Call 2018-09-25](https://wiki.geneontology.org/index.php/GO-CAM_Working_Group_Call_2018-09-25)
- [Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)
- [Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)

**go-annotation issues**

- [#943](https://github.com/geneontology/go-annotation/issues/943) ChIP and DNA binding
- [#1507](https://github.com/geneontology/go-annotation/issues/1507) host proteins and viral transcription
- [#1720](https://github.com/geneontology/go-annotation/issues/1720), [#2933](https://github.com/geneontology/go-annotation/issues/2933) use of the transcription term
- [#2046](https://github.com/geneontology/go-annotation/issues/2046) DNA-binding annotation for TFs
- [#2130](https://github.com/geneontology/go-annotation/issues/2130) catalytic activity plus dbTF
- [#2584](https://github.com/geneontology/go-annotation/issues/2584) `occurs_at` deprecation
- [#2598](https://github.com/geneontology/go-annotation/issues/2598) `regulates_transcription_of`
- [#2853](https://github.com/geneontology/go-annotation/issues/2853) GTF usage guidance
- [#2972](https://github.com/geneontology/go-annotation/issues/2972) Cdx2 and Pou5f1
- [#2985](https://github.com/geneontology/go-annotation/issues/2985) SKI and SKIL
- [#3086](https://github.com/geneontology/go-annotation/issues/3086) MeCP2
- [#3110](https://github.com/geneontology/go-annotation/issues/3110) ARID and AT-hook proteins
- [#3125](https://github.com/geneontology/go-annotation/issues/3125) THAP proteins
- [#3135](https://github.com/geneontology/go-annotation/issues/3135) NR0B1 hairpin binding
- [#3168](https://github.com/geneontology/go-annotation/issues/3168) MACC1
- [#3231](https://github.com/geneontology/go-annotation/issues/3231) single zinc finger proteins
- [#3235](https://github.com/geneontology/go-annotation/issues/3235) LYAR
- [#3414](https://github.com/geneontology/go-annotation/issues/3414), [#4040](https://github.com/geneontology/go-annotation/issues/4040) histone chaperones as coregulators
- [#3932](https://github.com/geneontology/go-annotation/issues/3932) direction of regulation
- [#4000](https://github.com/geneontology/go-annotation/issues/4000) Epe1 and coTF criteria
- [#4554](https://github.com/geneontology/go-annotation/issues/4554) Taf11, GTF versus coTF
- [#5743](https://github.com/geneontology/go-annotation/issues/5743) NOTCH1

**Repository pages**

- [TRANSCRIPTION_FACTORS](https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html) and its synthesized guidelines
- [YEAST_EPIGENETICS_HISTONE_INHERITANCE](https://ai4curation.io/ai-gene-review/pages/projects/YEAST_EPIGENETICS_HISTONE_INHERITANCE.html)
- [YEAST_DNA_REPAIR_CHROMATIN](https://ai4curation.io/ai-gene-review/pages/projects/YEAST_DNA_REPAIR_CHROMATIN.html)
- [FUNCTION_REQUIREMENT_RULES](https://ai4curation.io/ai-gene-review/pages/projects/FUNCTION_REQUIREMENT_RULES.html)
- [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)
- [ARATH](https://ai4curation.io/ai-gene-review/pages/projects/ARATH.html), [BACSU](https://ai4curation.io/ai-gene-review/pages/projects/BACSU.html)
- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: TF annotation guidelines (archived 2023)](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs) vs [wiki: ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments) and [go-annotation#3168](https://github.com/geneontology/go-annotation/issues/3168) | Guideline: for well-characterised families "weaker evidence of DNA binding, such as ChIP experiments is sufficient". Wiki and issue: ChIP does not show binding | ChIP may complete a dbTF annotation for a well-characterised family member, but never supports a DNA-binding MF on its own, and never for a protein without a recognised DBD ([TR-2](TR-2.md), [TR-3](TR-3.md)) | The sources conflict; the reconciliation keeps both the family prior and the ChIP limitation |
| [Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs) | dbTFs and coTFs "part of GO:0005667 transcription factor complex" | `GO:0005667` (now "transcription regulator complex") or `GO:0090575` only when the complex is shown | A dbTF is not by definition in a stable complex; the label has also changed |

## Open questions

1. **Locus by modification.** MeCP2 binds methyl-CpG and recruits corepressors, doing for methylated sites what a dbTF does for motifs. One curator argued for a new "methyl-CpG-dependent" regulator term rather than methyl-CpG binding plus coTF ([go-annotation#3086](https://github.com/geneontology/go-annotation/issues/3086)). Should GO create one?
2. **Definition of GO:0000976.** Should the definition be widened to match its comment (non-specific regulatory-region binding), or should a separate non-specific term be created?
3. **Direction for coTFs.** Can a corepressor be inferred from deacetylase or H3K27 methyltransferase activity, or must direction always be shown at a target?
4. **HT-SELEX plus domain.** SKI and SKIL were annotated as dbTFs by PAINT because the SKOR DNA-binding domain is present and SKOR proteins bind DNA in HT-SELEX, despite evidence that SKI binds DNA only in complex ([go-annotation#2985](https://github.com/geneontology/go-annotation/issues/2985)). When is domain-plus-relative evidence enough?
5. **Identifier namespace for target genes.** The question raised when `regulates_transcription_of` was retired, whether `has_input` takes gene or gene-product identifiers, is unresolved ([go-annotation#2598](https://github.com/geneontology/go-annotation/issues/2598)).
6. **Should `GO:0006351` become do-not-annotate?** Proposed in 2017 and still open ([go-annotation#1720](https://github.com/geneontology/go-annotation/issues/1720)).
7. **Bacterial and plant guidance.** The GOC guidelines were written for eukaryotic Pol II. Should bacterial regulators (sigma factors, response regulators, nucleoid proteins such as H-NS) have their own documented conventions?

<!-- END GENERATED -->
