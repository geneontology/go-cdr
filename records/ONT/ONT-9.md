---
id: ONT-9
title: Fix a wrong annotation at its source; fix a wrong term in the ontology; do not confuse the two
status: proposed
topic: ONT
provenance: GOC
go_terms:
- term_id: GO:0003400
  obsolete: true
- term_id: GO:0048208
  label: COPII vesicle coat assembly
related:
- REV-17
sources:
- kind: wiki
  title: Principles for term obsoletion
  url: https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion
- kind: repo
  title: ontology changes
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md
- kind: wiki
  title: Manager 09Feb11
  url: https://wiki.geneontology.org/index.php/Manager_09Feb11
- kind: web
  title: COPII_VESICLE_COATING_REGULATION_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/COPII_VESICLE_COATING_REGULATION_OBSOLETION.html
date: '2026-11-15'
---

# ONT-9. Fix a wrong annotation at its source; fix a wrong term in the ontology; do not confuse the two

## Decision

Incorrect annotations are not a reason to obsolete a term; report them to the group that
made them. A defective term is a reason to request an ontology change, and obsoleting it does
not repair the annotations that used it. A review that finds both records both, separately.

## Context

GO's obsoletion principles say this directly: incorrect annotations should be reported to the
submitting database, and obsoletion is for terms whose meaning is broken
([wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion)).
In this repository, an annotation error is a `source_defects` entry addressed to the
`assigned_by` group or pipeline; a term error is a `proposed_ontology_changes` entry; a
missing term is a `proposed_new_terms` entry
([ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md),
[REV-17](../REV/REV-17.md)).

Likewise, a definition edit that does not make existing annotations wrong should not trigger
obsoletion; curators use the definition-change reports to refine their own annotations
([wiki: Manager 09Feb11](https://wiki.geneontology.org/index.php/Manager_09Feb11)).

## Application

*Example.* `GO:0003400` regulation of COPII vesicle coating was obsoleted because its
annotated genes (SAR1, SEC12, SEC23, SEC16) are parts of coat assembly, not regulators of it.
That was a term problem, and the annotations moved to `GO:0048208`, now labelled COPII vesicle
coat assembly. One human MAPK15 row in the same set was an annotation problem and is slated
for removal, which the obsoletion alone would not have achieved
([COPII_VESICLE_COATING_REGULATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/COPII_VESICLE_COATING_REGULATION_OBSOLETION.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Related | [REV-17](../REV/REV-17.md) |
| GO terms | `GO:0003400`  (obsolete); `GO:0048208` COPII vesicle coat assembly |

## Sources

- wiki: [Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion)
- repo: [ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)
- wiki: [Manager 09Feb11](https://wiki.geneontology.org/index.php/Manager_09Feb11)
- web: [COPII_VESICLE_COATING_REGULATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/COPII_VESICLE_COATING_REGULATION_OBSOLETION.html)

<!-- END GENERATED -->
