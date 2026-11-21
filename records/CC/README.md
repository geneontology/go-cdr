---
id: CC
title: Cellular component
record_kind: guideline
applies_to:
- contributing_group
status: proposed
aspects:
- C
differences:
- prior_source: Old GO annotation conventions page (quoted in the 2017-05-09 call)
  prior_said: Transient or peripheral association to an organelle or complex may use `colocalizes_with`
  we_recommend: Never on complexes; for organelles use `is_active_in` if it acts there
  why: '[#1940](https://github.com/geneontology/go-annotation/issues/1940), [#1500](https://github.com/geneontology/go-annotation/issues/1500)'
- prior_source: '[2022-08-23 call](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-08-23)'
  prior_said: Extrinsic component terms to be obsoleted with "consider" parent
  we_recommend: Do not use them for new annotations; prefer side-of-membrane terms (CC-9, CC-10)
  why: The terms are still live in the current release; the obsoletion appears unfinished
- prior_source: No GOC policy
  prior_said: Organelle granularity unaddressed
  we_recommend: Root organelle terms are informative; synthesis rows are red flags; add sub-compartments,
    do not substitute (CC-6 to CC-8)
  why: Repo survey of ~3,000 mitochondrion rows ([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html))
open_questions:
- '**Nucleus, series organelles and plastids.** CC-6 to CC-8 cover five organelles. Should `GO:0005634`
  nucleus rows be refined to nucleoplasm or chromatin as eagerly as the mitochondrion is refined to matrix?
  Is the maturation stage of endosomes and autophagosomes the analogue of the sub-compartment?'
- '**Extrinsic component terms.** Announced for obsoletion in 2022, still live. GOC should finish or withdraw
  the obsoletion.'
- '**Main versus additional location.** HPA distinguishes them; GO cannot. An extension or flag would
  let users filter.'
- '**Ligands in the receiving cell.** Is a membrane-bound ligand (ZP3, Delta) annotated to a location
  in the cell it signals to? Raised in 2017, never answered; we have no rule.'
- '**Condensate class.** GO has no term for "biomolecular condensate" that excludes ribosome and cytoskeleton
  and includes the phagophore assembly site.'
date: '2026-11-15'
---

# Cellular component: GO annotation guidelines


**In brief:**

- A cellular component (CC) annotation says where a gene product is. `located_in` is the
  default; `is_active_in` is a stronger claim that needs evidence the molecular function
  happens there; `part_of` is only for protein-containing complexes. Do not use
  `colocalizes_with`.
- Annotate residence, not transit. A secreted or plasma-membrane protein passing through the
  ER and Golgi does not get ER or Golgi rows unless the protein is retained or acts there.
- A root organelle term (mitochondrion, ER, Golgi, peroxisome, lysosome) is informative and is
  never `TOO_GENERAL`. When two independent lines of evidence agree on the sub-compartment,
  add the sub-compartment beside the root; do not replace the root.
- Membrane topology is no longer encoded by "integral" terms. Use the membrane term, and the
  side-of-membrane terms only when the leaflet is known. Correct a generic plasma-membrane row
  when it misleads about which side the protein is on.
- High-throughput localization (Human Protein Atlas, organelle proteomics, GFP screens) and
  overexpression data support `located_in` at the resolution of the assay, no more. Being
  in a condensate is a location; building one is a function.

## Scope


This document covers gene-product-to-CC annotations in standard GO annotation (GAF/GPAD) and
their review: the four CC relations, organelle and sub-compartment terms, transit versus
residence, membrane topology, extracellular and cell-surface terms, condensates, nucleus and
cytoplasm defaults, localization evidence from overexpression and high-throughput assays, and
locations in another organism. Membership of protein-containing complexes is covered in
[protein-complexes.md](../PC/README.md). The `occurs_in` extension and GO-CAM
compartments are covered in [annotation-extensions.md](../AE/README.md) and
[gocam-modeling.md](../CAM/README.md); evidence codes in general in
[evidence-codes.md](../EV/README.md).

## Principles


