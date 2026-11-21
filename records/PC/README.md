---
id: PC
title: Protein complexes
record_kind: guideline
applies_to:
- contributing_group
status: proposed
aspects:
- C
- F
differences:
- prior_source: '[Drive: Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s)
    (2026, discussion)'
  prior_said: 'Open options: status quo, export no MF, or new active/accessory member relations'
  we_recommend: 'Adopt the active-member intent now in curation: list as parts only subunits meeting PC-6
    (PC-14)'
  why: Avoids waiting for RO relations while preventing wrong exports
- prior_source: '[OXPHOS](https://ai4curation.io/ai-gene-review/pages/projects/OXPHOS.html) bottom line'
  prior_said: '"non-catalytic subunits only contribute"'
  we_recommend: Only non-catalytic subunits in the mechanism contribute; others get own MF or none
  why: The OXPHOS phrasing reads as licensing `contributes_to` for every subunit, which is how NDUFS4
    and COX4I1 rows were accepted
- prior_source: Same proposal, assembled subunits
  prior_said: Assembled subunits may be re-annotated to `GO:0005515` protein binding or `GO:0030674`
  we_recommend: Not bare protein binding; a specific MF or nothing (PC-9, PC-12)
  why: Repo protein-binding policy removes bare `GO:0005515`
- prior_source: '[wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)'
  prior_said: Examples use `GO:0001055` RNA polymerase II activity and (in the editors' page) `GO:0004738`
    pyruvate dehydrogenase activity
  we_recommend: Read with live terms (`GO:0003899`); the examples need updating
  why: Both terms are obsolete in the current release
open_questions:
- '**SDHA and `GO:0000104`.** Is the flavoprotein''s isolated succinate oxidation (artificial acceptor)
  an activity of SDHA, to be annotated with `enables` the parent term, or a substep excluded by the complex
  II decision? The answer generalises to any subunit with a measurable partial reaction.'
- '**Active-member relations.** Will RO add `has active member` and `has accessory/structural member`
  so that GO-CAM exports MF only for active members? Until then, curators carry the distinction by hand.'
- '**Multi-activity complexes.** The ribosome and proteasome have several activities with different active
  members (peptidyl transferase by rRNA; protease by beta subunits; structural roles for others). A per-activity
  member list is needed; GO has no convention.'
- '**Supernumerary subunits with no term.** Many OXPHOS supernumerary subunits have no MF at all. Is "structural
  constituent of respiratory chain complex" (by analogy with `GO:0003735` and `GO:0140756`) wanted?'
- '**Unfinished obsoletions.** `GO:0051259`, `GO:0042803` and `GO:0046982` were slated for obsoletion
  or merger in 2019 and are still live. GOC should finish or withdraw.'
- '**Complex Portal evidence.** Should CP-derived subunit rows use IC with a GO_REF (as the IEA working
  group proposed) rather than NAS against a paper that may not mention the subunit?'
- '**Heteromeric channels of one family.** The 2020 deck asked whether `contributes_to` on heteromeric
  ion channel subunits says anything that `enables` on each subunit does not. No decision was recorded.'
date: '2026-11-15'
---

# Protein complexes: GO annotation guidelines


**In brief:**

- `part_of` a protein-containing complex needs evidence that the complex exists as a stable
  unit and that this gene product is in it: stringent co-purification, a structure of the
  assembled complex, or purification of a tagged subunit with the complex. A binary
  interaction is not membership.
- Membership is not function. The subunit that performs an activity `enables` it, even inside
  a complex. `contributes_to` is only for an irreducible molecular machine, and only for the
  subunits whose part is in the mechanism.
- Accessory, structural and regulatory subunits get their own molecular function (structural
  constituent, regulator, adaptor) or none. A subunit whose loss abolishes complex activity
  because the complex falls apart has shown necessity, not activity.
- Assembly factors get assembly processes and their own activity, never the mature complex's
  activity. Subunits are not annotated to the assembly of their own complex just because the
  complex fails to form without them.
