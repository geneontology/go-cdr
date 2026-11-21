---
id: AE-7
title: Use `happens_during` only for a biological phase or life stage, never for a process that merely
  coincides.
status: proposed
topic: AE
provenance: GOC
go_terms:
- term_id: GO:0044848
  label: biological phase
- term_id: GO:0000090
  label: mitotic anaphase
- term_id: GO:0000084
  label: mitotic S phase
sources:
- kind: wiki
  title: Happens during
  url: https://wiki.geneontology.org/index.php/Happens_during
date: '2026-11-15'
---

# AE-7. Use `happens_during` only for a biological phase or life stage, never for a process that merely coincides.

## Decision

Use `happens_during` only for a biological phase or life stage, never for a process that merely coincides.

## Context

`happens_during` was once used to attach a co-occurring process when the gene product's role in it was unclear. The wiki has withdrawn that use. A function that is definitely part of a process takes `part_of`. One that only coincides with a process gets no extension ([wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during)).

**Allowed fillers.** Descendants of GO:0044848 biological phase (for example GO:0000090 mitotic anaphase, GO:0000084 mitotic S phase) and of UBERON:0000105 life cycle stage, or a species stage ontology.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0044848` biological phase; `GO:0000090` mitotic anaphase; `GO:0000084` mitotic S phase |

## Sources

- wiki: [Happens during](https://wiki.geneontology.org/index.php/Happens_during)

<!-- END GENERATED -->
