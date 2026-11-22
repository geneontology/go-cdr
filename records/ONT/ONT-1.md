---
id: ONT-1
title: Read the definition and the parents, not the label
status: proposed
topic: ONT
provenance: GOC
go_terms:
- term_id: GO:0140309
  label: unfolded protein holdase activity
- term_id: GO:0140597
  label: protein carrier activity
- term_id: GO:0102545
  label: B-type glycerophospholipase activity
differences:
- prior_source: '[wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion)'
  prior_said: Relabelling without a change of meaning keeps the id
  we_recommend: Same, and treat a relabel as a prompt to re-read the definition, because labels can drift
    away from definitions
  why: '`GO:0140309`''s new label invites a use its definition excludes ([ONT-1](ONT-1.md))'
sources:
- kind: wiki
  title: Ontology meeting 2024-01-22
  url: https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-22
- kind: web
  title: UNFOLDED_PROTEIN_BINDING
  url: https://ai4curation.io/ai-gene-review/pages/projects/UNFOLDED_PROTEIN_BINDING.html
- kind: web
  title: OVER_ANNOTATION_PATTERNS
  url: https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html
- kind: wiki
  title: Tips to Produce High Quality Annotations
  url: https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations
date: '2026-11-15'
---

# ONT-1. Read the definition and the parents, not the label

## Decision

Before annotating to a term, migrating to it, or arguing that it fits or does not, read its
current definition and its `is_a`/`part_of` parents. A label change does not change scope.

## Context

GO relabels terms to match community usage or to fix a misleading name, and it records the
old label as a synonym. When a label and definition disagree, the GOC's 2024 ontology call
agreed to keep the community label, add a systematic synonym, and add a curator note not to
annotate to the label ([wiki: Ontology meeting 2024-01-22](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-22)).
The definition governs.

## Application

*Example.* `GO:0140309` was relabelled "unfolded protein holdase activity". Its definition
still describes a protein carrier that binds an unfolded protein "and escorts it to an
acceptor molecule or to a specific location", and its parent is `GO:0140597` protein carrier
activity (both verified). It fits carrier-holdases such as the small TIMs, SecB and Skp. It
does not fit in-situ holdases such as the small heat shock proteins, which prevent
aggregation in place. Reading the new label as a general holdase term is the error this rule
exists to prevent, and it was made and caught in this repository
([UNFOLDED_PROTEIN_BINDING](https://ai4curation.io/ai-gene-review/pages/projects/UNFOLDED_PROTEIN_BINDING.html)).

*Example.* `GO:0102545` now carries the label "B-type glycerophospholipase activity"; older
pages cite it as "phospholipase B activity" ([OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html),
pattern 2). The definition, cleavage at both sn-1 and sn-2, is what to check against the
enzyme's data.

The GOC's Tips page makes the same point for parents: `DNA translocase activity` is a kind of
DNA-dependent ATPase, which the label does not reveal
([wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0140309` unfolded protein holdase activity; `GO:0140597` protein carrier activity; `GO:0102545` B-type glycerophospholipase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [ONT-1-E1](ONT-1.examples.yaml): A migrated holdase row on a zebrafish alpha-crystallin judged against the term's definition | Conformant | cryabb enables GO:0140309 unfolded protein holdase activity (IDA, PMID:16420472) |
| [ONT-1-E2](ONT-1.examples.yaml): SecB's unfolded protein binding moved to the carrier-holdase term | Conformant | SecB enables GO:0051082 unfolded protein binding (IBA, GO_REF:0000033) |
| [ONT-1-E3](ONT-1.examples.yaml): A small heat shock protein's unfolded protein binding moved to the carrier-holdase term | Contested | Hsp22 enables GO:0051082 unfolded protein binding (IDA, PMID:16572729) |
| [ONT-13-E1](ONT-13.examples.yaml): A zebrafish alpha-crystallin holdase row moved to an NTR placeholder (from [ONT-13](ONT-13.md)) | Conformant | cryaba enables GO:0140309 unfolded protein holdase activity (IDA, PMID:15692462) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion) | Relabelling without a change of meaning keeps the id | Same, and treat a relabel as a prompt to re-read the definition, because labels can drift away from definitions | `GO:0140309`'s new label invites a use its definition excludes ([ONT-1](ONT-1.md)) |

## Sources

- wiki: [Ontology meeting 2024-01-22](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-22)
- web: [UNFOLDED_PROTEIN_BINDING](https://ai4curation.io/ai-gene-review/pages/projects/UNFOLDED_PROTEIN_BINDING.html)
- web: [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)
- wiki: [Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)

<!-- END GENERATED -->
