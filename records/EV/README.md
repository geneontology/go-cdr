---
id: EV
title: Evidence codes
record_kind: guideline
applies_to:
- contributing_group
status: proposed
differences:
- prior_source: '[wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29)'
  prior_said: '`GO:0005515` must be IPI with a reciprocal annotation'
  we_recommend: Do not create bare protein-binding rows; MODIFY to a specific term or REMOVE
  why: Repo protein-binding policy; the term carries no functional information
- prior_source: '[wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29)
    before 2026'
  prior_said: Overexpression "considered to be an assay system" is IDA, including for processes
  we_recommend: IDA for activity or location assayed in an expression system; IMP for process inferred
    from the resulting phenotype (EV-2, EV-4)
  why: 'Settled in #6468; ECO:0000282 still projects to IEP, which conflicts'
- prior_source: '[wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29)'
  prior_said: IMP may support function, process or location
  we_recommend: IMP supports MF only with molecular corroboration
  why: Necessity of a gene for an activity is not possession of it (#4697)
- prior_source: '[wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29)'
  prior_said: Stage- or organ-selective expression may support "xxx development"
  we_recommend: Developmental time-courses do not support tissue-development terms unless the product
    is the differentiated output
  why: Metabolic demand tracks maturation without an instructive role ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html))
- prior_source: '[wiki: ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29)'
  prior_said: Donor may have experimental or IC support
  we_recommend: IC on the donor counts only if it rests on an experimental annotation of the donor
  why: Prevents transfers of transfers
- prior_source: '[wiki: TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29);
    [Annotation camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp)'
  prior_said: Remove TAS/NAS/IC rows once a better-evidenced row exists for the same term
  we_recommend: Producers should not create them; reviewers give them the same action as the experimental
    row and REMOVE only wrong claims
  why: Reviews judge claims, not codes; rows sharing a term must be consistent
- prior_source: '[wiki: NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29)'
  prior_said: Any author statement a curator wants to capture
  we_recommend: Assertions only; hedged speculation is not annotatable
  why: '#1381; speculation is not a claim'
- prior_source: '[go-annotation#2045](https://github.com/geneontology/go-annotation/issues/2045) (GOA
    proposal, 2018)'
  prior_said: Delete NDs automatically when EXP, HTP, ISS or IGC rows exist in the aspect
  we_recommend: ND stands unless literature on this gene in this species identifies a function; ISS/IGC/IBA/IEA
    do not count
  why: ND records a literature search; inference is not literature ([NO_DATA](https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html))
- prior_source: '[wiki: IC](https://wiki.geneontology.org/index.php/Inferred_by_Curator_%28IC%29); [go-annotation#1621](https://github.com/geneontology/go-annotation/issues/1621)'
  prior_said: IC from another annotation; IDA for experiment plus sequence (2016)
  we_recommend: Both stand; a reviewer's NEW row synthesised from several lines uses IC with the supporting
    GO id, while a single paper with location plus topology uses IDA
  why: Distinguishes the producer's paper-based row from the reviewer's synthesis
- prior_source: '[wiki: HTP family](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Experiment_%28HTP%29)'
  prior_said: Quality criteria per assay type
  we_recommend: 'Additionally judge by use: location from fraction is sound; function from co-location
    is not; vesicle cargo is non-core'
  why: Same data, different inference, different reliability ([OMICS_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html))
- prior_source: '[wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29)
    / GORULE:0000006'
  prior_said: IEP on CC is a curation error
  we_recommend: Most CC IEP rows are an ECO:0000279 projection artefact; read them as IDA
  why: ECO multiple parentage ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html))
open_questions:
- Should the GOC fix ECO-to-GAF projection by aspect (ECO:0000279 to IDA for CC), or re-parent ECO:0000279
  and ECO:0000282? Either clears about 1,100 GORULE:0000006 violations without curation.
- A DNA-binding ChIP assay has no stable partner identifier. Should the IPI WITH/FROM requirement be dropped
  for ECO classes whose partner is a genomic region (#2576)?
- '"Response to" terms conflate "acts in the response" with "is induced during it." Would a qualifier
  or extension distinguishing them let IEP rows coexist with agency claims ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)
  recommendation 5)?'
- 'There is no way in this repository to propose an evidence-code upgrade (right term, IEA only, but species
  IDA exists): NEW is rejected for a term already in GOA. This matters most for all-electronic species.'
- 'Should HTP rows be excluded from IBD seeding by default, given #1775 allows them as ISS donors?'
date: '2026-11-15'
---

# Evidence codes: GO annotation guidelines


**In brief:**

