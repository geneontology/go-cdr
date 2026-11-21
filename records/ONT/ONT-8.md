---
id: ONT-8
title: Merges are now obsoletions with `replaced_by`; read old secondary ids accordingly
status: proposed
topic: ONT
provenance: GOC
evidence_codes:
- IBD
go_terms:
- term_id: GO:0008785
  obsolete: true
- term_id: GO:0102039
  label: NADH-dependent peroxiredoxin activity
related:
- ONT-3
sources:
- kind: wiki
  title: Annotation Conf. Call 2023-04-18
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18
- kind: drive
  title: Automated Ontology Term Updates in Noctua
  url: https://drive.google.com/open?id=1QrKtMLMjBFoUaceh5UJX5IP_EtqMEx9igsqj_73DrFQ
- kind: web
  title: ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION.html
- kind: drive
  title: PAINT Pipeline Update 2018
  url: https://drive.google.com/open?id=1HqVWDk-B99U5DA5udeTJqnmbJstOVRI5aQTZ3H9alpo
date: '2026-11-15'
---

# ONT-8. Merges are now obsoletions with `replaced_by`; read old secondary ids accordingly

## Decision

Treat a merged-away identifier as an obsolete term whose `replaced_by` is the survivor, and
apply [ONT-3](ONT-3.md) to it.

## Context

Historically GO merged terms, turning the absorbed term's id into an `alt_id` of the survivor.
In 2023 the annotation call adopted a new procedure: no more merges, only obsoletion with
`replaced_by`, and a plan to convert every existing `alt_id` into an obsolete stanza pointing
to the active term, for consistency with OWL and other OBO ontologies
([wiki: Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18)).
Noctua had applied merges and `replaced_by` updates to models automatically since April 2022
([Drive: Automated Ontology Term Updates in Noctua](https://drive.google.com/open?id=1QrKtMLMjBFoUaceh5UJX5IP_EtqMEx9igsqj_73DrFQ)).

## Application

*Example.* `GO:0008785` alkyl hydroperoxide reductase activity fixed a substrate no known
enzyme is specific for, and was obsoleted with `replaced_by` `GO:0102039` NADH-dependent
peroxiredoxin activity, the new form of a merge
([ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION.html)).
The target names an electron donor; before accepting the redirect for a curated row, check that
the enzyme's characterized donor is NADH.

PAINT handles obsoletions in its monthly update: IBDs on obsoleted terms are obsoleted or
moved to the replacement, and an IBD is obsoleted when every experimental annotation at its
leaves is gone and restored when a new one appears
([Drive: PAINT Pipeline Update 2018](https://drive.google.com/open?id=1HqVWDk-B99U5DA5udeTJqnmbJstOVRI5aQTZ3H9alpo)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Related | [ONT-3](ONT-3.md) |
| Evidence codes | IBD |
| GO terms | `GO:0008785`  (obsolete); `GO:0102039` NADH-dependent peroxiredoxin activity |

## Sources

- wiki: [Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18)
- drive: [Automated Ontology Term Updates in Noctua](https://drive.google.com/open?id=1QrKtMLMjBFoUaceh5UJX5IP_EtqMEx9igsqj_73DrFQ)
- web: [ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION.html)
- drive: [PAINT Pipeline Update 2018](https://drive.google.com/open?id=1HqVWDk-B99U5DA5udeTJqnmbJstOVRI5aQTZ3H9alpo)

<!-- END GENERATED -->
