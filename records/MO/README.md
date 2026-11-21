---
id: MO
title: Multi-organism processes and non-coding RNAs
record_kind: guideline
applies_to:
- contributing_group
status: proposed
differences:
- prior_source: '[Drive: Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU)
    (wiki-derived, marked "to be reviewed")'
  prior_said: Use terms under multi-organism process `GO:0051704` and CC other organism `GO:0044215`.
  we_recommend: Use `GO:0044419` descendants and `GO:0018995` host cellular component descendants (MO-1,
    MO-7).
  why: Both old roots are obsolete; `GO:0044419` itself is do-not-annotate, so annotate to its children.
- prior_source: Same
  prior_said: If a symbiont affects a normal host process, request a new term in the multi-organism node
    rather than annotate the normal term with two taxa.
  we_recommend: Unchanged in spirit; the new terms now follow the "symbiont-mediated perturbation/suppression/activation
    of host X" pattern (MO-1, MO-6).
  why: The 2023-2024 relabelling made agency explicit and removed separate "by virus" terms.
- prior_source: '[Drive: Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E)
    (2023)'
  prior_said: The discussion preferred "modulation" to "perturbation".
  we_recommend: Use the labels GO adopted ("symbiont-mediated perturbation of host ...").
  why: The ontology chose "perturbation"; guidelines follow the ontology.
- prior_source: '[wiki: LncRNA GO annotation manual](https://wiki.geneontology.org/index.php/LncRNA_GO_annotation_manual)'
  prior_said: Examples include a malformed identifier ("UniProtKB:Q62504Q8VEK3" for Xist partners) and
    a mouse lncRNA (Mhrt) given a `_9606` RNAcentral suffix.
  we_recommend: Check identifiers and taxon suffixes when copying the manual's examples.
  why: Errors in the source text; reported here so they are not propagated.
open_questions:
- '**Co-opted host factors.** Is there any case where a host gene product should carry a viral-process
  term, for example host thioredoxin acting as the processivity factor of T7 DNA polymerase, where the
  host protein is a physical part of the viral machine? If so, GO needs a term family that keeps these
  out of host-process enrichment (the 2017 thread suggested a separate branch).'
- '**Virus receptors.** `GO:0001618` virus receptor activity is a binding term under exogenous protein
  binding. Should it be retained, replaced by `has input` on the host protein''s normal receptor activity,
  or obsoleted, given that "receptor" here describes the virus''s use of the protein?'
- '**Interacting taxon.** Taxon field or `has input` extension? The 2020 recommendation was never carried
  into the file formats.'
- '**Immune system process.** Is `GO:0002376` immune system process a system process, and should its definition
  exclude unicellular defence?'
- '**`GO:0080185` placement.** Should effector-mediated activation of the plant hypersensitive response
  move out from under suppression of host innate immunity?'
- '**ncRNA reviews in this repository.** The review pipeline is keyed to UniProt. Should ncRNA genes be
  reviewed with RNAcentral identifiers, and how should their GOA rows (many from RNAcentral propagation
  and Rfam2GO) be fetched?'
- '**Phylogenetic propagation for ncRNAs.** miRNA families are deeply conserved, but seed identity does
  not guarantee shared targets. Should Rfam2GO-style propagation carry target-specific BP at all, or only
  MF?'
- '**lncRNA product versus locus.** Should GO provide a way to state that a function belongs to the act
  of transcription at a locus rather than to the RNA (a qualifier, or a process term on the gene)?'
date: '2026-11-15'
---

# Multi-organism processes and non-coding RNAs: GO annotation guidelines


**In brief:**

- Annotate the organism that does the work. A symbiont gene product that acts on its host gets a "symbiont-mediated ... of host ..." term; the host gene product that responds gets a host-side term (defence response, host-mediated suppression, regulation of a viral process). Never the reverse.
- "Host" is the larger organism and "symbiont" the smaller, with no implication of harm; viruses, bacteria and parasites are all symbionts.
- Do not annotate host proteins to viral or symbiont life-cycle processes because a virus uses them. A host protein keeps its normal function; the dependence is recorded on the viral side, or in a GO-CAM.
- A symbiont term needs agency: the symbiont product evolved to do it. Being recognised by host immunity is not a symbiont process, and an antimicrobial effector is not a participant in the signalling that induces it.
- Annotate a non-coding RNA by its mature, identified product (an RNAcentral or MOD identifier), with RNA-specific function terms: base-pairing repressor, miRNA inhibitor, adaptor, scaffold, guide. Never with bare `RNA binding` or `protein binding`.
- miRNA function comes only from adding the miRNA (IDA) or removing it (IMP), never from expression changes. Target-specific MF annotations need binding evidence in the paper being annotated; prediction alone captures nothing.

