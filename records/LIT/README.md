---
id: LIT
title: From paper to annotation
record_kind: guideline
applies_to:
- contributing_group
status: proposed
differences:
- prior_source: '[wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)'
  prior_said: Select terms that reflect the core function; avoid maximising terms
  we_recommend: Make sound non-core rows when the evidence supports them and mark them non-core; do not
    create uninformative ones
  why: Non-core is a review judgement recorded on the row; deleting true peripheral facts loses information
- prior_source: '[wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)'
  prior_said: For high-level phenotypes, "strongly encourage" not annotating; elsewhere, `acts_upstream_of_or_within`
    is acceptable when little else is known
  we_recommend: Default to not annotating high-level phenotypes; use `acts_upstream_of_or_within` only
    for the most proximal process the phenotype reports, and only when the gene has no better annotation
  why: The page gives both answers; we pick one
- prior_source: '[wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29)
    (pre-2026)'
  prior_said: Overexpression is IDA when "considered an assay system", without separating MF from BP
  we_recommend: Activity or location in an expression system is IDA; a phenotype from it is IMP and judged
    as a phenotype
  why: 'Resolved in #6468 after MGI used IDA for CREG1 process rows'
- prior_source: 'wiki: IDA'
  prior_said: Overexpressed localisation is acceptable IDA
  we_recommend: Rank localisation evidence; overexpressed protein supports the root organelle at most;
    transit is not residence
  why: ER retention and saturation artefacts ([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html))
- prior_source: '[wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29)'
  prior_said: Inhibitor effects are IMP (baicalein, 12-LOX, proliferation)
  we_recommend: Inhibitor effects are IMP for the target only if the drug is specific; a hub readout gives
    at most a non-core upstream row
  why: The example uses a convergent readout and a promiscuous drug
- prior_source: '[wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29)'
  prior_said: Selective expression at a stage may support "xxx development"
  we_recommend: Not unless the product is the differentiated output
  why: Metabolic demand tracks maturation ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html))
- prior_source: '[Guidelines from annotation camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp)'
  prior_said: Request "X involved in Y" terms for downstream processes
  we_recommend: Annotate X; record Y in GO-CAM, a module or core functions
  why: Current practice decomposes precomposed terms ([INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html))
- prior_source: Annotation camp
  prior_said: For poorly characterised genes, annotate downstream processes and remove them later
  we_recommend: Prefer ND or `acts_upstream_of_or_within` to the most proximal process; do not create
    rows expected to be removed
  why: Downstream rows propagate by IBA and ISO before anyone removes them
- prior_source: GO documentation (none)
  prior_said: No rule for negative controls or reported negatives
  we_recommend: A negative result supports NOT; a positive row from it is a `MISSING_NEGATION` defect
  why: SULT1B1, PNPLA3
- prior_source: GO documentation (none)
  prior_said: No rule on promiscuous activity
  we_recommend: 'Three tiers: non-core, over-annotated, REMOVE even on IDA'
  why: '[ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html);
    #5845'
- prior_source: '[wiki: NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29)'
  prior_said: Annotate an author statement the curator wants to capture
  we_recommend: Discussion-section speculation is not annotatable
  why: '#1381'
- prior_source: GO documentation (none)
  prior_said: No guidance on reviewing others' literature annotations
  we_recommend: Abstract can confirm; refute only from full text; flags are leads
  why: '[CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md); [EVIDENCE_SOURCE_SUFFICIENCY](https://ai4curation.io/ai-gene-review/pages/projects/EVIDENCE_SOURCE_SUFFICIENCY.html)'
- prior_source: '[CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) substrate
    convention vs GO practice'
  prior_said: GO annotates thyroglobulin, fibrinogen and C3 to the processes acting on them
  we_recommend: A substrate gets the process term only if it does part of the work (scaffold, cofactor,
    chemistry)
  why: The exceptions define the line; necessity alone never does
open_questions:
- Should "required for" phenotypes on high-level processes be disallowed outright for genes with no known
  MF, rather than discouraged?
- Is a promiscuity threshold needed in GO documentation, or is a stated judgement (no number) enough?
  The repository has chosen the latter.
