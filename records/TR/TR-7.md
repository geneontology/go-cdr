---
id: TR-7
title: Proteins that act on transcription regulators away from chromatin are regulator-of-regulator, not
  coTFs
status: proposed
topic: TR
provenance: GOC_PLUS
provenance_note: '[GOC] for the class; [GOC+] for the covalent-modification exclusion.'
aspects:
- F
- P
go_terms:
- term_id: GO:0140416
  label: transcription regulator inhibitor activity
- term_id: GO:0140537
  label: transcription regulator activator activity
- term_id: GO:0051090
  obsolete: true
related:
- MF-17
differences:
- prior_source: GO:0140416 / GO:0140537 definitions
  prior_said: Regulator-of-regulator activity "via direct binding and/or post-translational modification"
  we_recommend: Covalent modification of a regulator is a catalytic activity with `has_input`
  why: Aligns with the general regulator principle in [molecular-function.md](../MF/MF-17.md)
sources:
- kind: drive
  title: TF annotation guidelines
  url: https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs
- kind: wiki
  title: Ontology meeting 2018-10-01
  url: https://wiki.geneontology.org/index.php/Ontology_meeting_2018-10-01
- kind: web
  title: TRANSCRIPTION_FACTORS
  url: https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html
date: '2026-11-15'
---

# TR-7. Proteins that act on transcription regulators away from chromatin are regulator-of-regulator, not coTFs

## Decision

A protein that binds a dbTF or coTF and keeps it from chromatin (cytoplasmic or
nuclear sequestration, blocking DNA binding by heterodimerisation) enables
`GO:0140416` transcription regulator inhibitor activity, `has_input` the regulator. One
that enables a regulator to reach chromatin or its partners enables `GO:0140537`
transcription regulator activator activity. Do not annotate coTF terms or regulation of
dbTF activity BP terms for these.

## Context

"The difference between coTFs and dbTF regulators is that the latter do not
act at the genomic location of target regulated gene"
([Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)).
GO:0140416's usage note gives TCF23 (heterodimerises with dbTFs and prevents DNA
binding), NFKBIA (holds NF-kB in the cytoplasm) and HSP90 (holds steroid receptors away
from DNA) as examples. The BP terms for regulation of dbTF activity (for example
`GO:0051090`, now obsolete) were retired, partly because the `regulates` inference chain
turned regulation of a dbTF's activity into regulation of DNA binding
([wiki: Ontology meeting 2018-10-01](https://wiki.geneontology.org/index.php/Ontology_meeting_2018-10-01)).

## Application

Worked example. The bHLH ID proteins lack a basic region and inhibit dbTFs by
dimerisation; they are correctly excluded from dbTF annotation
([TRANSCRIPTION_FACTORS](https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html)) and fit GO:0140416.

Note that GO:0140416 and GO:0140537 are defined "via direct binding and/or
post-translational modification". Where the effect is a covalent modification of the
regulator (a kinase or SUMO ligase acting on a dbTF), annotate the catalytic activity with
`has_input` the regulator, consistent with [MF-17](../MF/MF-17.md).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the class; [GOC+] for the covalent-modification exclusion. |
| Date | 2026-11-15 |
| Related | [MF-17](../MF/MF-17.md) |
| GO terms | `GO:0140416` transcription regulator inhibitor activity; `GO:0140537` transcription regulator activator activity; `GO:0051090`  (obsolete) |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [TR-7-E1](TR-7.examples.yaml): Glutamine synthetase inhibiting TnrA DNA binding | Conformant | glnA enables GO:0140416 transcription regulator inhibitor activity (IDA, PMID:11719184) |
| [TR-7-E2](TR-7.examples.yaml): An Id protein annotated as a transcription corepressor | Non-conformant | id3-a enables GO:0003714 transcription corepressor activity (IBA, GO_REF:0000033) |
| [TR-7-E3](TR-7.examples.yaml): A single-repeat MYB protein that competes for bHLH partners, annotated as a dbTF | Non-conformant | CPC enables GO:0003700 DNA-binding transcription factor activity (ISS, PMID:11118137) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| GO:0140416 / GO:0140537 definitions | Regulator-of-regulator activity "via direct binding and/or post-translational modification" | Covalent modification of a regulator is a catalytic activity with `has_input` | Aligns with the general regulator principle in [molecular-function.md](../MF/MF-17.md) |

## Sources

- drive: [TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)
- wiki: [Ontology meeting 2018-10-01](https://wiki.geneontology.org/index.php/Ontology_meeting_2018-10-01)
- web: [TRANSCRIPTION_FACTORS](https://ai4curation.io/ai-gene-review/pages/projects/TRANSCRIPTION_FACTORS.html)

<!-- END GENERATED -->