- Pick the code from what the experiment did to the gene product, not from how convinced you are. A direct assay of the product is IDA; a perturbation of the product is IMP; two perturbations are IGI; an identified partner is IPI; the product's own abundance changing is IEP.
- An evidence code records provenance, not quality. A review judges the claim about the gene. A weak code is never by itself a reason to remove a row.
- IEP supports only biological process terms, and only from the gene's normal expression. Ask whether the product does the work of the process or is merely induced during it.
- Every inferential code (IPI, IGI, ISS family, IC, IEA) needs a WITH/FROM value that a reader can check. IDA, EXP, TAS and ND take none.
- High-throughput (HTP family) evidence meets the same bar as low-throughput evidence. What the dataset was used to claim matters more than the code it carries.
- ND is correct when no literature on this gene product, in this species, identifies a function in that aspect. Inferred rows in the same aspect do not make it stale.

## Scope


This document covers the choice and the review of GO evidence codes for single
(standard) annotations, and the ECO classes that sit behind them. It covers the
experimental codes (EXP, IDA, IPI, IMP, IGI, IEP), their high-throughput twins
(HTP, HDA, HMP, HGI, HEP), the similarity codes (ISS, ISO, ISA, ISM, IGC), author
and curator statements (TAS, NAS, IC), ND, and, briefly, RCA and IEA. The
phylogenetic codes (IBA, IBD, IKR, IRD) are summarised in one rule and treated in
full in [phylogenetic-propagation.md](../PH/README.md); electronic
pipelines are treated in [electronic-annotation.md](../IEA/README.md).

Going from a paper's figures to a term is the subject of
[from-paper-to-annotation.md](../LIT/README.md). This document assumes
the term is chosen and asks which code, which WITH/FROM, and which reference.
Qualifiers (NOT, contributes_to) are in
[qualifiers-and-negation.md](../QN/README.md).

## Principles


