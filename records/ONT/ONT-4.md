---
id: ONT-4
title: Treat `consider` as a list of options and triage annotations by mechanism
status: proposed
topic: ONT
provenance: GOC
go_terms:
- term_id: GO:0008139
  obsolete: true
- term_id: GO:0140142
  label: nucleocytoplasmic carrier activity
- term_id: GO:0017056
  label: structural constituent of nuclear pore
- term_id: GO:0030943
  obsolete: true
- term_id: GO:0140436
  label: mitochondrial signal sequence receptor activity
- term_id: GO:0008320
  label: transmembrane protein transporter activity
- term_id: GO:0061753
  label: substrate localization to autophagosome
sources:
- kind: wiki
  title: Obsoleting an Existing Ontology Term
  url: https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term
- kind: web
  title: NLS_BINDING_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/NLS_BINDING_OBSOLETION.html
- kind: web
  title: MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.html
- kind: web
  title: SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION.html
date: '2026-11-15'
---

# ONT-4. Treat `consider` as a list of options and triage annotations by mechanism

## Decision

When an obsolete term has only `consider` targets, sort its annotations by what each gene
product actually does, and give each class its own destination. Some rows will have no
destination and should be removed.

## Context

`consider` exists because no single term replaces the obsolete one
([wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)).
A term goes this way most often because it lumped different mechanisms.

## Application

*Example.* `GO:0008139` nuclear localization sequence binding was obsoleted as the same
activity as `GO:0140142` nucleocytoplasmic carrier activity. That is correct for importins
(KPNA2, KPNB1). It is wrong for a protein that binds an NLS in order to mask it (IκBα), and
for nucleoporins, whose annotations belong on `GO:0017056` structural constituent of nuclear
pore ([NLS_BINDING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/NLS_BINDING_OBSOLETION.html)).

*Example.* `GO:0030943` mitochondrion targeting sequence binding was obsoleted "in favor of
more specific molecular functions". TOM20 and TOM22 move to `GO:0140436` mitochondrial
signal sequence receptor activity; the TOM40 channel moves to `GO:0008320` transmembrane
protein transporter activity; TIM22, a carrier-pathway channel whose substrates use internal
signals, may fit neither ([MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.html)).

Upstream remapping tables are drafts too. The review of `GO:0061753` substrate localization to
autophagosome found two errors in the upstream table and one case (IRGQ) with no adequate
destination term ([SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0008139`  (obsolete); `GO:0140142` nucleocytoplasmic carrier activity; `GO:0017056` structural constituent of nuclear pore; `GO:0030943`  (obsolete); `GO:0140436` mitochondrial signal sequence receptor activity; `GO:0008320` transmembrane protein transporter activity; `GO:0061753` substrate localization to autophagosome |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [ONT-4-E1](ONT-4.examples.yaml): The TOM40 channel's mitochondrion targeting sequence binding sent to protein transporter activity | Conformant | TOMM40 enables GO:0030943 mitochondrion targeting sequence binding (IBA, GO_REF:0000033) |
| [ONT-4-E2](ONT-4.examples.yaml): An Acl4 row on mitochondrion targeting sequence binding removed with no destination | Conformant | ACL4 enables GO:0030943 mitochondrion targeting sequence binding (IBA, GO_REF:0000033) |
| [ONT-4-E3](ONT-4.examples.yaml): TIMM22's targeting-signal row sent to the transporter rather than the receptor | Conformant | TIMM22 enables GO:0030943 mitochondrion targeting sequence binding (IBA, GO_REF:0000033) |

## Sources

- wiki: [Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)
- web: [NLS_BINDING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/NLS_BINDING_OBSOLETION.html)
- web: [MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.html)
- web: [SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION.html)

<!-- END GENERATED -->
