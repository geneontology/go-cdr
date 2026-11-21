---
id: BP
title: Biological process
record_kind: guideline
applies_to:
- contributing_group
status: proposed
aspects:
- P
differences:
- prior_source: '[wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)'
  prior_said: Older IMP annotations "should be reviewed and removed" when they no longer reflect the MF–BP
    relation.
  we_recommend: Change the relation (record `WRONG_QUALIFIER`) or the term (`MODIFY`). Remove only if
    the claim is false (BP-4, BP-14).
  why: A true upstream effect annotated with too strong a relation is still true. Removing it loses information
    that the correct relation would carry.
- prior_source: '[wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
    (high-level phenotypes)'
  prior_said: '"Strongly encourage" not annotating high-level processes without mechanism.'
  we_recommend: 'Same for new annotations. For existing rows: the BEHAVIOR rubric (accept if the gene
    acts in the circuit, non-core if distal, over-annotated if uselessly broad, remove if contradicted)
    (BP-7, BP-14).'
  why: The wiki gives no review-time guidance. The repository rubric fills that gap.
- prior_source: '[wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual),
    "Other annotation examples"'
  prior_said: Staurosporine-induced or light-induced death data support "positive/negative regulation
    of apoptotic process".
  we_recommend: For a phenotype with no mechanism, use `acts upstream of or within` with a sign on GO:0006915.
    A regulation term needs a specific effect (BP-4, BP-10, BP-13).
  why: The manual contradicts itself. Its later section says current practice requires a known mechanism,
    and the phenotype guideline's CHCHD10 example forbids the regulation term. We follow the newer statements.
- prior_source: '[wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)
    vs [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)'
  prior_said: The manual recommends a cell-type extension on GO:0006915 over a cell-type-specific term.
    The repository forbids `part_of(Y)` extensions as re-precomposition.
  we_recommend: 'Both hold: `occurs_in` cell type is context and fine; `part_of` another process is a
    precomposition and not (BP-10, BP-11).'
  why: Apparent conflict. The two concern different relations.
open_questions:
- '**Scaffold proteins in pathways.** Is a MAPK scaffold part of the cascade, or a regulator of it? [go-annotation#1592](https://github.com/geneontology/go-annotation/issues/1592)
  settled on "part of", with a separate regulator MF where the scaffold also allosterically activates
  a kinase. The thread records dissent. We follow #1592 in [RS-7](../RS/RS-7.md),
  but the GOC has not written the rule into a guideline.'
- '**When is `acts upstream of` worth asserting?** PomBase does not use it ([go-annotation#2417](https://github.com/geneontology/go-annotation/issues/2417)).
  The wiki leaves it to the curator. A criterion is needed, for example "only when the upstream process
  has no GO term".'
