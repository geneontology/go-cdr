---
id: CAM-15
title: 'Every asserted edge carries its own evidence: one ECO class and one reference per evidence instance,
  supporting that edge.'
status: proposed
topic: CAM
provenance: GOC_PLUS
provenance_note: '[GOC] for evidence per triple and the IEA restriction; [GOC+] for the requirement that
  edge evidence address the edge.'
evidence_codes:
- IEA
sources:
- kind: drive
  title: GO-CAM Curation Documentation
  url: https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4
- kind: drive
  title: GO-CAM to GPAD and GPAD to GO-CAM (2019)
  url: https://drive.google.com/open?id=1AgkJqA4-V0HG0SaDiNO9ENTxaQC_1HwsmwyhyHhuxog
- kind: drive
  title: Evidence unwinding meeting 2026-01-20
  url: https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8
- kind: issue
  title: go-annotation#6085
  url: https://github.com/geneontology/go-annotation/issues/6085
date: '2026-11-15'
---

# CAM-15. Every asserted edge carries its own evidence: one ECO class and one reference per evidence instance, supporting that edge.

## Decision

Every asserted edge carries its own evidence: one ECO class and one reference per evidence instance, supporting that edge.

## Context

Each triple a curator asserts (enabled by, occurs in, part of, has input, each
causal edge) needs an ECO class and a reference. A causal edge's evidence must
show the causal relation, not merely the existence of the two activities; an
edge that cites exactly the references of its upstream enabler
(`edge_evidence_copied`) usually has not been checked. Electronic evidence from
UniProt keyword, UniProt subcellular location and UniPathway mappings may no
longer support Noctua assertions (2025). Where several papers support one
triple, record them as separate evidence instances, as the 2026 evidence
unwinding project does for standard annotations. NOT on an edge states evidence
against it.

*Rationale.* Missing evidence is the most common lint warning: 1,836 causal
edges in the cached corpus have none. The GPAD export drops a candidate
annotation if any asserted triple in its explanation lacks evidence, so
unevidenced edges also silently remove standard annotations.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for evidence per triple and the IEA restriction; [GOC+] for the requirement that edge evidence address the edge. |
| Date | 2026-11-15 |
| Evidence codes | IEA |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CAM-15-E1](CAM-15.examples.yaml): An IRAK1 to TAK1 edge with no evidence | Non-conformant | gomodel:59cc772c00000000 |
| [CAM-15-E2](CAM-15.examples.yaml): A STAT1 to EP300 edge citing a paper that assays no coactivator | Non-conformant | gomodel:62b4ffe300004489 |
| [CAM-8-E3](CAM-8.examples.yaml): A cholesterol-esterifying enzyme drawn as directly inhibiting a viral fusion protein (from [CAM-8](CAM-8.md)) | Non-conformant | gomodel:6796b94c00004996 |
| [CAM-11-E2](CAM-11.examples.yaml): A coactivator removes input for a ligase, with no shared input stated and no evidence (from [CAM-11](CAM-11.md)) | Non-conformant | gomodel:6606056e00000678 |

## Sources

- drive: [GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4)
- drive: [GO-CAM to GPAD and GPAD to GO-CAM (2019)](https://drive.google.com/open?id=1AgkJqA4-V0HG0SaDiNO9ENTxaQC_1HwsmwyhyHhuxog)
- drive: [Evidence unwinding meeting 2026-01-20](https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8)
- issue: [go-annotation#6085](https://github.com/geneontology/go-annotation/issues/6085)

<!-- END GENERATED -->