- Oligomeric state is out of GO's scope. Homodimerization and oligomerization annotations
  record stoichiometry, not function, and are never core.

## Scope


This document covers how gene products are linked to protein-containing complexes in standard
GO annotation and review: complex membership (`part_of`), choice of complex term, binding to a
complex, molecular function of subunits (`enables` versus `contributes_to`), assembly factors,
homo- and hetero-oligomerization, Complex Portal-derived annotations, and how a review records
complex roles in `core_functions`. The modelling of complexes in GO-CAM is summarised in PC-14
and covered fully in [gocam-modeling.md](../CAM/README.md). The gp2term relations in general
are in [qualifiers-and-negation.md](../QN/README.md); binding terms in general in
[molecular-function.md](../MF/README.md); IPI and IDA in
[evidence-codes.md](../EV/README.md).

## Principles


1. **A complex is a place; an activity belongs to whatever performs it.** GO models a
   complex as a cellular component. Saying a gene product is part of the pyruvate
   dehydrogenase complex (`GO:0045254`) does not say which chemistry it does
   ([wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)).
2. **Users read an MF annotation as "this protein does this".** A list of gene products with
   "protein kinase activity" should not include regulatory subunits that cannot phosphorylate
   anything. The 2020 Complex Working Group made this the central argument: users querying by
   MF expect gene products that perform the activity, and had to consult other databases to
   find out which `contributes_to` subunits were catalytic
   ([Drive: GOC 2021-05 Contributes_to](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks)).
3. **Necessity is not participation.** Knockout of almost any subunit destroys a complex's
   activity. That shows the subunit is needed, which is true of structural parts, assembly
   factors and the substrate alike. Ask which entity performs the step (see the participation
   test in [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) "Do not add what curators deliberately declined to
   add").
4. **Keep the parts of a machine visible.** CC and BP annotations carry complex context to
   every member; MF annotations carry the division of labour. Flattening the second into the
   first teaches enrichment tools and ML models to predict membership rather than role
   ([PROTEIN_COMPLEX_FUNCTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html)).

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [PC-1](PC-1.md) | Annotate `part_of` a complex only with evidence that the complex exists as a stable unit and that this gene product is an intrinsic member. | proposed | [GOC+] |
| [PC-2](PC-2.md) | Use the most specific complex term that the evidence supports; treat bare `GO:0032991` protein-containing complex as a placeholder to refine; record the organelle separately. | proposed | [GOC+] |
| [PC-3](PC-3.md) | A gene product that binds a complex without being part of it gets `GO:0044877` protein-containing complex binding or a specific child, not `part_of` or `located_in` the complex. | proposed | [GOC] |
| [PC-4](PC-4.md) | Do not infer a molecular function from complex membership, co-purification or loss of complex activity on knockout. | proposed | [GOC+] |
| [PC-5](PC-5.md) | The subunit that performs the activity `enables` it, with no qualifier, even when it works inside a complex; homomultimers also `enable`. | proposed | [GOC] |
| [PC-6](PC-6.md) | Use `contributes_to` only when no single subunit has the activity and the activity is that of an irreducible molecular machine, and give it only to the subunits whose part is in the mechanism. | proposed | [GOC] |
| [PC-7](PC-7.md) | Accessory, structural and regulatory subunits get their own MF or none; do not give them `contributes_to` the complex's catalytic activity. | proposed | [GOC+] |
| [PC-8](PC-8.md) | Annotate subunits to the complex-level activity, not to its substeps; a subunit that catalyses a half-reaction on its own may `enable` the parent term. | proposed | [GOC+] |
| [PC-9](PC-9.md) | When the active subunit of a complex is not known, give no subunit the complex's MF; use CC membership and BP. | proposed | [GOC] |
| [PC-10](PC-10.md) | Assembly factors get assembly processes and their own activity; they are not `part_of` the mature complex and never receive its activity. | proposed | [GOC+] |
| [PC-11](PC-11.md) | Do not annotate a subunit to the assembly of its own complex because the complex fails to form without it; require evidence that it acts on the assembly of other parts. | proposed | [GOC+] |
| [PC-12](PC-12.md) | Treat oligomeric state as out of scope: do not propose oligomerization or homodimerization terms, and review existing ones by their evidence. | proposed | [GOC+] |
| [PC-13](PC-13.md) | Review Complex Portal-derived subunit rows as claims about the subunit; never propagate the complex's MF to its subunits. | proposed | [NEW] |
| [PC-14](PC-14.md) | In GO-CAM, use a complex as the enabler only for an emergent activity, list as `has_part` only the subunits that take part, and link subunits to complexes with `part_of`, never MF `occurs_in` a complex. | proposed | [GOC] |
| [PC-15](PC-15.md) | In a review's `core_functions`, state the attribution level: the subunit's own activity in `molecular_function`, the machine's activity in `contributes_to_molecular_function` only for direct participants. | proposed | [NEW] |
| [PC-16](PC-16.md) | Check propagated complex-activity rows (IBA, ISS, InterPro2GO) for transfer to non-catalytic subunits or paralogs. | proposed | [GOC+] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


**Which MF annotation does this complex subunit get?**

1. Is the activity known to be performed by this subunit alone (purified activity, active site
   in this chain, homomultimer of this chain)? → `enables` the activity. Stop.
2. Is the activity that of the complex as a whole, with no single subunit able to perform it
   (composite active site, compound reaction, coupled machine)?
   - No, or unknown which subunit → no MF from the complex; CC `part_of` and BP only (PC-9).
   - Yes → go to 3.
3. Does this subunit's own part sit in the mechanism (catalytic residues, cofactor or relay
   group, substrate or quinone site, rotor, stator, channel)?
   - Yes → `contributes_to` the complex activity, plus its own MF if a term exists.
   - No → its own regulator, adaptor or structural MF, or none (PC-7).
