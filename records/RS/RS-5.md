---
id: RS-5
title: Judge sign in vivo, from the gene product's effect, and correct a wrong sign rather than tolerating
  it
status: proposed
topic: RS
provenance: NEW
provenance_note: '[GOC+]. The in vivo principle and the handling of in vitro opposite-sign activity are
  [NEW], from [REGULATION_SIGN](https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html).'
aspects:
- P
evidence_codes:
- IMP
- IBA
- ISS
- IEA
go_terms:
- term_id: GO:0007189
  label: adenylate cyclase-activating G protein-coupled receptor signaling pathway
- term_id: GO:0007193
  label: adenylate cyclase-inhibiting G protein-coupled receptor signaling pathway
- term_id: GO:0050728
  label: negative regulation of inflammatory response
- term_id: GO:0050729
  label: positive regulation of inflammatory response
- term_id: GO:0045668
  label: negative regulation of osteoblast differentiation
- term_id: GO:0045669
  label: positive regulation of osteoblast differentiation
- term_id: GO:0040017
  label: positive regulation of locomotion
- term_id: GO:0040012
  label: regulation of locomotion
differences:
- prior_source: '[REGULATION_SIGN](https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html)
    (repository) vs earlier review practice'
  prior_said: An earlier review held GNAI1's AC-activating row UNDECIDED because of in vitro cyclase stimulation.
  we_recommend: Sign is judged in vivo. Opposite-sign in vitro activity is not grounds for UNDECIDED (RS-5).
  why: Sharpens a gap. GOC documents no rule on conflicting in vitro and in vivo sign.
sources:
- kind: web
  title: REGULATION_SIGN
  url: https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html
- kind: drive
  title: FlyBase pathway curation guide
  url: https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI
- kind: wiki
  title: Annotation Relations
  url: https://wiki.geneontology.org/index.php/Annotation_Relations
date: '2026-11-15'
---

# RS-5. Judge sign in vivo, from the gene product's effect, and correct a wrong sign rather than tolerating it

## Decision

**Statement.** The sign of a regulation annotation is the direction in which the normal gene product changes the process in the organism. Derive it from the gene product's effect, not from the mutant's phenotype: a knockout that increases X means the gene negatively regulates X. Use the signed term whenever the direction is known. Use the sign-neutral parent only when the direction genuinely depends on context, and say so. An in vitro activity of the opposite sign does not outweigh an established in vivo direction. In review, a wrong sign is `MODIFY` to the opposite-sign term (a lateral correction, not a refinement). Use `REMOVE` if the row also has no sound source.

## Context

A too-general term is still true. An inverted one is false, and it propagates intact through ISS, IBA, Ensembl Compara and GO-CAM causal edges ([REGULATION_SIGN](https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html)). A census of reviews in this repository found 35 sign-flip MODIFYs on 25 genes. IMP was the largest evidence class (15 of 35), consistent with phenotype direction being recorded as gene effect. FlyBase requires signed regulation terms for pathways ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)). GO asks for the signed child of `acts upstream of or within` for the same reason ([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)).

## Application

**Worked examples.**

- Human GNAI2, GO:0007189 adenylate cyclase-activating G protein-coupled receptor signaling pathway (IEA, Ensembl Compara): Gαi2 inhibits the cyclase, so MODIFY to GO:0007193 adenylate cyclase-inhibiting G protein-coupled receptor signaling pathway (review `genes/human/GNAI2`).
- Human GNAI1, the same term by ISS from an adenylyl cyclase donor: the in vitro stimulation of type I/II cyclases by high Gαi concentrations does not rescue it, so REMOVE ([REGULATION_SIGN](https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html)).
- Human NLRP3, GO:0050728 negative regulation of inflammatory response (IMP ×3): MODIFY to GO:0050729 positive regulation of inflammatory response. Human LRP5, GO:0045668 negative regulation of osteoblast differentiation: MODIFY to GO:0045669 positive regulation of osteoblast differentiation.
- Human NTSR1, GO:0040017 positive regulation of locomotion: knockouts are hypolocomotor, but the receptor also mediates stimulant-induced hyperactivity. MODIFY to the sign-neutral GO:0040012 regulation of locomotion, and record that the direction is context-dependent.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] [GOC+]. The in vivo principle and the handling of in vitro opposite-sign activity are [NEW], from [REGULATION_SIGN](https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html). |
| Date | 2026-11-15 |
| Evidence codes | IMP, IBA, ISS, IEA |
| GO terms | `GO:0007189` adenylate cyclase-activating G protein-coupled receptor signaling pathway; `GO:0007193` adenylate cyclase-inhibiting G protein-coupled receptor signaling pathway; `GO:0050728` negative regulation of inflammatory response; `GO:0050729` positive regulation of inflammatory response; `GO:0045668` negative regulation of osteoblast differentiation; `GO:0045669` positive regulation of osteoblast differentiation; `GO:0040017` positive regulation of locomotion; `GO:0040012` regulation of locomotion |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [RS-5-E1](RS-5.examples.yaml): A sign-inverted motor neuron apoptosis row on MKK4 corrected from the knockout | Conformant | Map2k4 acts_upstream_of_or_within GO:2000672 negative regulation of motor neuron apoptotic process (ISO, GO_REF:0000121) |
| [RS-5-E2](RS-5.examples.yaml): Sign-neutral dauer regulation on daf-7 refined to negative regulation | Conformant | daf-7 involved_in GO:0061065 regulation of dauer larval development (IGI, PMID:1732156) |
| [RS-5-E3](RS-5.examples.yaml): An InterPro-derived positive regulation of transcription on SVP flipped to negative | Non-conformant | SVP involved_in GO:0045944 positive regulation of transcription by RNA polymerase II (IEA, GO_REF:0000002) |
| [RS-9-E3](RS-9.examples.yaml): An AC-activating pathway ISS on Gi1 removed: wrong sign, wrong donor (from [RS-9](RS-9.md)) | Conformant | GNAI1 involved_in GO:0007189 adenylate cyclase-activating G protein-coupled receptor signaling pathway (ISS, GO_REF:0000024) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [REGULATION_SIGN](https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html) (repository) vs earlier review practice | An earlier review held GNAI1's AC-activating row UNDECIDED because of in vitro cyclase stimulation. | Sign is judged in vivo. Opposite-sign in vitro activity is not grounds for UNDECIDED (RS-5). | Sharpens a gap. GOC documents no rule on conflicting in vitro and in vivo sign. |

## Sources

- web: [REGULATION_SIGN](https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html)
- drive: [FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)
- wiki: [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)

<!-- END GENERATED -->