- '**Developmental terms whose distinctions are rarely tested.** Should the specification/determination
  split be retired in favour of commitment for lineages where single-cell data show continuous trajectories
  ([NEURON_DEVELOPMENT](https://ai4curation.io/ai-gene-review/pages/projects/NEURON_DEVELOPMENT.html))?'
- '**Should cell population proliferation and its regulation terms carry a GO rule requiring an extension**,
  as proposed in #2204?'
- '**Machine-readable substrate relationships.** GO puts substrate relations on the enzyme (`has_input`),
  but `has_input` on a BP annotation does not appear in the GAF. How should standard annotation expose
  that angiotensinogen is the input of angiotensin maturation?'
- '**Repository schema fix.** Correct the `acts_upstream_of` description in `AnnotationQualifierEnum`,
  and decide whether the relation-only MODIFY + NEW pattern ([QN-7](../QN/QN-7.md))
  should become a dedicated field.'
date: '2026-11-15'
---

# Biological process: GO annotation guidelines


**In brief:**

- `involved_in` says the gene product's own activity is a step of the process. Before using it, name the step the product performs. If the honest answer is "it is needed for the process" or "it is what the process acts on", the relation is wrong, the term is wrong, or both.
- A knockout phenotype shows necessity, not participation. With no known mechanism, use `acts upstream of or within`, choose its positive or negative child, and use the most proximal process the data support. Leaving the row unannotated is also acceptable.
- Annotate the process nearest the activity, not the assay readout and not the organism-level outcome. Behaviour, development, lifespan, growth, proliferation and cell death need a mechanism before they become GO terms.
- Do not request, add or split precomposed "X involved in Y" terms. Annotate X, and record where Y went: a model, a core function, or nowhere.
- Before adding a process term because "every other participant has it", run the comparator check. A systematic absence across species is usually a convention.
- In review, a real but distal process is `KEEP_AS_NON_CORE`. `REMOVE` is for claims that are contradicted, not for claims that are merely far from the core.

## Scope


This document covers annotation of gene products to Biological Process (BP) terms with the BP gene-product-to-term relations (`involved in`, `acts upstream of or within` and `acts upstream of`, with their positive- and negative-effect children). It covers choosing between participation and upstream effect, interpreting phenotypes, developmental and organism-level processes, cell death, precomposed terms, pathway versus step terms, term depth, and the core versus non-core call made in reviews.

Out of scope, with pointers:

- Regulation terms, signalling pathways and "response to" terms: [regulation-and-signaling.md](../RS/README.md). The boundary between "part of X" and "regulation of X" is drawn there (RS-1 to RS-5).
- Transcription and its regulation: [transcription-regulation.md](../TR/README.md).
- Evidence-code mechanics (IMP versus IGI versus HMP, IEP): [evidence-codes.md](../EV/README.md).
- Annotation extension syntax (`occurs_in`, `has_input`): [annotation-extensions.md](../AE/README.md).
- IBA and other propagation of BP terms: [phylogenetic-propagation.md](../PH/README.md).
- NOT annotations: [qualifiers-and-negation.md](../QN/README.md).

## Principles


**A BP annotation is a claim about normal biology.** It says that, in the wild-type organism, an activity of this gene product contributes to the process. Mutant, overexpression and drug experiments are evidence for that claim. They are not the claim. GO is not a phenotype database, and most contributing groups curate phenotypes separately ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)).

**A process is an ordered assembly of molecular functions.** RO and GO define `involved_in` as: the gene product enables some function that is `part_of` the process ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes); [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)). Every `involved_in` row should therefore be explainable by an MF, known or unknown, that is a step of the process. A row that cannot be explained this way is an upstream claim and needs an upstream relation.

**The relation carries directness; the term carries the process.** Do not use one to repair the other. A distal phenotype is not fixed by moving to a vaguer term while keeping `involved_in`. It is fixed by choosing the proximal process, the upstream relation, or both.

**Necessity is not participation.** Substrates, precursors, cofactor suppliers, assembly factors and housekeeping machinery are all necessary for many processes. Being necessary is exactly what a substrate is. A perturbation experiment, however clean, cannot tell a participant from a substrate. Only a model of which entity performs which step can ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), "Do not add what curators deliberately declined to add").

**Annotations are for users who ask "which genes do X?"** An annotation that puts a ribosomal protein in apoptosis or a tubulin in locomotory behaviour makes that query less accurate. That cost is why the bar for organism-level terms is high.

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [BP-1](BP-1.md) | Use `involved in` only when the gene product's activity is a step of the process | proposed | [GOC+] |
| [BP-2](BP-2.md) | Name the entity that performs the step; substrates and products are not participants unless they do some of the work | proposed | [GOC+] |
| [BP-3](BP-3.md) | Run the comparator check before treating an absence as a gap | proposed | [NEW] |
| [BP-4](BP-4.md) | When the mechanism is unknown, use `acts upstream of or within`, choose a sign, and choose the most proximal process | proposed | [GOC+] |
| [BP-5](BP-5.md) | Use `acts upstream of` (without "or within") only when the mechanism is known and the activity is outside the process and does not regulate it | proposed | [GOC] |
| [BP-6](BP-6.md) | Annotate the process the gene product acts in, not the readout that was measured | proposed | [GOC] |
| [BP-7](BP-7.md) | Organism-level and other "high-level" processes need a mechanism | proposed | [GOC+] |
| [BP-8](BP-8.md) | Give pleiotropic core machinery its core processes, not every process it affects | proposed | [GOC] |
| [BP-9](BP-9.md) | Developmental processes: annotate the cell-level step, at the right grain, for genes that perform it | proposed | [GOC+] |
| [BP-10](BP-10.md) | Cell death: choose the phase, keep regulation for specific effects, and do not equate death with apoptosis | proposed | [GOC+] |
| [BP-11](BP-11.md) | Do not request, add or split precomposed "X involved in Y" terms; decompose them to X and record where Y went | proposed | [NEW] |
| [BP-12](BP-12.md) | Annotate the step term when the evidence reaches it; do not demand BP specificity that only restates the MF | proposed | [GOC+] |
| [BP-13](BP-13.md) | Choose the deepest term the row's own evidence supports, and no deeper | proposed | [GOC+] |
| [BP-14](BP-14.md) | In review, separate core processes from real but peripheral ones, and reserve REMOVE for contradicted claims | proposed | [NEW] |
| [BP-15](BP-15.md) | Do not propagate developmental, behavioural or stimulus-response terms without a conserved mechanism, and check that the pathway can exist in the target taxon | proposed | [GOC+] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


