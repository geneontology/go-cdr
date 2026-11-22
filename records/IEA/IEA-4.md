---
id: IEA-4
title: Never map to root, do-not-annotate, binding-only or obsolete terms
status: proposed
topic: IEA
provenance: GOC
evidence_codes:
- ND
- IEA
go_terms:
- term_id: GO:0003674
  label: molecular_function
- term_id: GO:0008150
  label: biological_process
- term_id: GO:0005575
  label: cellular_component
- term_id: GO:0005515
  label: protein binding
- term_id: GO:0006139
  label: nucleobase-containing compound metabolic process
sources:
- kind: issue
  title: go-annotation#1020
  url: https://github.com/geneontology/go-annotation/issues/1020
- kind: drive
  title: Best practices for predicting GO data
  url: https://drive.google.com/open?id=1z-6rNJ4tg3M-Ant-2kqDXohPZUlkw9GEZ5qlNZDYj18
- kind: issue
  title: go-annotation#1887
  url: https://github.com/geneontology/go-annotation/issues/1887
- kind: drive
  title: IEA WG pipelines update GOC 2026
  url: https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y
- kind: issue
  title: go-annotation#5902
  url: https://github.com/geneontology/go-annotation/issues/5902
date: '2026-11-15'
---

# IEA-4. Never map to root, do-not-annotate, binding-only or obsolete terms

## Decision

A mapping must not target a GO root (`GO:0003674`, `GO:0008150`, `GO:0005575`), any term in
`gocheck_do_not_annotate` or `gocheck_obsoletion_candidate`, `GO:0005515` protein binding, or an
obsolete term. A mapping file that cannot keep its targets current should be retired.

## Context

root-term annotations may only use ND, and InterPro runs a pre-release check against
root mappings ([go-annotation#1020](https://github.com/geneontology/go-annotation/issues/1020)).
Predictions to do-not-annotate and obsoletion-candidate terms are excluded in GO's guidance for
external predictors ([Drive: Best practices for predicting GO data](https://drive.google.com/open?id=1z-6rNJ4tg3M-Ant-2kqDXohPZUlkw9GEZ5qlNZDYj18);
a legacy draft of the published external-guidelines page). When "biological regulation" and the
generic regulation terms became not-for-direct-annotation, InterPro2GO and UniRule mappings had to
be fixed as well as manual rows ([go-annotation#1887](https://github.com/geneontology/go-annotation/issues/1887)).
The UniPathway mapping file contains many obsolete terms and has not been maintained since 2015,
which is part of why it is being retired
([Drive: IEA WG pipelines update GOC 2026](https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y)).

## Application

Worked example: ARBA00026572 put `GO:0006139` nucleobase-containing compound metabolic process on
over 36,000 proteins, including *S. pombe* rib2, whose substrate is a flavin, not a nucleobase. The
curator asked for the term to be flagged do-not-annotate ([go-annotation#5902](https://github.com/geneontology/go-annotation/issues/5902));
in the current ontology it is in `gocheck_do_not_annotate`, so no mapping or rule should target it.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | ND, IEA |
| GO terms | `GO:0003674` molecular_function; `GO:0008150` biological_process; `GO:0005575` cellular_component; `GO:0005515` protein binding; `GO:0006139` nucleobase-containing compound metabolic process |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-4-E1](IEA-4.examples.yaml): ARBA rule targeting an obsolete lipid X process term | Non-conformant | LPXC1 involved_in GO:2001289 lipid X metabolic process (IEA, GO_REF:0000117) |
| [IEA-4-E2](IEA-4.examples.yaml): A withdrawn ARBA rule whose only consequent is an obsolete term | Non-conformant | ARBA |

## Sources

- issue: [go-annotation#1020](https://github.com/geneontology/go-annotation/issues/1020)
- drive: [Best practices for predicting GO data](https://drive.google.com/open?id=1z-6rNJ4tg3M-Ant-2kqDXohPZUlkw9GEZ5qlNZDYj18)
- issue: [go-annotation#1887](https://github.com/geneontology/go-annotation/issues/1887)
- drive: [IEA WG pipelines update GOC 2026](https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y)
- issue: [go-annotation#5902](https://github.com/geneontology/go-annotation/issues/5902)

<!-- END GENERATED -->
