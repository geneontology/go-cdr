---
id: CAM-16
title: 'A model is a module: include the activities specific to its process, reuse general machinery by
  reference, and link models through a shared activity.'
status: proposed
topic: CAM
provenance: GOC_PLUS
provenance_note: '[GOC] for modules and reuse; [GOC+] for the linking convention, which is a 2021 draft;
  [GOC+] for the no-edges rule, which follows the 2026 evidence-unwinding binning of standard versus GO-CAM
  models.'
differences:
- prior_source: '[Drive: Convention for Linking GO-CAMs](https://drive.google.com/open?id=1iXgErHVojMFtbteiquzfJw76kPPs851XRVC558VdtGI)
    (draft)'
  prior_said: Draft, with open questions on metabolic and signalling cases.
  we_recommend: Adopt the shared-activity convention as "should" (CAM-16).
  why: It is the only written convention and matches PomBase practice; leave its open questions open.
sources:
- kind: drive
  title: GO-CAM modeling guidelines
  url: https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA
- kind: drive
  title: Convention for Linking GO-CAMs (draft)
  url: https://drive.google.com/open?id=1iXgErHVojMFtbteiquzfJw76kPPs851XRVC558VdtGI
- kind: drive
  title: Evidence unwinding meeting 2026-01-20
  url: https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8
date: '2026-11-15'
---

# CAM-16. A model is a module: include the activities specific to its process, reuse general machinery by reference, and link models through a shared activity.

## Decision

A model is a module: include the activities specific to its process, reuse general machinery by reference, and link models through a shared activity.

## Context

A model should cover one process, or a few closely interacting ones (a
pathway and its regulation). Activities that recur in many models (the
transcription machinery, the proteasome, nuclear import) belong in their own
models; refer to them with a process term in the `part of` chain or as a
process the model's last activity regulates. To link two pathway models, end
the first and start the second with the same activity: same gene product, MF,
location and process, and optionally the same input. Instances are not shared
across models.

A model with no causal edges is a set of standard annotations, not a GO-CAM,
and should be curated (and reviewed) as such. `small_model` (two or fewer
activities) and `orphan_activity` lint findings are prompts to check this.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for modules and reuse; [GOC+] for the linking convention, which is a 2021 draft; [GOC+] for the no-edges rule, which follows the 2026 evidence-unwinding binning of standard versus GO-CAM models. |
| Date | 2026-11-15 |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CAM-16-E1](CAM-16.examples.yaml): Four calmodulin-JAK-STAT models that never connect to the interferon pathway they modulate | Non-conformant | gomodel:62b4ffe300004489 |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: Convention for Linking GO-CAMs](https://drive.google.com/open?id=1iXgErHVojMFtbteiquzfJw76kPPs851XRVC558VdtGI) (draft) | Draft, with open questions on metabolic and signalling cases. | Adopt the shared-activity convention as "should" (CAM-16). | It is the only written convention and matches PomBase practice; leave its open questions open. |

## Sources

- drive: [GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)
- drive: [Convention for Linking GO-CAMs (draft)](https://drive.google.com/open?id=1iXgErHVojMFtbteiquzfJw76kPPs851XRVC558VdtGI)
- drive: [Evidence unwinding meeting 2026-01-20](https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8)

<!-- END GENERATED -->
