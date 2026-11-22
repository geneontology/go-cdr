---
id: IEA-8
title: A keyword or location mapping must respect GO's distinctions, which vocabularies often do not
status: proposed
topic: IEA
provenance: GOC_PLUS
provenance_note: '[GOC+]. These are GOC principles applied to vocabularies that predate them.'
go_terms:
- term_id: GO:0005794
  label: Golgi apparatus
- term_id: GO:0051536
  label: iron-sulfur cluster binding
- term_id: GO:0005506
  label: iron ion binding
- term_id: GO:0006915
  label: apoptotic process
- term_id: GO:0039527
  obsolete: true
- term_id: GO:0140476
  label: symbiont-mediated suppression of host cytoplasmic pattern recognition receptor signaling pathway
    via inhibition of TRAF activity
differences:
- prior_source: '[go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573)'
  prior_said: Open question whether keyword-based CC relations should default to `located_in` rather than
    `is_active_in`.
  we_recommend: A keyword or subcellular-location row is a location claim; transit compartments are not
    locations of activity and should not be mapped (IEA-8).
  why: Consistent with the ER transit rule in [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
    and [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html).
sources:
- kind: drive
  title: KW2GO announcement
  url: https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk
- kind: web
  title: SPKW
  url: https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html
- kind: issue
  title: go-annotation#1134
  url: https://github.com/geneontology/go-annotation/issues/1134
- kind: issue
  title: go-annotation#4573
  url: https://github.com/geneontology/go-annotation/issues/4573
- kind: issue
  title: go-annotation#390
  url: https://github.com/geneontology/go-annotation/issues/390
- kind: web
  title: KW_1110_TRAF_KW2GO
  url: https://ai4curation.io/ai-gene-review/pages/projects/KW_1110_TRAF_KW2GO.html
date: '2026-11-15'
---

# IEA-8. A keyword or location mapping must respect GO's distinctions, which vocabularies often do not

## Decision

When reviewing a keyword- or subcellular-location-derived row, check three things: participation
versus regulation (a regulator is not part of the process); location of activity versus transit or
sequestration (Golgi for a secreted protein is transit); a metal cofactor versus a binding
function.

## Context

UniProt keywords are thematic; GO process terms are mechanistic. The KW2GO review found
"regulation of" and "in process" conflated, and that 35-50% of keyword-unique MF rows were binding
terms, mostly metal ion binding describing cofactors in metalloproteins
([Drive: KW2GO announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)).
The repo's keyword review found 79-100% over-annotation for eukaryotic apoptosis, autophagy, rhythm
and meiosis keywords, mostly a regulator or bystander annotated as a participant, while bacterial
keyword rows were mostly sound ([SPKW](https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html)). Earlier tracker cases make the same point:
about 50 *S. pombe* "DNA repair" keyword rows were upstream chromatin or checkpoint effects
([go-annotation#1134](https://github.com/geneontology/go-annotation/issues/1134)); keyword-derived
`GO:0005794` Golgi apparatus on a protein that only passes through the Golgi is not a location of
activity ([go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573)); and
iron-sulfur cluster binding is not a kind of iron ion binding, so `GO:0051536` should not imply
`GO:0005506` ([go-annotation#390](https://github.com/geneontology/go-annotation/issues/390)).

## Application

Worked example: caspase substrates such as AIMP1 and BCAP31 carried `GO:0006915` apoptotic process
from the apoptosis keyword; being cleaved during apoptosis is not participation. The repo removed
them ([SPKW](https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html)). Where GO's own concept changes, a keyword mapping must follow: KW-1110
moved from the obsolete `GO:0039527` to `GO:0140476` symbiont-mediated suppression of host
cytoplasmic pattern recognition receptor signaling pathway via inhibition of TRAF activity
([KW_1110_TRAF_KW2GO](https://ai4curation.io/ai-gene-review/pages/projects/KW_1110_TRAF_KW2GO.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. These are GOC principles applied to vocabularies that predate them. |
| Date | 2026-11-15 |
| GO terms | `GO:0005794` Golgi apparatus; `GO:0051536` iron-sulfur cluster binding; `GO:0005506` iron ion binding; `GO:0006915` apoptotic process; `GO:0039527`  (obsolete); `GO:0140476` symbiont-mediated suppression of host cytoplasmic pattern recognition receptor signaling pathway via inhibition of TRAF activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-8-E1](IEA-8.examples.yaml): Flowering keyword annotates a flowering-time regulator to flower development | Non-conformant | ELF4 involved_in GO:0009908 flower development (IEA, GO_REF:0000043) |
| [IEA-8-E2](IEA-8.examples.yaml): Metal ion binding from the keyword for a protein that binds iron-sulfur clusters | Non-conformant | psaC GO:0046872 metal ion binding (IEA, GO_REF:0000043) |
| [IEA-8-E3](IEA-8.examples.yaml): Apoptosis keyword on an autophagy protease that caspase-3 cleaves | Non-conformant | ATG4D involved_in GO:0006915 apoptotic process (IEA, GO_REF:0000043) |
| [IEA-6-E1](IEA-6.examples.yaml): A retired-keyword row reviewed for the record and recognised as historical (from [IEA-6](IEA-6.md)) | Conformant | GI GO:0009908 flower development (IEA, GO_REF:0000043) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573) | Open question whether keyword-based CC relations should default to `located_in` rather than `is_active_in`. | A keyword or subcellular-location row is a location claim; transit compartments are not locations of activity and should not be mapped (IEA-8). | Consistent with the ER transit rule in [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) and [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html). |

## Sources

- drive: [KW2GO announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)
- web: [SPKW](https://ai4curation.io/ai-gene-review/pages/projects/SPKW.html)
- issue: [go-annotation#1134](https://github.com/geneontology/go-annotation/issues/1134)
- issue: [go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573)
- issue: [go-annotation#390](https://github.com/geneontology/go-annotation/issues/390)
- web: [KW_1110_TRAF_KW2GO](https://ai4curation.io/ai-gene-review/pages/projects/KW_1110_TRAF_KW2GO.html)

<!-- END GENERATED -->
