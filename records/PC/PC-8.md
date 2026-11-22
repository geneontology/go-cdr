---
id: PC-8
title: Annotate subunits to the complex-level activity, not to its substeps; a subunit that catalyses
  a half-reaction on its own may `enable` the parent term.
status: proposed
topic: PC
provenance: GOC_PLUS
aspects:
- C
- F
go_terms:
- term_id: GO:0008177
  label: succinate dehydrogenase (quinone) activity
- term_id: GO:0000104
  label: succinate dehydrogenase activity
differences:
- prior_source: '[SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html)
    vs [#6357](https://github.com/geneontology/go-annotation/issues/6357)'
  prior_said: 'Repo: SDHA `enables GO:0000104` defensible; GO: all four subunits contribute and substeps
    are not captured'
  we_recommend: Complex activity for all; `enables` on a half-reaction parent only when the subunit performs
    it alone, pending GO decision (PC-8)
  why: GO's answer addresses `GO:0008177`; it does not say whether an independently measurable parent
    activity counts as a substep
sources:
- kind: issue
  title: go-annotation#6357
  url: https://github.com/geneontology/go-annotation/issues/6357
- kind: web
  title: SDH_GP2TERM_CONTRIBUTES_TO
  url: https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html
- kind: issue
  title: go-annotation#1487
  url: https://github.com/geneontology/go-annotation/issues/1487
date: '2026-11-15'
---

# PC-8. Annotate subunits to the complex-level activity, not to its substeps; a subunit that catalyses a half-reaction on its own may `enable` the parent term.

## Decision

Annotate subunits to the complex-level activity, not to its substeps; a subunit that catalyses a half-reaction on its own may `enable` the parent term.

## Context

For complex II, GO's position in 2026 is that SdhA, SdhB, SdhC and SdhD each contribute to
`GO:0008177`, and the individual reactions (succinate oxidation, electron tunnelling, quinone
reduction) "should not be captured, as they correspond to substeps"
([go-annotation#6357](https://github.com/geneontology/go-annotation/issues/6357)). This keeps
subunits of one machine consistent and avoids inventing MF terms for partial reactions.

There is one principled exception. SDHA, the flavoprotein, can oxidise succinate with an
artificial acceptor in isolation. That is the parent `GO:0000104` succinate dehydrogenase
activity (succinate + acceptor = fumarate + reduced acceptor). `enables GO:0000104` on SDHA is
defensible because the subunit performs that activity on its own, which is the test for
`enables`. The repo treats this as unresolved
([SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html)); see Open questions.

`contributes_to` qualifies MF annotations only. A `contributes_to` on a CC or BP term is a data
error; one 2017 audit found such rows produced by inference pipelines
([go-annotation#1487](https://github.com/geneontology/go-annotation/issues/1487)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| GO terms | `GO:0008177` succinate dehydrogenase (quinone) activity; `GO:0000104` succinate dehydrogenase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [PC-8-E1](PC-8.examples.yaml): SDHA given the parent succinate dehydrogenase activity for its isolated half-reaction | Contested | SDHA GO:0000104 succinate dehydrogenase activity (IDA, PMID:7550341) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html) vs [#6357](https://github.com/geneontology/go-annotation/issues/6357) | Repo: SDHA `enables GO:0000104` defensible; GO: all four subunits contribute and substeps are not captured | Complex activity for all; `enables` on a half-reaction parent only when the subunit performs it alone, pending GO decision (PC-8) | GO's answer addresses `GO:0008177`; it does not say whether an independently measurable parent activity counts as a substep |

## Sources

- issue: [go-annotation#6357](https://github.com/geneontology/go-annotation/issues/6357)
- web: [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html)
- issue: [go-annotation#1487](https://github.com/geneontology/go-annotation/issues/1487)

<!-- END GENERATED -->
