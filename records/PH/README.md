---
id: PH
title: Phylogenetic and orthology-based propagation
record_kind: guideline
applies_to:
- contributing_group
status: proposed
open_questions:
- '**Evidence code for automated orthology pipelines.** The mammalian ISO pipelines are automated but
  emit ISO; Ensembl Compara emits IEA for the same kind of transfer. Should GO require IEA for both, create
  a distinct code, or accept ISO for pipelines with documented filters? The IEA working group asked for
  a consortium-wide decision on mass transfer via orthology ([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).'
- '**Self-referential IBAs.** Our rule keeps them. Should GO formally retire the 2018 statement in go-annotation#2042,
  and should browsers suppress the IBA where the same gene has EXP to the same term?'
- '**IRD visibility.** Should PAINT export NOT|IBA for IRD clades, or a separate "propagation blocked"
  file, so that reviewers can see deliberate absences?'
- '**Residue disclosure for IKR.** Can PAINT record the residues behind each IKR in a field rather than
  in the curator''s head?'
- '**A machine-readable "do not propagate by orthology" flag on terms** (proposed in [go-annotation#1344](https://github.com/geneontology/go-annotation/issues/1344)
  and [#1807](https://github.com/geneontology/go-annotation/issues/1807)). Taxon constraints cover lineage,
  but not tissue or physiological context.'
- '**Mixed seeds for sign.** When a family node''s seeds include both positive and negative regulators
  of a process, should PAINT require the parent "regulation of" term on the node?'
date: '2026-11-15'
---

# Phylogenetic and orthology-based propagation: GO annotation guidelines


**In brief:**

- An IBA is the mechanical consequence of a PAINT curator's IBD placed on an ancestral
  PANTHER node. To challenge an IBA, argue with the node placement or the seed, never with
  the number of donors.
- The target gene appearing in its own IBA `WITH/FROM` is expected and is not circular.
  Genuine circularity is a chain with no experimental grounding anywhere in it.
- Propagate what the lineage inherited: conserved molecular function first, cellular
  processes cautiously, organismal, tissue, "response to" and regulatory-sign context almost
  never.
- Record a loss explicitly (IKR when key residues are gone, IRD for divergence without a
  residue explanation) rather than silently declining to propagate, and never add back what a
  PAINT loss deliberately removed without saying so.
- ISO and ISS need an experimentally supported donor that still carries the term, the right
  orthology edge (all paralogs named for one-to-many), and a term that is safe to move.
- A leaf whose only annotations are IBA is under-annotated, not finished.

## Scope


This document covers annotations that reach a gene product by inheritance or transfer from
another gene product:

- **PAINT** curation on PANTHER trees: IBD (ECO:0000319, biological aspect of descendant
  evidence used in manual assertion) on ancestral nodes, and the IBA (ECO:0000318) rows that
  descendants receive, with `GO_REF:0000033`.
- **PAINT losses**: IKR (ECO:0000320, phylogenetic determination of loss of key residues) and
  IRD (ECO:0000321, rapid divergence from ancestral sequence).
- **Curator-reviewed similarity transfers**: ISS (ECO:0000250), ISA (ECO:0000247) and ISO
  (ECO:0000266), including the automated mammalian ISO pipelines (`GO_REF:0000119`,
  `GO_REF:0000096`, `GO_REF:0000121`).
- When and why propagation should stop: subfunctionalisation, neofunctionalisation,
  pseudo-enzymes, lineage-specific processes and taxon constraints.

TreeGrafter (`GO_REF:0000118`) and Ensembl Compara (`GO_REF:0000107`) are electronic and are
covered in [electronic-annotation.md](../IEA/README.md); this document refers to them
only where they share a failure mode with IBA or ISO. ISM (sequence-model matches) is also in
the electronic document, since it is not a transfer from a gene. How NOT behaves in general is
in [qualifiers-and-negation.md](../QN/README.md); how to record a verdict on an
existing row is in [reviewing-annotations.md](../REV/README.md).

## Principles


**Every transfer has three parts, and each can fail on its own.** A donor (the gene product
with experimental evidence), an intermediate (the orthology call, similarity judgement or
PANTHER node), and a target. A review asks three separate questions: is the donor annotation
sound and current, is the relation the right one, and is this term safe to move. The repo's
`propagation_review` vocabulary records where the defect lives
([HOMOLOGY_PROPAGATION](https://ai4curation.io/ai-gene-review/pages/projects/HOMOLOGY_PROPAGATION.html), [ISO](https://ai4curation.io/ai-gene-review/pages/projects/ISO.html#failure-taxonomy)).

**PAINT is a judgement, not a similarity score.** The curator inspects the tree, the
alignment and every experimental annotation in the family, then decides where a function
arose ([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines);
[PMID:21873635](https://europepmc.org/article/MED/21873635), Gaudet et al. 2011). A single
judgement at a deep node reaches thousands of proteins, so the cost of an error and the value
of a fix are both multiplied. Fix the node, not the leaves.

**Molecular function is more conserved than process, and process more than context.** The
ortholog conjecture is a reasonable prior for biochemistry, a weak one for cellular process,
and no guide at all for tissue, developmental stage or physiological response
([ORTHOLOG_CONJECTURE](https://ai4curation.io/ai-gene-review/pages/projects/ORTHOLOG_CONJECTURE.html)). In the repo's ISO review, the commonest
failure was context that does not carry over, not wrong biochemistry ([ISO](https://ai4curation.io/ai-gene-review/pages/projects/ISO.html)).

**Absence of a propagated term is not evidence of absence, and absence of an IBA is not
evidence of novelty.** PAINT is conservative by construction. In 1,015 reviewed human genes,
511 curated core molecular functions had no IBA support at all
([IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html#iba-incompleteness-core-function-that-iba-fails-to-propagate)).

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [PH-1](PH-1.md) | Review an IBA by its node placement, not by its donor count | proposed | [GOC+] |
| [PH-2](PH-2.md) | Seed an IBD only from experimental annotations that make the claim the term makes | proposed | [GOC+] |
| [PH-3](PH-3.md) | Use high-throughput seeds and single seeds only with an independent second line | proposed | [GOC+] |
| [PH-4](PH-4.md) | Place the IBD at the deepest node the evidence supports, and no deeper | proposed | [GOC+] |
| [PH-5](PH-5.md) | Do not propagate binding-only, redundant, indirect or contextual terms | proposed | [GOC+] |
| [PH-6](PH-6.md) | Propagate substrate and cargo specificity only within a duplication-free clade | proposed | [GOC+] |
| [PH-7](PH-7.md) | Do not propagate a cellular component across a node whose members live in different compartments | proposed | [GOC+] |
| [PH-8](PH-8.md) | Ignore seed qualifiers except NOT; carry `contributes_to` only where the subunit's role is conserved | proposed | [GOC+] |
| [PH-9](PH-9.md) | Record a loss with IKR or IRD, and choose IKR when a key residue explains it | proposed | [NEW] |
| [PH-10](PH-10.md) | NOT propagates only to the term annotated; a positive general term still descends | proposed | [GOC] |
| [PH-11](PH-11.md) | The target in its own `WITH/FROM` is not circular | proposed | [NEW] |
| [PH-12](PH-12.md) | Read the `WITH/FROM` first, and count donors correctly | proposed | [GOC+] |
| [PH-13](PH-13.md) | Stop propagation at duplications that changed function, at pseudo-enzymes, and at lineage boundaries | proposed | [GOC+] |
| [PH-14](PH-14.md) | Before REMOVE on an IBA, complete the checklist and route the fix to the node | proposed | [GOC+] |
| [PH-15](PH-15.md) | Treat an IBA-only leaf as under-annotated, and check for orthologs split across families | proposed | [NEW] |
| [PH-16](PH-16.md) | ISO needs a current experimental donor, the right orthology edge, and every co-ortholog named | proposed | [GOC+] |
| [PH-17](PH-17.md) | Move conserved activity by orthology; do not move context | proposed | [GOC+] |
| [PH-18](PH-18.md) | ISS and ISA need an experimentally characterised match, a reviewed alignment, and no binding-only terms | proposed | [GOC] |
| [PH-19](PH-19.md) | Do not add back what a phylogenetic curator deliberately removed | proposed | [NEW] |
| [PH-20](PH-20.md) | Keep IBA, TreeGrafter and automated orthology distinct in review and in tickets | proposed | [GOC+] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


| Situation | Action on the row | Upstream fix |
|---|---|---|
| IBA term true for target, target also has EXP and appears in `WITH/FROM` | ACCEPT (PH-11) | none |
| IBA donors are a coherent set of orthologs, target has no contrary evidence | ACCEPT or KEEP_AS_NON_CORE by core status (PH-1, PH-12) | none |
| Target lost catalytic residues; fold retained; independently documented | REMOVE (PH-13) | ADD_IKR below node, naming residues (PH-9) |
| Subclade has a different substrate or co-substrate; correct term exists | MODIFY to the subclade term, lateral if needed (PH-6) | MOVE_IBD for the specific term |
| Process absent from target lineage, or prerequisite absent | REMOVE (PH-4, PH-13) | MOVE_IBD (`TOO_DEEP`) or ADD_IRD; propose taxon constraint |
| Compartment mutually exclusive with target's known location | REMOVE (PH-7) | REMOVE_IBD on mixed node |
| Compartment broader than but containing target's location | keep; do not REMOVE (PH-7) | none |
| Sole seed is IMP for an MF, or seed's paper is a phenotype list | REMOVE or UNDECIDED (PH-2) | REMOVE_IBD; dispute the seed row |
| Family node mixes activators and inhibitors; sign leaks | MODIFY to the correct-sign term (PH-13) | MOVE_IBD to the correct-sign clade |
| ISO donor no longer carries term | Check target biology; stale donor alone is not REMOVE (PH-16) | refresh pipeline |
| ISO donor is a paralog / expanded-family member | Scrutinise; REMOVE if target evidence diverges (PH-17) | report orthology call |
| ISO of a tissue, response-to or developmental term, no target evidence | KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED (PH-17) | none |
| Target under a PAINT IRD/IKR for a term you want to add | Do not add, or add with explicit dispute (PH-19) | PAINT ticket |
| Leaf has only general IBA term | Look for specific EXP activity; MODIFY or NEW (PH-15) | request deeper IBD |
| Gene has no IBA, ortholog has many | Check PANTHER family split (PH-15) | PANTHER ticket |

## Common errors


**Removing an IBA because the target "has only one donor".** Donor count is not evidential
strength. Fix: argue the node or the leaf (PH-1).

**Marking self-reference as circular.** Fix: leave the source as `SUPPORTS_TRANSFER`; use
`CIRCULAR_OR_REDUNDANT` only for ungrounded chains (PH-11).

**Calling a broad localisation IBA wrong.** `GO:0005737` cytoplasm on an organellar protein is
imprecise, not false. Fix: check `part_of` before REMOVE (PH-7).

**Treating the PTN node as a donor, or one gene's two identifiers as two donors.** Fix: resolve
`WITH/FROM` before counting (PH-12).

**"Lacks the catalytic residues" asserted without an alignment.** About a quarter of such claims
in one repo pass were wrong about the mechanism. Fix: align against an active control and state
the residue (PH-9, PH-13).

**Fixing the leaf and leaving the node.** The next PAINT or GOA release restores the row. Fix:
file `paint_action` with `target_node_id` (PH-14).

**ISO rows rejected because "there is no mouse evidence".** Transfer without target data is what
ISO asserts; that sentence is a tautology. Fix: give the reason the term does not transfer
(divergence, context, stale donor) ([IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html), "What the count is for").

**Upgrading the relation by propagation.** An `acts_upstream_of_or_within` seed yields an
`involved_in` IBA (PH-8), and Ensembl Compara has done the same across species
([go-annotation#5411](https://github.com/geneontology/go-annotation/issues/5411)). Fix: check the
seed's relation, not only its evidence code.

**Re-adding a term PAINT withdrew.** Cached GOA files can predate an IRD. Fix: check the current
PAINT release before writing NEW (PH-19).

## Reading list


**GO wiki**

- [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) (last reviewed 2021)
- [wiki: Inferred from Key Residues (IKR)](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29) (2018)
- [wiki: Inferred from Rapid Divergence (IRD)](https://wiki.geneontology.org/index.php/Inferred_from_Rapid_Divergence%28IRD%29) (2018; thin)
- [wiki: Inferred from Biological aspect of Ancestor (IBA)](https://wiki.geneontology.org/index.php/Inferred_from_Biological_aspect_of_Ancestor_%28IBA%29) (2018; thin)
- [wiki: Inferred from Sequence Orthology (ISO)](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29) (2018)
- [wiki: Inferred from Sequence Alignment (ISA)](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29) (2018)
- [wiki: Inferred from Sequence or structural Similarity (ISS)](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29) (2024)
- [wiki: 11 MAR 2014 PAINT call](https://wiki.geneontology.org/index.php/11_MAR_2014_PAINT_Conference_Call) (historical)
- [wiki: 5 May 2020 PAINT call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)
- [wiki: 1 March 2023 PAINT call](https://wiki.geneontology.org/index.php/1_March_2023_PAINT_Conference_Call)
- [wiki: 13 March 2024 PAINT call](https://wiki.geneontology.org/index.php/13_March_2024_PAINT_Conference_Call)
- [wiki: 10 July 2024 PAINT call](https://wiki.geneontology.org/index.php/10_July_2024_PAINT_Conference_Call)
- [wiki: 14 Aug 2024 PAINT call](https://wiki.geneontology.org/index.php/14_August_2024_PAINT_Conference_Call)
- [wiki: 14 Jan 2026 PAINT call](https://wiki.geneontology.org/index.php/14_Jan_2026_PAINT_Conference_Call)
- [wiki: 11 Feb 2026 PAINT call](https://wiki.geneontology.org/index.php/11_Feb_2026_PAINT_Conference_Call)

**Drive**

- [Drive: IEA WG GOC meeting Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)
- [Drive: MGI ISO rat filters](https://drive.google.com/open?id=1lx65V8ikyofnkDdwojm6fhHZ801ET1Z9)

**GitHub issues (geneontology/go-annotation)**

[#11](https://github.com/geneontology/go-annotation/issues/11),
[#1319](https://github.com/geneontology/go-annotation/issues/1319),
[#1344](https://github.com/geneontology/go-annotation/issues/1344),
[#1380](https://github.com/geneontology/go-annotation/issues/1380),
[#1775](https://github.com/geneontology/go-annotation/issues/1775),
[#1807](https://github.com/geneontology/go-annotation/issues/1807),
[#1876](https://github.com/geneontology/go-annotation/issues/1876),
[#1925](https://github.com/geneontology/go-annotation/issues/1925),
[#2033](https://github.com/geneontology/go-annotation/issues/2033),
[#2042](https://github.com/geneontology/go-annotation/issues/2042),
[#2097](https://github.com/geneontology/go-annotation/issues/2097),
[#2109](https://github.com/geneontology/go-annotation/issues/2109),
[#2171](https://github.com/geneontology/go-annotation/issues/2171),
[#2219](https://github.com/geneontology/go-annotation/issues/2219),
[#2250](https://github.com/geneontology/go-annotation/issues/2250),
[#2382](https://github.com/geneontology/go-annotation/issues/2382),
[#3242](https://github.com/geneontology/go-annotation/issues/3242),
[#3413](https://github.com/geneontology/go-annotation/issues/3413),
[#4697](https://github.com/geneontology/go-annotation/issues/4697),
[#5254](https://github.com/geneontology/go-annotation/issues/5254),
[#5411](https://github.com/geneontology/go-annotation/issues/5411),
[#5546](https://github.com/geneontology/go-annotation/issues/5546),
[#5691](https://github.com/geneontology/go-annotation/issues/5691)

**Papers**

- [PMID:21873635](https://europepmc.org/article/MED/21873635) Gaudet et al. 2011, Phylogenetic-based propagation of functional annotations within the Gene Ontology consortium
- [PMID:38995546](https://europepmc.org/article/MED/38995546) Interpreting Gene Ontology annotations derived from sequence homology methods (2024)

**Repository pages**

- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) (IBA section; PANTHER section; NEW bar)
- [IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/IBA_REVIEW.html), [PANTHER_IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/PANTHER_IBA_REVIEW.html), [PAINT](https://ai4curation.io/ai-gene-review/pages/projects/PAINT.html)
- [IRD_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html), [ISO](https://ai4curation.io/ai-gene-review/pages/projects/ISO.html), [HOMOLOGY_PROPAGATION](https://ai4curation.io/ai-gene-review/pages/projects/HOMOLOGY_PROPAGATION.html)
- [ORTHOLOG_CONJECTURE](https://ai4curation.io/ai-gene-review/pages/projects/ORTHOLOG_CONJECTURE.html), [TREEGRAFTER](https://ai4curation.io/ai-gene-review/pages/projects/TREEGRAFTER.html), [FAMILIES](https://ai4curation.io/ai-gene-review/pages/projects/FAMILIES.html), [FUNGAL_PAINT_FAMILIES](https://ai4curation.io/ai-gene-review/pages/projects/FUNGAL_PAINT_FAMILIES.html) (family-level reviews of fungal IBD nodes)
- [ENZYME_SPECIFICITY](https://ai4curation.io/ai-gene-review/pages/projects/ENZYME_SPECIFICITY.html), [TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html), [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Open questions

1. **Evidence code for automated orthology pipelines.** The mammalian ISO pipelines are automated but emit ISO; Ensembl Compara emits IEA for the same kind of transfer. Should GO require IEA for both, create a distinct code, or accept ISO for pipelines with documented filters? The IEA working group asked for a consortium-wide decision on mass transfer via orthology ([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).
2. **Self-referential IBAs.** Our rule keeps them. Should GO formally retire the 2018 statement in go-annotation#2042, and should browsers suppress the IBA where the same gene has EXP to the same term?
3. **IRD visibility.** Should PAINT export NOT|IBA for IRD clades, or a separate "propagation blocked" file, so that reviewers can see deliberate absences?
4. **Residue disclosure for IKR.** Can PAINT record the residues behind each IKR in a field rather than in the curator's head?
5. **A machine-readable "do not propagate by orthology" flag on terms** (proposed in [go-annotation#1344](https://github.com/geneontology/go-annotation/issues/1344) and [#1807](https://github.com/geneontology/go-annotation/issues/1807)). Taxon constraints cover lineage, but not tissue or physiological context.
6. **Mixed seeds for sign.** When a family node's seeds include both positive and negative regulators of a process, should PAINT require the parent "regulation of" term on the node?

<!-- END GENERATED -->