4. Is it present only during assembly or maturation? → assembly BP and own MF (PC-10); no
   complex MF.

**Common hard calls**

| Situation | Call |
|---|---|
| Knockout abolishes complex activity, subunit is supernumerary | no MF from the complex; assembly or stability BP only if the subunit acts on assembly (PC-4, PC-11) |
| Regulatory subunit of a kinase or phosphatase | `GO:0019887` or other regulator term with `has_input` |
| Substrate receptor of a cullin-RING ligase | `GO:1990756`; not `contributes_to` ligase activity |
| Translation factor that binds the ribosome | `GO:0043022`; not `part_of` ribosome |
| Assembly chaperone in a pre-assembly complex | `part_of` the intermediate term if GO has one; assembly BP with `has_output` |
| Two-hybrid hit with one subunit | binding MF (not bare protein binding); not `part_of` |
| Crystal structure shows a tetramer | no oligomerization annotation |
| Complex term exists only for the whole machine, protein is in a core subcomplex | `part_of` the whole complex term |

## Common errors


| Pattern | Example | Fix |
|---|---|---|
| Accessory subunit `enables` the complex activity on knockout evidence | NDUFS4 IMP `enables GO:0008137`, core MF `GO:0008137` | PC-4: MODIFY; core function to membership and assembly |
| Structural subunit carries the complex activity as core | UQCRC1 core `GO:0008121`; PSMA1 `contributes_to GO:0004298` | PC-7: structural MF as core; no `contributes_to` |
| Regulatory subunit `enables` the activity | COX4I1 TAS `enables GO:0004129` ACCEPTed | PC-7: regulator term; MODIFY the row |
| Assembly factor annotated to the mature activity | SURF1 IEA `GO:0004129` | PC-10: REMOVE |
| Subunit annotated to assembly of its own complex | exocyst Exo84 IBA exocyst assembly | PC-11 |
| `contributes_to` for every subunit of a complex with an identifiable catalytic subunit | HDAC complexes, E3 ligases, kinase complexes (2020 audit) | PC-5, PC-7 |
| Non-member annotated `part_of` the complex | elongation factor `part_of` cytosolic small ribosomal subunit | PC-3: complex binding |
| `colocalizes_with` a complex term | about 1,600 rows across groups in 2018 | PC-3; see [CC-2](../CC/CC-2.md) |
| Homodimerization from crystallography | oligomeric state read from a structure | PC-12: REMOVE |
| Complex activity propagated to non-catalytic paralogs | INO80 Arp subunits `contributes_to` helicase activity | PC-16 |
| Bare `GO:0032991` when the complex is known | IEA protein-containing complex | PC-2: MODIFY to the specific term |
| Complex row taken to imply the organelle | complex II without a mitochondrion row | PC-2 point 3 |
| CP-derived BP with the regulation sign reversed | BAK1, DFFB, CED-3 | PC-13 |
| Structured qualifier missing where prose argues `contributes_to` | SDHB, SDHD before PR #3223 | PC-6: MODIFY plus paired NEW `contributes_to` row |

