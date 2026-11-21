---
id: ONT-6
title: When nothing replaces the term, put the content on what the gene does, or on its partner
status: proposed
topic: ONT
provenance: GOC_PLUS
evidence_codes:
- IDA
- ISO
go_terms:
- term_id: GO:0140355
  label: cargo receptor ligand activity
- term_id: GO:0038024
  label: cargo receptor activity
- term_id: GO:0031419
  label: cobalamin binding
- term_id: GO:0015889
  label: cobalamin transport
sources:
- kind: web
  title: CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.html
- kind: drive
  title: Protein oligomerization obsoletion proposal
  url: https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo
- kind: issue
  title: go-annotation#2521
  url: https://github.com/geneontology/go-annotation/issues/2521
date: '2026-11-15'
---

# ONT-6. When nothing replaces the term, put the content on what the gene does, or on its partner

## Decision

If an obsolete term has no replacement, do not search for the nearest live term. Ask what
the gene product actually does; annotate that if it is not already annotated; and if the
obsolete term described something done to the gene product, the content belongs on the
partner that does it.

## Application

*Example.* `GO:0140355` cargo receptor ligand activity is being retired with no replacement,
because being recognized by a cargo receptor is something done to a protein. For
transcobalamin, the receptor CD320 carries `GO:0038024` cargo receptor activity with the
ligand as input, and the carrier keeps what it does: `GO:0031419` cobalamin binding and
`GO:0015889` cobalamin transport. Two rows should go regardless: a yeast ATG5 IDA and an
orphaned mouse ISO whose human source no longer exists
([CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.html)).

*Example.* GO's 2016 decision on protein oligomerization terms set a class-wide rule: a gene
product that mediates assembly goes to complex assembly with the complex as output; an
assembled subunit gets the complex CC term or a structural or bridging MF; and the annotation
is removed if nothing fits ([Drive: Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo),
[go-annotation#2521](https://github.com/geneontology/go-annotation/issues/2521)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Evidence codes | IDA, ISO |
| GO terms | `GO:0140355` cargo receptor ligand activity; `GO:0038024` cargo receptor activity; `GO:0031419` cobalamin binding; `GO:0015889` cobalamin transport |

## Sources

- web: [CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.html)
- drive: [Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo)
- issue: [go-annotation#2521](https://github.com/geneontology/go-annotation/issues/2521)

<!-- END GENERATED -->
