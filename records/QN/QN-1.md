---
id: QN-1
title: Every annotation must carry an explicit relation that matches its aspect and term type.
status: proposed
topic: QN
provenance: GOC
provenance_note: '[GOC]. [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations);
  [wiki: Located in](https://wiki.geneontology.org/index.php/Located_in); [Drive: Feedback on GO rules
  (FlyBase copy)](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM).'
go_terms:
- term_id: GO:0032991
  label: protein-containing complex
- term_id: GO:0005739
  label: mitochondrion
sources:
- kind: wiki
  title: Annotation Relations
  url: https://wiki.geneontology.org/index.php/Annotation_Relations
- kind: wiki
  title: Located in
  url: https://wiki.geneontology.org/index.php/Located_in
- kind: drive
  title: Feedback on GO rules (FlyBase copy)
  url: https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM
date: '2026-11-15'
---

# QN-1. Every annotation must carry an explicit relation that matches its aspect and term type.

## Decision

Every annotation must carry an explicit relation that matches its aspect and term type.

## Context

Since GAF 2.2 and GPAD 2.0, column 4 always holds a relation. A relation from the wrong aspect, or `located_in`/`is_active_in` on a complex term, is malformed. gorule-0000061 repairs some cases, but repair is not the same as a curator's statement.

**Rule detail.** MF terms take `enables` or `contributes_to`. BP terms take `involved_in` or one of the six `acts_upstream_of...` relations. CC terms below GO:0032991 protein-containing complex take `part_of`. Other CC terms take `located_in` or `is_active_in`. Protein complexes are not annotation subjects for `part_of GO:0032991` or its descendants (gorule-0000039): a complex is not a member of itself, so annotate the individual proteins.

## Application

**Example.** A row "UniProtKB:Q15526 SURF1 `located_in` GO:0005739 mitochondrion" is well-formed. "SDHB `located_in` respiratory chain complex II" is not: complex membership is `part_of`.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC]. [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations); [wiki: Located in](https://wiki.geneontology.org/index.php/Located_in); [Drive: Feedback on GO rules (FlyBase copy)](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM). |
| Date | 2026-11-15 |
| GO terms | `GO:0032991` protein-containing complex; `GO:0005739` mitochondrion |

## Sources

- wiki: [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- wiki: [Located in](https://wiki.geneontology.org/index.php/Located_in)
- drive: [Feedback on GO rules (FlyBase copy)](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM)

<!-- END GENERATED -->
