---
id: CAM
title: GO-CAM modelling
record_kind: guideline
applies_to:
- contributing_group
status: proposed
differences:
- prior_source: '[Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)
    (undated, open comments)'
  prior_said: Use "regulates" for known but non-direct control, with the mechanism named in the first
    `part of` BP.
  we_recommend: Use the signed `indirectly positively/negatively regulates` (RO:0002407, RO:0002409);
    keep naming the mechanism in the BP (CAM-7, CAM-9).
  why: The 2022 decision tree has no path to unsigned relations; reviewers of the guideline asked for
    signed children.
- prior_source: '[gocam-curation causal-relations reference](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/causal-relations.md)
    (repo)'
  prior_said: Lists `positively regulates` RO:0002213 / `negatively regulates` RO:0002212 as the indirect
    relations, alongside the explicit indirect ones.
  we_recommend: Treat RO:0002213/RO:0002212 as legacy parents; new or corrected edges use RO:0002407/RO:0002409.
  why: RO:0002213 is the parent of the direct relation, so it does not assert indirectness.
- prior_source: '[Drive: Regulation Notes, 2020 Jamboree](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)
    vs [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)'
  prior_said: The Jamboree notes allow a regulatory edge between two MFs of the same gene product (unfolded
    protein binding regulates kinase activity). The February 2020 call limits "directly regulates" to
    activities of different gene products.
  we_recommend: One node with the compound MF for a single gene product; no causal edges between nodes
    of the same gene product to represent its internal switch (CAM-2, CAM-8).
  why: Self-edges create spurious MF-regulator inferences and the `same_gene_chain` pattern.
- prior_source: '[Drive: New Causal Relations Decision Tree](https://drive.google.com/open?id=1ODFtV2aEeUeOUDs8dupre-3hUJchLFMMu-kChPKR1Oc)'
  prior_said: Gives `indirectly positively regulates` as "RO:00002407".
  we_recommend: RO:0002407 (verified).
  why: Typo in the deck; the extra digit makes an invalid CURIE.
- prior_source: '[Drive: 2025 complexes deck](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE),
    Case 4'
  prior_said: Notes that listing inactive members as `has part` will export contributes_to, "should not
    be allowed but we have no way to identify these".
  we_recommend: '`has part` is limited to subunits that form the active unit; reviewers flag violations
    as `COMPLEX_SUBUNIT_REPRESENTATION`.'
  why: Closes the gap the deck identified, at the curation step rather than in software.
- prior_source: '[Drive: Complex active units notes, 2025-07](https://drive.google.com/open?id=19GdhwjKWXGzkxBIL0eVxrdDvgzunW542DGkbD9W-1c8)'
  prior_said: Asks why CASP3 is annotated to cysteine-type endopeptidase activity, calling it "a well-known
    aspartic-type endopeptidase".
  we_recommend: Keep `GO:0004197` cysteine-type endopeptidase activity for caspases.
  why: Caspases are cysteine proteases that cleave after aspartate; the aside confuses substrate specificity
    with catalytic class.
open_questions:
- '**Complex context for a subunit''s activity.** The 2025 deck proposes a relation stating that an activity
  is performed by a subunit while in a named complex (KAT8 in the MSL versus NSL complex). Until it exists,
  a subunit active in two complexes can only be modelled as two nodes differing in process. Should GO-CAM
  add `part of` (complex) on the activity, or a dedicated relation?'
- '**Contributes_to export.** Case 2 export is not implemented. Until it is, emergent activities produce
  no MF rows. Should curators also make standard contributes_to annotations by hand in the meantime?'
- '**Compound functions.** Nuclear receptors, receptor kinases and ligand-gated channels combine binding
  and a downstream activity. The 2020 call noted that their logical definitions were under review. Should
  these ever be split into sub-activities joined by `has part`, as the 2016 documentation allowed?'
- '**Small-molecule regulators.** If GOC prefers the 2023 relation-page reading (direct edges for small-molecule
  effects), the binding inference attached to "directly" needs to be dropped. This needs a decision from
  the ontology and software groups together.'
- '**Host and symbiont activities in one model.** Models such as `62b4ffe300002385` (Shigella OspC3 inactivating
  human CASP4) put activities of two organisms in one graph. The location chain can nest a host organism,
  but there is no agreed way to record the interacting taxon on exported rows ([MO-8](../MO/MO-8.md)).'
- '**Standard versus GO-CAM models.** The evidence-unwinding project will bin "mixed" models. Should a
  model with one causal edge and many unconnected standard annotations be split?'
date: '2026-11-15'
---

# GO-CAM modelling: GO annotation guidelines


