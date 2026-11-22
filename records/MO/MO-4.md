---
id: MO-4
title: A symbiont term requires that the symbiont product evolved to cause the effect; being recognised
  is not a symbiont process.
status: proposed
topic: MO
provenance: GOC_PLUS
go_terms:
- term_id: GO:0044416
  obsolete: true
- term_id: GO:0080185
  label: effector-mediated activation of plant hypersensitive response by symbiont
- term_id: GO:0052170
  label: symbiont-mediated suppression of host innate immune response
differences:
- prior_source: Pre-2021 ontology
  prior_said: '"induction by symbiont of host defense response" and similar terms were available.'
  we_recommend: Never annotate a symbiont product to activation of host immunity because it is recognised
    (MO-4).
  why: Obsoleted by the working group (`GO:0044416` is obsolete).
- prior_source: '[Drive: Intro - Host-Pathogen interaction session](https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70)
    (2021)'
  prior_said: Kept an effector-mediated term for deliberate induction of plant hypersensitive response
    (`GO:0080185`) as the exception.
  we_recommend: Use it only for effectors whose evolved role is induction, and request a move out from
    under suppression (MO-4).
  why: The current ontology places `GO:0080185` under `GO:0052170` symbiont-mediated suppression of host
    innate immune response, so every annotation inherits a contradictory claim.
sources:
- kind: web
  title: PLANT_FUNGAL_INTERACTIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/PLANT_FUNGAL_INTERACTIONS.html
- kind: drive
  title: Intro - Host-Pathogen interaction session
  url: https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70
- kind: drive
  title: Interspecies interaction - level of granularity
  url: https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E
date: '2026-11-15'
---

# MO-4. A symbiont term requires that the symbiont product evolved to cause the effect; being recognised is not a symbiont process.

## Decision

A symbiont term requires that the symbiont product evolved to cause the effect; being recognised is not a symbiont process.

## Context

A microbial molecule that the host detects (a flagellin, a lipopolysaccharide
biosynthetic enzyme, a pore-forming toxin that trips the inflammasome) does
not "activate the host immune response". The host's detection is a host
process. GO obsoleted the "induction by symbiont of host defense response"
terms (`GO:0044416` is obsolete) and removed terms such as "modulation by
symbiont of microbe-associated molecular pattern-induced host innate immune
response" for this reason.

Effector-mediated terms apply when there is evidence that the effector targets
the host function: a biochemical activity on a host target, a host protein it
binds and inhibits, a phenotype specific to the effector rather than to the
presence of the microbe.

Avirulence effectors recognised by a plant resistance protein are a special
case. `GO:0080185` effector-mediated activation of plant hypersensitive
response by symbiont is the term the working group kept for necrotrophs that
induce host cell death deliberately. In the current ontology it sits under
`GO:0052170` symbiont-mediated suppression of host innate immune response, so
every effector annotated to it also inherits a suppression claim. Use it only
when the effector's evolved role is to trigger the response, and report the
placement upstream.

## Application

*Example.* The repository's plant-fungal review found AVR4 and AVR9 annotated
to `GO:0080185`; AVR4's real function is protecting hyphae from plant
chitinases, and its recognition by Cf-4 is a host process
([PLANT_FUNGAL_INTERACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PLANT_FUNGAL_INTERACTIONS.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| GO terms | `GO:0044416`  (obsolete); `GO:0080185` effector-mediated activation of plant hypersensitive response by symbiont; `GO:0052170` symbiont-mediated suppression of host innate immune response |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [MO-4-E1](MO-4.examples.yaml): A LysM effector that sequesters the chitin elicitor, on effector-mediated suppression of PTI | Conformant | ECP6 involved_in GO:0140423 effector-mediated suppression of host pattern-triggered immunity signaling (EXP, PMID:23840930) |
| [MO-4-E2](MO-4.examples.yaml): AVR4 on effector-mediated activation of plant hypersensitive response | Non-conformant | AVR4 involved_in GO:0080185 effector-mediated activation of plant hypersensitive response by symbiont (EXP, PMID:10998185) |
| [MO-4-E3](MO-4.examples.yaml): AVR9 accepted on effector-mediated activation of plant hypersensitive response | Contested | AVR9 involved_in GO:0080185 effector-mediated activation of plant hypersensitive response by symbiont (EXP, PMID:10998185) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| Pre-2021 ontology | "induction by symbiont of host defense response" and similar terms were available. | Never annotate a symbiont product to activation of host immunity because it is recognised (MO-4). | Obsoleted by the working group (`GO:0044416` is obsolete). |
| [Drive: Intro - Host-Pathogen interaction session](https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70) (2021) | Kept an effector-mediated term for deliberate induction of plant hypersensitive response (`GO:0080185`) as the exception. | Use it only for effectors whose evolved role is induction, and request a move out from under suppression (MO-4). | The current ontology places `GO:0080185` under `GO:0052170` symbiont-mediated suppression of host innate immune response, so every annotation inherits a contradictory claim. |

## Sources

- web: [PLANT_FUNGAL_INTERACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PLANT_FUNGAL_INTERACTIONS.html)
- drive: [Intro - Host-Pathogen interaction session](https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70)
- drive: [Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E)

<!-- END GENERATED -->
