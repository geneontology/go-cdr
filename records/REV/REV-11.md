---
id: REV-11
title: '`NEW` is the one action that manufactures a claim; hold it to a higher bar'
status: proposed
topic: REV
provenance: GOC_PLUS
provenance_note: '[GOC+]. GOC guidance asks for few, informative annotations; the participation test and
  comparator check are ours ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).'
related:
- REV-10
sources:
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# REV-11. `NEW` is the one action that manufactures a claim; hold it to a higher bar

## Decision

Propose a new annotation only with direct evidence of the gene doing the work, after naming
the entity that performs the step, running a comparator check, reading the term's parents and
checking existing GO-CAM models. Never propose a term that is an ancestor or descendant of
another proposed or existing term on the gene.

## Context

The comparator check turns "the curators missed it" into a falsifiable prediction: name two or
three gene products in the same role relative to the same kind of process and see whether they
carry the term. A systematic absence across species and MODs is a convention to identify, not
a twenty-year oversight. INS is absent from insulin processing; POMC, GCG and PENK are absent
from peptide hormone processing; APP is absent from amyloid-beta formation. All three absences
say the same thing: the processing term belongs to the enzymes ([REV-10](REV-10.md)).

A GO-CAM that includes the gene in a different role is a curator decision to argue with
explicitly, not a gap. When a substrate relationship needs to be machine-readable, it goes on
the enzyme as `has_input`, raised as a suggested question rather than asserted on the
substrate.

A limitation of this repository's tooling: `NEW` is rejected for any term already in the gene's
GOA, even when the existing row is electronic and the reviewer has species-specific
experimental evidence. Record such an upgrade in the existing row's `reason` and `supported_by`.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. GOC guidance asks for few, informative annotations; the participation test and comparator check are ours ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)). |
| Date | 2026-11-15 |
| Related | [REV-10](REV-10.md) |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [REV-11-E1](REV-11.examples.yaml): CRISPR-cas system proposed for Cas10 with a participation test and comparators | Conformant | cas10 involved_in GO:0099048 CRISPR-cas system (IDA, PMID:27105119) |
| [REV-11-E2](REV-11.examples.yaml): Nodulation proposed for the CASTOR channel, not from the mutant phenotype alone | Conformant | CASTOR GO:0009877 nodulation (IMP, PMID:31420535) |
| [REV-11-E3](REV-11.examples.yaml): Melanin biosynthesis proposed for POMC with a boilerplate reason | Non-conformant | POMC GO:0042438 melanin biosynthetic process (NAS) |
| [REV-13-E2](REV-13.examples.yaml): Bare protein binding proposed as a NEW core function for worm MKS-1 (from [REV-13](REV-13.md)) | Non-conformant | mks-1 GO:0005515 protein binding (NAS) |
| [RS-8-E1](../RS/RS-8.examples.yaml): Kit signaling pathway proposed for KITLG, the gap the ligand survey found (from [RS-8](../RS/RS-8.md)) | Conformant | KITLG involved_in GO:0038109 Kit signaling pathway (IDA, PMID:17662946) |

## Sources

- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