**In brief:**

- The unit of a GO-CAM is the activity: one molecular function, enabled by one gene product (or, for an emergent activity, one complex), occurring in one location, as part of one process chain. Make a second node for the same gene product only when the function, input, location, process or timing differs.
- Choose a causal relation in three steps: relationship type (regulation, provides input for, constitutively upstream, removes input for, or undetermined), then sign, then directness. When the mechanism is unknown, use `causally upstream of, positive/negative effect`. Do not let a phenotype stand in for a mechanism.
- "Directly" means two successive activities of different gene products, with no activity in between, the upstream one acting on the enabler of the downstream one. Transcriptional and miRNA control is always indirect. If a small molecule carries the effect, model the molecule.
- `has input` names what the activity acts on: the substrate, the target gene, the effector a receptor activates, the partners an adaptor bridges. It never names a receptor's ligand, a cofactor, a currency metabolite or an assay reagent. Where a ChEBI product links two steps, use `has output` and `has input` rather than `provides input for`.
- Every location must resolve to a real compartment, and a material-flow edge must not jump a membrane without the transporter or secretion step that crosses it.
- A model produces standard annotations. Before choosing an enabler or a relation, know which GAF/GPAD rows it will generate, and give every asserted edge its own evidence.

## Scope


This document covers how to build and how to review GO Causal Activity Models
(GO-CAMs). It sets out what an activity unit is, how molecular functions are
typed and linked by causal relations, how inputs, outputs, locations and
processes are attached, how complexes are represented, how evidence attaches
to edges, and how standard annotations are derived from a model.

It does not repeat the term-choice rules for molecular functions in general
([molecular-function.md](../MF/README.md)), for complexes in standard
annotation ([protein-complexes.md](../PC/README.md)), or for annotation
extensions ([annotation-extensions.md](../AE/README.md)). Many GO-CAM
relations (`has input`, `occurs in`, `part of`) are also extension relations,
and the rules here agree with those documents. Relations that exist only in
GO-CAM (the MF-to-MF causal relations) are treated fully here.

