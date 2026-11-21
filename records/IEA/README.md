---
id: IEA
title: Electronic annotation
record_kind: guideline
applies_to:
- contributing_group
status: proposed
differences:
- prior_source: '[wiki: Annotation consistency: IEA, ISS, IC](https://wiki.geneontology.org/index.php/Annotation_consistency%3A_IEA%2C_ISS%2C_IC_Usage_Discussion)
    (archived, 2007)'
  prior_said: Keyword2GO, EC2GO, SubCell2GO and Compara are reliable enough to display without other information.
  we_recommend: Several are now retired or under replacement; Compara needs a consortium decision (IEA-6,
    IEA-10).
  why: Reviews since 2025 found high error rates and multi-hop provenance; the 2007 assessment predates
    them.
- prior_source: '[go-annotation#615](https://github.com/geneontology/go-annotation/issues/615) (2008)'
  prior_said: Correct but uninformative IEAs are kept; filtering is the browser's job.
  we_recommend: Agree for review actions (IEA-12), but mappings must not target do-not-annotate terms
    (IEA-4).
  why: The do-not-annotate subset now names terms GO considers unfit for any annotation; [#5902](https://github.com/geneontology/go-annotation/issues/5902)
    moved one such IEA target into it.
- prior_source: '[wiki: ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29)
    and Compara page'
  prior_said: Automated orthology transfer is IEA; manually reviewed is ISO.
  we_recommend: We note that automated mammalian ISO pipelines contradict this and leave the code question
    open (see Open questions).
  why: 'The IEA working group recorded the same inconsistency ([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).'
- prior_source: 'UniProt ARBA documentation as summarised in [Drive: ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz)'
  prior_said: Rules have 100% confidence.
  we_recommend: Read 100% as in-sample consistency; judge each condition set against experimental annotations
    (IEA-9, IEA-16).
  why: The same notes list training bias, excluded negatives, template errors and leaking signatures.
open_questions:
- '**Mass transfer by orthology.** Should GO keep any automated orthology pipeline (Compara, mammalian
  ISO) for species with active curation, reserve it for "unadopted" species, or retire it? If kept, which
  evidence code? The IEA working group asked for a consortium-wide decision and a new working group ([Drive:
  IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).'
- '**Conditional mappings upstream.** Should interpro2go (or a successor) support taxon and negative-domain
  conditions, so that rules like CR-0001 and CR-0005 can live at the source?'
- '**TrEMBL coverage after SubCell2GO, Rhea2GO and EC2GO stop.** The plan is to rely on ARBA gaining GO
  coverage; who measures whether it does, and against what out-of-sample standard?'
- '**Collateral loss from retirement.** Blanket retirement of KW2GO removed correct annotations that no
  other source carried (DELLA signalling, patatin storage activity in the repo''s plant review). Should
  retirement loss files be curated into manual or PAINT annotations before deletion as standard practice?'
- '**Viral keywords.** KW2GO survives for viruses. Should ViralZone keywords map to GO at all, given the
  clade-dependent host-context errors the repo found for phage immune terms ([SPKW](https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html))?'
- '**Pfam and NCBIfam coverage.** Most Pfam-A families and most NCBIfam models reach no GO term. Should
  GO accept member-database mappings directly when InterPro has not integrated the signature?'
date: '2026-11-15'
---

# Electronic annotation: GO annotation guidelines


**In brief:**

- An IEA is a claim about a mapping or rule, applied to a gene. Review it by asking whether the
  mapping holds for every protein it fires on, and fix it where it was made.
- A signature-to-GO mapping is appropriate only if every protein matching the signature has the
  function. A term true for a subset belongs on a narrower entry or in a conditional rule.
- Provenance must be one hop from a curated or sequence-feature source to GO. Chains such as
  ARBA to keyword to GO, or ARBA to Rhea to GO, are not acceptable.
- A correct but general IEA is kept, never removed for being general. REMOVE is for a mapping
  that is wrong for the gene, an over-propagation you can argue on biological grounds, or a
  premise that has fallen.
- Before proposing a mapping removal, check what else would still supply the term to the members
  that should keep it, and record a replacement rule when only a condition can separate right
  from wrong members.

## Scope


This document covers annotations made without curator review of the individual gene product,
which carry IEA (ECO:0000501, evidence used in automatic assertion) and a GO_REF naming the
method:

- **Signature mappings**: InterPro2GO (`GO_REF:0000002`), including member databases that reach
  GO only through it (Pfam, NCBIfam, CDD, PANTHER via InterPro), and Rfam2GO.
- **Controlled-vocabulary mappings**: UniProt keywords (KW2GO, `GO_REF:0000043`, retired for
  cellular organisms), UniProt subcellular locations (SubCell2GO, `GO_REF:0000044`), EC2GO
  (`GO_REF:0000003`), Rhea2GO (`GO_REF:0000116`) and UniPathway2GO (`GO_REF:0000041`).
- **Rule systems**: UniRule (including HAMAP) and ARBA (`GO_REF:0000117`).
- **Phylogenetic and orthology pipelines** that run without a curator: TreeGrafter
  (`GO_REF:0000118`) and Ensembl Compara (`GO_REF:0000107`).
- **GO's own logical inferences** across aspects (`GO_REF:0000108`), and UniProt's combined
  record of identical predictions from several pipelines (`GO_REF:0000120`).
- How to review and challenge an IEA row, and how to record a mapping fix, including this
  repository's curated rules in `rules/curated/`.

PAINT/IBA, ISO, ISS and ISA are in [phylogenetic-propagation.md](../PH/README.md).
Machine-learning and language-model predictions outside these pipelines share several failure
modes and are touched on in IEA-15; evidence-code choice in general is in
[evidence-codes.md](../EV/README.md).

## Principles


**A mapping is a universal claim.** InterPro2GO attaches a term to every protein that matches an
entry ([PMID:22301074](https://europepmc.org/article/MED/22301074), the InterPro GO-mapping
protocol). A term true of most members is false of the rest, and a single wrong mapping repeats
across every matched gene. The repo's InterPro review found mapping errors that each reached
hundreds to thousands of proteins ([INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html)).

**Provenance has to reach the source in one step.** The GO IEA working group's rubric scores
pipelines on responsiveness, currency, conformance to GO rules, provenance, explainability,
documentation, accuracy and uniqueness, and it judged multi-hop chains to be the main reason
KW2GO errors were hard to trace and harder to fix
([Drive: IEA WG pipelines update GOC 2026](https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y)).

**IEAs fill real gaps.** For many proteins in poorly curated organisms an IEA is the only
annotation. TreeGrafter supplied the only annotation to a term on 623 reviewed rows, of which
reviewers kept 70% ([TREEGRAFTER](https://ai4curation.io/ai-gene-review/pages/projects/TREEGRAFTER.html)); the plant keyword review found that
retiring KW2GO also removed correct facts carried nowhere else ([SPKW](https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html)). The aim is
a leaner, more informative set, not a smaller one for its own sake
([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).

**Fix the source, not the symptom.** A gene-level REMOVE leaves the mapping in place and the next
release restores it. Every correction should name the mapping, rule or node that produced the row.

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [IEA-1](IEA-1.md) | Identify the pipeline before judging the row | proposed | [GOC+] |
| [IEA-2](IEA-2.md) | A signature mapping must hold for every member of the entry | proposed | [NEW] |
| [IEA-3](IEA-3.md) | Map a domain to what the domain does, not to what proteins containing it do | proposed | [GOC] |
| [IEA-4](IEA-4.md) | Never map to root, do-not-annotate, binding-only or obsolete terms | proposed | [GOC] |
| [IEA-5](IEA-5.md) | Accept only one-hop provenance | proposed | [GOC] |
| [IEA-6](IEA-6.md) | Know the current status of each pipeline | proposed | [GOC] |
| [IEA-7](IEA-7.md) | Use only exact reaction mappings, and only for physiological reactions | proposed | [GOC] |
| [IEA-8](IEA-8.md) | A keyword or location mapping must respect GO's distinctions, which vocabularies often do not | proposed | [GOC+] |
| [IEA-9](IEA-9.md) | Judge a rule by its condition sets, as conjunctions, against the experimental record | proposed | [GOC+] |
| [IEA-10](IEA-10.md) | Automated orthology transfer must preserve relations and stop at context | proposed | [GOC+] |
| [IEA-11](IEA-11.md) | An inferred annotation falls with its premise | proposed | [GOC+] |
| [IEA-12](IEA-12.md) | Review actions: keep true general rows, remove wrong ones, never cite an IEA as evidence | proposed | [GOC+] |
| [IEA-13](IEA-13.md) | When a mapping is wrong, route the fix to the mapping and record it in a form the source can use | proposed | [NEW] |
| [IEA-14](IEA-14.md) | Use a curated conditional rule when only a condition can separate right from wrong members | proposed | [NEW] |
| [IEA-15](IEA-15.md) | Do not launder a prediction into manual evidence | proposed | [GOC] |
| [IEA-16](IEA-16.md) | Hold new prediction pipelines to the rubric before they enter GO | proposed | [GOC+] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


| Row | Question | Action |
|---|---|---|
| InterPro2GO term false for this gene, gene is an atypical member (pseudo-enzyme, divergent paralog) | Does a narrower entry or rule cover the true members? | REMOVE on the gene; propose narrowing or removal with rule-cover note (IEA-2, IEA-13) |
| InterPro2GO term false for every member of the entry | | REMOVE; propose removal and the correct family-wide term (IEA-2) |
| InterPro2GO term true but general; gene has a specific term from other evidence | Does this row's evidence support the specific term? | KEEP_AS_NON_CORE or ACCEPT; MODIFY only if the row's own signature supports the descendant (IEA-12) |
| Domain entry carries a whole-protein or neighbouring-domain function | | REMOVE on genes lacking that function; propose moving the mapping (IEA-3) |
| Mapping target is root, do-not-annotate or obsolete | | REMOVE or MODIFY; report the mapping (IEA-4) |
| KW2GO, SubCell2GO or UniPathway row in a cached file | Is the biology right? | Review for the record; do not cite; expect it to disappear (IEA-6) |
| Keyword row: regulator annotated to process, transit compartment, cofactor as binding | | MODIFY to regulation term, REMOVE transit location, REMOVE cofactor binding unless binding is the function (IEA-8) |
| EC2GO or Rhea2GO row from a broadMatch or non-physiological reaction | | REMOVE; report the mapping (IEA-7) |
| ARBA or UniRule row looks wrong | Which condition set fired? Does the protein have experimental annotation to the term or a descendant? | If no: REMOVE and file a rule review with the accession as counterexample; if yes: the row is probably right (IEA-9) |
| Compara row with development, response-to or tissue term | Is the donor row experimental and direct? | REMOVE or MARK_AS_OVER_ANNOTATED (IEA-10) |
| `GO_REF:0000108` row whose premise you removed | | REMOVE (IEA-11) |
| Term true for members in some taxa or contexts only | Does a taxon, module or feature separate them? | Write a curated rule (IEA-14) |

## Common errors


**Removing a true general IEA as redundant.** Redundancy is a display concern. Fix: KEEP_AS_NON_CORE,
or MODIFY only with the row's own evidence (IEA-12).

**Treating a gene-level MODIFY as a mapping error.** A specific term on one gene does not make the
general mapping wrong. Fix: record whether the proposal needs removal, a narrower entry, or nothing
upstream ([INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html)).

**Proposing a mapping removal without counting the cost.** Fix: run the sole-source and rule-cover
checks and state them (IEA-13).

**Judging a rule from its size or from one signature.** Fix: read the condition sets as conjunctions
(IEA-9).

**Naming an InterPro, Pfam or FunFam id from memory.** The label is the checksum of the id; over 20
ARBA reviews gave an id another entry's name. Fix: copy the official name ([docs: rule review
receipts](https://github.com/ai4curation/ai-gene-review/blob/main/docs/rule_review_receipts.md)).

**Calling a protein a rule's false positive without checking its curated annotations.** Rules are
mined from curated annotations; a surprising family is more often a curated row the reviewer did not
know. Fix: check experimental annotations to the term and descendants first (IEA-9).

**Citing ARBA text or the record's `DR GO` lines as evidence.** Fix: quote the curated or
experimental statement behind the annotation, or mark the row UNDECIDED (IEA-12).

**Leaving the inferred BP after removing the MF.** Fix: follow `GO_REF:0000108` rows to their premise
(IEA-11).

**Reading a mapping's precision as recall, or vice versa.** A mapping can be correct wherever it
fires and still miss most of the family (82.6% of Pfam-A families get no GO term through InterPro).
Absence of an IEA is not evidence of absence ([PFAM](https://ai4curation.io/ai-gene-review/pages/projects/PFAM.html)).

## Reading list


**GO wiki**

- [wiki: Inferred from Electronic Annotation (IEA)](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)
- [wiki: Inferred from Sequence Model (ISM)](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29)
- [wiki: Inferred from Sequence Orthology (ISO)](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29)
- [wiki: Ensembl Compara annotation projection](https://wiki.geneontology.org/index.php/Ensembl_Compara_annotation_projection)
- [wiki: Annotation Assigned by](https://wiki.geneontology.org/index.php/Annotation_Assigned_by) (draft)
- [wiki: Annotation consistency: IEA, ISS, IC Usage Discussion](https://wiki.geneontology.org/index.php/Annotation_consistency%3A_IEA%2C_ISS%2C_IC_Usage_Discussion) (archived)
- [wiki: InterPro2GO Session October 4th 2011](https://wiki.geneontology.org/index.php/InterPro2GO_Session_October_4th_2011) (historical)
- [wiki: Planned changes to the IEA GO_REFs cited by UniProtKB](https://wiki.geneontology.org/index.php/Planned_changes_to_the_IEA_GO_REFs_cited_by_UniProtKB.) (archived)

**Drive**

- [Drive: IEA WG GOC meeting Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I) (current decisions)
- [Drive: IEA WG pipelines update Sept 2026](https://drive.google.com/open?id=1FQpXSPZdK78X3wX5UEQ9jkFk6Xex0NCi8NeDawOs7IE)
- [Drive: IEA WG pipelines update GOC 2026](https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y) (rubric)
- [Drive: Retiring the KW2GO pipeline](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)
- [Drive: Ensembl and ISO pipelines](https://drive.google.com/open?id=1q9m9RbQqdpXMPrLq-jzTC-ouLJjUda_XAA93U8zTkNw)
- [Drive: ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz)
- [Drive: Including IBA annotations in ARBA training](https://drive.google.com/open?id=1eIC-6mENH1bQoHsjDuaXu52IlXm5PyCD)
- [Drive: Rule-based systems in GOA (2025)](https://drive.google.com/open?id=1_XLWtDWUzR0A-u8TTE3OoZa46XpHgICo)
- [Drive: Best practices for predicting GO data](https://drive.google.com/open?id=1z-6rNJ4tg3M-Ant-2kqDXohPZUlkw9GEZ5qlNZDYj18) (legacy draft of the published external-guidelines page)
- [Drive: Draft AI policy statement](https://drive.google.com/open?id=1leeuPb1WDgyORZHrxhapW9HKLTPrCi6xsMi-KaZNCIQ) (draft)

**GitHub issues (geneontology/go-annotation)**

[#385](https://github.com/geneontology/go-annotation/issues/385),
[#390](https://github.com/geneontology/go-annotation/issues/390),
[#615](https://github.com/geneontology/go-annotation/issues/615),
[#1020](https://github.com/geneontology/go-annotation/issues/1020),
[#1134](https://github.com/geneontology/go-annotation/issues/1134),
[#1344](https://github.com/geneontology/go-annotation/issues/1344),
[#1386](https://github.com/geneontology/go-annotation/issues/1386),
[#1519](https://github.com/geneontology/go-annotation/issues/1519),
[#1807](https://github.com/geneontology/go-annotation/issues/1807),
[#1879](https://github.com/geneontology/go-annotation/issues/1879),
[#1887](https://github.com/geneontology/go-annotation/issues/1887),
[#2710](https://github.com/geneontology/go-annotation/issues/2710),
[#2921](https://github.com/geneontology/go-annotation/issues/2921),
[#3007](https://github.com/geneontology/go-annotation/issues/3007),
[#4573](https://github.com/geneontology/go-annotation/issues/4573),
[#5411](https://github.com/geneontology/go-annotation/issues/5411),
[#5432](https://github.com/geneontology/go-annotation/issues/5432),
[#5902](https://github.com/geneontology/go-annotation/issues/5902),
[#6018](https://github.com/geneontology/go-annotation/issues/6018),
[#6085](https://github.com/geneontology/go-annotation/issues/6085)

**Papers**

- [PMID:22301074](https://europepmc.org/article/MED/22301074) Manual GO annotation of predictive protein signatures: the InterPro approach to GO curation (2012)
- [PMID:38995546](https://europepmc.org/article/MED/38995546) Interpreting Gene Ontology annotations derived from sequence homology methods (2024)

**Repository pages**

- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) (curated rules; reviewing rules; quoting UniProt)
- [INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html) and [INTERPRO README](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO/README.html), [PFAM](https://ai4curation.io/ai-gene-review/pages/projects/PFAM.html), [NCBIFam](https://ai4curation.io/ai-gene-review/pages/projects/NCBIFam.html)
- [ARBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/ARBA_REVIEW.html), [docs: rule review receipts](https://github.com/ai4curation/ai-gene-review/blob/main/docs/rule_review_receipts.md), [rules/curated README](https://github.com/ai4curation/ai-gene-review/blob/main/rules/curated/README.md)
- [SPKW](https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html), [KW_1110_TRAF_KW2GO](https://ai4curation.io/ai-gene-review/pages/projects/KW_1110_TRAF_KW2GO.html), [RHEA](https://ai4curation.io/ai-gene-review/pages/projects/RHEA.html)
- [TREEGRAFTER](https://ai4curation.io/ai-gene-review/pages/projects/TREEGRAFTER.html), [HOMOLOGY_PROPAGATION](https://ai4curation.io/ai-gene-review/pages/projects/HOMOLOGY_PROPAGATION.html), [ISO](https://ai4curation.io/ai-gene-review/pages/projects/ISO.html), [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html)
- [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html), [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html), [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotation consistency: IEA, ISS, IC](https://wiki.geneontology.org/index.php/Annotation_consistency%3A_IEA%2C_ISS%2C_IC_Usage_Discussion) (archived, 2007) | Keyword2GO, EC2GO, SubCell2GO and Compara are reliable enough to display without other information. | Several are now retired or under replacement; Compara needs a consortium decision (IEA-6, IEA-10). | Reviews since 2025 found high error rates and multi-hop provenance; the 2007 assessment predates them. |
| [go-annotation#615](https://github.com/geneontology/go-annotation/issues/615) (2008) | Correct but uninformative IEAs are kept; filtering is the browser's job. | Agree for review actions (IEA-12), but mappings must not target do-not-annotate terms (IEA-4). | The do-not-annotate subset now names terms GO considers unfit for any annotation; [#5902](https://github.com/geneontology/go-annotation/issues/5902) moved one such IEA target into it. |
| [wiki: ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29) and Compara page | Automated orthology transfer is IEA; manually reviewed is ISO. | We note that automated mammalian ISO pipelines contradict this and leave the code question open (see Open questions). | The IEA working group recorded the same inconsistency ([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)). |
| UniProt ARBA documentation as summarised in [Drive: ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz) | Rules have 100% confidence. | Read 100% as in-sample consistency; judge each condition set against experimental annotations (IEA-9, IEA-16). | The same notes list training bias, excluded negatives, template errors and leaking signatures. |

## Open questions

1. **Mass transfer by orthology.** Should GO keep any automated orthology pipeline (Compara, mammalian ISO) for species with active curation, reserve it for "unadopted" species, or retire it? If kept, which evidence code? The IEA working group asked for a consortium-wide decision and a new working group ([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).
2. **Conditional mappings upstream.** Should interpro2go (or a successor) support taxon and negative-domain conditions, so that rules like CR-0001 and CR-0005 can live at the source?
3. **TrEMBL coverage after SubCell2GO, Rhea2GO and EC2GO stop.** The plan is to rely on ARBA gaining GO coverage; who measures whether it does, and against what out-of-sample standard?
4. **Collateral loss from retirement.** Blanket retirement of KW2GO removed correct annotations that no other source carried (DELLA signalling, patatin storage activity in the repo's plant review). Should retirement loss files be curated into manual or PAINT annotations before deletion as standard practice?
5. **Viral keywords.** KW2GO survives for viruses. Should ViralZone keywords map to GO at all, given the clade-dependent host-context errors the repo found for phage immune terms ([SPKW](https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html))?
6. **Pfam and NCBIfam coverage.** Most Pfam-A families and most NCBIfam models reach no GO term. Should GO accept member-database mappings directly when InterPro has not integrated the signature?

<!-- END GENERATED -->
