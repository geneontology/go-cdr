---
id: ONT-15
title: Propose an obsoletion only for a term whose meaning is broken, with a remapping for every curated
  row
status: proposed
topic: ONT
provenance: GOC_PLUS
go_terms:
- term_id: GO:0014029
  label: neural crest formation
sources:
- kind: wiki
  title: Obsoleting an Existing Ontology Term
  url: https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term
- kind: wiki
  title: Restoring an Obsolete Ontology Term
  url: https://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term
- kind: web
  title: NEURAL_CREST_FORMATION_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/NEURAL_CREST_FORMATION_OBSOLETION.html
- kind: repo
  title: ontology changes
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md
date: '2026-11-15'
---

# ONT-15. Propose an obsoletion only for a term whose meaning is broken, with a remapping for every curated row

## Decision

Request obsoletion when a term's definition and placement contradict each other, when its
usage is so inconsistent that it has no single meaning, or when it falls in a class GO has
ruled out of scope. Supply a destination for every experimental annotation, and say which rows
should simply go.

## Context

GO's list of obsoletion reasons covers the main cases: unclear definition and inconsistent
usage, precomposed content better as GO-CAM, an assay, a phenotype, an MF stated as a process,
a gene product or protein class, equivalence to another term, and no evidence that the function
exists or is catalysed ([wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)).
Restoration of an obsolete term is possible when its original meaning survives
([wiki: Restoring an Obsolete Ontology Term](https://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term)).

## Application

*Example.* `GO:0014029` neural crest formation has 1,454 annotations, 91% electronic and 665
from a single ARBA rule. The text defines forming a region of ectoderm while the graph places
it under EMT, so the annotations mix border specifiers, crest specifiers, competence factors
and ribosome-biogenesis genes. The proposal remaps the 84 experimental rows to precise existing
terms or one of two new terms (five rows remain undecided for want of full text), and names the ARBA rule to report to UniProt
([NEURAL_CREST_FORMATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/NEURAL_CREST_FORMATION_OBSOLETION.html)).

The structured form of such a request in this repository uses KGCL change types, with direct
replacements in `has_direct_replacement` and per-annotation advice in
`has_nondirect_replacement`; KGCL's controlled English has no statement for a non-direct
replacement or a merge, so those are carried in the structured slots
([ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)).

### Taxon scope

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| GO terms | `GO:0014029` neural crest formation |

## Sources

- wiki: [Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)
- wiki: [Restoring an Obsolete Ontology Term](https://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term)
- web: [NEURAL_CREST_FORMATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/NEURAL_CREST_FORMATION_OBSOLETION.html)
- repo: [ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)

<!-- END GENERATED -->