## Scope


This document covers two areas that need rules beyond the general ones.

**Part A, multi-organism processes:** host-symbiont interactions of every kind
(viral, bacterial, fungal, oomycete, protist and metazoan parasites, mutualists,
venoms and toxins), the "symbiont" and "host" terms under `GO:0044419`
biological process involved in interspecies interaction between organisms,
effector proteins, host cellular component terms, recording the interacting
taxon, and immune and defence process terms on the host side.

**Part B, non-coding RNA genes:** miRNAs, siRNAs, piRNAs, lncRNAs and guide RNAs
(snoRNAs), as annotated objects; the proteins that make and regulate them; and
the evidence pitfalls specific to RNA experiments.

Evidence code choice in general is in [evidence-codes.md](../EV/README.md);
extension syntax is in [annotation-extensions.md](../AE/README.md);
GO-CAM modelling of host-symbiont interactions follows
[gocam-modeling.md](../CAM/README.md). Prokaryotic anti-phage defence is in
scope where it concerns process term choice.

This repository reviews gene products keyed by UniProt accession. ncRNA genes
have no UniProt entry, so Part B applies mainly to the protein side (Dicer,
Argonaute, TDMD ligases, snoRNP proteins) and to future ncRNA reviews; see Open
questions.

## Principles


**GO describes what a gene product evolved to do.** The 2021 multi-organism
working group restated this as its first aim: keep terms for normal gene
functions, and remove terms whose content is a host's reaction or a
pathological outcome. More than 300 terms were obsoleted, `multi-organism
process` (`GO:0051704`) among them, and the branch was rebuilt under
`GO:0044419`, which itself is in the do-not-annotate subset
([Drive: Intro - Host-Pathogen interaction session](https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70)).
A virus subverting host translation is the virus's process. The host ribosome
is still doing host translation.