- How should a reviewer record a suspected wrong-gene attribution when the full text is unavailable and
  the curator cannot be reached? `SUSPECTED` source defects exist, but nothing routes them to the source.
- Should GOC require a figure or section reference on literature annotations, as this repository does
  with `supporting_text`?
date: '2026-11-15'
---

# From paper to annotation: GO annotation guidelines


**In brief:**

- Annotate what the experiment shows, not what the authors conclude or what the assay is called. A wound-healing assay measures cell motility.
- The readout sets the aspect. A measurement of the product's own activity can support a molecular function; a downstream phenotype supports at most a process, usually as non-core.
- A phenotype shows that a gene is necessary. Participation needs a mechanism: name which gene product performs the step before writing `involved_in`.
- Annotate the gene product and species that were actually assayed, cite the primary paper that contains the data, and check that the identifiers resolve to what you think they do.
- Read the negatives. A paper that reports no activity supports a NOT, and a negative control is not a positive result.
- One row per claim per method, each traceable to a figure or a quoted sentence. Less is more.

## Scope


This document covers the step from a paper's experiments to a set of GO
annotations: which assays support which aspect and how deep a term, overexpression
and heterologous systems, the right reference and the right organism,
phenotype-to-process traps, findings that should not be annotated, and how to
record one annotation per claim. It applies both to making new annotations and to
reviewing existing literature-based ones.

The choice of evidence code is in [evidence-codes.md](../EV/README.md). Detailed
process rules (relations, regulation, causal distance) are in
[biological-process.md](../BP/README.md) and
[regulation-and-signaling.md](../RS/README.md); location rules in
[cellular-component.md](../CC/README.md); NOT and other qualifiers in
[qualifiers-and-negation.md](../QN/README.md); the review workflow in
[reviewing-annotations.md](../REV/README.md).

## Principles


