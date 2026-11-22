---
id: CC-2
title: Do not make new `colocalizes_with` annotations; resolve existing ones to `located_in`, `is_active_in`,
  a binding term, or removal.
status: proposed
topic: CC
provenance: GOC_PLUS
provenance_note: '[GOC+] GOC deprecated the relation but left the per-row replacement to curators; the
  decision list above is ours, assembled from the three sources.'
aspects:
- C
go_terms:
- term_id: GO:0044877
  label: protein-containing complex binding
differences:
- prior_source: '[Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with) (2018) and
    2023 calls'
  prior_said: Relation deprecated; existing rows "under review"; proposal to migrate automatically to
    `located_in` ([2023-05-16](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-16))
  we_recommend: 'Per-row decision: `is_active_in`, `located_in`, complex binding, or removal (CC-2)'
  why: Automatic migration to `located_in` keeps trafficking-only rows that should go
sources:
- kind: wiki
  title: Colocalizes with
  url: https://wiki.geneontology.org/index.php/Colocalizes_with
- kind: wiki
  title: Annotation Conf. Call 2023-11-28
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-11-28
- kind: issue
  title: go-annotation#1940
  url: https://github.com/geneontology/go-annotation/issues/1940
- kind: drive
  title: Reviewing colocalizes_with annotations
  url: https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o
date: '2026-11-15'
---

# CC-2. Do not make new `colocalizes_with` annotations; resolve existing ones to `located_in`, `is_active_in`, a binding term, or removal.

## Decision

Do not make new `colocalizes_with` annotations; resolve existing ones to `located_in`, `is_active_in`, a binding term, or removal.

## Context

`colocalizes_with` was used for transient or peripheral association and for assays too coarse
to show membership. Curators read it in incompatible ways, and GO now marks it as deprecated
([wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with);
[Annotation Conf. Call 2023-11-28](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-11-28)).
When reviewing an existing row:

- **On a protein-containing complex term**, the 2018 Protein Complex Working Group ruled the
  combination invalid. Replace it with `GO:0044877` protein-containing complex binding (or a
  specific complex-binding child) if there is interaction evidence, or remove it
  ([go-annotation#1940](https://github.com/geneontology/go-annotation/issues/1940)).
- **On a cellular anatomical entity**, ask what the paper showed. If the protein acts there,
  even transiently, the relation is `is_active_in`
  ([wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with)). If it is
  only detected there, `located_in`. If the "colocalization" is a receptor trafficking through
  the endomembrane system with no activity there, remove it (the 2023 Padua breakout's
  "low-hanging fruit": Frizzled, insulin-family and vitellogenin receptors annotated to
  endomembrane system;
  [Drive: Reviewing colocalizes_with annotations](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o)).

In a review YAML, a `colocalizes_with` row is judged as a claim about the location; if the
location stands but the relation is wrong, say so in `reason` and record the corrected
relation (see [qualifiers-and-negation.md](../QN/README.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] GOC deprecated the relation but left the per-row replacement to curators; the decision list above is ours, assembled from the three sources. |
| Date | 2026-11-15 |
| GO terms | `GO:0044877` protein-containing complex binding |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CC-2-E1](CC-2.examples.yaml): A colocalizes_with row on the P-TEFb complex resting on an interaction | Non-conformant | RB1 colocalizes_with GO:0008024 cyclin/CDK positive transcription elongation factor complex (IDA, PMID:12037672) |
| [CC-2-E2](CC-2.examples.yaml): A colocalizes_with lysosome row from marginal marker overlap | Non-conformant | MYO5A colocalizes_with GO:0005764 lysosome (IDA, PMID:24006491) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with) (2018) and 2023 calls | Relation deprecated; existing rows "under review"; proposal to migrate automatically to `located_in` ([2023-05-16](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-16)) | Per-row decision: `is_active_in`, `located_in`, complex binding, or removal (CC-2) | Automatic migration to `located_in` keeps trafficking-only rows that should go |

## Sources

- wiki: [Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with)
- wiki: [Annotation Conf. Call 2023-11-28](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-11-28)
- issue: [go-annotation#1940](https://github.com/geneontology/go-annotation/issues/1940)
- drive: [Reviewing colocalizes_with annotations](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o)

<!-- END GENERATED -->