**A code names an inference, not an experiment.** The [GO evidence code
guide](https://wiki.geneontology.org/index.php/Guide_to_GO_Evidence_Codes) says
codes "are not necessarily a classification of types of experiments" and must
not be read apart from the term. The same immunoprecipitation supports IDA for a
complex term and IPI for a binding term. The question is always: what step of
reasoning connects this observation to this term for this gene product?

**A code is not a confidence score.** The same guide states that evidence codes
"cannot be used as a measure of the quality of the annotation." This repository
holds the reviewing side of that principle: a review judges claims about the gene,
and rows that share a term reinforce each other
([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md); [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)).

**Inferential codes must be auditable.** An IPI row without the partner, an ISO
row without the donor, or an IC row without the source annotation cannot be
checked, so it cannot be trusted. WITH/FROM is how a reader re-runs the curator's
reasoning.

**GAF codes are a lossy projection of ECO.** Curation tools now record ECO classes.
Each class maps to one GAF code, and a class with two parents in different GAF
branches is forced into one of them. Several systematic errors in GOA come from
that projection, not from curators (rule [EV-15](EV-15.md)).

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [EV-1](EV-1.md) | Use the most specific experimental code; do not use EXP when IDA, IPI, IMP, IGI or IEP applies. | proposed | [GOC] |
| [EV-2](EV-2.md) | Use IDA when the experiment measures the gene product's own activity, location or complex membership directly. | proposed | [GOC] |
| [EV-3](EV-3.md) | Use IPI only with the partner's identifier in WITH/FROM, and only for binding, complex or interaction-dependent terms; never for catalytic activity. | proposed | [NEW] |
| [EV-4](EV-4.md) | Use IMP when the inference rests on comparing alleles, or perturbed and unperturbed states, of one gene. | proposed | [GOC+] |
| [EV-5](EV-5.md) | Use IGI when the inference depends on perturbing two or more genes; put the other gene in WITH/FROM; annotate only the gene whose role the experiment informs. | proposed | [GOC+] |
| [EV-6](EV-6.md) | Use IEP only for biological process terms, only from normal expression, and only when the gene product's job is the response itself. | proposed | [GOC+] |
| [EV-7](EV-7.md) | Classify a paper as high-throughput by how it was done, not by how many genes it names; then hold its annotations to the low-throughput standard. | proposed | [GOC+] |
| [EV-8](EV-8.md) | Use ISS, ISO, ISA or ISM only after a curator has reviewed the inference; name the experimentally supported donor or the model in WITH/FROM. | proposed | [GOC+] |
| [EV-9](EV-9.md) | Treat the phylogenetic codes as a PAINT curator's node judgement; challenge the node placement, not the donor count. | proposed | [GOC+] |
| [EV-10](EV-10.md) | Use TAS only when the cited source is traceable and you cannot annotate from the primary paper; a textbook or "common knowledge" is not traceable. | proposed | [NEW] |
| [EV-11](EV-11.md) | Use NAS only for an author's assertion, not for their speculation. | proposed | [GOC+] |
| [EV-12](EV-12.md) | Use IC only for a one-step inference from another annotation on the same gene product; put the GO id of that annotation in WITH/FROM. | proposed | [GOC+] |
| [EV-13](EV-13.md) | ND says a curator searched the literature for one aspect and found nothing; accept it when that is still true, whatever inferred rows exist. | proposed | [GOC+] |
| [EV-14](EV-14.md) | Use RCA and IEA only for what they define; do not recode reviewed work as IEA or unreviewed predictions as anything else. | proposed | [GOC] |
| [EV-15](EV-15.md) | Read the ECO class, not only the GAF code. | proposed | [NEW] |
| [EV-16](EV-16.md) | Several codes from one paper are several annotations; never let a code stand in for a judgement of the claim. | proposed | [GOC+] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


**Choosing a code from an experiment.**

| What the experiment did | Code | WITH/FROM |
|---|---|---|
| Assayed the purified or expressed product's activity | IDA | none |
| Localised the product (antibody, tag, fractionation) | IDA | none |
| Pulled down a complex via a tagged subunit (CC term) | IDA | none |
| Showed binding to an identified molecule | IPI | partner id |
| Showed binding to an unidentifiable partner (DNA region, lipid, F-actin) | IDA | none |
| Compared mutant or knocked-down with wild type (one gene) | IMP | allele or reagent, if any |
| Rescued a mutant with the same gene | IMP | |
| Compared single and double perturbations; complemented gene A's mutant with gene B | IGI | the other gene |
| Overexpressed to assay activity | IDA | none |
| Overexpressed and read a phenotype | IMP | |
| Measured the gene's own normal expression under a condition (BP only) | IEP | none |
| Any of the above in a screen without target selection | HDA / HMP / HGI / HEP | as for the LTP code |
| Curator-reviewed sequence or orthology inference | ISS / ISO / ISA / ISM | donor or model |
| Statement in a review citing primary work | TAS (prefer the primary paper) | none |
| Uncited author assertion | NAS | none |
| One-step inference from another annotation on the same gene | IC | GO id |
| Searched, found nothing (root term only) | ND | none |

**Reviewing a row by code: the first question to ask.**

| Code | First question |
|---|---|
| IDA | Was the assay of the product's own activity or location, or a phenotype coded as IDA? |
| IPI | Is WITH/FROM the partner the paper reports, and is the term a binding or interaction-dependent term? |
| IMP | Is the readout proximal to the term, or a convergent phenotype? Is the term MF? |
| IGI | Which gene was perturbed, and is that the gene annotated? |
| IEP | Does the product exist for this process, or is it induced by it? |
| HDA/HMP/HEP | How were the data used (location, assay, co-location, differential abundance, primary screen)? |
| ISS/ISO | Is the donor still experimental, an ortholog, and is the term safe to move? |
| TAS/NAS | Does the source say this, about this gene, in this species, as an assertion? |
| IC | Is the WITH/FROM annotation real, on the same gene, and is the step one inference? |
| ND | Is there literature on this gene in this species identifying a function in this aspect? |

## Common errors


| Error | Example | Fix |
|---|---|---|
| Phenotype coded IDA | CREG1 endocytosis and autophagy from overexpression and knockdown phenotypes (#6468) | Recode IMP; judge the process term as a phenotype inference |
| Positive row from a negative result | PNPLA3 LPAAT EXP from a paper reporting no activity | MARK_AS_OVER_ANNOTATED; record a `MISSING_NEGATION` source defect |
| Wrong partner in IPI WITH/FROM | ZBP1 with KRR1 for RIPK1; GRID1 with haemoglobin beta | Source defect on the WITH/FROM; judge the binding claim on the real partner |
| IEP stimulus cloud | rat/Gstt1 four `response to X` terms | Keep the parent stimulus term; mark the rest over-annotated or non-core |
| IEP developmental time-course | rat/Ckmt2 `GO:0007507` heart development | MARK_AS_OVER_ANNOTATED |
| Differential proteome coded HDA for a process | `GO:0001649` osteoblast differentiation from PMID:16210410 (42 rows) | It is HEP at most; usually MARK_AS_OVER_ANNOTATED |
| CC rows coded IEP | SynGO western-blot fractions (ECO:0000279) | Read as IDA; review the location on its merits |
| IC for predictions | CAFA ribosome-assembly IC rows (#1626) | REMOVE |
| NAS from speculation | SDHAF1 Fe-S assembly (#1381) | REMOVE |
| ND removed because an IBA exists | 37 reviews in the [NO_DATA](https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html) inventory | ACCEPT the ND; review the IBA on its own row |
| TAS removed as redundant to an IDA | common in older reviews | Give both rows the same action |
| ISO from a paralog | mouse Ang2 from human ANG | REMOVE with `propagation_review` naming WRONG_ORTHOLOG_OR_PARALOG |

## Reading list


**GO wiki (evidence codes):**
[Guide to GO evidence codes](https://wiki.geneontology.org/index.php/Guide_to_GO_Evidence_Codes) ·
[EXP](https://wiki.geneontology.org/index.php/Inferred_from_Experiment_%28EXP%29) ·
[IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29) ·
[IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) ·
[IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29) ·
[IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29) ·
[IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) ·
[HTP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Experiment_%28HTP%29) ·
[HDA](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Direct_Assay_%28HDA%29) ·
[HMP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_%28HMP%29) ·
[HEP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Expression_Pattern_%28HEP%29) ·
[HGI](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Genetic_Interaction_%28HGI%29) ·
[ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29) ·
[ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29) ·
[ISA](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29) ·
[ISM](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29) ·
[IGC](https://wiki.geneontology.org/index.php/Inferred_from_Genomic_Context_%28IGC%29) ·
[TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29) ·
[NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29) ·
[IC](https://wiki.geneontology.org/index.php/Inferred_by_Curator_%28IC%29) ·
[ND](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code) ·
[RCA](https://wiki.geneontology.org/index.php/Inferred_from_Reviewed_Computational_Analysis_%28RCA%29) ·
[IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)

**GO wiki (other):**
[Tips to produce high quality annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) (reviewed 2025) ·
[Transmembrane proteins](https://wiki.geneontology.org/index.php/Transmembrane_Proteins) (refers to the obsolete integral-to-membrane terms) ·
[Guidelines from annotation camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) (historical, c. 2007-2010)

**go-annotation issues:**
[#11](https://github.com/geneontology/go-annotation/issues/11) antibody cross-reactivity is not ISS ·
[#170](https://github.com/geneontology/go-annotation/issues/170) ND vs TAS/NAS for "unknown" ·
[#1327](https://github.com/geneontology/go-annotation/issues/1327) IGI vs IMP wording ·
[#1381](https://github.com/geneontology/go-annotation/issues/1381) NAS from speculation ·
[#1382](https://github.com/geneontology/go-annotation/issues/1382) HTP proteomics criteria applied ·
[#1390](https://github.com/geneontology/go-annotation/issues/1390) what counts as HTP ·
[#1407](https://github.com/geneontology/go-annotation/issues/1407) siRNA is IMP ·
[#1621](https://github.com/geneontology/go-annotation/issues/1621) IDA for experiment plus sequence ·
[#1626](https://github.com/geneontology/go-annotation/issues/1626) no IC for predictions ·
[#1774](https://github.com/geneontology/go-annotation/issues/1774) large screens need case-by-case review ·
[#1775](https://github.com/geneontology/go-annotation/issues/1775) HTP as a propagation source ·
[#1801](https://github.com/geneontology/go-annotation/issues/1801) RCA review ·
[#1839](https://github.com/geneontology/go-annotation/issues/1839) RNAi screen: IMP for validated, HMP otherwise ·
[#2025](https://github.com/geneontology/go-annotation/issues/2025) IEP and ND conflicts ·
[#2045](https://github.com/geneontology/go-annotation/issues/2045) proposed automatic ND deletion ·
[#2131](https://github.com/geneontology/go-annotation/issues/2131) GORULE:0000007 ·
[#2349](https://github.com/geneontology/go-annotation/issues/2349) comma vs pipe in WITH/FROM ·
[#2576](https://github.com/geneontology/go-annotation/issues/2576) ChIP-qPCR ECO and WITH/FROM ·
[#2771](https://github.com/geneontology/go-annotation/issues/2771) EMSA moved to IPI ·
[#4697](https://github.com/geneontology/go-annotation/issues/4697) MF by IMP; IDA over-use ·
[#6468](https://github.com/geneontology/go-annotation/issues/6468) IDA vs IMP for overexpression (2026)

**Papers:**
[PMID:23842463](https://europepmc.org/article/MED/23842463) GO best practices ·
[PMID:30715275](https://europepmc.org/article/MED/30715275) annotation of high-throughput studies ·
[PMID:21873635](https://europepmc.org/article/MED/21873635) PAINT ·
[PMID:21878620](https://europepmc.org/article/MED/21878620) PNPLA3 enzymology ·
[PMID:19590578](https://europepmc.org/article/MED/19590578) ZBP1 interaction ·
[PMID:21492153](https://europepmc.org/article/MED/21492153) Caco-2 differentiation proteome ·
[PMID:21900231](https://europepmc.org/article/MED/21900231) NAA50 structure and activity

**Repository:**
[CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) ·
[action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md) ·
[goa-evidence](https://github.com/ai4curation/ai-gene-review/blob/main/docs/goa-evidence.md) ·
[source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md) ·
[IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html) ·
[ISO](https://ai4curation.io/ai-gene-review/pages/projects/ISO.html) ·
[IRD_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html) ·
[IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html) ·
[OMICS_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html) ·
[NO_DATA](https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html) ·
[MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html) ·
[ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html) ·
[REACTOME](https://ai4curation.io/ai-gene-review/pages/projects/REACTOME.html)

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) | `GO:0005515` must be IPI with a reciprocal annotation | Do not create bare protein-binding rows; MODIFY to a specific term or REMOVE | Repo protein-binding policy; the term carries no functional information |
| [wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29) before 2026 | Overexpression "considered to be an assay system" is IDA, including for processes | IDA for activity or location assayed in an expression system; IMP for process inferred from the resulting phenotype (EV-2, EV-4) | Settled in #6468; ECO:0000282 still projects to IEP, which conflicts |
| [wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29) | IMP may support function, process or location | IMP supports MF only with molecular corroboration | Necessity of a gene for an activity is not possession of it (#4697) |
| [wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) | Stage- or organ-selective expression may support "xxx development" | Developmental time-courses do not support tissue-development terms unless the product is the differentiated output | Metabolic demand tracks maturation without an instructive role ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)) |
| [wiki: ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29) | Donor may have experimental or IC support | IC on the donor counts only if it rests on an experimental annotation of the donor | Prevents transfers of transfers |
| [wiki: TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29); [Annotation camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) | Remove TAS/NAS/IC rows once a better-evidenced row exists for the same term | Producers should not create them; reviewers give them the same action as the experimental row and REMOVE only wrong claims | Reviews judge claims, not codes; rows sharing a term must be consistent |
| [wiki: NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29) | Any author statement a curator wants to capture | Assertions only; hedged speculation is not annotatable | #1381; speculation is not a claim |
| [go-annotation#2045](https://github.com/geneontology/go-annotation/issues/2045) (GOA proposal, 2018) | Delete NDs automatically when EXP, HTP, ISS or IGC rows exist in the aspect | ND stands unless literature on this gene in this species identifies a function; ISS/IGC/IBA/IEA do not count | ND records a literature search; inference is not literature ([NO_DATA](https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html)) |
| [wiki: IC](https://wiki.geneontology.org/index.php/Inferred_by_Curator_%28IC%29); [go-annotation#1621](https://github.com/geneontology/go-annotation/issues/1621) | IC from another annotation; IDA for experiment plus sequence (2016) | Both stand; a reviewer's NEW row synthesised from several lines uses IC with the supporting GO id, while a single paper with location plus topology uses IDA | Distinguishes the producer's paper-based row from the reviewer's synthesis |
| [wiki: HTP family](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Experiment_%28HTP%29) | Quality criteria per assay type | Additionally judge by use: location from fraction is sound; function from co-location is not; vesicle cargo is non-core | Same data, different inference, different reliability ([OMICS_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html)) |
| [wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) / GORULE:0000006 | IEP on CC is a curation error | Most CC IEP rows are an ECO:0000279 projection artefact; read them as IDA | ECO multiple parentage ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)) |

## Open questions

1. Should the GOC fix ECO-to-GAF projection by aspect (ECO:0000279 to IDA for CC), or re-parent ECO:0000279 and ECO:0000282? Either clears about 1,100 GORULE:0000006 violations without curation.
2. A DNA-binding ChIP assay has no stable partner identifier. Should the IPI WITH/FROM requirement be dropped for ECO classes whose partner is a genomic region (#2576)?
3. "Response to" terms conflate "acts in the response" with "is induced during it." Would a qualifier or extension distinguishing them let IEP rows coexist with agency claims ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html) recommendation 5)?
4. There is no way in this repository to propose an evidence-code upgrade (right term, IEA only, but species IDA exists): NEW is rejected for a term already in GOA. This matters most for all-electronic species.
5. Should HTP rows be excluded from IBD seeding by default, given #1775 allows them as ISS donors?

<!-- END GENERATED -->
