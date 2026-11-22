---
id: IEA-5
title: Accept only one-hop provenance
status: proposed
topic: IEA
provenance: GOC
provenance_note: '[GOC] (IEA working group decision, 2026).'
evidence_codes:
- IEA
differences:
- prior_source: '[wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)'
  prior_said: Mappings between vocabularies "manually assessed to be equivalent" are sound bases for IEA.
  we_recommend: Only one-hop provenance is acceptable; a vocabulary term assigned by a rule is itself
    a prediction (IEA-5).
  why: 'KW2GO could not distinguish manual from predicted keywords; the chain hid errors ([Drive: KW2GO
    announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)).'
sources:
- kind: drive
  title: KW2GO announcement
  url: https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk
- kind: drive
  title: IEA WG Fall 2026
  url: https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I
- kind: issue
  title: go-annotation#6085
  url: https://github.com/geneontology/go-annotation/issues/6085
- kind: drive
  title: ARBA notes for curators
  url: https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz
date: '2026-11-15'
---

# IEA-5. Accept only one-hop provenance

## Decision

An electronic annotation must derive directly from a curated assertion or a sequence feature.
Reject pipelines, and treat rows with suspicion, where GO is reached through an intermediate
prediction: ARBA or UniRule to a keyword to GO; ARBA to a Rhea reaction or EC number to GO; an IEA
used as the premise for another IEA.

## Context

the IEA working group found that most automatic keyword assignments in TrEMBL came from
UniRule and ARBA, that KW2GO could not tell manual keywords from predicted ones, and that the chain
lost the evidence and propagated mistakes. On that basis it retired KW2GO (except for viruses) and
scheduled SubCell2GO, Rhea2GO and EC2GO for replacement on Swiss-Prot and withdrawal from TrEMBL
([Drive: KW2GO announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk);
[Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).
The GO-CAM editor now refuses IEA rows from keywords, subcellular locations and UniPathway as
supporting evidence ([go-annotation#6085](https://github.com/geneontology/go-annotation/issues/6085)).
The ARBA-for-curators notes make the feedback-loop risk explicit: rules mined from annotations that
were themselves predicted inherit their errors at 100% "confidence"
([Drive: ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz)).

## Application

Worked example: KW2GO annotated about 175 *Drosophila* genes that do not encode enzymes with
catalytic-activity terms, and ribosome methyltransferases as ribosomal proteins from a historic
EMBL import ([Drive: KW2GO announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)).
Neither error could be traced from the GO row back to its cause without reconstructing the chain.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] (IEA working group decision, 2026). |
| Date | 2026-11-15 |
| Evidence codes | IEA |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-5-E1](IEA-5.examples.yaml): A plasma membrane row reached through an ARBA-predicted subcellular location | Non-conformant | BST1 located_in GO:0005886 plasma membrane (IEA, GO_REF:0000044) |
| [IEA-5-E2](IEA-5.examples.yaml): EC2GO NADase activity on a receptor TIR domain, from a ProRule-assigned EC number | Non-conformant | Il1rl1 enables GO:0061809 NAD+ nucleosidase activity, cyclic ADP-ribose generating (IEA, GO_REF:0000003) |
| [PIPE-4-E1](../PIPE/PIPE-4.examples.yaml): EC2GO on a TrEMBL entry whose EC number came from an imported record (from [PIPE-4](../PIPE/PIPE-4.md)) | Non-conformant | EC2GO |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29) | Mappings between vocabularies "manually assessed to be equivalent" are sound bases for IEA. | Only one-hop provenance is acceptable; a vocabulary term assigned by a rule is itself a prediction (IEA-5). | KW2GO could not distinguish manual from predicted keywords; the chain hid errors ([Drive: KW2GO announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)). |

## Sources

- drive: [KW2GO announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)
- drive: [IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)
- issue: [go-annotation#6085](https://github.com/geneontology/go-annotation/issues/6085)
- drive: [ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz)

<!-- END GENERATED -->
