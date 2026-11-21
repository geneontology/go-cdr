---
id: RS
title: Regulation and signalling
record_kind: guideline
applies_to:
- contributing_group
status: proposed
aspects:
- P
differences:
- prior_source: '[wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation),
    Guideline 2'
  prior_said: If unsure, annotate the parent process with `acts upstream of or within`.
  we_recommend: Same, but always with the positive- or negative-effect child (RS-1, RS-5).
  why: The relation table and wiki now ask for the signed child. A perturbation almost always gives the
    direction.
- prior_source: '[wiki: Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual)'
  prior_said: Extracellular ligands of PI3K signalling are annotated to "positive regulation of phosphatidylinositol
    3-kinase signaling". Ligands use "receptor agonist activity".
  we_recommend: GO:0014068 and GO:0014065 are obsolete. Ligands get receptor ligand activity and the receptor
    pathway term; "positive regulation of" the cassette only when the cassette is annotated without pathway
    context (RS-7, RS-8).
  why: The page dates from 2018 and cites obsolete terms. "Receptor agonist activity" was renamed receptor
    ligand activity in 2017 ([LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html)).
- prior_source: PomBase convention, reported in [LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html)
  prior_said: Pheromones, receptors and Gα annotated to "positive regulation of pheromone response MAPK
    cascade"; only the kinases are `involved_in` the cascade.
  we_recommend: Ligand, receptor and Gα `involved_in` the receptor pathway term where one exists (RS-6,
    RS-8).
  why: One convention across GO. PomBase's choice follows from the obsolescence of the old pathway term,
    so the fix may be ontological (a pathway term to annotate to). Raise it with PomBase rather than overriding
    locally.
- prior_source: '[Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)
    (FlyBase-only)'
  prior_said: Regulation does not traverse transcription; general regulators stay off pathways; regulation
    terms must be signed.
  we_recommend: Adopt for all groups (RS-5, RS-10).
  why: The rules work well in FlyBase's exhaustive pathway curation and match the GOC wiki's intent.