1. **A CC annotation is a claim about a place, and the relation states how strong the claim
   is.** The 2017 Cambridge GOC session asked what a CC annotation means and listed four
   cases: known active there, plausibly active there, known not active there (sequestration,
   transit), and unknown
   ([Drive: GOC 2017-10 Cellular_Component_Annotations](https://drive.google.com/open?id=19QGQd6Ps0xQssV6LBPgPwVHNhuDmXFPgFDGjPRehUkM)).
   GAF 2.2 answered with two relations: `located_in` (detected there) and `is_active_in` (enables
   its function there). We hold curators to that split.
2. **Annotate to the precision of the evidence, and review to the precision of the biology.**
   A row records what its source could resolve. A review asks whether the gene, as a whole,
   is described as precisely as the combined evidence allows, and adds rows where it is not.
3. **Location is not function.** A protein seen in a stress granule, an exosome or the nucleus
   has a location. Whether it does anything there is a separate question for MF and BP.
4. **Topology is a fact about the protein; GO CC terms describe places.** GO dropped "integral
   component" terms because they described proteins rather than locations
   ([wiki: Membrane proteins](https://wiki.geneontology.org/index.php/Membrane_proteins)).
   The side-of-membrane terms survive because a leaflet is a place.

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [CC-1](CC-1.md) | Use `located_in` by default, `is_active_in` only when the activity is shown at that location, and `part_of` only for complex terms. | proposed | [GOC] |
| [CC-2](CC-2.md) | Do not make new `colocalizes_with` annotations; resolve existing ones to `located_in`, `is_active_in`, a binding term, or removal. | proposed | [GOC+] |
| [CC-3](CC-3.md) | Treat an `is_active_in` row from IBA, a root-term ND, or a pipeline default as no stronger than `located_in` until the activity location is checked. | proposed | [NEW] |
| [CC-4](CC-4.md) | Annotate residence, not transit. | proposed | [GOC+] |
| [CC-5](CC-5.md) | Record sequestration and regulated relocation with `located_in`; reserve `is_active_in` for the compartment where the protein works. | proposed | [GOC+] |
| [CC-6](CC-6.md) | A root organelle term is informative: never `TOO_GENERAL`, and never `MODIFY` it to a sub-compartment. | proposed | [NEW] |
| [CC-7](CC-7.md) | Examine every root organelle row that comes from synthesis (IBA, ISS, ISO, IEA, IC, RCA); keep it only if the organelle claim survives the check. | proposed | [NEW] |
| [CC-8](CC-8.md) | Add the sub-compartment as a separate row when at least two independent lines agree; do not substitute it for the root. | proposed | [NEW] |
| [CC-9](CC-9.md) | A soluble protein stably tethered to an organelle by a named integral partner gets the cytoplasmic-side term; brief or regulated recruitment stays at the root. | proposed | [NEW] |
| [CC-10](CC-10.md) | Do not encode membrane topology with "integral" or "anchored" terms; use the membrane term, refine generic `membrane`, and use side terms only when the leaflet is known. | proposed | [GOC+] |
| [CC-11](CC-11.md) | When a generic plasma-membrane row misleads about which side the protein is on, or whether it is in the plasma membrane at all, `MODIFY` it; otherwise accept it at its own resolution and add the specific term as a `NEW` row. | proposed | [NEW] |
| [CC-12](CC-12.md) | Annotate secreted proteins to `GO:0005576` extracellular region (or a specific extracellular structure), never to `GO:0005615`; use cell surface for proteins held on the outer face. | proposed | [GOC+] |
| [CC-13](CC-13.md) | Localization from overexpression, tagging or mutants supports a CC row only when a marker resolves the compartment and the protein is wild type. | proposed | [NEW] |
| [CC-14](CC-14.md) | High-throughput localization supports `located_in` at the assay's resolution; weigh the source's grade, and treat "additional" locations as non-core by default. | proposed | [NEW] |
| [CC-15](CC-15.md) | Annotate presence in a condensate as a location; claim condensate formation only with condensate-grade evidence, and never infer a localization process from co-localization. | proposed | [GOC+] |
| [CC-16](CC-16.md) | Prefer `GO:0005829` cytosol to `GO:0005737` cytoplasm, and refine `GO:0005634` nucleus to its interior structures when the evidence allows; keep the nucleus row when the refinement is chromatin. | proposed | [GOC+] |
| [CC-17](CC-17.md) | Do not propagate a location across paralogs that live in different compartments. | proposed | [GOC] |
| [CC-18](CC-18.md) | A gene product acting in another organism is annotated to that organism's compartment; a host protein co-opted by a pathogen keeps its own. | proposed | [GOC] |
| [CC-19](CC-19.md) | In `core_functions`, name the location where the core activity is shown to happen, not every well-supported location. | proposed | [NEW] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


**Relation for a single CC observation**

| What the evidence shows | Relation | Typical action in review |
|---|---|---|
| Detected there (IF, fractionation, proteomics) | `located_in` | ACCEPT or KEEP_AS_NON_CORE |
| Activity measured there, or function requires that compartment | `is_active_in` | ACCEPT; candidate core location |
| Stable member of a protein-containing complex | `part_of` | see [protein-complexes.md](../PC/README.md) |
| Binds a complex but is not a member | MF `GO:0044877` or child, not CC | MODIFY a `part_of` or `located_in` row |
| Transient, peripheral, low resolution | not `colocalizes_with`; pick one of the above | resolve per CC-2 |

**Root organelle row**

1. Is the organelle claim true for this gene? No: `MARK_AS_OVER_ANNOTATED` or `REMOVE`.
2. Direct assay that cannot resolve further? `ACCEPT` / `KEEP_AS_NON_CORE`.
3. Synthesis row? Check the source (CC-7), then `ACCEPT` / `KEEP_AS_NON_CORE` with the check in
   `reason`.
4. Does the gene lack a sub-compartment row, with two agreeing lines? Add a `NEW` row (CC-8).
5. Soluble, tethered by a named integral partner, cytosolic synthesis? Add the cytoplasmic-side
   term (CC-9).

**Organelle row on a protein that acts elsewhere**

| Pool | Example | Action |
|---|---|---|
| Biosynthetic transit only | ATP1A1 Golgi | MARK_AS_OVER_ANNOTATED |
| Overexpression or mutant retention only | CABP2 Golgi | MARK_AS_OVER_ANNOTATED |
| Endogenous, marker-confirmed minor pool | ABCA1 Golgi | KEEP_AS_NON_CORE |
| Regulated retrograde or recycling pool | ADRB2 Golgi | KEEP_AS_NON_CORE |
| Sequestration (inactive reservoir) | DAF-16 cytoplasm | `located_in`, KEEP_AS_NON_CORE |
| Signalling from that compartment shown | endosomal GPCR | `is_active_in`, may be core |

**Plasma membrane row**

| Situation | Action |
|---|---|
| Inner-leaflet protein (KRAS, LYN, BTK) | MODIFY to `GO:0009898` |
| ER protein acting at ER-PM junctions (STIM1) | MODIFY to `GO:0140268` |
| Generic `GO:0016020` and the membrane is known | MODIFY to the specific membrane |
| Several sources stop at PM; subdomain known from other evidence | ACCEPT at own resolution, add NEW subdomain row |
| Ligand bound to its receptor on the surface | `GO:0009986` cell surface |

## Common errors


| Pattern | Example | Fix |
|---|---|---|
| Secretory-pathway rows on secreted or surface proteins | ATP1A1 ISS Golgi; mainly perinuclear overexpression calls | CC-4: MARK_AS_OVER_ANNOTATED unless direct evidence of a resident pool |
| `TOO_GENERAL` or MODIFY on a root organelle row | early drafts of the repo's matrix pilot MODIFYed IBA mitochondrion rows | CC-6: keep the root; add the sub-compartment |
| Sub-compartment substituted for the root, splitting actions on one term | PR #5208 first version | CC-8: add, do not substitute |
| IBA `is_active_in` accepted as an activity claim | ADO, BRAF mitochondrion IBA | CC-3: judge as `located_in` |
| Paralog-seeded CC IBD | CEPT1 Golgi (CHPT1 seeds); AlaRS mitochondrion in fly | CC-17 |
| Plain plasma membrane on inner-leaflet proteins | KRAS, LYN, JAKs | CC-11: MODIFY to `GO:0009898` |
| ER protein annotated to plasma membrane | STIM1 SOCE IDA rows | CC-11: MODIFY to `GO:0140268` |
| Topology terms requested or proposed | "integral component of plasma membrane" in a `NEW` row | CC-10: obsolete; use the membrane term |
| Reviewer-authored `GO:0005615` | `NEW` extracellular space rows | CC-12: use `GO:0005576` |
| HPA citation on an MF or BP row | PEX19 `NEW` peroxisome membrane biogenesis citing `GO_REF:0000052` | CC-14: HPA supports CC only |
| Stress-granule co-localization turned into a localization process | GO:1903608 annotations | CC-15: `located_in GO:0010494` |
| Microsomal or crude mitochondrial fraction read as ER or mitochondrion | "mitochondrial" fraction without ER marker | CC-8: require markers |
| UniProt location item read with another item's evidence tag | AP3S2 Golgi read as by-similarity | CC-7: read the tag per item |
| Location under perturbation taken as native | BST2 TGN with Vpu | CC-13 |
| Chromatin row taken to imply nucleus in a model | SMAD1 activity in chromatin (GO-CAM `600ced8500002343`) | CC-16: keep nucleus, or use `GO:0000228` |
| Spilled contents annotated as extracellular | histones from lysed cells | CC-5 |

## Reading list


**GO wiki**
- [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- [Located in](https://wiki.geneontology.org/index.php/Located_in)
- [Is active in](https://wiki.geneontology.org/index.php/Is_active_in)
- [Part of relation](https://wiki.geneontology.org/index.php/Part_of_relation)
- [Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with)
- [Membrane proteins](https://wiki.geneontology.org/index.php/Membrane_proteins)
- [Transmembrane Proteins](https://wiki.geneontology.org/index.php/Transmembrane_Proteins) (out of date)
- [Annotation consistency : ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments)
- [Multi-species processes](https://wiki.geneontology.org/index.php/Multi-species_processes)
- [Annotations to Cell Fraction-type terms](https://wiki.geneontology.org/index.php/Annotations_to_Cell_Fraction-type_terms) (archived)
- [5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call); [7 April 2015 PAINT Conference Call](https://wiki.geneontology.org/index.php/7_April_2015_PAINT_Conference_Call)
- Annotation calls: [2017-05-09](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09), [2022-05-24](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-05-24), [2022-07-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-07-19), [2022-08-23](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-08-23), [2023-05-16](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-16), [2023-05-30](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-30), [2023-11-28](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-11-28)
- Manager calls: [2017-04-19](https://wiki.geneontology.org/index.php/Manager_Call_2017-04-19), [2020-11-04](https://wiki.geneontology.org/index.php/Manager_Call_2020-11-04)

**GO Drive (GOC-internal)**
- [Drive: Annotation guidelines/Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- [Drive: GOC 2017-10 Cambridge/Cellular_Component_Annotations](https://drive.google.com/open?id=19QGQd6Ps0xQssV6LBPgPwVHNhuDmXFPgFDGjPRehUkM) (2017 proposal)
- [Drive: GOC 2023-04 Padua/Reviewing colocalizes_with annotations](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o)
- [Drive: HTP working group initial discussion points](https://drive.google.com/open?id=1I2PiQ7ApuE5K5-FFUQ9rGH71D6tpS_ui) (legacy, frozen)

**GitHub issues (geneontology/go-annotation)**
- [#1226](https://github.com/geneontology/go-annotation/issues/1226) extracellular annotations from lysed cells
- [#1500](https://github.com/geneontology/go-annotation/issues/1500), [#1940](https://github.com/geneontology/go-annotation/issues/1940) `colocalizes_with` on complexes
- [#1507](https://github.com/geneontology/go-annotation/issues/1507) host proteins and viral processes
- [#2929](https://github.com/geneontology/go-annotation/issues/2929) TM proteins spanning compartments
- [#3595](https://github.com/geneontology/go-annotation/issues/3595) `located_in` versus `is_active_in`
- [#4573](https://github.com/geneontology/go-annotation/issues/4573) Golgi transit and keyword mappings
- [#5546](https://github.com/geneontology/go-annotation/issues/5546), [#5691](https://github.com/geneontology/go-annotation/issues/5691) CC and localization in PAINT
- [#5694](https://github.com/geneontology/go-annotation/issues/5694) extrinsic component versus cytoplasmic side
- [#6484](https://github.com/geneontology/go-annotation/issues/6484) protein localization to stress granule
- [#6525](https://github.com/geneontology/go-annotation/issues/6525) compartment is not an MF distinction

**Papers**
- [PMID:10802651](https://europepmc.org/article/MED/10802651) Ashburner et al. 2000, Gene Ontology: tool for the unification of biology (CC definition, as quoted in the 2017 GOC deck)

**Repository pages**
- [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html) (policy, ER and Golgi batches, tethering rule)
- [SURFACEOME](https://ai4curation.io/ai-gene-review/pages/projects/SURFACEOME.html) (plasma-membrane subdomain convention, cell surface)
- [HUMAN_PROTEIN_ATLAS](https://ai4curation.io/ai-gene-review/pages/projects/HUMAN_PROTEIN_ATLAS.html) and [HPA evidence re-evaluation](https://ai4curation.io/ai-gene-review/pages/projects/HUMAN_PROTEIN_ATLAS/hpa-evidence-reevaluation.html)
- [CONDENSATES](https://ai4curation.io/ai-gene-review/pages/projects/CONDENSATES.html); [STRESS_GRANULES](https://ai4curation.io/ai-gene-review/pages/projects/STRESS_GRANULES.html)
- [GOCAM_COMPARTMENTS](https://ai4curation.io/ai-gene-review/pages/projects/GOCAM_COMPARTMENTS.html)
- [PEROXISOME](https://ai4curation.io/ai-gene-review/pages/projects/PEROXISOME.html); [MITO_INTERACTOME](https://ai4curation.io/ai-gene-review/pages/projects/MITO_INTERACTOME.html); [ORGANELLE_LIFECYCLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLE_LIFECYCLES.html)
- [OMICS_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/OMICS_EVIDENCE.html); [BIOREASON_COMPARISON](https://ai4curation.io/ai-gene-review/pages/projects/BIOREASON_COMPARISON.html); [RADICAL_SAM](https://ai4curation.io/ai-gene-review/pages/projects/RADICAL_SAM.html)
- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) "Root organelle terms", "Correct but general terms are MODIFY"

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| Old GO annotation conventions page (quoted in the 2017-05-09 call) | Transient or peripheral association to an organelle or complex may use `colocalizes_with` | Never on complexes; for organelles use `is_active_in` if it acts there | [#1940](https://github.com/geneontology/go-annotation/issues/1940), [#1500](https://github.com/geneontology/go-annotation/issues/1500) |
| [2022-08-23 call](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-08-23) | Extrinsic component terms to be obsoleted with "consider" parent | Do not use them for new annotations; prefer side-of-membrane terms (CC-9, CC-10) | The terms are still live in the current release; the obsoletion appears unfinished |
| No GOC policy | Organelle granularity unaddressed | Root organelle terms are informative; synthesis rows are red flags; add sub-compartments, do not substitute (CC-6 to CC-8) | Repo survey of ~3,000 mitochondrion rows ([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)) |

## Open questions

1. **Nucleus, series organelles and plastids.** CC-6 to CC-8 cover five organelles. Should `GO:0005634` nucleus rows be refined to nucleoplasm or chromatin as eagerly as the mitochondrion is refined to matrix? Is the maturation stage of endosomes and autophagosomes the analogue of the sub-compartment?
2. **Extrinsic component terms.** Announced for obsoletion in 2022, still live. GOC should finish or withdraw the obsoletion.
3. **Main versus additional location.** HPA distinguishes them; GO cannot. An extension or flag would let users filter.
4. **Ligands in the receiving cell.** Is a membrane-bound ligand (ZP3, Delta) annotated to a location in the cell it signals to? Raised in 2017, never answered; we have no rule.
5. **Condensate class.** GO has no term for "biomolecular condensate" that excludes ribosome and cytoskeleton and includes the phagophore assembly site.

<!-- END GENERATED -->
