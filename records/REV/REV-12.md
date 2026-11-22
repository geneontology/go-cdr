---
id: REV-12
title: An ND row is a statement about the literature
status: proposed
topic: REV
provenance: GOC_PLUS
evidence_codes:
- IPI
- IBA
- ISS
- ISO
- TAS
- NAS
- ND
- IEA
sources:
- kind: drive
  title: GO rules update 2023
  url: https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI
- kind: web
  title: NO_DATA
  url: https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html
date: '2026-11-15'
---

# REV-12. An ND row is a statement about the literature

## Decision

`ACCEPT` an ND root-term row when no literature on this gene product, in this species,
identifies a function in that aspect, and cite the search. Remove it (or `MODIFY` it) only when
such literature exists, quoting the paper.

## Context

ND (`GO_REF:0000015`) says a curator searched and found nothing to annotate. GORULE:0000011
restricts ND to the three root terms and the roots to ND
([Drive: GO rules update 2023](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI)).
IBA, ISO, ISS or IEA rows in the same aspect are not literature on the gene and do not make an
ND stale. A bare protein-binding IPI does not either; an ortholog paper does not; an NAS or a
Reactome TAS on the gene itself does. `KEEP_AS_NON_CORE`, `MARK_AS_OVER_ANNOTATED` and
`TOO_GENERAL` are never used on an ND, and a `NEW` ND is never proposed. Record why there is
no data (`nd_case`), and pair a true gap with a biology knowledge gap
([evidence-codes.md](../EV/README.md), [NO_DATA](https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Evidence codes | IPI, IBA, ISS, ISO, TAS, NAS, ND, IEA |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [REV-12-E1](REV-12.examples.yaml): An accepted BP ND that cites its literature search | Conformant | At5g03810 involved_in GO:0008150 biological_process (ND, GO_REF:0000015) |
| [REV-12-E2](REV-12.examples.yaml): A stale BP ND on rat Aga removed, quoting the paper | Conformant | Aga involved_in GO:0008150 biological_process (ND, GO_REF:0000015) |
| [REV-12-E3](REV-12.examples.yaml): A NEW ND row proposed for a microprotein of unknown function | Non-conformant | P3R3URF GO:0003674 molecular_function (ND) |
| [REV-19-E2](REV-19.examples.yaml): A root molecular_function row proposed by NAS for KCTD18 (from [REV-19](REV-19.md)) | Non-conformant | KCTD18 GO:0003674 molecular_function (NAS) |

## Sources

- drive: [GO rules update 2023](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI)
- web: [NO_DATA](https://ai4curation.io/ai-gene-review/pages/projects/NO_DATA.html)

<!-- END GENERATED -->
