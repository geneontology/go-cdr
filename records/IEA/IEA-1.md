---
id: IEA-1
title: Identify the pipeline before judging the row
status: proposed
topic: IEA
provenance: GOC_PLUS
provenance_note: '[GOC] for the fields; [GOC+] for reading `GO_REF:0000120` as corroboration.'
evidence_codes:
- IEA
go_terms:
- term_id: GO:0005524
  label: ATP binding
sources:
- kind: wiki
  title: IEA
  url: https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29
- kind: wiki
  title: Annotation Assigned by
  url: https://wiki.geneontology.org/index.php/Annotation_Assigned_by
- kind: issue
  title: go-annotation#1386
  url: https://github.com/geneontology/go-annotation/issues/1386
- kind: web
  title: TREEGRAFTER
  url: https://ai4curation.io/ai-gene-review/pages/projects/TREEGRAFTER.html
- kind: web
  title: INTERPRO
  url: https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html
date: '2026-11-15'
---

# IEA-1. Identify the pipeline before judging the row

## Decision

Read the GO_REF, `assigned_by` and `WITH/FROM` of every IEA row before reviewing it. Judge the
claim the pipeline made: the signature, keyword, EC number, reaction, rule or ortholog in
`WITH/FROM` is the premise.

## Context

every IEA must cite a GO_REF and a `WITH/FROM` naming its basis
([wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)).
`assigned_by` credits the group that made the decision (InterPro for InterPro2GO, UniProt for
keyword and HAMAP mappings) ([wiki: Annotation Assigned by](https://wiki.geneontology.org/index.php/Annotation_Assigned_by);
[go-annotation#1386](https://github.com/geneontology/go-annotation/issues/1386)). `GO_REF:0000120`
means two or more pipelines produced the same term, with the contributors listed in `WITH/FROM`; in
the repo's corpus a `GO_REF:0000118` row is therefore a TreeGrafter call no other pipeline
reproduced, and corroborated TreeGrafter calls were accepted 77% of the time against 43% for
uncorroborated ones ([TREEGRAFTER](https://ai4curation.io/ai-gene-review/pages/projects/TREEGRAFTER.html)). Corroboration raises confidence; it does
not make two pipelines independent if they share a training source.

## Application

Worked example: an IEA row of `GO:0005524` ATP binding with `GO_REF:0000002` and
`InterPro:IPR000719` in `WITH/FROM` is a claim that every protein-kinase-domain protein binds ATP.
The same term with `InterPro:IPR017441` is a claim from the kinase ATP-binding-site entry, which
requires the motif. The first fails for pseudokinases; the second does not
([INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the fields; [GOC+] for reading `GO_REF:0000120` as corroboration. |
| Date | 2026-11-15 |
| Evidence codes | IEA |
| GO terms | `GO:0005524` ATP binding |

## Sources

- wiki: [IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)
- wiki: [Annotation Assigned by](https://wiki.geneontology.org/index.php/Annotation_Assigned_by)
- issue: [go-annotation#1386](https://github.com/geneontology/go-annotation/issues/1386)
- web: [TREEGRAFTER](https://ai4curation.io/ai-gene-review/pages/projects/TREEGRAFTER.html)
- web: [INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html)

<!-- END GENERATED -->
