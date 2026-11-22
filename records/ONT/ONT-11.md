---
id: ONT-11
title: Request a new term only when real evidence for a real gene needs it
status: proposed
topic: ONT
provenance: GOC_PLUS
provenance_note: '[GOC+]. The request contents and the evidence-first test are our sharpening.'
go_terms:
- term_id: GO:0014029
  label: neural crest formation
sources:
- kind: repo
  title: go-annotation CONTRIBUTING
  url: https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md
- kind: wiki
  title: Tips
  url: https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations
- kind: wiki
  title: Ontology meeting 2024-01-22
  url: https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-22
- kind: web
  title: NEURAL_CREST_FORMATION_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/NEURAL_CREST_FORMATION_OBSOLETION.html
date: '2026-11-15'
---

# ONT-11. Request a new term only when real evidence for a real gene needs it

## Decision

Request a term when (a) published evidence for a specific gene product would support an
annotation, (b) no existing term, extension, or GO-CAM pattern can express it, and (c) you can
write a definition with a genus and differentia that places it under a verified parent. A good
request carries all of these.

## Context

A request should state:

| Element | Content |
|---|---|
| Label | Following GO naming conventions (MF labels end in "activity" or "binding") |
| Definition | Genus (the verified parent) plus what distinguishes it, with references; for enzymes, the reaction (Rhea or EC) |
| Parent(s) | Verified `is_a` and, where relevant, `part_of` |
| Gene products | At least one, with the papers that would support the annotation and the evidence code |
| Why existing terms fail | The candidates you checked, by id, and why each is wrong or too broad |
| Taxon scope | Whether the concept is lineage-restricted, and the constraint that follows |
| Annotations affected | What would move to the new term, if anything |

GOC guidance for ticket writers asks for "what is new, what is wrong, why and how to fix it",
with PMIDs ([go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)),
and the Tips page tells curators to open a go-ontology ticket when a term cannot be found
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).
New term requests remained a high priority for the ontology group in 2024
([wiki: Ontology meeting 2024-01-22](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-22)).

## Application

*Example of a request that clears the bar.* The neural crest work proposes *neural plate
border formation* because `GO:0014029` neural crest formation is defined as forming a region
of ectoderm but placed under epithelial-to-mesenchymal transition, and border specifiers (Gbx2,
Msx1, Pax7) build the border without doing EMT. The proposal names the genes, the papers and
a 94-row per-annotation remapping table for GO. The same project considered terms for
regulation of delamination and regulation of crest migration and did not propose them, because
no annotation cleared the evidence bar ([NEURAL_CREST_FORMATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/NEURAL_CREST_FORMATION_OBSOLETION.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The request contents and the evidence-first test are our sharpening. |
| Date | 2026-11-15 |
| GO terms | `GO:0014029` neural crest formation |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [ONT-11-E1](ONT-11.examples.yaml): A proposed neural plate border formation term for border specifiers such as Pax3 | Conformant | GO:0014029 neural crest formation |
| [ONT-15-E1](ONT-15.examples.yaml): A Pax3 neural crest formation row remapped while the term is proposed for obsoletion (from [ONT-15](ONT-15.md)) | Conformant | pax3-a involved_in GO:0014029 neural crest formation (IGI, PMID:15691759) |

## Sources

- repo: [go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)
- wiki: [Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
- wiki: [Ontology meeting 2024-01-22](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-22)
- web: [NEURAL_CREST_FORMATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/NEURAL_CREST_FORMATION_OBSOLETION.html)

<!-- END GENERATED -->
