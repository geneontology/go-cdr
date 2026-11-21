---
id: AE
title: Annotation extensions
record_kind: guideline
applies_to:
- contributing_group
status: proposed
differences:
- prior_source: 'Same page; [wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types)'
  prior_said: Example GO:0007242 "intracellular signaling cascade"; temporal example GO:0007067
  we_recommend: Both ids no longer resolve in the current GO build. Use current terms
  why: Examples went stale
- prior_source: '[wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during) (BP example)
    vs [Drive: Annotation Extension Relations - 2022-09-09](https://drive.google.com/open?id=13MOVlRD1_iBJyw7whO7lK0KTCaLW0dbbtcpgGOthKqA)
    (BP `happens_during`: N) and [Drive: SAE specs](https://drive.google.com/open?id=1mBzbiqey0fyFUhWtKE5UKvIPNvpJ2Kx1XNkPgCPorpc)
    (BP: Y)'
  prior_said: Sources disagree on whether BP may carry `happens_during`
  we_recommend: Allow it on MF. On BP, use it only for phases and stages and expect tooling differences
  why: The wiki's own example is BP; the 2022 table says no; the SAE allows it. GOC should decide
- prior_source: '[wiki: Annotation Extension field: Supplying temporal location information](https://wiki.geneontology.org/index.php/Annotation_Extension_field%3A_Supplying_temporal_location_information_to_a_GO_annotation)'
  prior_said: '`exists_during` for CC stage'
  we_recommend: '`existence_overlaps` / `existence_starts_and_ends_during`'
  why: '`exists_during` is not in RO ([wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during));
    the SAE uses the RO pair'
- prior_source: '[Drive: Annotation Extension Sept 2017](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk)
    and legacy rows'
  prior_said: '`has_regulation_target` allowed, "use something more specific"'
  we_recommend: Not for new annotations. `has_input` on the regulation term
  why: Ambiguous; imports already convert it; absent from the SAE
- prior_source: '[wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19)'
  prior_said: Replace `activated_by` with binding plus `directly_positively_regulates` in the extension
  we_recommend: Put the causal link in a GO-CAM
  why: Causal extensions flagged for removal (2022); chained and nested extensions to be archived (2026)
- prior_source: '[Drive: Harmonizing input/output relations (Fall 2024)](https://drive.google.com/open?id=1GUfrZgxeal3L99v3BCRs4yyrsq_D8yGwq8RwNuQ6OMs)
    vs [Drive: Review & update Noctua documentation](https://drive.google.com/open?id=13MWyxdfcS78dYz9hg61R4ZS4ydp3OY8Y16LAb3xD3Ug)'
  prior_said: Convert to `has_primary_input/output` vs keep `has_input/has_output` for now
  we_recommend: Capture only the primary participant, under either label
  why: The semantics agree even though the labels differ
- prior_source: '[wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)
    vs gorule-0000053 deprecation'
  prior_said: NOT forbidden with extensions vs "will not be implemented"
  we_recommend: No NOT with extensions
  why: See [qualifiers-and-negation.md](../QN/README.md#differences-from-prior-guidance)
- prior_source: '[wiki: Column 16](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions)'
  prior_said: Add a "redundant" bare annotation "sometimes"
  we_recommend: Always add the bare BP row for an MF `part_of`(BP), and the CC row for an MF `occurs_in`(CC)
  why: '"Sometimes" gave no test. Users who ignore column 16 lose information otherwise'
- prior_source: '[wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types)'
  prior_said: Use the cell-type ontology for context
  we_recommend: Also prefer `occurs_in` fillers that resolve to one compartment (nuclear chromosome, not
    chromatin)
  why: Repo analysis of GO-CAMs found chromatin locations that reach no compartment ([GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html))
- prior_source: '[go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204)'
  prior_said: Proposal to make cell population proliferation do-not-annotate
  we_recommend: Allowed with a required extension
  why: The thread's own outcome; restated as a general rule for readout terms
- prior_source: None (gap)
  prior_said: No guidance on reviewing extensions
  we_recommend: Action table ([AE-14](AE-14.md)) and the cache caveat ([AE-13](AE-13.md))
  why: Reviewers working from the repo's GOA cache cannot see extensions
open_questions:
- '**`happens_during` on BP.** The wiki, the 2022 relation review and the SAE disagree.'
- '**Causal relations in extensions.** The SAE still allows `causally_upstream_of...` and `regulates`
  on BP and MF extensions, while the 2022 review asked whether to remove them. Will standard annotations
  lose them in the 2026 data-store split?'
- '**`has_agent` replacement.** Cell-cell adhesion annotations used `has_agent` for the cell type ([go-annotation#2047](https://github.com/geneontology/go-annotation/issues/2047);
  [wiki: Ontology meeting 2020-08-24](https://wiki.geneontology.org/index.php/Ontology_meeting_2020-08-24)).
  No replacement has been agreed.'
- '**Which terms require an extension?** gorule-0000051 exists, but the list of terms it covers is not
  in our sources.'
- '**Primary input labels.** Will GO move existing standard annotations to `has_primary_input` and `has_primary_output`,
  and should reviews then rewrite predicates?'
- '**ChEBI fillers.** The 2020 decision to post-compose chemical binding raised concerns about curators
  navigating ChEBI. Is a curated ChEBI subset for annotation tools still planned?'
date: '2026-11-15'
---

# Annotation extensions: GO annotation guidelines


**In brief:**

- An extension narrows the GO term. "Term plus extension" must name a subclass of the term, and the annotation must stay true if the extension is deleted. Extensions do not express conditions, negation or causal chains.
- Use only a small set of relations: `has_input` / `has_output` for the specific molecular target or product, `occurs_in` for where an MF or BP happens, `part_of` for the process an MF serves or the cell a CC sits in, `happens_during` for a phase or life stage, and the `results_in_...` family for developmental processes. Do not use `has_regulation_target`, `occurs_at`, `has_direct_input`, `activated_by`, `independent_of` or chained relations in new annotations.
- An extension that restates the term is noise. Do not add `has_input` hexose to hexokinase activity, `occurs_in` T cell to T cell receptor signaling, or `part_of` phosphorylation to kinase activity.
- `part_of(Y)` is not a home for a retired "X involved in Y" term. If GO obsoleted the precomposition and asked for a GO-CAM, put Y in a model, the gene's core functions, or nowhere.
- A standard annotation is one line with one evidence and no nested or causal extensions. Anything that needs two linked activities is a GO-CAM.
- In this repository the cached GOA file has no extension column, so read the row's extension in QuickGO or GOA before calling it too general.

## Scope


This document covers annotation extensions on standard GO annotations: GAF column 16 and the GPAD 2.0 extension column, written as `relation(ID)` with comma for "and" and pipe for "or". It covers their purpose, the relations allowed for each aspect and the ontologies they draw on, the choice between an extension and a new precomposed term, how extensions relate to GO-CAM, how to review rows that carry them, and the history of the allowed-relation list.

Out of scope: the gene product-to-term relation in column 4 (see [qualifiers-and-negation.md](../QN/README.md)); relations between activities in GO-CAM (see [gocam-modeling.md](../CAM/README.md)); `with/from` usage (see [evidence-codes.md](../EV/README.md)); term-request policy in general (see [ontology-change-and-taxa.md](../ONT/README.md)).

## Principles


**Extensions are post-composition.** The GO cannot hold a term for every substrate, cell type or stage, so the annotation can build the class at curation time: "protein serine/threonine kinase activity *with input* MCM2" is a class nobody has to request. The 2014 description of extensions presents them as recording effector-target relationships (substrates, regulation targets, localisation dependencies) and spatial and temporal context ([PMID:24885854](https://europepmc.org/article/MED/24885854), "A method for increasing expressivity of Gene Ontology annotations using a compositional approach").

**The extension modifies the term, not the gene product.** The extension field extends the GO term in column 5 and does not extend the gene product ([Drive: Annotation Extension Sept 2017 (GOC Cambridge)](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk)). Because the term plus extension is a class, it can be "folded" into a named term later. When GO adds the precomposed term, the annotation maps forward without curator work ([wiki: Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions)). Any extension that cannot fold, because it states a condition or a negation, is malformed. That is why `independent_of` and `in_absence_of` were deprecated ([wiki: Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of)).

**Context is not exclusivity.** `occurs_in(CL:0000746 cardiac muscle cell)` says that in this experiment the activity was seen in cardiac muscle cells. It does not say the activity happens only there, and a missing extension does not say it happens everywhere ([wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types)).

**Standard annotations and GO-CAMs are separate data models.** As of 2026 GO is separating the two stores. A standard annotation has evidence cardinality 1, may carry independent (pipe) and dependent (comma) extensions, and has no nested extensions. Chained extensions such as `regulates_o_occurs_in` that cannot be flattened will be archived ([Drive: GO-CAMs and standard annotations in Noctua (Fall 2026 GOC)](https://drive.google.com/open?id=1CY1Py4e9jTSXDn_mircd-C3aVLHqNJ2x3BvH90EKFj8)). Extensions have become the contextual layer of a single statement, and mechanisms belong in models.

## The allowed relations


Ids were checked against RO with `runoak -i sqlite:obo:ro info`. "Allowed" reflects the Noctua Standard Annotation Editor (SAE) specification and the 2022 relation review ([Drive: SAE - Annotation Extension Relations specs](https://drive.google.com/open?id=1mBzbiqey0fyFUhWtKE5UKvIPNvpJ2Kx1XNkPgCPorpc); [Drive: Annotation Extension Relations - 2022-09-09](https://drive.google.com/open?id=13MOVlRD1_iBJyw7whO7lK0KTCaLW0dbbtcpgGOthKqA)), reconciled with the wiki relation pages.

| Relation | Id | On | Range (filler) | Use for |
|---|---|---|---|---|
| `has_input` | RO:0002233 | MF, BP | Gene/gene product id (UniProtKB, MOD, RNAcentral, PR), CHEBI chemical entity, GO:0032991 complex | The specific molecular target: enzyme substrate, binding partner, transcription factor target gene, the regulated gene product for a regulator activity |
| `has_output` | RO:0002234 | MF, BP | CHEBI, complex, gene product | The specific product of a reaction or process |
| `occurs_in` | BFO:0000066 | MF, BP | GO CC (GO:0110165 cellular anatomical structure), CL, UBERON, species anatomy (EMAPA, FBbt, WBbt, ZFA, PO...) | Where the activity or the whole process takes place |
| `part_of` | BFO:0000050 | MF | GO BP | The process an activity is a step in |
| `part_of` | BFO:0000050 | CC (not complexes) | CL, UBERON, species anatomy | The cell or tissue in which the component sits |
| `happens_during` | RO:0002092 | MF (BP: see Differences) | GO:0044848 biological phase descendants, UBERON:0000105 life cycle stage descendants, plant development stages | The phase or stage when the activity occurs |
| `existence_overlaps`, `existence_starts_and_ends_during` | RO:0002490, RO:0002491 | CC | GO BP, life stage | The stage or process during which a localisation is observed. Successors to the legacy `exists_during` |
| `results_in_development_of`, `..._formation_of`, `..._morphogenesis_of`, `..._maturation_of`, `..._growth_of` and siblings | e.g. RO:0002296 | BP | CL, UBERON, species anatomy | The structure a developmental process acts on |
| `transports_or_maintains_localization_of` | RO:0002313 | MF, BP | Gene product, complex, chemical | The cargo of a transport or localisation process |
| `has_target_start_location`, `has_target_end_location` | RO:0002338, RO:0002339 | MF, BP | GO CC, anatomy | Origin and destination of a transport |
| `acts_on_population_of` | RO:0012003 | BP | CL, organism | The population acted on, e.g. a cell type whose proliferation is controlled |
| `adjacent_to`, `overlaps` | — | CC | anatomy | Rare refinements of a location |

**Not for new annotations.**

| Relation | Status | Replace with |
|---|---|---|
| `occurs_at` | Deprecated 2019 ([go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584)) | `occurs_in` for GO CC or CL fillers; for SO motifs, a specific DNA-binding term with `has_input` the gene, or drop; drop Pfam fillers |
| `has_direct_input` | Merged into `has_input` (2020) ([wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04); [go-annotation#2076](https://github.com/geneontology/go-annotation/issues/2076)) | `has_input` |
| `activated_by`, `inhibited_by` | Retired 2019 ([wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19)) | A binding annotation for the regulator plus a causal link in GO-CAM; for a binding term, `has_input` the bound entity; drop it if the mechanism is unknown |
| `independent_of`, `in_absence_of` | Deprecated (hidden negation, does not fold) | Nothing |
| `has_regulation_target` | Legacy, ambiguous; GOC's own description calls it "very general" ([Drive: Annotation Extension Sept 2017](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk)); converted to `has_input` on import ([wiki: Noctua MOD Imports](https://wiki.geneontology.org/index.php/Noctua_MOD_Imports)); absent from the SAE list | `has_input` on the regulation term |
| `has_agent` | Under review since 2020; no replacement agreed ([wiki: Ontology meeting 2020-08-24](https://wiki.geneontology.org/index.php/Ontology_meeting_2020-08-24)) | `occurs_in` or `acts_on_population_of` where one fits; otherwise a GO-CAM |
| `regulates_o_occurs_in` and other chains | To be archived in the 2026 data-store split | A GO-CAM |
| Causal relations (`causally_upstream_of...`, `directly_positively_regulates`...) in extensions | Allowed by the SAE but flagged "Causal - can we remove from AE?" in the 2022 review; `causally_upstream_of_or_within` is never to be used directly ([wiki: Causally upstream of or within](https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within)) | A GO-CAM |

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [AE-1](AE-1.md) | An extension must narrow the term, so that the annotation stays true without it. Do not use extensions for conditions, negation or exclusivity. | proposed | [GOC] |
| [AE-2](AE-2.md) | Use comma for facts that hold together and pipe for independent statements. Make separate annotations for alternative substrates or targets. | proposed | [GOC] |
| [AE-3](AE-3.md) | Use `has_input` for the specific, physiologically relevant molecular target that the term does not already name: a substrate, a binding partner, a target gene, or the gene product a regulator acts on. | proposed | [GOC] |
| [AE-4](AE-4.md) | Use `has_output` only for a specific product the term does not already name, and only for a single reaction. | proposed | [GOC+] |
| [AE-5](AE-5.md) | Use `occurs_in` for the place where an MF happens, or where *every* step of a BP happens. Choose a location that places the activity unambiguously, and do not restate the term. | proposed | [GOC+] |
| [AE-6](AE-6.md) | On CC annotations, use `part_of` with a cell or anatomy term for the cell or tissue in which the component sits, and an existence relation for the stage. | proposed | [GOC+] |
| [AE-7](AE-7.md) | Use `happens_during` only for a biological phase or life stage, never for a process that merely coincides. | proposed | [GOC] |
| [AE-8](AE-8.md) | Use `part_of`(BP) on an MF to say which process the activity serves. Make the matching BP annotation as a separate row, and do not add a `part_of` the ontology already entails. | proposed | [GOC] |
| [AE-9](AE-9.md) | Do not use `part_of(Y)` to rebuild a precomposed "X involved in Y" term that GO has obsoleted for GO-CAM. | proposed | [NEW] |
| [AE-10](AE-10.md) | Prefer an extension for target-, cell-type- and stage-specific context. Request a precomposed term only for a recognised biological concept that is not an arbitrary cross-product. | proposed | [GOC+] |
| [AE-11](AE-11.md) | Keep extensions to what a single statement can hold. Causal, chained or multi-activity knowledge goes in a GO-CAM. | proposed | [GOC+] |
| [AE-12](AE-12.md) | An extension needs the same evidence as the annotation. Do not expect or invent extensions on propagated rows. | proposed | [GOC] |
| [AE-13](AE-13.md) | Before judging a row, read its extension in QuickGO or GOA. The repository's cached GOA file does not include one. | proposed | [NEW] |
| [AE-14](AE-14.md) | When reviewing, judge an extension like the term: keep it if it holds, fix its relation if that is legacy, and remove it if it restates the term or encodes a condition. | proposed | [NEW] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


**Which relation?**

| You want to say... | Relation | Filler |
|---|---|---|
| The kinase phosphorylates protein P | `has_input` | UniProtKB id of P |
| The transporter moves chemical C | `has_input`, or `transports_or_maintains_localization_of` on a BP | CHEBI |
| The enzyme makes product M | `has_output` | CHEBI |
| The activity happens in the mitochondrion | `occurs_in` | GO CC |
| ...in cardiac muscle cells | `occurs_in` | CL |
| The process happens in a tissue (all steps) | `occurs_in` | UBERON / species anatomy |
| The protein sits in the nucleus of spermatocytes | `part_of` on the CC row | CL |
| The localisation is seen in interphase | `existence_overlaps` | GO BP / phase |
| The activity occurs in mitotic anaphase | `happens_during` | GO:0044848 descendant |
| The activity is a step in pathway P | `part_of` on the MF row, plus an `involved_in` P row | GO BP |
| A regulates B's activity | No extension. Use a GO-CAM | — |
| The process does not need X | No extension. Use nothing | — |

**Extension or term?** See the table in [AE-10](AE-10.md).

## Common errors


| Error | Example | Fix |
|---|---|---|
| Restating the term | GO:0004396 hexokinase activity `has_input` hexose | Drop the extension |
| Currency metabolite or cofactor as input | kinase `has_input` ATP; enzyme `has_input` Zn2+ | Drop it |
| Assay analogue as input | Artificial peptide substrate | Use the physiological substrate or none |
| `occurs_in` on a multi-compartment BP | Signalling pathway `occurs_in` nucleus | Move `occurs_in` to the MF row of the nuclear step |
| Cell type inferred from a cell line | HeLa experiment → `occurs_in` cervical epithelial cell | Drop it |
| `happens_during` a co-occurring process | X `happens_during` DNA repair | `part_of` if a step, otherwise drop |
| NOT with extension | NOT kinase activity `has_input` B | Drop the NOT row ([QN-12](../QN/QN-12.md)) |
| Retired precomposition re-encoded | protein targeting to lysosome `part_of` chaperone-mediated autophagy | `decomposed_into` ([AE-9](AE-9.md)) |
| Condition as extension | `independent_of`, `in_absence_of` | Judge the bare row |
| `has_input` on BP inferred from the MF | Expecting the BP "regulation of transcription" to inherit the MF's target | Add the input to the BP row explicitly |
| Errors in published examples | Wiki `occurs_in` example annotates ATP13A2 with `enables` on a BP and uses the now-obsolete CL:0002609; the LIG3 table shows UniProtKB:P23743 (DGKA) as the object | Use `involved_in` for BP. Check every example id before copying it |

## Reading list


**GO wiki**
- [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) (reviewed 2023-09-05)
- [wiki: Has input](https://wiki.geneontology.org/index.php/Has_input); [wiki: Has output](https://wiki.geneontology.org/index.php/Has_output); [wiki: Occurs in](https://wiki.geneontology.org/index.php/Occurs_in) (reviewed 2021-10-07); [wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during); [wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in)
- [wiki: Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions)
- [wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types)
- [wiki: Annotation Extension field: Supplying temporal location information](https://wiki.geneontology.org/index.php/Annotation_Extension_field%3A_Supplying_temporal_location_information_to_a_GO_annotation)
- [wiki: Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of) (deprecated)
- [wiki: Causally upstream of or within](https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within)
- [wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding) (proposal, 2020)
- [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to); [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)
- [wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19); [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)
- [wiki: Noctua MOD Imports](https://wiki.geneontology.org/index.php/Noctua_MOD_Imports); [wiki: Ontology meeting 2020-08-24](https://wiki.geneontology.org/index.php/Ontology_meeting_2020-08-24)

**GO Consortium Drive**
- [Drive: Use of relations for GO annotation - GP2term and extensions (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc)
- [Drive: SAE - Annotation Extension Relations specs](https://drive.google.com/open?id=1mBzbiqey0fyFUhWtKE5UKvIPNvpJ2Kx1XNkPgCPorpc)
- [Drive: Annotation Extension Relations - 2022-09-09](https://drive.google.com/open?id=13MOVlRD1_iBJyw7whO7lK0KTCaLW0dbbtcpgGOthKqA)
- [Drive: Annotation Extension Sept 2017 (GOC Cambridge)](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk)
- [Drive: GO-CAMs and standard annotations in Noctua (Fall 2026 GOC)](https://drive.google.com/open?id=1CY1Py4e9jTSXDn_mircd-C3aVLHqNJ2x3BvH90EKFj8)
- [Drive: Evidence unwinding meeting with curators (2026-01-20)](https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8)
- [Drive: Noctua Standard Annotations evidence splitting](https://drive.google.com/open?id=1p2pwOCovVbX61bQspUcptSt2pkA3OSzDHulOpQhZElQ)
- [Drive: Harmonizing use of input/output relations in GO (Fall 2024 GOC)](https://drive.google.com/open?id=1GUfrZgxeal3L99v3BCRs4yyrsq_D8yGwq8RwNuQ6OMs)
- [Drive: Review & update Noctua documentation](https://drive.google.com/open?id=13MWyxdfcS78dYz9hg61R4ZS4ydp3OY8Y16LAb3xD3Ug)
- [Drive: Feedback on GO rules (FlyBase copy)](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM)
- [Drive: MGI ISO rat filters](https://drive.google.com/open?id=1lx65V8ikyofnkDdwojm6fhHZ801ET1Z9)

**GitHub issues (geneontology/go-annotation)**
- [go-annotation#1487](https://github.com/geneontology/go-annotation/issues/1487) (GOC-OWL inferences from extensions)
- [go-annotation#2047](https://github.com/geneontology/go-annotation/issues/2047) (cell types for adhesion terms)
- [go-annotation#2076](https://github.com/geneontology/go-annotation/issues/2076) (has_input vs has_direct_input)
- [go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204) (cell population proliferation)
- [go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584) (occurs_at deprecation)

**Papers**
- [PMID:24885854](https://europepmc.org/article/MED/24885854) A method for increasing expressivity of Gene Ontology annotations using a compositional approach (2014)

**Repository**
- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) (decomposing precomposed terms; `decomposed_into`)
- [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html); [GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)
- Gene review cited: `genes/human/FXN` (GO:0008047 with `has_input` NFS1)
- Code: `src/ai_gene_review/etl/gene.py` (`fetch_goa_data` row collapse); `src/ai_gene_review/schema/gene_review.yaml` (`AnnotationExtension`, `ROTermEnum`)

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| Same page; [wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types) | Example GO:0007242 "intracellular signaling cascade"; temporal example GO:0007067 | Both ids no longer resolve in the current GO build. Use current terms | Examples went stale |
| [wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during) (BP example) vs [Drive: Annotation Extension Relations - 2022-09-09](https://drive.google.com/open?id=13MOVlRD1_iBJyw7whO7lK0KTCaLW0dbbtcpgGOthKqA) (BP `happens_during`: N) and [Drive: SAE specs](https://drive.google.com/open?id=1mBzbiqey0fyFUhWtKE5UKvIPNvpJ2Kx1XNkPgCPorpc) (BP: Y) | Sources disagree on whether BP may carry `happens_during` | Allow it on MF. On BP, use it only for phases and stages and expect tooling differences | The wiki's own example is BP; the 2022 table says no; the SAE allows it. GOC should decide |
| [wiki: Annotation Extension field: Supplying temporal location information](https://wiki.geneontology.org/index.php/Annotation_Extension_field%3A_Supplying_temporal_location_information_to_a_GO_annotation) | `exists_during` for CC stage | `existence_overlaps` / `existence_starts_and_ends_during` | `exists_during` is not in RO ([wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during)); the SAE uses the RO pair |
| [Drive: Annotation Extension Sept 2017](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk) and legacy rows | `has_regulation_target` allowed, "use something more specific" | Not for new annotations. `has_input` on the regulation term | Ambiguous; imports already convert it; absent from the SAE |
| [wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19) | Replace `activated_by` with binding plus `directly_positively_regulates` in the extension | Put the causal link in a GO-CAM | Causal extensions flagged for removal (2022); chained and nested extensions to be archived (2026) |
| [Drive: Harmonizing input/output relations (Fall 2024)](https://drive.google.com/open?id=1GUfrZgxeal3L99v3BCRs4yyrsq_D8yGwq8RwNuQ6OMs) vs [Drive: Review & update Noctua documentation](https://drive.google.com/open?id=13MWyxdfcS78dYz9hg61R4ZS4ydp3OY8Y16LAb3xD3Ug) | Convert to `has_primary_input/output` vs keep `has_input/has_output` for now | Capture only the primary participant, under either label | The semantics agree even though the labels differ |
| [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation) vs gorule-0000053 deprecation | NOT forbidden with extensions vs "will not be implemented" | No NOT with extensions | See [qualifiers-and-negation.md](../QN/README.md#differences-from-prior-guidance) |
| [wiki: Column 16](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions) | Add a "redundant" bare annotation "sometimes" | Always add the bare BP row for an MF `part_of`(BP), and the CC row for an MF `occurs_in`(CC) | "Sometimes" gave no test. Users who ignore column 16 lose information otherwise |
| [wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types) | Use the cell-type ontology for context | Also prefer `occurs_in` fillers that resolve to one compartment (nuclear chromosome, not chromatin) | Repo analysis of GO-CAMs found chromatin locations that reach no compartment ([GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)) |
| [go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204) | Proposal to make cell population proliferation do-not-annotate | Allowed with a required extension | The thread's own outcome; restated as a general rule for readout terms |
| None (gap) | No guidance on reviewing extensions | Action table ([AE-14](AE-14.md)) and the cache caveat ([AE-13](AE-13.md)) | Reviewers working from the repo's GOA cache cannot see extensions |

## Open questions

1. **`happens_during` on BP.** The wiki, the 2022 relation review and the SAE disagree.
2. **Causal relations in extensions.** The SAE still allows `causally_upstream_of...` and `regulates` on BP and MF extensions, while the 2022 review asked whether to remove them. Will standard annotations lose them in the 2026 data-store split?
3. **`has_agent` replacement.** Cell-cell adhesion annotations used `has_agent` for the cell type ([go-annotation#2047](https://github.com/geneontology/go-annotation/issues/2047); [wiki: Ontology meeting 2020-08-24](https://wiki.geneontology.org/index.php/Ontology_meeting_2020-08-24)). No replacement has been agreed.
4. **Which terms require an extension?** gorule-0000051 exists, but the list of terms it covers is not in our sources.
5. **Primary input labels.** Will GO move existing standard annotations to `has_primary_input` and `has_primary_output`, and should reviews then rewrite predicates?
6. **ChEBI fillers.** The 2020 decision to post-compose chemical binding raised concerns about curators navigating ChEBI. Is a curated ChEBI subset for annotation tools still planned?

<!-- END GENERATED -->
