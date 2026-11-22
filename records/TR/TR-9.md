---
id: TR-9
title: State activator or repressor when the direction at a target is shown; allow both when context changes
  it
status: proposed
topic: TR
provenance: GOC_PLUS
aspects:
- F
- P
evidence_codes:
- IBA
differences:
- prior_source: '[go-annotation#3932](https://github.com/geneontology/go-annotation/issues/3932)'
  prior_said: Use unqualified "regulation of transcription" for dbTFs
  we_recommend: Directional terms for experimental rows with a named target; unqualified for propagated
    rows
  why: The GO-CAM guideline and the activator/repressor MF children assume direction is captured where
    known
sources:
- kind: drive
  title: TF annotation guidelines
  url: https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs
- kind: drive
  title: MF guidelines for GO-CAM
  url: https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4
- kind: issue
  title: go-annotation#3932
  url: https://github.com/geneontology/go-annotation/issues/3932
- kind: web
  title: YEAST_EPIGENETICS_HISTONE_INHERITANCE
  url: https://ai4curation.io/ai-gene-review/pages/projects/YEAST_EPIGENETICS_HISTONE_INHERITANCE.html
date: '2026-11-15'
---

# TR-9. State activator or repressor when the direction at a target is shown; allow both when context changes it

## Decision

Use the activator or repressor child of dbTF activity (or coactivator/corepressor)
when the paper shows the direction of the effect on an identified target. A protein may
carry both, each with its own target or context. When direction is not shown, or the
paper's effect may be indirect, use the unqualified term. Do not infer direction for a
coTF from the class of its chromatin activity alone.

## Context

The archived guideline: dbTFs and coregulators "often act as activators or
repressors in different promoters or dependent on the context, so annotation to both
activator and repressor is not considered inconsistent"
([Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)).
The GO-CAM activity units use the activator and repressor children and capture one target
per activity unit ([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
A PAINT discussion recorded agreement to use the unqualified "regulation of
transcription" for dbTFs, and doubt over whether coTF direction can be read from the
chromatin modification they catalyse
([go-annotation#3932](https://github.com/geneontology/go-annotation/issues/3932)). We
reconcile the two by applying the unqualified term to propagated and family-level rows,
where direction varies between members and targets, and the directional terms to
experimental rows with a target.

## Application

Worked example. Rpd3S complex members (S. cerevisiae RCO1, S. pombe Cph1/Cph2) carry
IBA rows to positive regulation of transcription by RNA polymerase II, although the
complex is a deacetylase that represses cryptic transcription. The direction depends on
the target gene and assay; the RCO1 review modified the broad BP toward the chromatin
mechanism rather than choosing a direction ([YEAST_EPIGENETICS_HISTONE_INHERITANCE](https://ai4curation.io/ai-gene-review/pages/projects/YEAST_EPIGENETICS_HISTONE_INHERITANCE.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Evidence codes | IBA |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [TR-9-E1](TR-9.examples.yaml): Positive regulation from a reporter carrying the target gene's regulatory sites | Conformant | FOXE1 involved_in GO:0045893 positive regulation of DNA-templated transcription (IDA, PMID:9697705) |
| [TR-9-E2](TR-9.examples.yaml): An electronic activator-only row on a MADS factor that both activates and represses | Non-conformant | PI involved_in GO:0045944 positive regulation of transcription by RNA polymerase II (IEA, GO_REF:0000002) |
| [TR-2-E1](TR-2.examples.yaml): An ETS repressor shown to act through its binding site in a reporter (from [TR-2](TR-2.md)) | Conformant | ERF enables GO:0001227 DNA-binding transcription repressor activity, RNA polymerase II-specific (IDA, PMID:7588608) |
| [TR-14-E1](TR-14.examples.yaml): A forkhead activator row with its directly regulated target gene as input (from [TR-14](TR-14.md)) | Conformant | FOXC1 enables GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific (IDA, PMID:17993506) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [go-annotation#3932](https://github.com/geneontology/go-annotation/issues/3932) | Use unqualified "regulation of transcription" for dbTFs | Directional terms for experimental rows with a named target; unqualified for propagated rows | The GO-CAM guideline and the activator/repressor MF children assume direction is captured where known |

## Sources

- drive: [TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)
- drive: [MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)
- issue: [go-annotation#3932](https://github.com/geneontology/go-annotation/issues/3932)
- web: [YEAST_EPIGENETICS_HISTONE_INHERITANCE](https://ai4curation.io/ai-gene-review/pages/projects/YEAST_EPIGENETICS_HISTONE_INHERITANCE.html)

<!-- END GENERATED -->
