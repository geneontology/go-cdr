---
id: ONT
title: Ontology change and taxon scope
record_kind: guideline
applies_to:
- contributing_group
status: proposed
differences:
- prior_source: '[wiki: Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18)'
  prior_said: Proposed that automated replacement makes per-annotation review unnecessary for `replaced_by`
  we_recommend: Agree for the bulk of electronic rows; curated rows in a review still get a check
  why: A one-term redirect cannot serve a term whose annotations fell into distinct classes
- prior_source: '[wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)'
  prior_said: Use `binding` + `has_input` ChEBI instead of new chemical binding terms; criteria for binding
    terms left for future work
  we_recommend: Same; existing chemical binding terms remain usable
  why: The 2020 decision left the criteria open; we do not resolve them here
- prior_source: '[VESICLE_TETHERING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/VESICLE_TETHERING_OBSOLETION.html)
    (upstream recommendation relayed) vs [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)'
  prior_said: GO recommends the new MF with a `part_of` extension to the transport BP; the repository's
    review schema dropped its extension slot because MF + `part_of(Y)` restates the retired class
  we_recommend: In GAF/GPAD, follow GO and use the extension; in this repository's review records, carry
    Y by reference to a module, GO-CAM or core function
  why: The two sources answer different questions (annotation format vs review record); flagged as an
    open question
- prior_source: '[Drive: Changes to viral processes 2017](https://drive.google.com/open?id=1TO6RuYf8C1ANLVQp_mr1bkn_9I_CLtu18KIrPHHgVdE)
    vs the 2015 viral ontology paper'
  prior_said: '2015: viral process terms are agnostic between host and virus; 2017: proposed constraints
    so viral processes are only viral and host processes only host'
  we_recommend: Not resolved here; see [multi-organism-and-ncrna.md](../MO/README.md)
  why: The sources conflict and the 2021 proposal allows only "only in Viruses" for viral-only terms
open_questions:
- Should GO forbid cross-aspect `replaced_by` in its editor documentation and add a QC check, as the May
  2026 call suggested might be needed?
- Should every `replaced_by` be validated against the obsolete term's former parents (a redirect outside
  the old branch would be flagged for review)?
- In GAF/GPAD, is an MF with a `part_of` BP extension the endorsed replacement for obsoleted tethering,
  docking and similar process terms, given GO's broader move to retire precomposed "X involved in Y" content?
  How should a review record that pattern?
- GO has no general holdase chaperone term since `GO:0051082` was obsoleted. Should `GO:0140309` be redefined
  to match its label, or a new parent created?
- Should taxon constraints on pathway terms named after one receptor subfamily (TGF-beta, JAK-STAT) be
  resolved by renaming and regrouping the terms, by constraints, or both?
- Should TreeGrafter apply GO taxon constraints before grafting unreviewed proteins onto PAINT nodes?
- When a constraint is applied without a prerequisite re-parenting (the `GO:0007260` case), who tracks
  the inherited conflict?
- Should the GOC publish which release each service (QuickGO, AmiGO, OLS, the PURL) is serving, so that
  curators can cite term state reproducibly?
date: '2026-11-15'
---

# Ontology change and taxon scope: GO annotation guidelines


**In brief:**

- A GO term means its definition and its place in the graph, not its label. A relabel is not
  a redefinition; read the definition and parents before using, migrating or arguing about a term.
- `replaced_by` claims the two terms mean the same thing and is applied mechanically. Check
  that it stays in the right branch and fits your gene before accepting it. `consider` is
  advice; every annotation needs its own decision.
- An obsoletion does not repoint annotations, and a wrong annotation is not a reason to
  obsolete a term. Requests to the ontology and corrections to annotation records go to
  different places.
- Request a new term only when real evidence for a real gene needs it and no existing term,
  composition or GO-CAM pattern can carry it. Never request precomposed "X involved in Y",
  chemical-specific binding, assay or taxon-named terms.
- A missing term is an ontology gap, not a knowledge gap. Record it as a proposed term or a
  question, not as a biological unknown.
