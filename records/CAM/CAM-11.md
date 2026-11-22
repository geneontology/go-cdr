---
id: CAM-11
title: Use `removes input for` only for a switch in which the upstream activity uses up the downstream
  activity's input site.
status: proposed
topic: CAM
provenance: GOC
provenance_note: '[GOC]. Source: [wiki: Removes input for](https://wiki.geneontology.org/index.php/Removes_input_for).'
go_terms:
- term_id: GO:0140944
  label: histone H4K20 monomethyltransferase activity
- term_id: GO:0140566
  label: histone reader activity
sources:
- kind: wiki
  title: Removes input for
  url: https://wiki.geneontology.org/index.php/Removes_input_for
date: '2026-11-15'
---

# CAM-11. Use `removes input for` only for a switch in which the upstream activity uses up the downstream activity's input site.

## Decision

Use `removes input for` only for a switch in which the upstream activity uses up the downstream activity's input site.

## Context

`removes input for` applies when both activities act on the same site of the
same target, and the upstream modification makes the site unavailable: the
histone code, the ubiquitin code, CpG methylation blocking TF binding. It does
not apply to an inducible enzyme that degrades a substrate in order to regulate
a pathway; that is regulation.

## Application

*Example.* KMT5A (`GO:0140944` histone H4K20 monomethyltransferase activity)
methylates H4K20 and so removes the input of TONSL's `GO:0140566` histone
reader activity, which binds unmethylated H4K20 (model `623d156d00000817`,
PMID:27338793).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC]. Source: [wiki: Removes input for](https://wiki.geneontology.org/index.php/Removes_input_for). |
| Date | 2026-11-15 |
| GO terms | `GO:0140944` histone H4K20 monomethyltransferase activity; `GO:0140566` histone reader activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CAM-11-E1](CAM-11.examples.yaml): RNF115 ubiquitination of RAB1A and RAB13 removes the input of GDI1 | Conformant | gomodel:65692e7e00001822 |
| [CAM-11-E2](CAM-11.examples.yaml): A coactivator removes input for a ligase, with no shared input stated and no evidence | Non-conformant | gomodel:6606056e00000678 |

## Sources

- wiki: [Removes input for](https://wiki.geneontology.org/index.php/Removes_input_for)

<!-- END GENERATED -->