**GO describes the normal role of a gene product.** The
[Tips page](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
(reviewed 2025) and the [phenotype guideline](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
both start here. Experiments perturb, overexpress and relocate proteins; the
curator's job is to infer the unperturbed function from them, and to stop where
the inference stops.

**What a paper shows is narrower than what it claims.** Titles, abstracts and
discussions summarise and speculate. The annotation must rest on a result: a
figure, a table, a sentence in Results. Authors write "required for" and "plays a
role in"; GO's `involved_in` has a defined meaning that those phrases do not carry
([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)).

**The distance from readout to product decides what a result licenses.** The
[ASSAY_TO_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION.html) project mined the papers behind
about 37,000 PMID-backed annotations: across thematically aligned annotations,
molecular readouts supported a molecular-function term 77% of the time (567/738)
and phenotypic hub readouts 8% (90/1,087), most of the latter being the legitimate
case of a reporter assay for a real transcription factor. Evidence codes do not
record this distance, so the curator must.

**A paper is evidence about the gene product it studied.** Papers on paralogs,
orthologs, complexes and pathways are routinely cited for the wrong member. The
[Wrong-Gene Leads](https://ai4curation.io/ai-gene-review/pages/projects/WRONG_GENE_LEADS.html) and
[Miscitation](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html) projects found that most such errors pass
every mechanical check.

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [LIT-1](LIT-1.md) | Annotate the conclusion the experiment supports, not the assay's name or the authors' framing. | proposed | [GOC] |
| [LIT-2](LIT-2.md) | Let the readout's proximity to the gene product set the aspect and the depth of the term. | proposed | [GOC+] |
| [LIT-3](LIT-3.md) | An in vitro activity supports a molecular function only at the depth that was tested; decide whether the protein evolved to perform it. | proposed | [GOC+] |
| [LIT-4](LIT-4.md) | Weigh localisation data by what was localised: endogenous protein in its native cell outranks a tagged, overexpressed construct. | proposed | [GOC+] |
| [LIT-5](LIT-5.md) | In overexpression and heterologous systems, separate the assay from the phenotype, and annotate the gene that was expressed. | proposed | [GOC+] |
| [LIT-6](LIT-6.md) | Annotate the gene product and organism actually assayed; a paper about a paralog, ortholog or partner is not evidence for your gene. | proposed | [GOC+] |
| [LIT-7](LIT-7.md) | Cite the primary paper that contains the evidence, and verify that the identifier resolves to it. | proposed | [GOC+] |
| [LIT-8](LIT-8.md) | A phenotype shows necessity; annotate the most proximal process and use the weakest relation the evidence allows. | proposed | [GOC+] |
| [LIT-9](LIT-9.md) | Read what the paper reports as negative; never annotate a negative control or a failed assay as a positive. | proposed | [GOC+] |
| [LIT-10](LIT-10.md) | Know which findings are not annotatable, and leave them out. | proposed | [GOC+] |
| [LIT-11](LIT-11.md) | Make one annotation per claim per method, each traceable to a result; do not harvest every term a paper touches. | proposed | [GOC+] |
| [LIT-12](LIT-12.md) | Judge a paper against the rest of the literature: contested, superseded and retracted findings need explicit handling. | proposed | [GOC+] |
| [LIT-13](LIT-13.md) | When reviewing someone else's literature annotation, read what they read before overruling it; an abstract can confirm, but only the full text can refute. | proposed | [NEW] |
| [LIT-14](LIT-14.md) | Record provenance so the next reader can check the inference without rereading the paper. | proposed | [GOC+] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


**What an assay can support.**

| Assay | Aspect | Typical code | How deep | Watch for |
|---|---|---|---|---|
| Purified-protein enzyme assay | MF | IDA | the reaction and substrate tested | promiscuity tiers (LIT-3) |
| Active-site point mutant, purified protein | MF | IDA (also IMP) | as above | folding defect |
| Knockout lysate loses activity | MF only with corroboration | IMP | — | necessity, not possession |
| EMSA, ChIP, DNA footprinting | MF (DNA binding) | IDA or IPI by ECO class | sequence-specific binding | ChIP partner has no identifier |
| Reporter assay, sequence-specific TF | MF (TF activity), BP | IDA | Pol II-specific child if shown | coregulators without DNA binding |
| Co-IP, two-hybrid, pull-down | MF (specific binding) | IPI | the partner class | WITH/FROM partner; contaminants |
| Tagged-subunit complex purification | CC (complex) | IDA | the named complex | substoichiometric contaminants |
| Immunofluorescence, endogenous, with marker | CC | IDA | organelle; sub-compartment if resolved | — |
| Overexpressed tagged protein | CC | IDA | organelle at most | ER retention, saturation |
| Fractionation | CC | IDA / HDA | fraction purity decides | MAM contamination; `membrane` |
| Knockout or knockdown phenotype | BP | IMP | most proximal process; `acts_upstream_of_or_within` if MF unknown | high-level phenotypes, pleiotropy |
| Double mutant, suppression, complementation | BP | IGI | as above | which gene is annotated |
| Hub readout (ROS, caspase, viability, ΔΨm) | BP | IMP | the level the readout reports | non-core by default; never MF |
| Induced expression under a stimulus | BP | IEP | parent stimulus term | agency test |
| Genome-wide screen | BP / CC | HMP / HDA | validated hits only | primary screen |

**Is this result annotatable?**

```
Is there a result (figure, table, Results sentence), not speculation?
├─ No  → do not annotate (or NAS only for a clear uncited assertion)
└─ Yes → Was THIS gene product, in THIS species, assayed?
         ├─ No  → annotate the gene that was assayed; yours gets ISO/ISS later
         └─ Yes → Is the readout the product's own activity/location?
                  ├─ Yes → MF/CC at the depth tested (LIT-2, LIT-3, LIT-4)
                  └─ No (phenotype) → Is the product's MF part of the process?
                           ├─ Yes → involved_in the most proximal process
                           ├─ Unknown → acts_upstream_of_or_within, or nothing
                           └─ It is a substrate/regulator elsewhere → not this term
```

## Common errors


| Error | Example | Fix |
|---|---|---|
| Assay name used as term | wound-healing assay → `GO:0042060` wound healing | `GO:0048870` cell motility, or nothing |
| Hub readout drives a core process | VEGFA anti-apoptosis from survival signalling | KEEP_AS_NON_CORE |
| Reporter drives coactivator MF for a non-DNA-binding protein | AIP → transcription coactivator activity | MARK_AS_OVER_ANNOTATED |
| Weak in vitro activity accepted as function | ECOLI/yciO TC-AMP synthase | REMOVE (promiscuous noise tier) |
| Overexpressed construct read as residence | CABP2 Golgi, CERKL ER | stay at the root or MARK_AS_OVER_ANNOTATED |
| Paralog's paper on the gene | CSGALNACT1 from a CHSY1 paper | `WRONG_GENE_PRODUCT` source defect |
| Name collision | TFAP2A IPI from a clathrin AP-2 paper | MISCITED; REMOVE the row |
| Wrong PMID | NLRP3 PMID:1189953 | `WRONG_IDENTIFIER` with a verified replacement if found |
| Negative control annotated positive | SULT1B1 ethanol catabolism | MARK_AS_OVER_ANNOTATED (abstract-only) or REMOVE |
| Negative result annotated positive | PNPLA3 LPAAT | `MISSING_NEGATION` source defect |
| Pleiotropic phenotype read as process | spliceosome mutants → translation | REMOVE once mechanism is known |
| Substrate given the processing term | angiotensinogen → angiotensin maturation (proposed NEW) | do not add |
| Meeting report as experimental evidence | PEX39 UniProt FUNCTION | cite the primary paper |
| Experimental row removed from an abstract | any abstract-only paralog-titled paper | UNDECIDED |

## Reading list


**GO wiki:**
[Tips to produce high quality annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) (reviewed 2025-11) ·
[Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) (reviewed 2018) ·
[Guidelines from annotation camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) (historical, partly superseded) ·
[IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29) ·
[IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29) ·
[IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) ·
[TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29) ·
[NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29) ·
[ND](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code) ·
[HMP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_%28HMP%29)

**Drive:**
[Case studies: annotating from mutant phenotypes](https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0) (draft discussion document)

**go-annotation issues:**
[#11](https://github.com/geneontology/go-annotation/issues/11) ·
[#1005](https://github.com/geneontology/go-annotation/issues/1005) "activated during" is not "involved in" ·
[#1381](https://github.com/geneontology/go-annotation/issues/1381) NAS from speculation ·
[#1626](https://github.com/geneontology/go-annotation/issues/1626) predictions are not IC ·
[#2521](https://github.com/geneontology/go-annotation/issues/2521) oligomerisation out of scope ·
[#5160](https://github.com/geneontology/go-annotation/issues/5160) readouts are not roles ·
[#5845](https://github.com/geneontology/go-annotation/issues/5845) secondary activity from overexpression ·
[#6468](https://github.com/geneontology/go-annotation/issues/6468) IDA vs IMP for overexpression

**Papers:**
[PMID:27812934](https://europepmc.org/article/MED/27812934) best practices in manual annotation ·
[PMID:18460184](https://europepmc.org/article/MED/18460184) what GO annotations mean ·
[PMID:16500043](https://europepmc.org/article/MED/16500043) DNase II glycosylation (Tips example) ·
[PMID:26666268](https://europepmc.org/article/MED/26666268) CHCHD10 (phenotype example) ·
[PMID:23207770](https://europepmc.org/article/MED/23207770) ethanol sulfation by SULTs ·
[PMID:21878620](https://europepmc.org/article/MED/21878620) PNPLA3 enzymology ·
[PMID:11514575](https://europepmc.org/article/MED/11514575) chondroitin synthase cloning ·
[PMID:37160800](https://europepmc.org/article/MED/37160800) peroxisome meeting report ·
[PMID:31206516](https://europepmc.org/article/MED/31206516) Epe1 dosage and JmjC

**Repository:**
[CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) ·
[ASSAY_TO_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION.html) and its [rubric](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION/RUBRIC.html) and [edits](https://ai4curation.io/ai-gene-review/pages/projects/ASSAY_TO_FUNCTION/EDITS.html) ·
[FUNCTION_REQUIREMENT_RULES](https://ai4curation.io/ai-gene-review/pages/projects/FUNCTION_REQUIREMENT_RULES.html) ·
[MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html) ·
[WRONG_GENE_LEADS](https://ai4curation.io/ai-gene-review/pages/projects/WRONG_GENE_LEADS.html) ·
[RETRACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/RETRACTIONS.html) ·
[CONTESTED_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/CONTESTED_FUNCTION.html) ·
[ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html) ·
[ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html) ·
[IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html) ·
[OMICS_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html) ·
[NO_DATA](https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html) ·
[EVIDENCE_SOURCE_SUFFICIENCY](https://ai4curation.io/ai-gene-review/pages/projects/EVIDENCE_SOURCE_SUFFICIENCY.html) ·
[INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html) ·
[reference curation](https://github.com/ai4curation/ai-gene-review/blob/main/docs/reference_curation.md) ·
[source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md) ·
[ISOFORMS](https://ai4curation.io/ai-gene-review/pages/projects/ISOFORMS.html)

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) | Select terms that reflect the core function; avoid maximising terms | Make sound non-core rows when the evidence supports them and mark them non-core; do not create uninformative ones | Non-core is a review judgement recorded on the row; deleting true peripheral facts loses information |
| [wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) | For high-level phenotypes, "strongly encourage" not annotating; elsewhere, `acts_upstream_of_or_within` is acceptable when little else is known | Default to not annotating high-level phenotypes; use `acts_upstream_of_or_within` only for the most proximal process the phenotype reports, and only when the gene has no better annotation | The page gives both answers; we pick one |
| [wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29) (pre-2026) | Overexpression is IDA when "considered an assay system", without separating MF from BP | Activity or location in an expression system is IDA; a phenotype from it is IMP and judged as a phenotype | Resolved in #6468 after MGI used IDA for CREG1 process rows |
| wiki: IDA | Overexpressed localisation is acceptable IDA | Rank localisation evidence; overexpressed protein supports the root organelle at most; transit is not residence | ER retention and saturation artefacts ([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)) |
| [wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29) | Inhibitor effects are IMP (baicalein, 12-LOX, proliferation) | Inhibitor effects are IMP for the target only if the drug is specific; a hub readout gives at most a non-core upstream row | The example uses a convergent readout and a promiscuous drug |
| [wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) | Selective expression at a stage may support "xxx development" | Not unless the product is the differentiated output | Metabolic demand tracks maturation ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)) |
| [Guidelines from annotation camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) | Request "X involved in Y" terms for downstream processes | Annotate X; record Y in GO-CAM, a module or core functions | Current practice decomposes precomposed terms ([INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)) |
| Annotation camp | For poorly characterised genes, annotate downstream processes and remove them later | Prefer ND or `acts_upstream_of_or_within` to the most proximal process; do not create rows expected to be removed | Downstream rows propagate by IBA and ISO before anyone removes them |
| GO documentation (none) | No rule for negative controls or reported negatives | A negative result supports NOT; a positive row from it is a `MISSING_NEGATION` defect | SULT1B1, PNPLA3 |
| GO documentation (none) | No rule on promiscuous activity | Three tiers: non-core, over-annotated, REMOVE even on IDA | [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html); #5845 |
| [wiki: NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29) | Annotate an author statement the curator wants to capture | Discussion-section speculation is not annotatable | #1381 |
| GO documentation (none) | No guidance on reviewing others' literature annotations | Abstract can confirm; refute only from full text; flags are leads | [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md); [EVIDENCE_SOURCE_SUFFICIENCY](https://ai4curation.io/ai-gene-review/pages/projects/EVIDENCE_SOURCE_SUFFICIENCY.html) |
| [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) substrate convention vs GO practice | GO annotates thyroglobulin, fibrinogen and C3 to the processes acting on them | A substrate gets the process term only if it does part of the work (scaffold, cofactor, chemistry) | The exceptions define the line; necessity alone never does |

## Open questions

1. Should "required for" phenotypes on high-level processes be disallowed outright for genes with no known MF, rather than discouraged?
2. Is a promiscuity threshold needed in GO documentation, or is a stated judgement (no number) enough? The repository has chosen the latter.
3. How should a reviewer record a suspected wrong-gene attribution when the full text is unavailable and the curator cannot be reached? `SUSPECTED` source defects exist, but nothing routes them to the source.
4. Should GOC require a figure or section reference on literature annotations, as this repository does with `supporting_text`?

<!-- END GENERATED -->
