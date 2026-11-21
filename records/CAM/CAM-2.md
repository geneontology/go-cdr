---
id: CAM-2
title: Give a gene product a second activity node only when the function, input, location, process or
  time differs.
status: proposed
topic: CAM
provenance: GOC_PLUS
provenance_note: '[GOC] for the five criteria; [GOC+] for the ban on activation-state chains, which the
  guideline implies but does not state.'
go_terms:
- term_id: GO:0004714
  label: transmembrane receptor protein tyrosine kinase activity
related:
- CAM-5
- CAM-8
sources:
- kind: drive
  title: GO-CAM modeling guidelines
  url: https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA
- kind: repo
  title: gocam_lint
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/gocam_lint.md
date: '2026-11-15'
---

# CAM-2. Give a gene product a second activity node only when the function, input, location, process or time differs.

## Decision

Give a gene product a second activity node only when the function, input, location, process or time differs.

## Context

A protein that is phosphorylated, moves, or changes partners does not
automatically get a new node. Create one when at least one of these differs:
the MF term; the `has input`; the `occurs in` chain; the `part of` chain; the
`happens during` value. Otherwise reuse the node.

The converse also holds: do not chain two nodes of one gene product with a
causal edge to represent an activation state (inactive kinase, then active
kinase). A state change caused by another gene product is an incoming edge on
one node. `gocam-lint` reports such chains as `same_gene_chain` (WARNING when
the MF repeats in one location) and duplicate nodes as `duplicate_activity`.

## Application

*Example.* A receptor tyrosine kinase that both binds its ligand and
phosphorylates an adaptor is one node, `GO:0004714` transmembrane receptor
protein tyrosine kinase activity, with `has input` the adaptor; the ligand
arrives on an incoming causal edge (CAM-5, CAM-8). A kinase that phosphorylates
two different substrates in two different processes is two nodes.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the five criteria; [GOC+] for the ban on activation-state chains, which the guideline implies but does not state. |
| Date | 2026-11-15 |
| Related | [CAM-5](CAM-5.md), [CAM-8](CAM-8.md) |
| GO terms | `GO:0004714` transmembrane receptor protein tyrosine kinase activity |

## Sources

- drive: [GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)
- repo: [gocam_lint](https://github.com/ai4curation/ai-gene-review/blob/main/docs/gocam_lint.md)

<!-- END GENERATED -->
