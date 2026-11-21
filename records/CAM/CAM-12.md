---
id: CAM-12
title: Connect an activity to a process by a causal edge only when the mechanism is unknown; otherwise
  use `part of`.
status: proposed
topic: CAM
provenance: GOC
sources:
- kind: drive
  title: GO-CAM modeling guidelines
  url: https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA
- kind: wiki
  title: Causally upstream of or within
  url: https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within
date: '2026-11-15'
---

# CAM-12. Connect an activity to a process by a causal edge only when the mechanism is unknown; otherwise use `part of`.

## Decision

Connect an activity to a process by a causal edge only when the mechanism is unknown; otherwise use `part of`.

## Context

If the activity is a step of the process, it is `part of` that process. If it
is a step of the regulation of the process, it is `part of` the regulation
term (`part of` positive regulation of X), not causally upstream of X. If the
activity is known to act before the process but its target is unknown, use
`causally upstream of, positive/negative effect`. If only a mutant effect is
known, use `causally upstream of or within` with a sign. A model should end in
an activity that regulates an activity of the next model, or in a regulation
term, not in a causal edge to a vague process.

Do not draw causal edges between two processes; process order follows from the
edges between their activities.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |

## Sources

- drive: [GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)
- wiki: [Causally upstream of or within](https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within)

<!-- END GENERATED -->
