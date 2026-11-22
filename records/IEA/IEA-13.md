---
id: IEA-13
title: When a mapping is wrong, route the fix to the mapping and record it in a form the source can use
status: proposed
topic: IEA
provenance: NEW
evidence_codes:
- IEA
go_terms:
- term_id: GO:0005524
  label: ATP binding
differences:
- prior_source: (no prior GOC guidance)
  prior_said: ''
  we_recommend: Sole-source and rule-cover checks before any mapping removal (IEA-13).
  why: Removals proposed without them would have cost correct annotations (IPR000719 ATP binding).
sources:
- kind: web
  title: INTERPRO README
  url: https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO/README.html#before-proposing-a-removal
- kind: drive
  title: IEA WG pipelines update Sept 2026
  url: https://drive.google.com/open?id=1FQpXSPZdK78X3wX5UEQ9jkFk6Xex0NCi8NeDawOs7IE
- kind: web
  title: INTERPRO
  url: https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html
date: '2026-11-15'
---

# IEA-13. When a mapping is wrong, route the fix to the mapping and record it in a form the source can use

## Decision

Record every proposed mapping change against the entry and term, not only against the gene:
removals and narrowings in the InterPro SSSOM mapping set, rule verdicts in a rule review, PAINT
changes in a family review. Before proposing a removal, run a sole-source check (which reviewed
genes lose the term outright) and a rule-cover check (what else still supplies the term to members
that should keep it).

## Context

a removal drops the term from every matched protein, including those for which it is
right. The repo's protocol asks for the cost to be stated in the row: list reviewed annotations for
which the entry is the only InterPro source and read their review actions; search interpro2go for
other entries carrying the term, the UniRule API for rules (HAMAP, PIRSR, PIRNR, RuleBase can
require a site, exclude a domain or restrict a taxon), and the EC mapping, since many rules assign
an EC number rather than a GO term ([INTERPRO README](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO/README.html#before-proposing-a-removal)).
Then choose: wrong for every member, remove; right for a subset another source covers, remove and
cite the cover; right for a subset nothing covers, remove only with a request for the covering rule,
otherwise propose narrowing. Disputes go through the GitHub trackers, which the IEA working group
kept as the channel for InterPro2GO, ARBA, UniRule and inter-ontology links
([Drive: IEA WG pipelines update Sept 2026](https://drive.google.com/open?id=1FQpXSPZdK78X3wX5UEQ9jkFk6Xex0NCi8NeDawOs7IE)).

## Application

Worked example: removing `GO:0005524` ATP binding from `IPR000719` costs annotations on seven
reviewed genes whose only InterPro source for the term is that entry, and reviewers accepted or kept
all seven. The note on the removal therefore asks for family rules (for example the JNK rule
UR001528758) to cover members without the site motif, rather than presenting the removal as free
([INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html)). For `IPR012724` (Chaperone DnaJ), ATP binding belongs to the Hsp70
partner and HAMAP MF_01152 assigns no ATP-binding term, so the removal needs no cover.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] |
| Date | 2026-11-15 |
| Evidence codes | IEA |
| GO terms | `GO:0005524` ATP binding |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-13-E1](IEA-13.examples.yaml): Narrow, not remove, a mapping that is the sole source of the term | Conformant | InterPro2GO |
| [IEA-13-E2](IEA-13.examples.yaml): Removing protein phosphorylation from the kinase domain, with the cover stated | Conformant | InterPro2GO |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| (no prior GOC guidance) |  | Sole-source and rule-cover checks before any mapping removal (IEA-13). | Removals proposed without them would have cost correct annotations (IPR000719 ATP binding). |

## Sources

- web: [INTERPRO README](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO/README.html#before-proposing-a-removal)
- drive: [IEA WG pipelines update Sept 2026](https://drive.google.com/open?id=1FQpXSPZdK78X3wX5UEQ9jkFk6Xex0NCi8NeDawOs7IE)
- web: [INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html)

<!-- END GENERATED -->