- Taxon constraints say where a term can apply. A non-experimental annotation that violates
  one is removed and its source fixed; an experimental one is examined, because the constraint
  may be too narrow.

## Scope


This document covers how curators live with a GO that changes under them: obsoletions and
how annotations should move, merges, relabelling and redefinition, proposals for new terms
and for obsoletion, the separation between ontology gaps and knowledge gaps, and the taxon
scope of terms (`only_in_taxon`, `never_in_taxon`, lineage-specific terms and pathways that
presuppose a component some lineages lack).

It is written for annotating curators and reviewers, not for ontology editors. The editor
procedures (Protégé deprecation, notification email, xref clean-up) are referenced where they
determine what a curator will see. How to review an annotation set generally is in
[reviewing-annotations.md](../REV/README.md); how phylogenetic propagation places
and loses functions is in [phylogenetic-propagation.md](../PH/README.md);
multi-organism terms and their taxon handling are in
[multi-organism-and-ncrna.md](../MO/README.md).

## Principles


**An identifier is bound to a meaning.** GO keeps every identifier it has issued; removed
terms are deprecated, not deleted. A new meaning needs a new identifier even if the label
stays, and a reworded definition with the same meaning keeps its identifier
([wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion)).
Everything below follows from taking that seriously in both directions.

**Ontology change is cheap for editors and expensive for annotators.** One obsoletion can
touch thousands of rows, mostly electronic copies of a few seeds. The GOC's own policy asks
editors to be conservative for this reason
([wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion)).
The corresponding duty for curators is to migrate deliberately rather than accept every
automated redirect.

**Term state is a fact with a date.** Different GO services run different releases, and a
term can be live in one and obsolete in another on the same day. A claim that a term is
obsolete, merged or childless is only as good as the release and the service it was read from.

**Taxon constraints are evolutionary statements.** `only_in` says a feature arose on a branch;
`never_in` says it was lost on one. Treated that way, a constraint is a hypothesis that one
annotation can test, not an administrative block
([Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)).

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [ONT-1](ONT-1.md) | Read the definition and the parents, not the label | proposed | [GOC] |
| [ONT-2](ONT-2.md) | Establish a term's state against a named release, from two independent services | proposed | [NEW] |
| [ONT-3](ONT-3.md) | Treat `replaced_by` as a mechanical redirect that you must check | proposed | [GOC+] |
| [ONT-4](ONT-4.md) | Treat `consider` as a list of options and triage annotations by mechanism | proposed | [GOC] |
| [ONT-5](ONT-5.md) | A replacement in another aspect is a `consider`, never a `replaced_by` | proposed | [GOC+] |
| [ONT-6](ONT-6.md) | When nothing replaces the term, put the content on what the gene does, or on its partner | proposed | [GOC+] |
| [ONT-7](ONT-7.md) | Migrate an obsolete term in a review with `MODIFY`, everywhere it occurs | proposed | [NEW] |
| [ONT-8](ONT-8.md) | Merges are now obsoletions with `replaced_by`; read old secondary ids accordingly | proposed | [GOC] |
| [ONT-9](ONT-9.md) | Fix a wrong annotation at its source; fix a wrong term in the ontology; do not confuse the two | proposed | [GOC] |
| [ONT-10](ONT-10.md) | Track upstream changes as inbound work, and argue disagreement in writing | proposed | [NEW] |
| [ONT-11](ONT-11.md) | Request a new term only when real evidence for a real gene needs it | proposed | [GOC+] |
| [ONT-12](ONT-12.md) | Do not request terms that GO has decided not to have | proposed | [GOC+] |
| [ONT-13](ONT-13.md) | In a review, propose a missing term with an NTR placeholder, never an ill-fitting id | proposed | [NEW] |
| [ONT-14](ONT-14.md) | An ontology gap is not a knowledge gap | proposed | [NEW] |
| [ONT-15](ONT-15.md) | Propose an obsoletion only for a term whose meaning is broken, with a remapping for every curated row | proposed | [GOC+] |
| [ONT-16](ONT-16.md) | Know what a taxon constraint says and how it propagates | proposed | [GOC] |
| [ONT-17](ONT-17.md) | When an annotation violates a constraint, decide which of the two is wrong | proposed | [GOC+] |
| [ONT-18](ONT-18.md) | A pathway named for a component does not exist where the component is absent | proposed | [GOC+] |
| [ONT-19](ONT-19.md) | Propose a taxon constraint only with evidence of absence and a measured payoff | proposed | [NEW] |
| [ONT-20](ONT-20.md) | Do not annotate new rows to flagged terms, and read existing rows on them as review prompts | proposed | [GOC] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