Start with the evidence and the gene product, and ask in order:

| # | Question | If yes | If no |
|---|---|---|---|
| 1 | Is the claim contradicted (wrong gene, opposite sign, refuted)? | Do not annotate / `REMOVE` | go on |
| 2 | Can you name the gene product's activity that is a step of P? | `involved_in` P (BP-1) | go on |
| 3 | Is the gene product a substrate, product, precursor or other input of P that supplies no scaffold, cofactor role or chemistry? | Not P; the agent gets P (BP-2) | go on |
| 4 | Is the gene product a known modulator of a P participant? | Regulation term (see [RS-2](../RS/RS-2.md)) | go on |
| 5 | Is P a readout for something more proximal? | Annotate the proximal process (BP-6) | go on |
| 6 | Is P organism-level (behaviour, development, growth, lifespan, proliferation, death)? | Only with a mechanism; else none (new) / non-core (review) (BP-7) | go on |
| 7 | Is the mechanism unknown but the effect real and directional? | `acts upstream of or within, positive/negative effect` P (BP-4) | no annotation |

For precomposed terms, apply BP-11 before question 2: decompose first, then evaluate each half.

## Common errors


- **"Required for" read as "involved in".** Authors write "X is required for Y". The paper shows necessity, and a GO annotation states participation ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). Fix: upstream relation (BP-4) or proximal term (BP-6).
- **Substrate on the processing term.** A precursor annotated to its own maturation or processing term. Fix: remove the precursor from the term (BP-2) and check that the processing enzyme carries it.
- **Assembly factors on the complex's process.** Subunits or chaperones needed for a complex's assembly, annotated to the process the complex performs. [go-annotation#2942](https://github.com/geneontology/go-annotation/issues/2942) states that factors needed for maturation of a process's members are not normally annotated to that process. [go-annotation#2149](https://github.com/geneontology/go-annotation/issues/2149) found complex assembly itself over-annotated to subunits.
- **Housekeeping knockout on a specific process.** A ribosomal, splicing or proteasome subunit annotated to apoptosis, cell cycle or a signalling pathway from a knockdown. Fix: BP-8.
- **Behaviour or development from a structural or metabolic gene's phenotype.** Fix: BP-7 and BP-14 (`KEEP_AS_NON_CORE`, with the proximal defect named).
- **IEP time-course on a developmental term.** Expression rising as a tissue matures, annotated as building the tissue. Fix: `MARK_AS_OVER_ANNOTATED` ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)).
- **Batch annotation from one screen.** One paper, one term, many unrelated genes. Treat each row as suspect ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html), pattern 3; [go-annotation#1869](https://github.com/geneontology/go-annotation/issues/1869)).
- **Decomposing by splitting.** `involved_in` X plus `involved_in` Y loses the fact that X occurs as part of Y. Fix: BP-11.
- **Host proteins on pathogen processes.** Host factors co-opted by a virus annotated to viral transcription or replication. The host protein does not perform the viral process ([go-annotation#1507](https://github.com/geneontology/go-annotation/issues/1507); see [multi-organism-and-ncrna.md](../MO/README.md)).
- **Reading "activated during" as "involved in".** A gene activated during meiosis is not thereby `involved_in` meiosis, and the GO meiosis term means the meiotic division, not the developmental phase ([go-annotation#1005](https://github.com/geneontology/go-annotation/issues/1005)).

## Reading list


**GO wiki**

- [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) (reviewed 2018)
- [Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) (flagged "to be reviewed")
- [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) (edited 2026)
- [Causally upstream of or within](https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within) (reviewed 2023)
- [Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)
- [Development](https://wiki.geneontology.org/index.php/Development)
- [Guidelines for checkpoints](https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints)
- [Guidelines from Annotation Camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) (historical)
- [Inferred from High Throughput Mutant Phenotype (HMP)](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_(HMP))

**GO Consortium Drive**

- [Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- [Case studies annotating from mutant phenotypes](https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0)
- [GOC Corvallis 2017: Regulation and causality & use of qualifiers in legacy annotations](https://drive.google.com/open?id=1fmgRMOPel-8_7iIuMAkVDNGuxurUWTxJRdsZTgSeNRM)
- [GOC NYC 2018: QC group report](https://drive.google.com/open?id=1cTLQGeV9aUiMvMgW5DxB8pNOARlMoNmmz7nqiyxXPg0)
- [BP refactoring 2022 – developmental process](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg) (draft)
- [Decomposition of macro biological processes](https://drive.google.com/open?id=1q7PE8VGRGYWyohbLMwpiYpd6dnCJQVuomyzsK5dC9bc) (2023 draft)
- [FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI) (draft for discussion)
- [Taxon constraints for signaling pathways, Padua 2023](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)

**go-annotation issues**

[#211](https://github.com/geneontology/go-annotation/issues/211), [#1005](https://github.com/geneontology/go-annotation/issues/1005), [#1011](https://github.com/geneontology/go-annotation/issues/1011), [#1056](https://github.com/geneontology/go-annotation/issues/1056), [#1344](https://github.com/geneontology/go-annotation/issues/1344), [#1364](https://github.com/geneontology/go-annotation/issues/1364), [#1396](https://github.com/geneontology/go-annotation/issues/1396), [#1450](https://github.com/geneontology/go-annotation/issues/1450), [#1507](https://github.com/geneontology/go-annotation/issues/1507), [#1517](https://github.com/geneontology/go-annotation/issues/1517), [#1532](https://github.com/geneontology/go-annotation/issues/1532), [#1592](https://github.com/geneontology/go-annotation/issues/1592), [#1631](https://github.com/geneontology/go-annotation/issues/1631), [#1869](https://github.com/geneontology/go-annotation/issues/1869), [#1886](https://github.com/geneontology/go-annotation/issues/1886), [#2149](https://github.com/geneontology/go-annotation/issues/2149), [#2171](https://github.com/geneontology/go-annotation/issues/2171), [#2204](https://github.com/geneontology/go-annotation/issues/2204), [#2250](https://github.com/geneontology/go-annotation/issues/2250), [#2417](https://github.com/geneontology/go-annotation/issues/2417), [#2425](https://github.com/geneontology/go-annotation/issues/2425), [#2456](https://github.com/geneontology/go-annotation/issues/2456), [#2469](https://github.com/geneontology/go-annotation/issues/2469), [#2510](https://github.com/geneontology/go-annotation/issues/2510), [#2820](https://github.com/geneontology/go-annotation/issues/2820), [#2942](https://github.com/geneontology/go-annotation/issues/2942)

**Papers**

- [PMID:32875947](https://europepmc.org/article/MED/32875947) Term Matrix: a GO annotation quality control system based on ontology term co-annotation patterns (2020)

**Repository**

- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md): "Do not add what curators deliberately declined to add", MODIFY rules, "Decomposing precomposed terms", "Do not overrule curators"
- [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)
- [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)
- [BEHAVIOR](https://ai4curation.io/ai-gene-review/pages/projects/BEHAVIOR.html)
- [NEURON_DEVELOPMENT](https://ai4curation.io/ai-gene-review/pages/projects/NEURON_DEVELOPMENT.html)
- [APOPTOSIS](https://ai4curation.io/ai-gene-review/pages/projects/APOPTOSIS.html) and [APOPTOSIS/ASSAY_READOUT_OVERANNOTATION](https://ai4curation.io/ai-gene-review/pages/projects/APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.html)
- [FUNGAL_PHENOTYPES](https://ai4curation.io/ai-gene-review/pages/projects/FUNGAL_PHENOTYPES.html)
- [PATHWAY_SATISFIABILITY](https://ai4curation.io/ai-gene-review/pages/projects/PATHWAY_SATISFIABILITY.html) and its [taxon-absent-component detector](https://ai4curation.io/ai-gene-review/pages/projects/PATHWAY_SATISFIABILITY/taxon_absent_component/README.html)
- [IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)
- [FUNCTION_REQUIREMENT_RULES](https://ai4curation.io/ai-gene-review/pages/projects/FUNCTION_REQUIREMENT_RULES.html) (regulators annotated with the activity they regulate, as a flagged error class)
- [docs/action_consistency.md](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md), [docs/source_defects.md](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) | Older IMP annotations "should be reviewed and removed" when they no longer reflect the MF–BP relation. | Change the relation (record `WRONG_QUALIFIER`) or the term (`MODIFY`). Remove only if the claim is false (BP-4, BP-14). | A true upstream effect annotated with too strong a relation is still true. Removing it loses information that the correct relation would carry. |
| [wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) (high-level phenotypes) | "Strongly encourage" not annotating high-level processes without mechanism. | Same for new annotations. For existing rows: the BEHAVIOR rubric (accept if the gene acts in the circuit, non-core if distal, over-annotated if uselessly broad, remove if contradicted) (BP-7, BP-14). | The wiki gives no review-time guidance. The repository rubric fills that gap. |
| [wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual), "Other annotation examples" | Staurosporine-induced or light-induced death data support "positive/negative regulation of apoptotic process". | For a phenotype with no mechanism, use `acts upstream of or within` with a sign on GO:0006915. A regulation term needs a specific effect (BP-4, BP-10, BP-13). | The manual contradicts itself. Its later section says current practice requires a known mechanism, and the phenotype guideline's CHCHD10 example forbids the regulation term. We follow the newer statements. |
| [wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual) vs [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html) | The manual recommends a cell-type extension on GO:0006915 over a cell-type-specific term. The repository forbids `part_of(Y)` extensions as re-precomposition. | Both hold: `occurs_in` cell type is context and fine; `part_of` another process is a precomposition and not (BP-10, BP-11). | Apparent conflict. The two concern different relations. |

## Open questions

1. **Scaffold proteins in pathways.** Is a MAPK scaffold part of the cascade, or a regulator of it? [go-annotation#1592](https://github.com/geneontology/go-annotation/issues/1592) settled on "part of", with a separate regulator MF where the scaffold also allosterically activates a kinase. The thread records dissent. We follow #1592 in [RS-7](../RS/RS-7.md), but the GOC has not written the rule into a guideline.
2. **When is `acts upstream of` worth asserting?** PomBase does not use it ([go-annotation#2417](https://github.com/geneontology/go-annotation/issues/2417)). The wiki leaves it to the curator. A criterion is needed, for example "only when the upstream process has no GO term".
3. **Developmental terms whose distinctions are rarely tested.** Should the specification/determination split be retired in favour of commitment for lineages where single-cell data show continuous trajectories ([NEURON_DEVELOPMENT](https://ai4curation.io/ai-gene-review/pages/projects/NEURON_DEVELOPMENT.html))?
4. **Should cell population proliferation and its regulation terms carry a GO rule requiring an extension**, as proposed in #2204?
5. **Machine-readable substrate relationships.** GO puts substrate relations on the enzyme (`has_input`), but `has_input` on a BP annotation does not appear in the GAF. How should standard annotation expose that angiotensinogen is the input of angiotensin maturation?
6. **Repository schema fix.** Correct the `acts_upstream_of` description in `AnnotationQualifierEnum`, and decide whether the relation-only MODIFY + NEW pattern ([QN-7](../QN/QN-7.md)) should become a dedicated field.

<!-- END GENERATED -->