**The term name says which organism has agency.** The "symbiont-mediated"
labels introduced in 2023-2024 were chosen to settle this: the symbiont acts,
the host is acted on
([Drive: Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E)).
Most errors in this branch are host proteins annotated with symbiont terms. In
2021, 461 of 497 annotations to "modulation by symbiont of entry into host"
were to host proteins, and 557 of the first 600 annotations to viral entry into
host cell were host proteins
([go-annotation#3814](https://github.com/geneontology/go-annotation/issues/3814)).

**An RNA is annotated like a protein: with the activity it performs and the
process that activity serves.** The 2016 miRNA guidelines and the 2024 revision
of ncRNA terms gave RNAs their own MF terms, so the RNA no longer needs to
borrow its target's processes
([PMID:26917558](https://europepmc.org/article/MED/26917558) Guidelines for the functional annotation of microRNAs using the Gene Ontology;
[PMID:39374113](https://europepmc.org/article/MED/39374113) Representation of non-coding RNA-mediated regulation of gene expression using the Gene Ontology).

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [MO-1](MO-1.md) | Annotate each organism's gene products with the terms written from that organism's side. | proposed | [GOC+] |
| [MO-2](MO-2.md) | "Host" means the larger organism and "symbiont" the smaller; neither says anything about harm. | proposed | [GOC] |
| [MO-3](MO-3.md) | Do not annotate a host gene product to a viral or symbiont process because the symbiont uses it. | proposed | [GOC+] |
| [MO-4](MO-4.md) | A symbiont term requires that the symbiont product evolved to cause the effect; being recognised is not a symbiont process. | proposed | [GOC+] |
| [MO-5](MO-5.md) | Give an effector its molecular function, its host target and its host location, not only a process term. | proposed | [GOC+] |
| [MO-6](MO-6.md) | Use a single-organism process term only for a process within the organism that encodes the gene product. | proposed | [GOC] |
| [MO-7](MO-7.md) | Locate symbiont products in host compartments with host CC terms, and virion proteins with virion terms. | proposed | [GOC] |
| [MO-8](MO-8.md) | Record the other organism for interspecies annotations, and only for physiological interactions. | proposed | [GOC+] |
| [MO-9](MO-9.md) | On the host side, annotate participation in defence to the most specific defence or immune term the evidence supports, and keep response-to and susceptibility separate. | proposed | [GOC+] |
| [MO-10](MO-10.md) | An induced effector is not a participant in the signalling pathway that induces it, and an enzyme that makes a second messenger is not a regulator of the virus. | proposed | [GOC+] |
| [MO-11](MO-11.md) | Keep mutualistic programmes separate from defence. | proposed | [GOC+] |
| [MO-12](MO-12.md) | Check taxon fit before accepting an inferred multi-organism or immune annotation. | proposed | [GOC+] |
| [MO-13](MO-13.md) | Annotate the mature, functional RNA, identified by an RNAcentral or MOD identifier. | proposed | [GOC] |
| [MO-14](MO-14.md) | Give an RNA an RNA-specific function term; bare `RNA binding` and `protein binding` are not functions for an ncRNA. | proposed | [GOC+] |
| [MO-15](MO-15.md) | Annotate a miRNA target with BP plus `has input`; add the MF only from the paper that shows binding. | proposed | [GOC] |
| [MO-16](MO-16.md) | For RNA experiments, adding the RNA is IDA, removing or blocking it is IMP, a reporter assay is IDA, and expression change is never evidence of function. | proposed | [GOC] |
| [MO-17](MO-17.md) | Choose the silencing child term from what was measured. | proposed | [GOC] |
| [MO-18](MO-18.md) | Downstream processes of a miRNA are regulation terms and non-core; context extensions need evidence of endogenous expression. | proposed | [GOC+] |
| [MO-19](MO-19.md) | Annotate proteins that change miRNA levels to the step they act on; the core processing machinery carries no specific miRNA or mRNA in extensions. | proposed | [GOC] |
| [MO-20](MO-20.md) | For a lncRNA, establish the mechanism class first, and distinguish the RNA's activity from the act of transcribing the locus. | proposed | [NEW] |
| [MO-21](MO-21.md) | A guide RNA's family supports its guide activity; its target-specific process needs the target. | proposed | [GOC+] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


**Host or symbiont term?**

| Question | Yes | No |
|---|---|---|
| Is the gene product encoded by the smaller partner and acting on the larger? | symbiont-mediated / effector-mediated term, host CC, host target as input | next question |
| Is it the host's own component acting against the symbiont? | defence term, host-mediated suppression, or negative regulation of viral process | next question |
| Is it a host component the symbiont exploits? | normal host function only; dependence recorded on the symbiont side | next question |
| Is the evidence only that the host responds to the symbiont's presence? | host-side response term on host genes; nothing on the symbiont gene | |

**Which miRNA annotation?**

| Assay | Code | BP | MF |
|---|---|---|---|
| mimic, target protein down | IDA | `GO:0035195` + has input | none |
| inhibitor, target protein and mRNA up | IMP | `GO:0035279` + has input | none |
| reporter with UTR, seed mutant abolishes effect | IDA | `GO:0035195` + has input | `GO:1903231` + has input + part of |
| CLIP alone | none | none | none |
| miRNA changes with disease | none (IEP not allowed) | none | none |
| protein changes miRNA level, step unknown | IDA/IMP on the protein | `GO:0010468` child + has input miRNA | none |

## Common errors


| Error | Example | Fix |
|---|---|---|
| Host protein on a symbiont-process term | human proteins on `GO:0046718` symbiont entry into host cell; 59 of 206 annotations to the host programmed cell death symbiont term were host proteins (2021) | remove (electronic) or mark over-annotated (experimental); use the host's normal function |
| Host protein on viral translation or replication | SSB, PCBP2 on `GO:0075522` | as above |
| Keyword mapping to viral process | KW-0945 mapped CENP-A to viral process | mapping removed in 2016; remove remaining rows |
| PAMP-bearing protein on "activation of host immunity" | flagellin, toxin annotated to induction of host defence | no symbiont term; host receptors get the recognition terms |
| Single-organism term on a toxin | botulinum toxin on `GO:0046929` | `GO:0044762` |
| Plain CC for a symbiont protein in a host | effector on `GO:0005737` cytoplasm | `GO:0030430` host cell cytoplasm |
| Effector with process only | PWL2 with locations only | add MF, target, host CC |
| Antimicrobial effector on the inducing pathway | AMP on Toll signalling pathway | defence term for its target class |
| Susceptibility factor on defence response | MLO on defense response | negative regulation of defense response |
| Toll term on human IRAK4 by IBA | lineage-specific pathway term propagated | review the PAINT node; [phylogenetic-propagation.md](../PH/README.md) |
| Precursor miRNA annotated | Rfam2GO on dme-mir-998 stem-loop | annotate the mature 5p/3p record |
| miRNA MF from prediction | GO:1903231 with a TargetScan target only | no annotation; BP with has input only if a functional effect is shown |
| IGI for a reporter assay | miR-133 reporter as IGI | IDA |
| miRNA annotated from expression | IEP to a disease process | do not annotate |
| ncRNA with bare RNA binding | lncRNA `GO:0003723` RNA binding | the mechanism term from MO-14 |
| Core machinery with a miRNA extension | DICER1 `GO:0031054` with has input miR-X | remove the extension |

## Reading list


**GO Consortium Drive**

- [Ontology/Multiorganisms/Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU) (out of date)
- [Ontology/Multiorganisms/Combined multiorg + immune system process call 2021-11-22](https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so)
- [Ontology/Multiorganisms/host_symbiont_annotation](https://drive.google.com/open?id=1NiJfYB4JmClhbsr4G3Xwwr-6Bw4GWXGJ) (draft proposal)
- [Ontology/Multiorganisms/Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E)
- [2021-05 GOC/Intro - Host-Pathogen interaction session](https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70)
- [Ontology/ncRNAs/ncRNA Update](https://drive.google.com/open?id=1kxTQvGwlxlXWYrVcopDCoNrJ3deM2gNfCu7tg0VfDos)

**GO wiki**

- [MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual)
- [LncRNA GO annotation manual](https://wiki.geneontology.org/index.php/LncRNA_GO_annotation_manual)
- [SiRNA GO annotation manual](https://wiki.geneontology.org/index.php/SiRNA_GO_annotation_manual)
- [Inferred from Genetic Interaction (IGI)](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29)
- [Multi-species processes](https://wiki.geneontology.org/index.php/Multi-species_processes)
- [Immunology Revisions](https://wiki.geneontology.org/index.php/Immunology_Revisions)
- [Responses to MGI from Karen](https://wiki.geneontology.org/index.php/Responses_to_MGI_from_Karen)

**GitHub issues**

- [go-annotation#1](https://github.com/geneontology/go-annotation/issues/1) (viral terms on host gene products, 2003)
- [go-annotation#1367](https://github.com/geneontology/go-annotation/issues/1367) (viral process from UniProt keyword on CENP-A)
- [go-annotation#1407](https://github.com/geneontology/go-annotation/issues/1407) (evidence code for siRNA knockdown)
- [go-annotation#1507](https://github.com/geneontology/go-annotation/issues/1507) (human genes on viral processes)
- [go-annotation#1891](https://github.com/geneontology/go-annotation/issues/1891) (symbiont process on human genes)
- [go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979) (cGAS and cyclic nucleotide terms)
- [go-annotation#2720](https://github.com/geneontology/go-annotation/issues/2720) (symbiont programmed cell death term on host genes; taxon constraint)
- [go-annotation#3314](https://github.com/geneontology/go-annotation/issues/3314) (interspecies protein binding from IntAct)
- [go-annotation#3514](https://github.com/geneontology/go-annotation/issues/3514) (interacting species as has input)
- [go-annotation#3814](https://github.com/geneontology/go-annotation/issues/3814) (symbiont-specific terms on host proteins)
- [go-annotation#4195](https://github.com/geneontology/go-annotation/issues/4195) (Rfam2GO on miRNA precursors)
- [go-annotation#4582](https://github.com/geneontology/go-annotation/issues/4582) (neurotransmitter secretion term on a toxin)
- [go-annotation#4954](https://github.com/geneontology/go-annotation/issues/4954) (lncRNA annotation on fragments)

**Papers**

- [PMID:26917558](https://europepmc.org/article/MED/26917558) Guidelines for the functional annotation of microRNAs using the Gene Ontology (RNA, 2016)
- [PMID:39374113](https://europepmc.org/article/MED/39374113) Representation of non-coding RNA-mediated regulation of gene expression using the Gene Ontology (RNA Biology, 2024)
- Cited via the manuals' worked examples, not re-read here: [PMID:29887379](https://europepmc.org/article/MED/29887379) (Cyrano and miR-7), [PMID:19716791](https://europepmc.org/article/MED/19716791) (NEAT1), [PMID:22269326](https://europepmc.org/article/MED/22269326) (TGF-beta1 and miR-29b)

**Repository pages**

- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- [INNATE_IMMUNITY](https://ai4curation.io/ai-gene-review/pages/projects/INNATE_IMMUNITY.html)
- [ADAPTIVE_IMMUNITY](https://ai4curation.io/ai-gene-review/pages/projects/ADAPTIVE_IMMUNITY.html)
- [PLANT_FUNGAL_INTERACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PLANT_FUNGAL_INTERACTIONS.html)
- [PHAGES](https://ai4curation.io/ai-gene-review/pages/projects/PHAGES.html) (phage life-cycle terms; true biological absences of modules)
- [PARASITES](https://ai4curation.io/ai-gene-review/pages/projects/PARASITES.html) and [PARASITE_IMMUNE_MODULATORS](https://ai4curation.io/ai-gene-review/pages/projects/PARASITE_IMMUNE_MODULATORS.html)
- [CAEEL_SURVEILLANCE_IMMUNITY](https://ai4curation.io/ai-gene-review/pages/projects/CAEEL_SURVEILLANCE_IMMUNITY.html)
- [MIRNA_DEGRADATION](https://ai4curation.io/ai-gene-review/pages/projects/MIRNA_DEGRADATION.html)
- [GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)
- GO-CAM `62b4ffe300002385` (Shigella OspC3 and human CASP4), cached under `gocams/`

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU) (wiki-derived, marked "to be reviewed") | Use terms under multi-organism process `GO:0051704` and CC other organism `GO:0044215`. | Use `GO:0044419` descendants and `GO:0018995` host cellular component descendants (MO-1, MO-7). | Both old roots are obsolete; `GO:0044419` itself is do-not-annotate, so annotate to its children. |
| Same | If a symbiont affects a normal host process, request a new term in the multi-organism node rather than annotate the normal term with two taxa. | Unchanged in spirit; the new terms now follow the "symbiont-mediated perturbation/suppression/activation of host X" pattern (MO-1, MO-6). | The 2023-2024 relabelling made agency explicit and removed separate "by virus" terms. |
| [Drive: Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E) (2023) | The discussion preferred "modulation" to "perturbation". | Use the labels GO adopted ("symbiont-mediated perturbation of host ..."). | The ontology chose "perturbation"; guidelines follow the ontology. |
| [wiki: LncRNA GO annotation manual](https://wiki.geneontology.org/index.php/LncRNA_GO_annotation_manual) | Examples include a malformed identifier ("UniProtKB:Q62504Q8VEK3" for Xist partners) and a mouse lncRNA (Mhrt) given a `_9606` RNAcentral suffix. | Check identifiers and taxon suffixes when copying the manual's examples. | Errors in the source text; reported here so they are not propagated. |

## Open questions

1. **Co-opted host factors.** Is there any case where a host gene product should carry a viral-process term, for example host thioredoxin acting as the processivity factor of T7 DNA polymerase, where the host protein is a physical part of the viral machine? If so, GO needs a term family that keeps these out of host-process enrichment (the 2017 thread suggested a separate branch).
2. **Virus receptors.** `GO:0001618` virus receptor activity is a binding term under exogenous protein binding. Should it be retained, replaced by `has input` on the host protein's normal receptor activity, or obsoleted, given that "receptor" here describes the virus's use of the protein?
3. **Interacting taxon.** Taxon field or `has input` extension? The 2020 recommendation was never carried into the file formats.
4. **Immune system process.** Is `GO:0002376` immune system process a system process, and should its definition exclude unicellular defence?
5. **`GO:0080185` placement.** Should effector-mediated activation of the plant hypersensitive response move out from under suppression of host innate immunity?
6. **ncRNA reviews in this repository.** The review pipeline is keyed to UniProt. Should ncRNA genes be reviewed with RNAcentral identifiers, and how should their GOA rows (many from RNAcentral propagation and Rfam2GO) be fetched?
7. **Phylogenetic propagation for ncRNAs.** miRNA families are deeply conserved, but seed identity does not guarantee shared targets. Should Rfam2GO-style propagation carry target-specific BP at all, or only MF?
8. **lncRNA product versus locus.** Should GO provide a way to state that a function belongs to the act of transcription at a locus rather than to the RNA (a qualifier, or a process term on the gene)?

<!-- END GENERATED -->