**An annotation sits on an obsolete term.**

| Situation | Action in a review | Upstream |
|---|---|---|
| `replaced_by` exists, target in the right branch, fits this gene | `MODIFY` to the target | none |
| `replaced_by` exists but leaves the branch or misfits this gene | `MODIFY` to the correct term | flag the redirect ([ONT-3](ONT-3.md)) |
| Only `consider` targets | Triage by mechanism; `MODIFY` per class ([ONT-4](ONT-4.md)) | report errors in the remapping table |
| Target is in another aspect | `MODIFY` with a curator-chosen MF/BP and relation ([ONT-5](ONT-5.md)) | none |
| No replacement; content is something done to the gene | `REMOVE`; check the partner carries it ([ONT-6](ONT-6.md)) | none |
| No term fits the real activity | `MODIFY` to `NTR`, add a proposal ([ONT-13](ONT-13.md)) | term request |
| The row was wrong before the obsoletion | `REMOVE` | source defect to the `assigned_by` group ([ONT-9](ONT-9.md)) |

**An annotation violates a taxon constraint.**

| Evidence | Does the organism plausibly have the function? | Action |
|---|---|---|
| IEA / IBA / ISS / ISO | No | `REMOVE`; source defect at node, mapping or projection |
| IEA / IBA / ISS / ISO | Yes, with evidence | Keep; propose correcting the constraint |
| Experimental | No | `REMOVE` (term choice is wrong); source defect to the curator |
| Experimental | Yes | Keep; propose correcting the constraint |
| Any | The term presupposes a missing component | `MODIFY` to the generic sibling ([ONT-18](ONT-18.md)) |

**Should I request a term?**

1. Is there gene-specific evidence that would support the annotation? If not, stop.
2. Did you walk the branch (parents, siblings, children), not just a text search? If not, do.
3. Can an existing term plus an extension, or a GO-CAM pattern, express it? If yes, use that.
4. Is it in a class in [ONT-12](ONT-12.md)? If yes, use the alternative.
5. Can you write genus-differentia with a verified parent? If yes, request it with the contents
   in [ONT-11](ONT-11.md).

## Common errors


| Error | Example | Fix |
|---|---|---|
| Reading scope from a new label | `GO:0140309` applied to crystallins after its relabel | Read the definition ([ONT-1](ONT-1.md)) |
| Trusting one service's obsolescence answer | Term written off as obsolete on a QuickGO lookup, later reversed | Two independent services, dated ([ONT-2](ONT-2.md)) |
| Accepting a mechanical redirect | Asn-tRNA transamidase moved to L-asparagine biosynthesis | Check branch and fit ([ONT-3](ONT-3.md)) |
| Blanket remap of a `consider` term | Every NLS-binding row moved to carrier activity, including masking proteins and nucleoporins | Triage by mechanism ([ONT-4](ONT-4.md)) |
| Using a CC as the MF replacement | `GO:0099023` vesicle tethering complex as the tethering MF | Use `GO:7770062` ([ONT-5](ONT-5.md)) |
| `ACCEPT` on an obsolete term | Core MF still on an obsoleted binding term | `MODIFY`; update core functions ([ONT-7](ONT-7.md)) |
| Rewriting a GOA term id to pass validation | Obsolete id in `existing_annotations` replaced in place | Keep the id; act in the review |
| Requesting a precomposed term | "BMP signaling involved in cardiac cell differentiation" | Annotate the parts; GO-CAM ([ONT-12](ONT-12.md)) |
| Ill-fitting id in a core function | Obsolete unfolded protein binding kept as the holdase core MF | NTR proposal ([ONT-13](ONT-13.md)) |
| Filing an ontology gap as a knowledge gap | "No GO term for X" as a biology gap | `proposed_new_terms` or a question ([ONT-14](ONT-14.md)) |
| Deleting experimental rows to satisfy a constraint | Plant GLR3.3 channel activity removed as "Metazoa only" | Check whether the constraint is too narrow ([ONT-17](ONT-17.md)) |
| Keeping a component-presupposing pathway | Worm STAT annotated to JAK-STAT signaling | Generic sibling or `REMOVE` ([ONT-18](ONT-18.md)) |
| Stale page status | Audit says terms are live after GO retired them | Record and re-check `ontology_state_verified` ([ONT-10](ONT-10.md)) |

