---
id: IEA-14
title: Use a curated conditional rule when only a condition can separate right from wrong members
status: proposed
topic: IEA
provenance: NEW
evidence_codes:
- IEA
go_terms:
- term_id: GO:0007034
  label: vacuolar transport
- term_id: GO:0006511
  label: ubiquitin-dependent protein catabolic process
- term_id: GO:0044548
  label: S100 protein binding
differences:
- prior_source: (no prior GOC guidance)
  prior_said: ''
  we_recommend: Curated conditional rules that couple a sequence condition with a taxon, module or feature
    condition and name the mapping they replace (IEA-14).
  why: interpro2go cannot express conditions; GOA's taxon transformations were ad hoc and never published
    as rules.
sources:
- kind: wiki
  title: Planned changes to the IEA GO_REFs cited by UniProtKB
  url: https://wiki.geneontology.org/index.php/Planned_changes_to_the_IEA_GO_REFs_cited_by_UniProtKB.
- kind: repo
  title: rules/curated README
  url: https://github.com/ai4curation/ai-gene-review/blob/main/rules/curated/README.md
date: '2026-11-15'
---

# IEA-14. Use a curated conditional rule when only a condition can separate right from wrong members

## Decision

When a mapping is right for some members and wrong for others, and a taxon, module context or
sequence feature separates them, write a curated rule that couples the sequence condition with the
restricting condition and names the mapping it replaces. When the term is wrong for every member,
record a removal instead.

## Context

interpro2go has no conditions, so a taxon-dependent or context-dependent truth cannot be
expressed in it. GOA has long transformed or filtered taxon-violating IEAs (for example viral
proteins matched to `nucleus`) for the same reason ([wiki: Planned changes to the IEA GO_REFs cited by UniProtKB](https://wiki.geneontology.org/index.php/Planned_changes_to_the_IEA_GO_REFs_cited_by_UniProtKB.);
archived). This repository's `CuratedRule` records make the condition explicit and auditable
([rules/curated README](https://github.com/ai4curation/ai-gene-review/blob/main/rules/curated/README.md)). A rule fires when any condition set holds;
a set holds when all its conditions hold. Every set needs a non-negated sequence-feature condition;
taxon and module conditions only restrict. Module conditions are exclusion-only: they block an
annotation only where the module is shown to be unsatisfiable in a complete proteome, because a
missing component may be a detection gap. Choose the condition that actually separates right from
wrong: a taxon when a whole lineage lacks the prerequisite and the taxon is an exact proxy; a module
when a taxon only approximates the prerequisite; a sequence feature when paralogs share a genome.

## Application

Worked examples: CR-0001 assigns `GO:0007034` vacuolar transport on `IPR005024` AND Eukaryota,
replacing the unconditional interpro2go row, because only eukaryotes have a vacuole. CR-0003 assigns
`GO:0006511` ubiquitin-dependent protein catabolic process on `IPR000426` unless the ubiquitin relay
module is unsatisfiable in the organism, since some archaea may have a ubiquitin-like conjugation
system. CR-0005 restricts `GO:0044548` S100 protein binding on `IPR037893` to Chordata
([rules/curated README](https://github.com/ai4curation/ai-gene-review/blob/main/rules/curated/README.md)). Before choosing a module condition over a
taxon, count what each keeps and drops: CR-0003 keeps 149 archaeal annotations on unevaluated
proteomes although the relay was found in 3 of 504 complete ones.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| Evidence codes | IEA |
| GO terms | `GO:0007034` vacuolar transport; `GO:0006511` ubiquitin-dependent protein catabolic process; `GO:0044548` S100 protein binding |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-14-E1](IEA-14.examples.yaml): Sevenless binding restricted by a second family entry and Diptera | Conformant | curated rules (ai-gene-review rules/curated) |
| [IEA-14-E2](IEA-14.examples.yaml): Malonyl-CoA reductase separated from its same-genome paralog by a CDD model | Conformant | curated rules (ai-gene-review rules/curated) |
| [IEA-2-E2](IEA-2.examples.yaml): A PRINTS fingerprint carries sevenless binding to a mouse GPRC5 receptor (from [IEA-2](IEA-2.md)) | Non-conformant | Gprc5c enables GO:0005118 sevenless binding (IEA, GO_REF:0000002) |
| [IEA-13-E1](IEA-13.examples.yaml): Narrow, not remove, a mapping that is the sole source of the term (from [IEA-13](IEA-13.md)) | Conformant | InterPro2GO |
| [PIPE-3-E2](../PIPE/PIPE-3.examples.yaml): A curated rule checked against the taxon constraint of its process term (from [PIPE-3](../PIPE/PIPE-3.md)) | Conformant | curated rules (ai-gene-review rules/curated) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| (no prior GOC guidance) |  | Curated conditional rules that couple a sequence condition with a taxon, module or feature condition and name the mapping they replace (IEA-14). | interpro2go cannot express conditions; GOA's taxon transformations were ad hoc and never published as rules. |

## Sources

- wiki: [Planned changes to the IEA GO_REFs cited by UniProtKB](https://wiki.geneontology.org/index.php/Planned_changes_to_the_IEA_GO_REFs_cited_by_UniProtKB.)
- repo: [rules/curated README](https://github.com/ai4curation/ai-gene-review/blob/main/rules/curated/README.md)

<!-- END GENERATED -->