- prior_source: '[wiki: Response to and signaling](https://wiki.geneontology.org/index.php/Response_to_and_signaling);
    [LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html)'
  prior_said: Pathway terms are part of "cellular response to X", so ligands inherit response annotations.
    Whether ligands should carry the response term is unresolved (go-ontology#15477).
  we_recommend: Do not annotate ligands directly to "cellular response to [ligand]". Let inference supply
    it through the pathway term.
  why: Annotating the ligand as responding to itself reads badly in a GAF. Inference already gives users
    the link.
open_questions:
- '**Scaffolds and adaptors: part of, or regulation of?** [go-annotation#1592](https://github.com/geneontology/go-annotation/issues/1592)
  records dissent, and the 2022 PomBase questions (WASP and Arp2/3, securin and separase) show the same
  ambiguity outside signalling ([Drive: 2022 questions about regulation](https://drive.google.com/open?id=1J_WpQPSyn4wvsMtxEAG4d7xA4SLmA0m2)).
  Is a substrate inhibitor (securin) part of sister chromatid separation, or a negative regulator of it?'
- '**Upstream dependencies.** Should any "acts upstream of" annotations be made for constitutive metabolic
  prerequisites, such as folate for nucleotide synthesis? If so, where does the chain stop ([go-annotation#2431](https://github.com/geneontology/go-annotation/issues/2431))?'
- '**Antagonist ligands.** Receptor ligand activity is now classed as an activating activity, but Hedgehog
  binding inhibits Patched. Should GO have agonist and antagonist ligand terms (go-ontology#14275, open
  since 2017; [LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html))?'
- '**Pathway end for non-transcriptional outputs.** Where does a pathway end when its output is cytoskeletal
  or metabolic? The 2022 breakout noted that terms "ultimately effecting a change in the functioning of
  the cell" leave this unclear ([Drive: Breakout – Annotating to a process or its regulation, 2022](https://drive.google.com/open?id=1ii8kFkraHYYSGThmYZq9i6EyqNmY4v91hpGuuvIMunk)).'
- '**"Response to" qualifier.** Should GO distinguish "acts in the response" from "is induced during the
  response", by an extension or a qualifier, so that IEP rows stop competing with mechanistic ones ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html),
  recommendation 5)?'
- '**PomBase pheromone convention.** Should GO restore a pheromone signalling pathway term so that ligands
  and receptors can be `involved_in` it?'
- '**Tissue-development regulation.** The 2022 breakout asked where the boundary lies between a process
  and its regulation for tissue development, which needs signalling, trafficking and cell-cycle control.
  The BP refactoring draft suggests regulation exists only at the level of pathways and cells ([Drive:
  BP refactoring 2022](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg)).
  Should "regulation of [organ] development" terms be retired?'
date: '2026-11-15'
---

# Regulation and signalling: GO annotation guidelines


**In brief:**

- "Regulation of X" means the gene product's activity sits outside X and changes whether, how often, how fast or how much X happens. If you cannot name the X participant (or the step) that it acts on, the claim is an upstream effect. Annotate it under [BP-4](../BP/BP-4.md).
- Pathway members that activate the next step are part of the pathway, not its regulators. Limiting quantities, constitutive prerequisites and substrate supply are not regulation.
- Sign is judged in vivo, from the gene product's effect rather than the mutant's phenotype. A wrong sign is a contradiction to correct, not an imprecision to tolerate.
- A signalling pathway runs from ligand–receptor engagement to the last effector, often a transcription factor. The ligand, the receptor, the transducers and that effector are in it. Target genes and the downstream cellular process are not.
- Regulation does not cross transcription. A component of pathway A that changes transcription of pathway B's genes is not a regulator of pathway B.
- "Response to X" is for gene products that detect X, transduce it, or carry out a response specific to it. A change in expression after X is IEP evidence of a peripheral role at most, and usually non-core.

## Scope


This document covers:

- regulation terms ("regulation of", "positive regulation of", "negative regulation of" a process), including their sign and directness;
- the boundary between being part of a process and regulating it;
- signalling pathway annotation: ligands, receptors, transducers, intracellular cassettes, second messengers and pathway ends;
- "response to" terms, cellular versus organism-level responses, and IEP-based annotation.

Related documents:

- The general participation test (`involved_in` versus `acts upstream of`) is in [biological-process.md](../BP/README.md).
- Transcription regulation, DNA-binding transcription factor activity and target genes are in [transcription-regulation.md](../TR/README.md).
- The MF side of regulators (enzyme regulator, molecular adaptor, receptor ligand activity) is in [molecular-function.md](../MF/README.md).
- GO-CAM causal relations (`directly positively regulates`, `constitutively upstream of`, `removes input for`) are in [gocam-modeling.md](../CAM/README.md).
- Evidence codes, including IEP, are in [evidence-codes.md](../EV/README.md).

## Principles


**Regulation is a relation between activities, read at the process level.** GO defines process P1 as regulating P2 if P1 starts or stops P2, changes the frequency of its starting or stopping, or changes the rate or extent of its output ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). For a gene product, "involved in regulation of P2" therefore means: the gene product's activity acts on an activity that is part of P2. The phenotype guideline states the evidential bar. There "should be evidence that the MF of the gene product being annotated *regulates* an MF of a gene that is *involved in* the process" (same page).

**Every process has a start, a middle and an end.** Whether a gene product is in a process or regulating it depends on where the process boundaries are drawn. Signalling pathways have the clearest boundaries, and organism-level processes the vaguest ([wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation)). When the boundaries are vague, the safe annotation is the process itself with an upstream relation, not a regulation term.

**Regulation is conditional and specific.** A regulator changes an activity in response to something, and it targets particular activities. A housekeeping requirement does neither ([Drive: MF-MF relations abstract, ISB 2023](https://drive.google.com/open?id=1r-tnt3Jk7H4Sb3xzIbx7ODVGCUbbyh9uyxPN1JhUK-M); [Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)).

**Abundance change is not activity.** A transcript that rises after a stimulus says the gene is regulated by the response. It does not say the gene product takes part in it ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)).

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [RS-1](RS-1.md) | Decide between "part of X" and "regulation of X" by locating the gene product's activity relative to the process boundaries | proposed | [GOC] |
| [RS-2](RS-2.md) | Annotate regulation of X only when the gene product modulates X, and name the target | proposed | [GOC+] |
| [RS-3](RS-3.md) | Limiting quantities, constitutive prerequisites and substrate supply are not regulation | proposed | [GOC+] |
| [RS-4](RS-4.md) | Pathway members that activate the next member are part of the pathway, not regulators of it; feedback is the exception | proposed | [GOC] |
| [RS-5](RS-5.md) | Judge sign in vivo, from the gene product's effect, and correct a wrong sign rather than tolerating it | proposed | [NEW] |
| [RS-6](RS-6.md) | A signalling pathway runs from ligand–receptor engagement to the last effector; annotate its members, not its targets | proposed | [GOC] |
| [RS-7](RS-7.md) | Intracellular signalling cassettes are part of pathways; cassette members may carry both terms | proposed | [GOC+] |
| [RS-8](RS-8.md) | Protein ligands are part of the pathway they start; annotate them with receptor ligand activity, not receptor-specific binding terms | proposed | [GOC+] |
| [RS-9](RS-9.md) | Receptors, G proteins and second-messenger enzymes: annotate the specific pathway the evidence shows, with the right coupling and sign | proposed | [GOC+] |
| [RS-10](RS-10.md) | Regulation does not cross transcription, and general machinery is not a pathway regulator | proposed | [GOC+] |
| [RS-11](RS-11.md) | Use "response to X" for gene products that detect X, transduce it, or carry out a response specific to X | proposed | [GOC+] |
| [RS-12](RS-12.md) | IEP supports "response to" and other BP terms only for normal expression, and usually only as a non-core role | proposed | [GOC+] |
| [RS-13](RS-13.md) | Do not use MF regulator terms when the regulatory activity is unknown, and do not give a regulator the activity it regulates | proposed | [GOC] |
| [RS-14](RS-14.md) | Annotate regulation at the level where it acts, not at every enclosing process | proposed | [GOC+] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


For a gene product G and a process X that a paper says G "regulates":

| # | Question | If yes | If no |
|---|---|---|---|
| 1 | Does G perform an activity between X's start and end? | `involved_in` X (RS-1); add regulation only for feedback (RS-4) | go on |
| 2 | Is G a substrate supplier, a limiting component, a constitutive prerequisite, or the cause of damage that X detects? | Not regulation (RS-3); annotate G's own process | go on |
| 3 | Is there evidence that G changes the activity, amount or location of a named X participant, or X's timing? | `involved_in` (positive/negative) regulation of X, with the target as `has_input` (RS-2) | go on |
| 4 | Does G act through transcription of X's components while belonging to another pathway? | G's own pathway; no regulation of X (RS-10) | go on |
| 5 | Is the effect real, directional and mechanism-unknown? | `acts upstream of or within, positive/negative effect` X ([BP-4](../BP/BP-4.md)) | no annotation |

Then check the sign against the gene product's in vivo effect (RS-5).

For signalling-pathway membership:

| Entity | Pathway term | Regulation of pathway | Neither |
|---|---|---|---|
| Protein ligand, receptor, co-receptor, adaptor, transducer, second-messenger synthase, last effector (TF, S6K) | yes | feedback only | |
| Inhibitory receptor (Patched), second-messenger degrader (PDE), extracellular antagonist, pathway-specific E3 ligase targeting a component | | yes (signed) | |
| Ligand biogenesis/secretion factor | | | own process term |
| Target genes, downstream-process machinery, general chromatin/Mediator/ESCRT | | | yes |

## Common errors


- **Phenotype read as regulation.** "Knockdown reduced X" becomes "positive regulation of X". Fix: RS-2 and BP-4.
- **Sign inverted from the phenotype.** A knockout raises X, so the gene "positively regulates X". Fix: RS-5; record a sign correction as MODIFY.
- **Pathway member as its own pathway's regulator.** A kinase annotated to positive regulation of the cascade it is a tier of. Fix: RS-4.
- **Target gene in the pathway.** A gene induced by the pathway annotated to the pathway. Fix: RS-6.
- **Transcription traversed.** A signalling component annotated to regulation of a second pathway, or of a developmental process, through transcription. Fix: RS-10.
- **Ligand on a receptor-binding term only.** Fix: RS-8.
- **Second-messenger enzyme as a regulator of the outcome.** cGAS as "regulation of viral life cycle". Fix: RS-2 and RS-9; put the enzyme in the pathway.
- **Stimulus cloud.** Many "response to X" IEP rows on one enzyme. Fix: RS-12.
- **Hub inversion.** A master transcription factor annotated as responding to every stimulus whose programme it drives. Fix: RS-11, RS-12.
- **High-level response or regulation terms.** GO:0050896, GO:0042221, GO:0050794 regulation of cellular process, GO:0048583 regulation of response to stimulus and similar grouping terms are do-not-annotate. Fix: specific term or none.
- **Family-level sign leakage.** Gs/Gi coupling terms crossing the split by IBA or ISS. Fix: RS-5, RS-9; see [phylogenetic-propagation.md](../PH/README.md).

## Reading list


**GO wiki**

- [Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation) (flagged "to be reviewed"; updated 2021)
- [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
- [Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)
- [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- [Constitutively upstream of](https://wiki.geneontology.org/index.php/Constitutively_upstream_of)
- [Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual) (under construction, 2018)
- [2017 Cambridge GOC Signalling Workshop](https://wiki.geneontology.org/index.php/2017_Cambridge_GOC_Signalling_Workshop)
- [Response to x annotation guidelines](https://wiki.geneontology.org/index.php/Response_to_x_annotation_guidelines) (deprecated)
- [Response to and signaling](https://wiki.geneontology.org/index.php/Response_to_and_signaling)
- [Detection and Response to stimulus](https://wiki.geneontology.org/index.php/Detection_and_Response_to_stimulus)
- [Guidelines from Annotation Camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) (historical)
- [Guidelines for checkpoints](https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints)
- [Inferred from Expression Pattern (IEP)](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29)
- [Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)

**GO Consortium Drive**

- [Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4) (draft)
- [FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI) (draft for discussion)
- [Breakout – Annotating to a process or its regulation, 2022 (slides)](https://drive.google.com/open?id=1ii8kFkraHYYSGThmYZq9i6EyqNmY4v91hpGuuvIMunk)
- [Breakout use cases – Annotating to a process or its regulation, 2022](https://drive.google.com/open?id=1nSVZ-LoPOnnWf_2e9ZOLAxbBjnTT9QKVq_Vb0448yGw)
- [2022 questions about regulation (PomBase)](https://drive.google.com/open?id=1J_WpQPSyn4wvsMtxEAG4d7xA4SLmA0m2)
- [GO-CAM Jamboree 2020 – Regulation notes](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)
- [MF-MF relations abstract, ISB 2023](https://drive.google.com/open?id=1r-tnt3Jk7H4Sb3xzIbx7ODVGCUbbyh9uyxPN1JhUK-M)
- [Ontology development update, SAB 2019](https://drive.google.com/open?id=1csX9z0szrud0-XIUitPR2pesr8ry-0xcTQNkCv5fsHo)
- [Signaling receptor activity (archived)](https://drive.google.com/open?id=1dZKucnM45V05MYJUkpuf3Epje6mZRxRv3-62Y5JwAHw)
- [PAINT signaling annotation – meeting minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM)
- [Kimberly & Pascale – minutes](https://drive.google.com/open?id=1PTb0-s9LE8IhsStqhdc25Hb5prdlxBGWbOr8oLfIWNA)
- [BP refactoring 2022 – developmental process](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg) (draft)

**go-annotation issues**

[#1166](https://github.com/geneontology/go-annotation/issues/1166), [#1592](https://github.com/geneontology/go-annotation/issues/1592), [#1687](https://github.com/geneontology/go-annotation/issues/1687), [#1691](https://github.com/geneontology/go-annotation/issues/1691), [#1712](https://github.com/geneontology/go-annotation/issues/1712), [#1955](https://github.com/geneontology/go-annotation/issues/1955), [#1979](https://github.com/geneontology/go-annotation/issues/1979), [#2171](https://github.com/geneontology/go-annotation/issues/2171), [#2250](https://github.com/geneontology/go-annotation/issues/2250), [#2431](https://github.com/geneontology/go-annotation/issues/2431), [#2570](https://github.com/geneontology/go-annotation/issues/2570), [#2587](https://github.com/geneontology/go-annotation/issues/2587), [#2827](https://github.com/geneontology/go-annotation/issues/2827). go-ontology issues cited via LIGANDS_IN_SIGNALING: #14275, #15477, #31015.

**Papers**

- [PMID:23842463](https://europepmc.org/article/MED/23842463) A guide to best practices for Gene Ontology (GO) manual annotation (2013)

**Repository**

- [REGULATION_SIGN](https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html)
- [LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html)
- [MAPK_CASCADES](https://ai4curation.io/ai-gene-review/pages/projects/MAPK_CASCADES.html)
- [GPCR](https://ai4curation.io/ai-gene-review/pages/projects/GPCR.html)
- [IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)
- [INTEGRATED_STRESS_RESPONSE](https://ai4curation.io/ai-gene-review/pages/projects/INTEGRATED_STRESS_RESPONSE.html) (EIF2AK3: GO:0140467 not added as NEW, being an ancestor of the accepted GO:0036499)
- [CGAS_STING_PATHWAY](https://ai4curation.io/ai-gene-review/pages/projects/CGAS_STING_PATHWAY.html)
- [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)
- [FUNCTION_REQUIREMENT_RULES](https://ai4curation.io/ai-gene-review/pages/projects/FUNCTION_REQUIREMENT_RULES.html)
- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) (MODIFY for sign corrections; "Do not overrule curators")

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation), Guideline 2 | If unsure, annotate the parent process with `acts upstream of or within`. | Same, but always with the positive- or negative-effect child (RS-1, RS-5). | The relation table and wiki now ask for the signed child. A perturbation almost always gives the direction. |
| [wiki: Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual) | Extracellular ligands of PI3K signalling are annotated to "positive regulation of phosphatidylinositol 3-kinase signaling". Ligands use "receptor agonist activity". | GO:0014068 and GO:0014065 are obsolete. Ligands get receptor ligand activity and the receptor pathway term; "positive regulation of" the cassette only when the cassette is annotated without pathway context (RS-7, RS-8). | The page dates from 2018 and cites obsolete terms. "Receptor agonist activity" was renamed receptor ligand activity in 2017 ([LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html)). |
| PomBase convention, reported in [LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html) | Pheromones, receptors and Gα annotated to "positive regulation of pheromone response MAPK cascade"; only the kinases are `involved_in` the cascade. | Ligand, receptor and Gα `involved_in` the receptor pathway term where one exists (RS-6, RS-8). | One convention across GO. PomBase's choice follows from the obsolescence of the old pathway term, so the fix may be ontological (a pathway term to annotate to). Raise it with PomBase rather than overriding locally. |
| [Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI) (FlyBase-only) | Regulation does not traverse transcription; general regulators stay off pathways; regulation terms must be signed. | Adopt for all groups (RS-5, RS-10). | The rules work well in FlyBase's exhaustive pathway curation and match the GOC wiki's intent. |
| [wiki: Response to and signaling](https://wiki.geneontology.org/index.php/Response_to_and_signaling); [LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html) | Pathway terms are part of "cellular response to X", so ligands inherit response annotations. Whether ligands should carry the response term is unresolved (go-ontology#15477). | Do not annotate ligands directly to "cellular response to [ligand]". Let inference supply it through the pathway term. | Annotating the ligand as responding to itself reads badly in a GAF. Inference already gives users the link. |

## Open questions

1. **Scaffolds and adaptors: part of, or regulation of?** [go-annotation#1592](https://github.com/geneontology/go-annotation/issues/1592) records dissent, and the 2022 PomBase questions (WASP and Arp2/3, securin and separase) show the same ambiguity outside signalling ([Drive: 2022 questions about regulation](https://drive.google.com/open?id=1J_WpQPSyn4wvsMtxEAG4d7xA4SLmA0m2)). Is a substrate inhibitor (securin) part of sister chromatid separation, or a negative regulator of it?
2. **Upstream dependencies.** Should any "acts upstream of" annotations be made for constitutive metabolic prerequisites, such as folate for nucleotide synthesis? If so, where does the chain stop ([go-annotation#2431](https://github.com/geneontology/go-annotation/issues/2431))?
3. **Antagonist ligands.** Receptor ligand activity is now classed as an activating activity, but Hedgehog binding inhibits Patched. Should GO have agonist and antagonist ligand terms (go-ontology#14275, open since 2017; [LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html))?
4. **Pathway end for non-transcriptional outputs.** Where does a pathway end when its output is cytoskeletal or metabolic? The 2022 breakout noted that terms "ultimately effecting a change in the functioning of the cell" leave this unclear ([Drive: Breakout – Annotating to a process or its regulation, 2022](https://drive.google.com/open?id=1ii8kFkraHYYSGThmYZq9i6EyqNmY4v91hpGuuvIMunk)).
5. **"Response to" qualifier.** Should GO distinguish "acts in the response" from "is induced during the response", by an extension or a qualifier, so that IEP rows stop competing with mechanistic ones ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html), recommendation 5)?
6. **PomBase pheromone convention.** Should GO restore a pheromone signalling pathway term so that ligands and receptors can be `involved_in` it?
7. **Tissue-development regulation.** The 2022 breakout asked where the boundary lies between a process and its regulation for tissue development, which needs signalling, trafficking and cell-cycle control. The BP refactoring draft suggests regulation exists only at the level of pathways and cells ([Drive: BP refactoring 2022](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg)). Should "regulation of [organ] development" terms be retired?

<!-- END GENERATED -->