## Reading list


**GO wiki**

- [wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion)
- [wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term) (edited 2026-08)
- [wiki: Restoring an Obsolete Ontology Term](https://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term) (last reviewed 2019)
- [wiki: Manager 09Feb11](https://wiki.geneontology.org/index.php/Manager_09Feb11)
- [wiki: Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18) (merge SOP)
- [wiki: Annotation Conf. Call 2024-03-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12) (do-not-annotate, obsoletion_candidate)
- [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04) (binding + has_input)
- [wiki: Ontology meeting 2024-01-22](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-22)
- [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) (flagged for review)
- [wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
- [wiki: Species-Specific Terms](https://wiki.geneontology.org/index.php/Species-Specific_Terms) (2018 copy of a website page)
- [wiki: Adding, Editing, Deleting Taxon Restrictions](https://wiki.geneontology.org/index.php/Adding%2C_Editing%2C_Deleting_Taxon_Restrictions) (reviewed 2026-10)
- [wiki: GAF Taxonomy Reasoning](https://wiki.geneontology.org/index.php/GAF_Taxonomy_Reasoning) (old implementation; rules still apply)

**GO Consortium Drive**

- [Drive: GOC 2021-05 / Taxon constraints](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c) (proposal)
- [Drive: GOC 2023-04 / Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)
- [Drive: GOC 2017-06 / Changes to viral processes](https://drive.google.com/open?id=1TO6RuYf8C1ANLVQp_mr1bkn_9I_CLtu18KIrPHHgVdE)
- [Drive: Call Recordings / Ontology Developers 2026-05-11](https://drive.google.com/open?id=1LgDHGlk1SEX5fZ0DugEfs_YLPlMxvWmV) (unresolved discussion)
- [Drive: GOC 2022-04 / Automated Ontology Term Updates in Noctua](https://drive.google.com/open?id=1QrKtMLMjBFoUaceh5UJX5IP_EtqMEx9igsqj_73DrFQ)
- [Drive: GOC 2018-10 / PAINT Pipeline Update](https://drive.google.com/open?id=1HqVWDk-B99U5DA5udeTJqnmbJstOVRI5aQTZ3H9alpo)
- [Drive: GOC 2024-05 / GO rules](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)
- [Drive: Annotation Reviews / Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo)

**GitHub issues and files (geneontology/go-annotation)**

- [go-annotation#1452](https://github.com/geneontology/go-annotation/issues/1452) (obsolete ids in slims)
- [go-annotation#2521](https://github.com/geneontology/go-annotation/issues/2521) (oligomerization out of scope)
- [go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)

**Repository pages**

- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) (term-id validation, proposed terms, knowledge gaps, precomposed terms)
- [ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)
- [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)
- Obsoletion projects sampled: [VESICLE_TETHERING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/VESICLE_TETHERING_OBSOLETION.html),
  [AMINO_ACID_ACTIVATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/AMINO_ACID_ACTIVATION_OBSOLETION.html),
  [NLS_BINDING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/NLS_BINDING_OBSOLETION.html),
  [MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.html),
  [CALCITRIOL_BIOSYNTHESIS_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/CALCITRIOL_BIOSYNTHESIS_OBSOLETION.html),
  [CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.html),
  [COPII_VESICLE_COATING_REGULATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/COPII_VESICLE_COATING_REGULATION_OBSOLETION.html),
  [SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION.html),
  [NEURAL_CREST_FORMATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/NEURAL_CREST_FORMATION_OBSOLETION.html),
  [ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION.html),
  [ICAM3_RECEPTOR_ACTIVITY_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/ICAM3_RECEPTOR_ACTIVITY_OBSOLETION.html),
  [ENTNER_DOUDOROFF_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/ENTNER_DOUDOROFF_OBSOLETION.html)
- [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)
- [UNFOLDED_PROTEIN_BINDING](https://ai4curation.io/ai-gene-review/pages/projects/UNFOLDED_PROTEIN_BINDING.html)
- [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)
- [TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)
- [RAR_MISANNOTATION](https://ai4curation.io/ai-gene-review/pages/projects/RAR_MISANNOTATION.html)
- [MODULE_TAXON_AUDIT](https://ai4curation.io/ai-gene-review/pages/projects/MODULE_TAXON_AUDIT.html) (taxonomic envelope criteria for modules)

GO term ids and labels were checked against the local `sqlite:obo:go` build (2026-11-03).
That build predates some changes described here: it still lists `GO:0140355` and
`GO:0061753` as live, and gives `GO:0046425` its pre-November 2026 label "regulation of
receptor signaling pathway via JAK-STAT" (GO has since inserted "cell surface"). Parentage
claims for `GO:0140309` and `GO:0070127` were checked with `runoak ancestors`.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18) | Proposed that automated replacement makes per-annotation review unnecessary for `replaced_by` | Agree for the bulk of electronic rows; curated rows in a review still get a check | A one-term redirect cannot serve a term whose annotations fell into distinct classes |
| [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04) | Use `binding` + `has_input` ChEBI instead of new chemical binding terms; criteria for binding terms left for future work | Same; existing chemical binding terms remain usable | The 2020 decision left the criteria open; we do not resolve them here |
| [VESICLE_TETHERING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/VESICLE_TETHERING_OBSOLETION.html) (upstream recommendation relayed) vs [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html) | GO recommends the new MF with a `part_of` extension to the transport BP; the repository's review schema dropped its extension slot because MF + `part_of(Y)` restates the retired class | In GAF/GPAD, follow GO and use the extension; in this repository's review records, carry Y by reference to a module, GO-CAM or core function | The two sources answer different questions (annotation format vs review record); flagged as an open question |
| [Drive: Changes to viral processes 2017](https://drive.google.com/open?id=1TO6RuYf8C1ANLVQp_mr1bkn_9I_CLtu18KIrPHHgVdE) vs the 2015 viral ontology paper | 2015: viral process terms are agnostic between host and virus; 2017: proposed constraints so viral processes are only viral and host processes only host | Not resolved here; see [multi-organism-and-ncrna.md](../MO/README.md) | The sources conflict and the 2021 proposal allows only "only in Viruses" for viral-only terms |

## Open questions

1. Should GO forbid cross-aspect `replaced_by` in its editor documentation and add a QC check, as the May 2026 call suggested might be needed?
2. Should every `replaced_by` be validated against the obsolete term's former parents (a redirect outside the old branch would be flagged for review)?
3. In GAF/GPAD, is an MF with a `part_of` BP extension the endorsed replacement for obsoleted tethering, docking and similar process terms, given GO's broader move to retire precomposed "X involved in Y" content? How should a review record that pattern?
4. GO has no general holdase chaperone term since `GO:0051082` was obsoleted. Should `GO:0140309` be redefined to match its label, or a new parent created?
5. Should taxon constraints on pathway terms named after one receptor subfamily (TGF-beta, JAK-STAT) be resolved by renaming and regrouping the terms, by constraints, or both?
6. Should TreeGrafter apply GO taxon constraints before grafting unreviewed proteins onto PAINT nodes?
7. When a constraint is applied without a prerequisite re-parenting (the `GO:0007260` case), who tracks the inherited conflict?
8. Should the GOC publish which release each service (QuickGO, AmiGO, OLS, the PURL) is serving, so that curators can cite term state reproducibly?

<!-- END GENERATED -->
