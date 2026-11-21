---
id: PIPE
title: Rubrics for annotation pipelines
record_kind: rubric
applies_to:
- pipeline
status: proposed
sources:
- kind: drive
  title: GO annotation pipeline proposed rubrics and MOU (GOC meeting, Cambridge 2025)
  url: https://docs.google.com/presentation/d/1YudLhxPskOiptyhBkUo5sN6GkMjQWB4PIdM0_dNSZkw/edit
date: '2026-11-21'
open_questions:
- Which rubrics are the minimal criteria (MUST) for a pipeline to enter or stay in GO? Responsivity and
  Currency are proposed; what else?
- Should GO adopt shared redundancy rules for pipelines, and may they vary by taxon?
- Should each rubric carry a weight, as in the OBO Foundry dashboard, so that pipelines can be scored?
---

# Rubrics for annotation pipelines

GO already integrates many automated annotation pipelines, and there will be many more,
including AI pipelines. Decisions on including or excluding a pipeline have been made one
at a time. A shared set of rubrics makes those decisions consistent, efficient and
transparent to users. Each record in this chapter is one rubric; a pipeline signs off on
each in its file under `groups/`.

The model is the OBO Foundry dashboard: a set of principles, each checked separately and
each possibly weighted differently.

## How pipelines are chosen

Two approaches were considered:

- **"A thousand flowers"**: each group picks which pipelines to show. This confuses users,
  is inefficient and is unprincipled.
- **Co-curated selection**: the same GO inferences are shown for every GOC member. This is
  the proposal.

Entry and removal both have a high bar ("a puppy is for life"): adding a pipeline to
production is a long-term commitment and should not surprise users, and the same reasons
argue for care before removing one.

A joint annotation pipeline committee with members from across the GOC would define the
criteria, separating MUST from SHOULD.

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [PIPE-1](PIPE-1.md) | Responsivity: respond to curator issues in a timely way | proposed | [NEW] |
| [PIPE-2](PIPE-2.md) | Currency: rebuild and re-run the pipeline regularly | proposed | [NEW] |
| [PIPE-3](PIPE-3.md) | Conformance: follow all GO rules | proposed | [NEW] |
| [PIPE-4](PIPE-4.md) | Provenance: supply the complete inference chain | proposed | [NEW] |
| [PIPE-5](PIPE-5.md) | Biological explainability: explain each inference in known terms | proposed | [NEW] |
| [PIPE-6](PIPE-6.md) | Documentation: keep the GO_REF metadata complete and current | proposed | [NEW] |
| [PIPE-7](PIPE-7.md) | Benchmarking: evaluate against a consortium benchmark before release | proposed | [NEW] |
| [PIPE-8](PIPE-8.md) | Uniqueness: complement the existing pipelines | proposed | [NEW] |

<!-- END GENERATED RECORD INDEX -->

See also the guideline chapter on electronic annotation, especially
[IEA-16](../IEA/IEA-16.md), which applies a rubric to new prediction pipelines.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Open questions

1. Which rubrics are the minimal criteria (MUST) for a pipeline to enter or stay in GO? Responsivity and Currency are proposed; what else?
2. Should GO adopt shared redundancy rules for pipelines, and may they vary by taxon?
3. Should each rubric carry a weight, as in the OBO Foundry dashboard, so that pipelines can be scored?

## Sources

- drive: [GO annotation pipeline proposed rubrics and MOU (GOC meeting, Cambridge 2025)](https://docs.google.com/presentation/d/1YudLhxPskOiptyhBkUo5sN6GkMjQWB4PIdM0_dNSZkw/edit)

<!-- END GENERATED -->
