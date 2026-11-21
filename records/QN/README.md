---
id: QN
title: Gene product-to-term relations and negation
record_kind: guideline
applies_to:
- contributing_group
status: proposed
differences:
- prior_source: '[wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
    vs [Drive: GP2term deck (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc),
    [Drive: GAF 2.2 migration (2021)](https://drive.google.com/open?id=1E9Fd38LPle2RcQgbJ9kzF3vjC81lMqSeFIQRUFPTxsE)
    and [Drive: Draft GAF 2.2 documentation](https://drive.google.com/open?id=1Jbpm1l5xjSabywE6ulIflujcESkdkQvlVI7bECgLbtw)'
  prior_said: 'Wiki: BP default is `acts_upstream_of_or_within`. Protein2GO and GOA: default `involved_in`.
    GAF 2.2 draft: each group chooses'
  we_recommend: Read an unqualified BP row as `acts_upstream_of_or_within`. Assert `involved_in` only
    with a nameable MF
  why: The sources conflict. Only the weakest relation is always true, and the GOA default inflates phenotype-based
    rows into participation claims
- prior_source: '[wiki: 5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)'
  prior_said: PAINT ignores seed relations; all IBA BP rows are `involved_in`
  we_recommend: Reviewers read an IBA `involved_in` no more strongly than its seeds
  why: Otherwise IBA turns `acts_upstream_of_or_within` seeds into participation claims
- prior_source: Repo schema `AnnotationQualifierEnum`
  prior_said: '`colocalizes_with` "weaker than located_in"; `acts_upstream_of` described as "upstream
    of or within"'
  we_recommend: RO definitions; `colocalizes_with` deprecated
  why: Schema text predates or misreads GO
- prior_source: '[wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)
    and [go-annotation#2326](https://github.com/geneontology/go-annotation/issues/2326) vs gorule-0000053
    status ([Drive: Feedback on GO rules](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM))'
  prior_said: 'Wiki: no NOT with extensions. Rule registry: the rule forbidding it is deprecated, "will
    not be implemented"'
  we_recommend: No NOT with extensions
  why: The wiki is newer (2026) and the safer reading. Hidden conditions inside negations do not fold
- prior_source: Old qualifier documentation, quoted in [go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237)
  prior_said: NOT may be used when a paper says "not found in the nucleus"
  we_recommend: Never for "not found in"
  why: Removed by GO in 2019; restated here because legacy rows of this kind persist
- prior_source: '[wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)'
  prior_said: No aspect distinction for NOT
  we_recommend: MF NOTs are the strongest. Process NOTs need a test of the process's work. IEP never supports
    a NOT
  why: 'Repo audit: process NOTs from expression nulls are the main misuse (169 IEP-only rows)'
- prior_source: '[wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)'
  prior_said: RNA polymerase II example uses GO:0001055
  we_recommend: Use a current term. GO:0001055 is now obsolete ("obsolete RNA polymerase II activity"
    in the local GO build)
  why: Example term obsoleted
- prior_source: '[go-annotation#2109](https://github.com/geneontology/go-annotation/issues/2109)'
  prior_said: IRD used to "block" propagation even when residue loss is known
  we_recommend: IKR when residues are lost, IRD only for divergence without residue evidence
  why: IKR carries the reason, and gorule-0000042 requires NOT on it
open_questions:
- '**BP default.** Should GOC make `acts_upstream_of_or_within` the export default for BP rows that carry
  no asserted relation, including GOA''s legacy rows and PAINT IBAs? That would make the files match the
  wiki.'
- '**Scoped negation.** The COQ8B case (no activity in trans, activity on one substrate) cannot be expressed:
  NOT with `has_input` is disallowed and no term carries the distinction. Should GO allow NOT with `has_input`
  for the narrow substrate case that [go-annotation#2326](https://github.com/geneontology/go-annotation/issues/2326)
  proposed, or create terms, or accept the gap?'
- '**gorule-0000053.** The rule registry and the wiki disagree on NOT with extensions. Which one governs
  pipelines?'
- '**NOT on specific binding children.** gorule-0000002 covers GO:0005515 and GO:0005488. Are children
  such as GO:0005544 calcium-dependent phospholipid binding in or out?'
- '**PAINT release behaviour.** Which propagation rule (2014 silent skip, or 2021 propagate-and-block)
  produces current IBA releases? Reviewers cannot tell from the row.'
- '**Repo schema.** The `AnnotationQualifierEnum` descriptions should be corrected to the RO definitions,
  and `colocalizes_with` marked deprecated. That is a schema change and needs its own PR.'
date: '2026-11-15'
---

# Gene product-to-term relations and negation: GO annotation guidelines


**In brief:**

- Every annotation has a relation. MF: `enables`, or `contributes_to` only for a subunit of an irreducible molecular machine. BP: `involved_in` only when the gene product's own activity is a step in the process; otherwise one of the `acts_upstream_of...` relations, with a direction wherever the data give one. CC: `located_in` for where the product was seen, `is_active_in` for where its activity was shown, `part_of` only for protein-containing complexes. Do not use `colocalizes_with` for new annotations.
- A wrong relation is a wrong claim, even when the term is right. When reviewing, correct the relation as a structured field. Do not fix it in prose, and do not remove the term.
- A NOT says the gene product lacks a property that a reader would otherwise expect it to have, and an experiment (or loss of key residues) tested for that property and found it absent. A negative or inconclusive result, "not required for", "not found in" and "expression unchanged" do not support a NOT.
- A NOT applies to the term and to every descendant of it. Put it on the most general term the evidence excludes and no higher, and never on an ancestor of a term the gene product positively has.
- A NOT carries no extension and is never made to binding. It needs a positive annotation in the same aspect (the ND root if nothing else is known).
- A NOT on a pseudoenzyme blocks the IBA and IEA rows that would otherwise reassert the lost activity. Removing those rows one review at a time does not.

## Scope


This document covers the relation slot of a standard GO annotation (GAF 2.2 column 4 and GPAD 2.0 relation column, the "gp2term relation" or "qualifier") and the negation flag that can accompany it (`NOT|<relation>`). It covers when to make a NOT annotation, how NOT annotations interact with the ontology and with phylogenetic propagation, and how reviewers should judge existing NOT rows and conflicting positive/NOT pairs.

Out of scope: the relations used *inside* annotation extensions and between GO-CAM activities (see [annotation-extensions.md](../AE/README.md) and [gocam-modeling.md](../CAM/README.md)); evidence codes (see [evidence-codes.md](../EV/README.md)), except where a code constrains the relation or the NOT; the choice between a process and its regulation (see [regulation-and-signaling.md](../RS/README.md)); complex membership as such (see [protein-complexes.md](../PC/README.md)); PAINT procedure beyond its NOT logic (see [phylogenetic-propagation.md](../PH/README.md)).

## Principles


**The relation is part of the claim.** "SDHB enables succinate dehydrogenase (quinone) activity" and "SDHB contributes to succinate dehydrogenase (quinone) activity" are different statements, and only the second is true. Enrichment tools can filter on the relation, and GO-CAM imports turn it into model structure. A relation that is right in the reviewer's prose but wrong in the file is wrong in every downstream use.

**Relations encode how much is known about mechanism.** `involved_in` claims that the gene product's molecular activity is a step in the process. `acts_upstream_of_or_within` claims only that perturbing the gene product affects the process. Most phenotype-derived process annotations support the second and not the first. Being explicit about this is the reason GAF 2.2 exists ([Drive: Draft GAF 2.2 documentation for gp2term relations](https://drive.google.com/open?id=1Jbpm1l5xjSabywE6ulIflujcESkdkQvlVI7bECgLbtw); see also [Drive: Legacy Annotations and New Qualifiers](https://drive.google.com/open?id=1VJx9mJMvWfUEVF9vCmwhDY2NwgvHsWf3tRgKFluZLa8)).

**GO is open-world, and NOT is the closed-world exception.** The absence of an annotation says nothing. A NOT annotation is the only way to state in GO that a property is absent, so it should be reserved for cases where that statement is both tested and useful: where a reader, a homology pipeline or a prediction method would otherwise assume the property is there ([wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation); [Drive: Response to "evaluate GO prediction methods" Q from Biostars 2023](https://drive.google.com/open?id=1EodZspmExNTEu8c9Gzs6wpUZ4RWwj3aMlmk3TyAc4Bs)).

**Positive claims propagate up and NOT claims propagate down.** A positive annotation to a term entails the same annotation to its `is_a` and `part_of` ancestors. A NOT annotation entails NOT to every descendant. Every scope rule for NOT follows from this asymmetry.

## The relation table


All relations are from the Relations Ontology (RO) or BFO. Ids were checked against RO with `runoak -i sqlite:obo:ro info`. "Default" is the relation GO rule gorule-0000061 applies when none is asserted. The defaults differ between sources; see [QN-3](QN-3.md) and the Differences table.

| Aspect | Relation (GAF 2.2 token) | Id | Use when | Minimum evidence |
|---|---|---|---|---|
| MF | `enables` (default) | RO:0002327 | The gene product itself carries out the activity, alone, as a homomer, or as the catalytic subunit of a complex | Any MF-capable evidence (IDA, IMP on activity, IKR for NOT, IBA, IEA, ISS...) |
| MF | `contributes_to` | RO:0002326 | The activity belongs to a complex and cannot be assigned to this subunit or to a smaller set of subunits that includes it | An assay of the complex plus a reason the subunit is part of the active unit (shared active site, required core subunit) |
| BP | `involved_in` | RO:0002331 | The gene product's MF is a step in the process (`part_of`) | Knowledge of the MF and of its place in the process; an MF annotation `part_of` the BP in the ontology also qualifies |
| BP | `acts_upstream_of_or_within` | RO:0002264 | Perturbation affects the process and the mechanism is unknown; direction unknown | IMP, IGI, phenotype-derived evidence |
| BP | `acts_upstream_of_or_within, positive effect` | RO:0004032 | As above; loss reduces the process (or gain increases it) | As above, with direction |
| BP | `acts_upstream_of_or_within, negative effect` | RO:0004033 | As above; loss increases the process | As above, with direction |
| BP | `acts_upstream_of` | RO:0002263 | Mechanism known; the activity occurs before the process, is not a step in it, and does not regulate it | Mechanistic evidence placing the activity outside the process |
| BP | `acts_upstream_of, positive effect` | RO:0004034 | As above, and required for the process to occur | As above |
| BP | `acts_upstream_of, negative effect` | RO:0004035 | As above, and it prevents or reduces the process | As above |
| CC | `located_in` (default for non-complex CC) | RO:0001025 | The product was detected in a cellular anatomical structure (GO:0110165) or virion component (GO:0044423) | IDA, HDA, ISS, IEA... |
| CC | `is_active_in` | RO:0002432 | The product carries out its MF in that structure (`enables` composed with `occurs_in`) | A localisation plus evidence that the activity occurs there |
| CC | `part_of` (default for complexes) | BFO:0000050 | The product is a subunit of a protein-containing complex (GO:0032991 and descendants) | IDA/IPI on complex composition, ISS, IBA... |
| CC | `colocalizes_with` | RO:0002325 | Deprecated. Not for new annotations | n/a |

Sources: [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) (reviewed 2023-09-05); [Drive: Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc); [Drive: Use of relations for GO annotation - GP2term and extensions (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc).

Any of these can be negated (`NOT|enables`, `NOT|involved_in`, `NOT|located_in`...).

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [QN-1](QN-1.md) | Every annotation must carry an explicit relation that matches its aspect and term type. | proposed | [GOC] |
| [QN-2](QN-2.md) | Use `contributes_to` only when no single subunit, or smaller subset of subunits, can be said to carry out the activity. Annotate every catalytic-core subunit this way, and no accessory subunit. | proposed | [GOC+] |
| [QN-3](QN-3.md) | Use `involved_in` only when the gene product's own activity is a step in the process. Use an `acts_upstream_of...` relation for every other causal link, and treat a BP row with no stated relation as `acts_upstream_of_or_within`. | proposed | [NEW] |
| [QN-4](QN-4.md) | Use `is_active_in` only when the evidence places the activity, not just the protein, in the location. Otherwise use `located_in`. | proposed | [GOC+] |
| [QN-5](QN-5.md) | Do not make new `colocalizes_with` annotations. When reviewing one, convert it to `is_active_in` or `located_in` if the evidence supports that, or remove it. | proposed | [GOC+] |
| [QN-6](QN-6.md) | Judge the relation together with the term. Positive annotations entail ancestors only through relations that carry up. | proposed | [GOC+] |
| [QN-7](QN-7.md) | When reviewing, correct a wrong relation as a structured relation change. Do not REMOVE a right term because its relation is wrong. | proposed | [NEW] |
| [QN-8](QN-8.md) | Make a NOT annotation only when an experiment tested for the property and found it absent, or when the key residues for it are lost (IKR), and only when a reader would otherwise expect the property. | proposed | [NEW] |
| [QN-9](QN-9.md) | A NOT negates the term and all its descendants. Place it on the most general term the evidence excludes, and never on an ancestor of a term the gene product positively has. | proposed | [GOC+] |
| [QN-10](QN-10.md) | A positive and a NOT annotation to the same term may coexist only when the literature genuinely conflicts or the claims concern different gene products (isoforms). The reviewer must reconcile each pair in writing and narrow the NOT where the conflict is only apparent. | proposed | [GOC+] |
| [QN-11](QN-11.md) | A NOT to a molecular function is the strongest use of the qualifier. A NOT to a process needs evidence that the gene product was unable to do the process's work. | proposed | [NEW] |
| [QN-12](QN-12.md) | Do not attach an annotation extension to a NOT annotation. | proposed | [GOC] |
| [QN-13](QN-13.md) | Do not make NOT annotations to binding terms. | proposed | [GOC+] |
| [QN-14](QN-14.md) | A NOT needs a positive annotation in the same aspect, the ND root if nothing else is known. A NOT row does not make an ND row stale. | proposed | [GOC+] |
| [QN-15](QN-15.md) | Use NOT to stop propagation of a lost activity, and know how PAINT treats NOT. | proposed | [GOC+] |
| [QN-16](QN-16.md) | Review an existing NOT row as a claim of absence: ACCEPT, MODIFY (narrow the term or fix the isoform), REMOVE or UNDECIDED. Do not mark it non-core, over-annotated or too general. | proposed | [NEW] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


**Picking a relation**

| Question | Yes | No |
|---|---|---|
| MF: does this subunit alone (or as a homomer) carry the activity? | `enables` | next |
| MF: is it part of an irreducible active core with the other subunits? | `contributes_to` (all core subunits) | Give the accessory subunit its own MF (adaptor, regulator), or no MF |
| BP: can you name the MF, and is it a step in the process? | `involved_in` | next |
| BP: does the gene regulate the process through a known MF? | `involved_in` "regulation of X" | next |
| BP: is the mechanism known and the activity outside the process? | `acts_upstream_of, positive/negative effect` | `acts_upstream_of_or_within, positive/negative effect` |
| CC: is the term a protein-containing complex? | `part_of` | next |
| CC: was the activity shown in the location? | `is_active_in` | `located_in` (or nothing, if only in transit) |

**Should this be a NOT?**

| Evidence | NOT? |
|---|---|
| Activity assay negative, with a reason to expect activity (family, domain, paralogue) | Yes, to the MF |
| Catalytic residues lost, shown on an alignment | Yes, IKR |
| Knockout has no phenotype for process P | No |
| Not detected in compartment C | No |
| Expression or abundance unchanged after stimulus S | No, never with IEP |
| Inactive on substrate B, active on substrate A | No NOT. Use the positive with `has_input`(A) |
| Isoform 2 lacks the activity of isoform 1 | Yes, NOT on isoform 2 with the isoform id |
| Does not bind partner Y | No (binding NOT filtered) |

## Common errors


| Error | How to recognise it | Fix |
|---|---|---|
| `enables` on a non-catalytic subunit for the complex's activity | Subunit is regulatory, scaffold or assembly factor (SURF1 with GO:0004129) | REMOVE, and give it its own MF, or `contributes_to` if it is in the core |
| `contributes_to` on every member of a large complex | Annotation lists peripheral or regulatory subunits | REMOVE from non-core subunits |
| `involved_in` from a mutant phenotype | IMP or IGI only, no MF known | MODIFY to `acts_upstream_of_or_within` with direction (relation-only pattern) |
| Direction relation stacked on a regulation term | `acts_upstream_of, positive effect` "positive regulation of X" | MODIFY to `involved_in` the regulation term |
| `is_active_in` a transit compartment | Secretory or plasma-membrane protein `is_active_in` ER or Golgi | MODIFY to `located_in`, or REMOVE per [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html) |
| `located_in` a complex | CC term below GO:0032991 | MODIFY relation to `part_of` |
| NOT from a negative result | "not required", "no phenotype" | REMOVE |
| NOT from IEP | Evidence IEP, term "response to..." | REMOVE |
| NOT on an ancestor of a positive term | Consistency warning (DNM1L NOT ER vs ER membrane) | MODIFY the NOT down to the excluded sibling |
| NOT with an extension | Column 16 non-empty on a NOT row | Remove the extension. If the NOT is then false, REMOVE it |
| Relation fixed only in prose | Review text argues for `contributes_to`, structured row still `enables` | MODIFY plus NEW relation-only row |
| Repo schema misreading | The `AnnotationQualifierEnum` description says `acts_upstream_of` is "acts upstream of or within" | Use the RO definitions in the table above. The enum text is wrong (see Open questions) |

## Reading list


**GO wiki**
- [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) (reviewed 2023-09-05)
- [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation) (reviewed 2026-03-29)
- [wiki: Enables](https://wiki.geneontology.org/index.php/Enables); [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to); [wiki: Involved in](https://wiki.geneontology.org/index.php/Involved_in); [wiki: Acts upstream of](https://wiki.geneontology.org/index.php/Acts_upstream_of); [wiki: Acts upstream of or within](https://wiki.geneontology.org/index.php/Acts_upstream_of_or_within); [wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in); [wiki: Located in](https://wiki.geneontology.org/index.php/Located_in); [wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with)
- [wiki: ND evidence code](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code)
- [wiki: Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of) (deprecated)
- [wiki: 11 MAR 2014 PAINT Conference Call](https://wiki.geneontology.org/index.php/11_MAR_2014_PAINT_Conference_Call); [wiki: 16 December 2014 PAINT Conference Call](https://wiki.geneontology.org/index.php/16_December_2014_PAINT_Conference_Call); [wiki: 5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call); [wiki: 31 Aug 2021 PAINT Conference Call](https://wiki.geneontology.org/index.php/31_Aug_2021_PAINT_Conference_Call)

**GO Consortium Drive**
- [Drive: Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- [Drive: Use of relations for GO annotation - GP2term and extensions (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc)
- [Drive: Draft GOC GAF 2.2 documentation for gp2term relations](https://drive.google.com/open?id=1Jbpm1l5xjSabywE6ulIflujcESkdkQvlVI7bECgLbtw) (draft); [Drive: Heuristics for gp2term relations](https://drive.google.com/open?id=1GSLdTrBVdSyaWU4R0L3M0Y-rrNRW22aoYFBh_nwAwC0); [Drive: Legacy Annotations and New Qualifiers](https://drive.google.com/open?id=1VJx9mJMvWfUEVF9vCmwhDY2NwgvHsWf3tRgKFluZLa8)
- [Drive: Contributes_to (GOC 2021)](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks)
- [Drive: Response to "evaluate GO prediction methods" Q from Biostars 2023](https://drive.google.com/open?id=1EodZspmExNTEu8c9Gzs6wpUZ4RWwj3aMlmk3TyAc4Bs) (draft reply)
- [Drive: March 2021 migration to GAF2.2 and GPAD2.0](https://drive.google.com/open?id=1E9Fd38LPle2RcQgbJ9kzF3vjC81lMqSeFIQRUFPTxsE)
- [Drive: Review NOT annotation in PAINT (2022 GOC meeting)](https://drive.google.com/open?id=1Db0k2fuFzWYNoiHVGamYlJuhPm3bAku0)
- [Drive: Reviewing colocalizes_with annotations (2023 Padua breakout)](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o)
- [Drive: Feedback on GO rules (FlyBase copy)](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM)
- [Drive: GO rules (2024-05 GOC meeting)](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)

**GitHub issues (geneontology/go-annotation)**
- [go-annotation#3](https://github.com/geneontology/go-annotation/issues/3) (use of NOT, 2003)
- [go-annotation#1761](https://github.com/geneontology/go-annotation/issues/1761) (POLA1 NOT scope)
- [go-annotation#2109](https://github.com/geneontology/go-annotation/issues/2109) (IKR vs IRD)
- [go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237) (NOT documentation)
- [go-annotation#2326](https://github.com/geneontology/go-annotation/issues/2326) (NOT with extensions)
- [go-annotation#2377](https://github.com/geneontology/go-annotation/issues/2377) (BP qualifiers)
- [go-annotation#6414](https://github.com/geneontology/go-annotation/issues/6414) (SDH `contributes_to`)

**Repository**
- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) (participation test for NEW, isoform and negation tracking, ND policy, IBA reading)
- [NOT_ANNOTATION_USAGE](https://ai4curation.io/ai-gene-review/pages/projects/NOT_ANNOTATION_USAGE.html); [TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html); [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html); [ISOFORMS](https://ai4curation.io/ai-gene-review/pages/projects/ISOFORMS.html); [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html); [NO_DATA](https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html); [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html); [PAINT](https://ai4curation.io/ai-gene-review/pages/projects/PAINT.html); [NAKED_MOLE_RAT](https://ai4curation.io/ai-gene-review/pages/projects/NAKED_MOLE_RAT.html)
- [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)
- Gene reviews cited: `genes/human/COQ8B`, `genes/human/FGFR4`

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) vs [Drive: GP2term deck (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc), [Drive: GAF 2.2 migration (2021)](https://drive.google.com/open?id=1E9Fd38LPle2RcQgbJ9kzF3vjC81lMqSeFIQRUFPTxsE) and [Drive: Draft GAF 2.2 documentation](https://drive.google.com/open?id=1Jbpm1l5xjSabywE6ulIflujcESkdkQvlVI7bECgLbtw) | Wiki: BP default is `acts_upstream_of_or_within`. Protein2GO and GOA: default `involved_in`. GAF 2.2 draft: each group chooses | Read an unqualified BP row as `acts_upstream_of_or_within`. Assert `involved_in` only with a nameable MF | The sources conflict. Only the weakest relation is always true, and the GOA default inflates phenotype-based rows into participation claims |
| [wiki: 5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call) | PAINT ignores seed relations; all IBA BP rows are `involved_in` | Reviewers read an IBA `involved_in` no more strongly than its seeds | Otherwise IBA turns `acts_upstream_of_or_within` seeds into participation claims |
| Repo schema `AnnotationQualifierEnum` | `colocalizes_with` "weaker than located_in"; `acts_upstream_of` described as "upstream of or within" | RO definitions; `colocalizes_with` deprecated | Schema text predates or misreads GO |
| [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation) and [go-annotation#2326](https://github.com/geneontology/go-annotation/issues/2326) vs gorule-0000053 status ([Drive: Feedback on GO rules](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM)) | Wiki: no NOT with extensions. Rule registry: the rule forbidding it is deprecated, "will not be implemented" | No NOT with extensions | The wiki is newer (2026) and the safer reading. Hidden conditions inside negations do not fold |
| Old qualifier documentation, quoted in [go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237) | NOT may be used when a paper says "not found in the nucleus" | Never for "not found in" | Removed by GO in 2019; restated here because legacy rows of this kind persist |
| [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation) | No aspect distinction for NOT | MF NOTs are the strongest. Process NOTs need a test of the process's work. IEP never supports a NOT | Repo audit: process NOTs from expression nulls are the main misuse (169 IEP-only rows) |
| [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) | RNA polymerase II example uses GO:0001055 | Use a current term. GO:0001055 is now obsolete ("obsolete RNA polymerase II activity" in the local GO build) | Example term obsoleted |
| [go-annotation#2109](https://github.com/geneontology/go-annotation/issues/2109) | IRD used to "block" propagation even when residue loss is known | IKR when residues are lost, IRD only for divergence without residue evidence | IKR carries the reason, and gorule-0000042 requires NOT on it |

## Open questions

1. **BP default.** Should GOC make `acts_upstream_of_or_within` the export default for BP rows that carry no asserted relation, including GOA's legacy rows and PAINT IBAs? That would make the files match the wiki.
2. **Scoped negation.** The COQ8B case (no activity in trans, activity on one substrate) cannot be expressed: NOT with `has_input` is disallowed and no term carries the distinction. Should GO allow NOT with `has_input` for the narrow substrate case that [go-annotation#2326](https://github.com/geneontology/go-annotation/issues/2326) proposed, or create terms, or accept the gap?
3. **gorule-0000053.** The rule registry and the wiki disagree on NOT with extensions. Which one governs pipelines?
4. **NOT on specific binding children.** gorule-0000002 covers GO:0005515 and GO:0005488. Are children such as GO:0005544 calcium-dependent phospholipid binding in or out?
5. **PAINT release behaviour.** Which propagation rule (2014 silent skip, or 2021 propagate-and-block) produces current IBA releases? Reviewers cannot tell from the row.
6. **Repo schema.** The `AnnotationQualifierEnum` descriptions should be corrected to the RO definitions, and `colocalizes_with` marked deprecated. That is a schema change and needs its own PR.

<!-- END GENERATED -->