In this repository GO-CAMs are read-only. We cache production models
(`gocams/<id>/<id>-src.yaml`), index their activities (`gocams/index.tsv`),
lint them (`just gocam-lint`, [gocam_lint](https://github.com/ai4curation/ai-gene-review/blob/main/docs/gocam_lint.md)),
check their compartments (`just gocam-compartments`,
[GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)) and record assessments in
`gocams/<id>/<id>-review.yaml` (`GoCamReview`, with the workflow in
[the gocam-curation skill](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/SKILL.md)).
The rules apply equally to a curator building a model in Noctua and to a
reviewer judging one.

## Principles


A GO-CAM states a mechanism. Each node is a claim that a named gene product
carries out a named activity; each edge is a claim that one activity affects
another in a stated way. A standard annotation says a gene product is
"involved in" a process; a model says what it does there and what happens
next. The extra expressiveness is only worth having if each edge means one
thing, so the causal relations are deliberately few and the choice between
them is driven by mechanism.

A model is also a source of standard annotations. Noctua exports GPAD rows
from models by reasoning over the graph, so a modelling shortcut (a complex
as enabler, a direct edge that implies binding) becomes a row in GOA that
other people review without seeing the model. Modelling choices therefore
have to survive two readings: as a pathway, and as the gene-level rows it
produces.

Specificity should reflect the biological conclusion, not the experimental
set-up. The consortium's modelling guideline puts it plainly: capture a target,
location or time only when it is "biologically important", and keep models as
general as the biology allows
([Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)).

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [CAM-1](CAM-1.md) | Model activities, not genes: each activity unit has one function, one enabler, one location chain and one process chain. | proposed | [GOC] |
| [CAM-2](CAM-2.md) | Give a gene product a second activity node only when the function, input, location, process or time differs. | proposed | [GOC+] |
| [CAM-3](CAM-3.md) | The enabler is the gene product that performs the activity; use a complex as enabler only for an emergent activity, and never the root complex term. | proposed | [GOC+] |
| [CAM-4](CAM-4.md) | Type each activity by the role it plays in the flow; a bare binding term is not an activity. | proposed | [GOC+] |
| [CAM-5](CAM-5.md) | `has input` names what the activity acts on; the ligand of a receptor is upstream, not input. | proposed | [GOC] |
| [CAM-6](CAM-6.md) | Link metabolic steps through the ChEBI product; use `provides input for` only when the intermediate is a macromolecule or has no ChEBI entry. | proposed | [GOC] |
| [CAM-7](CAM-7.md) | Choose the causal relation by relationship type, then sign, then directness. | proposed | [GOC+] |
| [CAM-8](CAM-8.md) | Use a "directly" relation only between successive activities of different gene products, where the upstream activity acts on the downstream enabler; route small-molecule effects through the molecule. | proposed | [GOC+] |
| [CAM-9](CAM-9.md) | Control through gene expression is always indirect; the regulator's input is the target gene and its process names the mechanism. | proposed | [GOC] |
| [CAM-10](CAM-10.md) | Use `constitutively upstream of` for required housekeeping steps, not regulation. | proposed | [GOC] |
| [CAM-11](CAM-11.md) | Use `removes input for` only for a switch in which the upstream activity uses up the downstream activity's input site. | proposed | [GOC] |
| [CAM-12](CAM-12.md) | Connect an activity to a process by a causal edge only when the mechanism is unknown; otherwise use `part of`. | proposed | [GOC] |
| [CAM-13](CAM-13.md) | Give each activity one location that resolves to a distinct compartment. | proposed | [NEW] |
| [CAM-14](CAM-14.md) | A material-flow edge must not cross a membrane without the activity that crosses it; a regulation edge may join compartments only if the regulated protein moves. | proposed | [NEW] |
| [CAM-15](CAM-15.md) | Every asserted edge carries its own evidence: one ECO class and one reference per evidence instance, supporting that edge. | proposed | [GOC+] |
| [CAM-16](CAM-16.md) | A model is a module: include the activities specific to its process, reuse general machinery by reference, and link models through a shared activity. | proposed | [GOC+] |
| [CAM-17](CAM-17.md) | Know the standard annotations your model will export, and review exported rows against the model. | proposed | [GOC+] |
| [CAM-18](CAM-18.md) | In pathway imports, the enabler is the active unit, not the catalyst entity as drawn. | proposed | [GOC+] |
| [CAM-19](CAM-19.md) | When reviewing, check each activity against the gene review, and treat a model as one curator's assertion, not as evidence. | proposed | [NEW] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


**Choosing the edge between activity A (upstream) and activity B.**

| Question | Answer | Relation |
|---|---|---|
| Is A's product B's substrate? | yes, product in ChEBI | A `has output` X; B `has input` X |
| | yes, product is a modified macromolecule | `provides input for` |
| Do A and B act on the same site, A first? | yes | `removes input for` |
| Is A required but constant, not a control point? | yes | `constitutively upstream of` |
| Does A control B? | via B's protein, nothing between, different enablers | `directly positively/negatively regulates` |
| | via a small molecule A makes or destroys | A `has output` X; X `is small molecule activator/inhibitor of` B |
| | via gene expression, or other intervening steps | `indirectly positively/negatively regulates` |
| None of the above is known | effect sign known | `causally upstream of, positive/negative effect` |

**Choosing the enabler for a complex activity.**

| Situation | Enabler | `has part` | Export |
|---|---|---|---|
| One subunit carries the activity | that subunit | none | enables |
| Active site spans subunits | specific complex term | contributing subunits only | contributes_to (pending) |
| Active subunit unknown | specific complex term | none | none |
| No specific complex term exists | request one; meanwhile case 3 with the nearest specific term | none | none |

**Placing a location.**

| Term in hand | Use instead |
|---|---|
| `GO:0000785` chromatin, chromosome sub-terms | `GO:0000228` nuclear chromosome (eukaryotes) |
| `GO:0016020` membrane | the named membrane |
| `GO:0005737` cytoplasm | `GO:0005829` cytosol, or the organelle |
| a CL cell type | a CC term nested `part of` the cell type |
| a complex term | move it to the enabler |

## Common errors


| Error | How it shows | Fix |
|---|---|---|
| Ligand as receptor input | receptor `has input` its ligand (`receptor_ligand_input`) | ligand node `has input` receptor and directly positively regulates it; small-molecule ligands via `is small molecule activator of` |
| TF directly regulates a protein | `transcription_direct_edge`; nucleus to cytoplasm crossing | `indirectly positively/negatively regulates`; TF `has input` target gene |
| Binding as the activity | `binding_mf` | name the role (adaptor, sequestering, inhibitor) or drop the node |
| Generic MF | `generic_mf` (`kinase activity`, `catalytic activity`) | the specific activity the paper shows |
| Activation-state chain | `same_gene_chain`, `duplicate_activity` | one node; incoming edge carries the activation |
| Direct edge across a membrane | `compartment_crossing` ERROR | add the transport or secretion step |
| Unresolvable location | chromatin, cell junction, a CL term as `occurs in` | nuclear chromosome; name the side of the junction; nest the cell type |
| Phenotype as mechanism | direct edge supported only by knockdown | `causally upstream of` with sign, or omit |
| Every complex member as `has part` | contributes_to for structural subunits (on export) | only the subunits that form the active unit |
| Edge with no evidence | `missing_evidence` | add ECO and reference that show the edge |
| Copied edge evidence | `edge_evidence_copied` | find the experiment that shows the causal link |
| Model split from one paper | `near_duplicate_models` | merge, or make each model a distinct process |

## Reading list


**GO Consortium Drive**

- [GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)
- [GO-CAM specifications / GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4)
- [GO-CAM specifications / Copy of MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4) (a copy; the original "MF guidelines for GO-CAM" is canonical)
- [2025-05 GOC meeting / GO-CAM guidelines for protein-containing complexes](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE)
- [Noctua VPE / New Causal Relations Decision Tree (2022-12-20)](https://drive.google.com/open?id=1ODFtV2aEeUeOUDs8dupre-3hUJchLFMMu-kChPKR1Oc)
- [2020 GO-CAM Jamboree / Regulation Notes](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)
- [2021-05 GOC / Contributes_to](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks)
- [2019-02 Hackathon / GO-CAM to GPAD and GPAD to GO-CAM](https://drive.google.com/open?id=1AgkJqA4-V0HG0SaDiNO9ENTxaQC_1HwsmwyhyHhuxog)
- [Standard annotations from triples and GO-CAM annotations specifications (draft)](https://drive.google.com/open?id=1UwTDxUslfXEgdn4flcz1oBNKILtz3-alX5O_bcLtgLk)
- [Standard annotation GO-CAM criteria notes](https://drive.google.com/open?id=1vmP4fqTl4Sc2AaCTI2OG3WuKYBBs5dhItiYC9yloees)
- [Evidence Unwinding Project / 2026-01-20 meeting](https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8)
- [Convention for Linking GO-CAMs (draft)](https://drive.google.com/open?id=1iXgErHVojMFtbteiquzfJw76kPPs851XRVC558VdtGI)
- [GO-CAM Modeling Agenda and Minutes, 2020-2022](https://drive.google.com/open?id=1rA1RiHst8e9tulY0zeua96WJSG2lKNS9VFWhDCWW2Ps)
- [Reactome2GO / Complex active units 2025-07 notes](https://drive.google.com/open?id=19GdhwjKWXGzkxBIL0eVxrdDvgzunW542DGkbD9W-1c8)
- [Reactome2GO / molecular binding cleanup notes](https://drive.google.com/open?id=1ns86kSOMZsL84SLFQ60Bobl3t-0WNDa59oAhhc-JLsI)
- [Reactome and Pathway Mapping / Conversion Rules for Manuscript](https://drive.google.com/open?id=1SEj8BCjKa6ZFp4xEhRlGvCAEhZjlq880)

**GO wiki**

- [Provides input for](https://wiki.geneontology.org/index.php/Provides_input_for)
- [Removes input for](https://wiki.geneontology.org/index.php/Removes_input_for)
- [Constitutively upstream of](https://wiki.geneontology.org/index.php/Constitutively_upstream_of)
- [Directly positively regulates](https://wiki.geneontology.org/index.php/Directly_positively_regulates)
- [Has input](https://wiki.geneontology.org/index.php/Has_input)
- [Causally upstream of or within](https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within)
- [Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19)
- [Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)

**GitHub issues**

- [go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979) (cGAS: enzyme versus regulator of the viral life cycle)
- [go-annotation#6085](https://github.com/geneontology/go-annotation/issues/6085) (IEA sources no longer allowed in Noctua)

**Papers cited in source examples** (as cited by the wiki pages; not re-read here)

- [PMID:23512198](https://europepmc.org/article/MED/23512198) (AKT1, RAC1 and FBXL19)
- [PMID:26493479](https://europepmc.org/article/MED/26493479) (ZDHHC9 and NRAS palmitoylation)
- [PMID:27338793](https://europepmc.org/article/MED/27338793) (TONSL reads H4K20me0)

**Repository pages**

- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- [gocam-curation skill](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/SKILL.md) and its references ([causal relations](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/causal-relations.md), [has input](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/has-input.md), [complexes](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/complexes.md), [compartments](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/compartments.md), [QC and consistency](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/qc-and-consistency.md))
- [GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)
- [gocam_lint](https://github.com/ai4curation/ai-gene-review/blob/main/docs/gocam_lint.md)
- [REACTOME](https://ai4curation.io/ai-gene-review/pages/projects/REACTOME.html)
- [EXECUTABLE_MODELS](https://ai4curation.io/ai-gene-review/pages/projects/EXECUTABLE_MODELS.html) (modules as the curated wiring that models are generated from)
- [PROTEIN_COMPLEX_FUNCTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html)
- [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)
- Cached models cited: `568b0f9600000284`, `632cf60a00000169`, `600ced8500002343`, `59cc772c00000000`, `63d320cd00001536`, `623d156d00000817`, `62b4ffe300002385` (under `gocams/`); `635b1e3e00001677` is cited from the wiki and is not in the local cache, and `6348a65d00001727` is cited by the wiki for an EGF-MAPK model but the cached model with that id has different content.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA) (undated, open comments) | Use "regulates" for known but non-direct control, with the mechanism named in the first `part of` BP. | Use the signed `indirectly positively/negatively regulates` (RO:0002407, RO:0002409); keep naming the mechanism in the BP (CAM-7, CAM-9). | The 2022 decision tree has no path to unsigned relations; reviewers of the guideline asked for signed children. |
| [gocam-curation causal-relations reference](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/causal-relations.md) (repo) | Lists `positively regulates` RO:0002213 / `negatively regulates` RO:0002212 as the indirect relations, alongside the explicit indirect ones. | Treat RO:0002213/RO:0002212 as legacy parents; new or corrected edges use RO:0002407/RO:0002409. | RO:0002213 is the parent of the direct relation, so it does not assert indirectness. |
| [Drive: Regulation Notes, 2020 Jamboree](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40) vs [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04) | The Jamboree notes allow a regulatory edge between two MFs of the same gene product (unfolded protein binding regulates kinase activity). The February 2020 call limits "directly regulates" to activities of different gene products. | One node with the compound MF for a single gene product; no causal edges between nodes of the same gene product to represent its internal switch (CAM-2, CAM-8). | Self-edges create spurious MF-regulator inferences and the `same_gene_chain` pattern. |
| [Drive: New Causal Relations Decision Tree](https://drive.google.com/open?id=1ODFtV2aEeUeOUDs8dupre-3hUJchLFMMu-kChPKR1Oc) | Gives `indirectly positively regulates` as "RO:00002407". | RO:0002407 (verified). | Typo in the deck; the extra digit makes an invalid CURIE. |
| [Drive: 2025 complexes deck](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE), Case 4 | Notes that listing inactive members as `has part` will export contributes_to, "should not be allowed but we have no way to identify these". | `has part` is limited to subunits that form the active unit; reviewers flag violations as `COMPLEX_SUBUNIT_REPRESENTATION`. | Closes the gap the deck identified, at the curation step rather than in software. |
| [Drive: Complex active units notes, 2025-07](https://drive.google.com/open?id=19GdhwjKWXGzkxBIL0eVxrdDvgzunW542DGkbD9W-1c8) | Asks why CASP3 is annotated to cysteine-type endopeptidase activity, calling it "a well-known aspartic-type endopeptidase". | Keep `GO:0004197` cysteine-type endopeptidase activity for caspases. | Caspases are cysteine proteases that cleave after aspartate; the aside confuses substrate specificity with catalytic class. |

## Open questions

1. **Complex context for a subunit's activity.** The 2025 deck proposes a relation stating that an activity is performed by a subunit while in a named complex (KAT8 in the MSL versus NSL complex). Until it exists, a subunit active in two complexes can only be modelled as two nodes differing in process. Should GO-CAM add `part of` (complex) on the activity, or a dedicated relation?
2. **Contributes_to export.** Case 2 export is not implemented. Until it is, emergent activities produce no MF rows. Should curators also make standard contributes_to annotations by hand in the meantime?
3. **Compound functions.** Nuclear receptors, receptor kinases and ligand-gated channels combine binding and a downstream activity. The 2020 call noted that their logical definitions were under review. Should these ever be split into sub-activities joined by `has part`, as the 2016 documentation allowed?
4. **Small-molecule regulators.** If GOC prefers the 2023 relation-page reading (direct edges for small-molecule effects), the binding inference attached to "directly" needs to be dropped. This needs a decision from the ontology and software groups together.
5. **Host and symbiont activities in one model.** Models such as `62b4ffe300002385` (Shigella OspC3 inactivating human CASP4) put activities of two organisms in one graph. The location chain can nest a host organism, but there is no agreed way to record the interacting taxon on exported rows ([MO-8](../MO/MO-8.md)).
6. **Standard versus GO-CAM models.** The evidence-unwinding project will bin "mixed" models. Should a model with one causal edge and many unconnected standard annotations be split?

<!-- END GENERATED -->
