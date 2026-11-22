---
id: MO-3
title: Do not annotate a host gene product to a viral or symbiont process because the symbiont uses it.
status: proposed
topic: MO
provenance: GOC_PLUS
provenance_note: '[GOC+]. Earlier discussion conflicts: a 2016 comment recalled a decision allowing host
  proteins "co-opted for the parasitic process" ([go-annotation#1367](https://github.com/geneontology/go-annotation/issues/1367)),
  while the 2003, 2017 and 2018 threads and the 2021 working group took the opposite view. We take the
  stricter view; see Differences and Open questions.'
evidence_codes:
- IDA
go_terms:
- term_id: GO:0016032
  label: viral process
- term_id: GO:0019058
  label: viral life cycle
- term_id: GO:0075522
  label: IRES-dependent viral translational initiation
- term_id: GO:0046718
  label: symbiont entry into host cell
- term_id: GO:0001618
  label: virus receptor activity
differences:
- prior_source: '[go-annotation#1367](https://github.com/geneontology/go-annotation/issues/1367) (2016)
    vs [go-annotation#1](https://github.com/geneontology/go-annotation/issues/1), [#1507](https://github.com/geneontology/go-annotation/issues/1507),
    [#1891](https://github.com/geneontology/go-annotation/issues/1891)'
  prior_said: '2016: host proteins co-opted for a parasitic process may be annotated to it. Other threads:
    host proteins should not carry viral-process terms.'
  we_recommend: Do not annotate co-opted host proteins to symbiont processes; host-side regulation and
    defence terms remain (MO-3).
  why: 'The sources conflict. The 2021 working group''s first aim (normal functions only) and the annotation
    counts in #3814 support the stricter reading. A 2021 call raised a possible exception (T7 using host
    thioredoxin as a processivity factor); see Open questions.'
sources:
- kind: issue
  title: go-annotation#1507
  url: https://github.com/geneontology/go-annotation/issues/1507
- kind: issue
  title: go-annotation#1367
  url: https://github.com/geneontology/go-annotation/issues/1367
- kind: issue
  title: go-annotation#1
  url: https://github.com/geneontology/go-annotation/issues/1
- kind: issue
  title: go-annotation#1891
  url: https://github.com/geneontology/go-annotation/issues/1891
- kind: drive
  title: Combined multiorg + immune system process call 2021-11-22
  url: https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so
date: '2026-11-15'
---

# MO-3. Do not annotate a host gene product to a viral or symbiont process because the symbiont uses it.

## Decision

Do not annotate a host gene product to a viral or symbiont process because the symbiont uses it.

## Context

Host translation factors used for viral IRES-driven translation, host
transcription factors that transcribe a viral genome, host receptors a virus
enters through: each keeps its normal host function. Do not annotate them to
`GO:0016032` viral process, `GO:0019058` viral life cycle, `GO:0075522`
IRES-dependent viral translational initiation, `GO:0046718` symbiont entry into
host cell or other symbiont-process terms. Record the dependence on the
symbiont side, as an input of the viral protein's activity, or in a GO-CAM
that shows both.

For a host surface protein that a virus binds to enter, the MF `GO:0001618`
virus receptor activity is available. It is a binding term (its parent is
exogenous protein binding), not a receptor activity in the signalling sense.
Keep it as non-core when a direct binding or entry assay supports it; the
host protein's core function is its normal one.

## Application

In reviews, an existing host annotation to a symbiont-process term is
`MARK_AS_OVER_ANNOTATED` when it rests on an experiment (the curator saw real
data about the virus), and `REMOVE` when it comes from an electronic mapping or
propagation (a UniProt keyword such as KW-0945 Host-virus interaction once
mapped every tagged human protein to viral process).

*Example.* Human SSB and PCBP2 carried IDA annotations to `GO:0075522`
IRES-dependent viral translational initiation, which then implied a role in
host translation. Neither is a viral translation factor in the host's own
biology
([go-annotation#1507](https://github.com/geneontology/go-annotation/issues/1507)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. Earlier discussion conflicts: a 2016 comment recalled a decision allowing host proteins "co-opted for the parasitic process" ([go-annotation#1367](https://github.com/geneontology/go-annotation/issues/1367)), while the 2003, 2017 and 2018 threads and the 2021 working group took the opposite view. We take the stricter view; see Differences and Open questions. |
| Date | 2026-11-15 |
| Evidence codes | IDA |
| GO terms | `GO:0016032` viral process; `GO:0019058` viral life cycle; `GO:0075522` IRES-dependent viral translational initiation; `GO:0046718` symbiont entry into host cell; `GO:0001618` virus receptor activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [MO-3-E1](MO-3.examples.yaml): A host corepressor bound by E1A, kept off viral genome replication | Conformant | CTBP1 involved_in GO:0019079 viral genome replication (TAS, PMID:7479821) |
| [MO-3-E2](MO-3.examples.yaml): An inferred symbiont-entry row on CDK1 | Non-conformant | CDK1 involved_in GO:0046718 symbiont entry into host cell (IEA, GO_REF:0000108) |
| [MO-3-E3](MO-3.examples.yaml): CD4 kept on symbiont entry into host cell because it does the first step of HIV entry | Contested | CD4 involved_in GO:0046718 symbiont entry into host cell (IDA, PMID:9641677) |
| [MO-1-E2](MO-1.examples.yaml): A bacterial host factor annotated to the phage's own transcription process (from [MO-1](MO-1.md)) | Non-conformant | PSPPH_4093 acts_upstream_of_or_within_positive_effect GO:0039696 RNA-templated viral transcription (IDA, PMID:18836083) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [go-annotation#1367](https://github.com/geneontology/go-annotation/issues/1367) (2016) vs [go-annotation#1](https://github.com/geneontology/go-annotation/issues/1), [#1507](https://github.com/geneontology/go-annotation/issues/1507), [#1891](https://github.com/geneontology/go-annotation/issues/1891) | 2016: host proteins co-opted for a parasitic process may be annotated to it. Other threads: host proteins should not carry viral-process terms. | Do not annotate co-opted host proteins to symbiont processes; host-side regulation and defence terms remain (MO-3). | The sources conflict. The 2021 working group's first aim (normal functions only) and the annotation counts in #3814 support the stricter reading. A 2021 call raised a possible exception (T7 using host thioredoxin as a processivity factor); see Open questions. |

## Sources

- issue: [go-annotation#1507](https://github.com/geneontology/go-annotation/issues/1507)
- issue: [go-annotation#1367](https://github.com/geneontology/go-annotation/issues/1367)
- issue: [go-annotation#1](https://github.com/geneontology/go-annotation/issues/1)
- issue: [go-annotation#1891](https://github.com/geneontology/go-annotation/issues/1891)
- drive: [Combined multiorg + immune system process call 2021-11-22](https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so)

<!-- END GENERATED -->