## Reading list


**GO wiki**
- [Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes) (editors' page, reviewed 2023)
- [Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) (reviewed 2023)
- [Enables](https://wiki.geneontology.org/index.php/Enables)
- [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- [Part of relation](https://wiki.geneontology.org/index.php/Part_of_relation); [Located in](https://wiki.geneontology.org/index.php/Located_in)
- [Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)
- [Inferred from Direct Assay (IDA)](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29); [Inferred from Physical Interaction (IPI)](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29)
- [Ontology meeting 2024-01-29](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-29)

**GO Drive (GOC-internal)**
- [Drive: GOC 2021-05/Contributes_to](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks) (Complex Working Group, 2020)
- [Drive: GOC 2025-05/GO-CAM guidelines for protein-containing complexes](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE)
- [Drive: Protein Complexes/Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s) (GO-CAM call, 2026-01-27; discussion)
- [Drive: Annotation Reviews/Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo) (2019)
- [Drive: Ontology/Protein-binding announcement](https://drive.google.com/open?id=1CDLNsl-FgwqdsLP3jTfuA7h3nTdGq_ASEyYyLiTLhWE) (draft, status unclear)
- [Drive: Annotation guidelines/Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)

**GitHub issues (geneontology/go-annotation)**
- [#1487](https://github.com/geneontology/go-annotation/issues/1487) `contributes_to` on CC terms from inference pipelines
- [#1940](https://github.com/geneontology/go-annotation/issues/1940) no `colocalizes_with` on complexes
- [#2126](https://github.com/geneontology/go-annotation/issues/2126) Complex Portal IDs as subjects (2018)
- [#2149](https://github.com/geneontology/go-annotation/issues/2149), [#2213](https://github.com/geneontology/go-annotation/issues/2213), [#3002](https://github.com/geneontology/go-annotation/issues/3002) assembly terms on subunits
- [#2374](https://github.com/geneontology/go-annotation/issues/2374) INO80 Arp subunits and helicase activity
- [#2521](https://github.com/geneontology/go-annotation/issues/2521), [#2682](https://github.com/geneontology/go-annotation/issues/2682) oligomerization and homodimerization reviews
- [#2664](https://github.com/geneontology/go-annotation/issues/2664), [#3283](https://github.com/geneontology/go-annotation/issues/3283) catalytic versus non-catalytic subunits
- [#2760](https://github.com/geneontology/go-annotation/issues/2760) E3 adaptor subunits
- [#3242](https://github.com/geneontology/go-annotation/issues/3242), [#5254](https://github.com/geneontology/go-annotation/issues/5254) qualifiers in ISS and PAINT
- [#3510](https://github.com/geneontology/go-annotation/issues/3510) non-catalytic transporter subunits
- [#3616](https://github.com/geneontology/go-annotation/issues/3616) V-ATPase
- [#3865](https://github.com/geneontology/go-annotation/issues/3865) torsins and ATPase activators
- [#5574](https://github.com/geneontology/go-annotation/issues/5574) translation factor and the ribosome
- [#6310](https://github.com/geneontology/go-annotation/issues/6310) MF `occurs_in` complex
- [#6357](https://github.com/geneontology/go-annotation/issues/6357) SDHA consistency, substeps
- [#6414](https://github.com/geneontology/go-annotation/issues/6414) succinate dehydrogenase gp2term relations
- [#6466](https://github.com/geneontology/go-annotation/issues/6466) TOM complex subunits

**Repository pages**
- [PROTEIN_COMPLEX_FUNCTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html) (attribution framework, rubric, proteasome pilot)
- [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html)
- [COMPLEXPORTAL](https://ai4curation.io/ai-gene-review/pages/projects/COMPLEXPORTAL.html)
- [OXPHOS](https://ai4curation.io/ai-gene-review/pages/projects/OXPHOS.html); [HUMAN_BBSOME](https://ai4curation.io/ai-gene-review/pages/projects/HUMAN_BBSOME.html); [PEROXISOME](https://ai4curation.io/ai-gene-review/pages/projects/PEROXISOME.html)
- [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html); [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html); [COSCIENTIST](https://ai4curation.io/ai-gene-review/pages/projects/COSCIENTIST.html)
- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) (participation test, protein-binding policy, `COMPLEX_ACTIVITY_TRANSFER`)
- `src/ai_gene_review/schema/gene_review.yaml` (`CoreFunction.contributes_to_molecular_function`)

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s) (2026, discussion) | Open options: status quo, export no MF, or new active/accessory member relations | Adopt the active-member intent now in curation: list as parts only subunits meeting PC-6 (PC-14) | Avoids waiting for RO relations while preventing wrong exports |
| [OXPHOS](https://ai4curation.io/ai-gene-review/pages/projects/OXPHOS.html) bottom line | "non-catalytic subunits only contribute" | Only non-catalytic subunits in the mechanism contribute; others get own MF or none | The OXPHOS phrasing reads as licensing `contributes_to` for every subunit, which is how NDUFS4 and COX4I1 rows were accepted |
| Same proposal, assembled subunits | Assembled subunits may be re-annotated to `GO:0005515` protein binding or `GO:0030674` | Not bare protein binding; a specific MF or nothing (PC-9, PC-12) | Repo protein-binding policy removes bare `GO:0005515` |
| [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) | Examples use `GO:0001055` RNA polymerase II activity and (in the editors' page) `GO:0004738` pyruvate dehydrogenase activity | Read with live terms (`GO:0003899`); the examples need updating | Both terms are obsolete in the current release |

## Open questions

1. **SDHA and `GO:0000104`.** Is the flavoprotein's isolated succinate oxidation (artificial acceptor) an activity of SDHA, to be annotated with `enables` the parent term, or a substep excluded by the complex II decision? The answer generalises to any subunit with a measurable partial reaction.
2. **Active-member relations.** Will RO add `has active member` and `has accessory/structural member` so that GO-CAM exports MF only for active members? Until then, curators carry the distinction by hand.
3. **Multi-activity complexes.** The ribosome and proteasome have several activities with different active members (peptidyl transferase by rRNA; protease by beta subunits; structural roles for others). A per-activity member list is needed; GO has no convention.
4. **Supernumerary subunits with no term.** Many OXPHOS supernumerary subunits have no MF at all. Is "structural constituent of respiratory chain complex" (by analogy with `GO:0003735` and `GO:0140756`) wanted?
5. **Unfinished obsoletions.** `GO:0051259`, `GO:0042803` and `GO:0046982` were slated for obsoletion or merger in 2019 and are still live. GOC should finish or withdraw.
6. **Complex Portal evidence.** Should CP-derived subunit rows use IC with a GO_REF (as the IEA working group proposed) rather than NAS against a paper that may not mention the subunit?
7. **Heteromeric channels of one family.** The 2020 deck asked whether `contributes_to` on heteromeric ion channel subunits says anything that `enables` on each subunit does not. No decision was recorded.

<!-- END GENERATED -->
