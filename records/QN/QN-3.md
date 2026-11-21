---
id: QN-3
title: Use `involved_in` only when the gene product's own activity is a step in the process. Use an `acts_upstream_of...`
  relation for every other causal link, and treat a BP row with no stated relation as `acts_upstream_of_or_within`.
status: proposed
topic: QN
provenance: NEW
provenance_note: '[NEW] for the default reading and the IBA caveat; [GOC] for the relation definitions.
  [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations); [wiki: Acts
  upstream of](https://wiki.geneontology.org/index.php/Acts_upstream_of); [Drive: Annotation relations
  - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc);
  [Drive: Heuristics for gp2term relations](https://drive.google.com/open?id=1GSLdTrBVdSyaWU4R0L3M0Y-rrNRW22aoYFBh_nwAwC0);
  [go-annotation#2377](https://github.com/geneontology/go-annotation/issues/2377).'
evidence_codes:
- IMP
- IBA
- IBD
go_terms:
- term_id: GO:0004842
  label: ubiquitin-protein transferase activity
- term_id: GO:0006511
  label: ubiquitin-dependent protein catabolic process
sources:
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: wiki
  title: 5 May 2020 PAINT Conference Call
  url: https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call
- kind: wiki
  title: Acts upstream of or within
  url: https://wiki.geneontology.org/index.php/Acts_upstream_of_or_within
- kind: issue
  title: go-annotation#2377
  url: https://github.com/geneontology/go-annotation/issues/2377
- kind: wiki
  title: Involved in
  url: https://wiki.geneontology.org/index.php/Involved_in
- kind: wiki
  title: Annotation Relations
  url: https://wiki.geneontology.org/index.php/Annotation_Relations
- kind: wiki
  title: Acts upstream of
  url: https://wiki.geneontology.org/index.php/Acts_upstream_of
- kind: drive
  title: Annotation relations - Guidelines for P2GO
  url: https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc
- kind: drive
  title: Heuristics for gp2term relations
  url: https://drive.google.com/open?id=1GSLdTrBVdSyaWU4R0L3M0Y-rrNRW22aoYFBh_nwAwC0
date: '2026-11-15'
---

# QN-3. Use `involved_in` only when the gene product's own activity is a step in the process. Use an `acts_upstream_of...` relation for every other causal link, and treat a BP row with no stated relation as `acts_upstream_of_or_within`.

## Decision

Use `involved_in` only when the gene product's own activity is a step in the process. Use an `acts_upstream_of...` relation for every other causal link, and treat a BP row with no stated relation as `acts_upstream_of_or_within`.

## Context

The repo's participation test (see [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), "Do not add what curators deliberately declined to add") reads: a gene product is `involved_in` a process only if it does some of the work of that process. Necessity, the kind of evidence a knockout gives, does not meet this test. Mutant phenotypes support `acts_upstream_of_or_within` with a direction. `involved_in` needs to know what the product does and where that activity sits in the process.

The default needs a decision because the sources disagree. The current wiki marks `acts_upstream_of_or_within` as the default BP relation, the least specific one that is always true. The 2021 Protein2GO training and the GOA export defaults use `involved_in`. The 2018 GAF 2.2 draft left the choice to each contributing group. PAINT assigns `involved_in` to every IBD and IBA, whatever relation the seed annotations carried ([wiki: 5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)). We recommend reading an unqualified BP annotation as `acts_upstream_of_or_within`, which is the only reading that cannot be false. A curator asserting `involved_in` must be able to name the MF.

**Rule detail.**

- `involved_in`: you can state the MF, and the MF is `part_of` the process, either in the ontology (transporter activity `part_of` transport) or by evidence that places the activity as a step.
- `acts_upstream_of_or_within, positive effect` / `negative effect`: the default for phenotype-based BP annotation. Always pick a direction when the data show one. The bare relation is a grouping relation and should be rare ([wiki: Acts upstream of or within](https://wiki.geneontology.org/index.php/Acts_upstream_of_or_within)).
- `acts_upstream_of, positive/negative effect`: the mechanism is known, the activity comes earlier, and it is neither a step nor a regulator. Example: an enzyme that produces a precursor consumed by a later, separate process.
- A gene product that regulates X is `involved_in` "regulation of X", not `acts_upstream_of` X. Do not stack a direction relation on a regulation term (`acts_upstream_of, positive effect` "positive regulation of X"): the term already states the direction. This answers the question left open in [go-annotation#2377](https://github.com/geneontology/go-annotation/issues/2377).

## Application

**Examples.**

- NEDD4 `enables` GO:0004842 ubiquitin-protein transferase activity on RNA polymerase II and is `involved_in` GO:0006511 ubiquitin-dependent protein catabolic process ([wiki: Involved in](https://wiki.geneontology.org/index.php/Involved_in)).
- A transcription factor whose knockout reduces T cell numbers, with no target genes identified, is `acts_upstream_of_or_within, positive effect` of the relevant differentiation process, not `involved_in`.
- *IBA reading.* An IBA `involved_in` row inherits that relation from PAINT's default, not from its seeds. If every seed is an IMP phenotype, treat the IBA as `acts_upstream_of_or_within` when judging participation (see [phylogenetic-propagation.md](../PH/README.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] for the default reading and the IBA caveat; [GOC] for the relation definitions. [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations); [wiki: Acts upstream of](https://wiki.geneontology.org/index.php/Acts_upstream_of); [Drive: Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc); [Drive: Heuristics for gp2term relations](https://drive.google.com/open?id=1GSLdTrBVdSyaWU4R0L3M0Y-rrNRW22aoYFBh_nwAwC0); [go-annotation#2377](https://github.com/geneontology/go-annotation/issues/2377). |
| Date | 2026-11-15 |
| Evidence codes | IMP, IBA, IBD |
| GO terms | `GO:0004842` ubiquitin-protein transferase activity; `GO:0006511` ubiquitin-dependent protein catabolic process |

## Sources

- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- wiki: [5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)
- wiki: [Acts upstream of or within](https://wiki.geneontology.org/index.php/Acts_upstream_of_or_within)
- issue: [go-annotation#2377](https://github.com/geneontology/go-annotation/issues/2377)
- wiki: [Involved in](https://wiki.geneontology.org/index.php/Involved_in)
- wiki: [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- wiki: [Acts upstream of](https://wiki.geneontology.org/index.php/Acts_upstream_of)
- drive: [Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- drive: [Heuristics for gp2term relations](https://drive.google.com/open?id=1GSLdTrBVdSyaWU4R0L3M0Y-rrNRW22aoYFBh_nwAwC0)

<!-- END GENERATED -->
