---
id: RS-4
title: Pathway members that activate the next member are part of the pathway, not regulators of it; feedback
  is the exception
status: proposed
topic: RS
provenance: GOC
aspects:
- P
go_terms:
- term_id: GO:0000165
  label: MAPK cascade
- term_id: GO:0043410
  label: positive regulation of MAPK cascade
- term_id: GO:0035329
  label: hippo signaling
sources:
- kind: wiki
  title: Annotating regulation
  url: https://wiki.geneontology.org/index.php/Annotating_regulation
- kind: drive
  title: Ontology development update, SAB 2019
  url: https://drive.google.com/open?id=1csX9z0szrud0-XIUitPR2pesr8ry-0xcTQNkCv5fsHo
- kind: drive
  title: FlyBase pathway curation guide
  url: https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI
- kind: wiki
  title: Signaling Curation Manual
  url: https://wiki.geneontology.org/index.php/Signaling_Curation_Manual
date: '2026-11-15'
---

# RS-4. Pathway members that activate the next member are part of the pathway, not regulators of it; feedback is the exception

## Decision

**Statement.** Do not annotate a component to "positive regulation of P" because it activates the next component of P. Activation is how signalling pathways work. A component may also carry a regulation term for P when it feeds back on an earlier step, as in ERK inhibition of FRS2α, or when its role in P is to restrain P. Do not annotate both "P" and "regulation of P" from the same evidence.

## Context

[wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation), Guideline 6: "MAPKK would not be annotated to positive regulation of MAPKKK cascade just because it phosphorylates and activates MAPK." The ontology made the same correction. GO removed the `regulates o part_of → regulates` property chain because it inferred, for example, that MAPKK activity positively regulates the MAPK cascade ([Drive: Ontology development update, SAB 2019](https://drive.google.com/open?id=1csX9z0szrud0-XIUitPR2pesr8ry-0xcTQNkCv5fsHo)). The FlyBase rules allow a gene product to be both in a pathway and its regulator, as positive and negative regulator in different contexts ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)).

## Application

**Worked examples.**

- MAP2K1: `involved_in` GO:0000165 MAPK cascade. Not GO:0043410 positive regulation of MAPK cascade.
- In canonical Wnt signalling, the destruction complex keeps β-catenin low without a signal, and Wnt inhibits that degradation. Components such as GSK3 are participants in the pathway even though the signal inactivates them ([wiki: Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual), GSK3 example; [Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)). FlyBase likewise puts Yorkie, the transcriptional effector that Hippo signalling retains in the cytoplasm, directly on GO:0035329 hippo signaling.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0000165` MAPK cascade; `GO:0043410` positive regulation of MAPK cascade; `GO:0035329` hippo signaling |

## Sources

- wiki: [Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation)
- drive: [Ontology development update, SAB 2019](https://drive.google.com/open?id=1csX9z0szrud0-XIUitPR2pesr8ry-0xcTQNkCv5fsHo)
- drive: [FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)
- wiki: [Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual)

<!-- END GENERATED -->
