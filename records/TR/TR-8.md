---
id: TR-8
title: Use RNA polymerase II terms for eukaryotic protein-coding genes; name Pol I or III only when shown
status: proposed
topic: TR
provenance: GOC
aspects:
- F
- P
go_terms:
- term_id: GO:0000981
  label: DNA-binding transcription factor activity, RNA polymerase II-specific
- term_id: GO:0001228
  label: DNA-binding transcription activator activity, RNA polymerase II-specific
- term_id: GO:0001227
  label: DNA-binding transcription repressor activity, RNA polymerase II-specific
- term_id: GO:0000978
  label: RNA polymerase II cis-regulatory region sequence-specific DNA binding
- term_id: GO:0006357
  label: regulation of transcription by RNA polymerase II
- term_id: GO:0001181
  label: RNA polymerase I general transcription initiation factor activity
- term_id: GO:0000995
  label: RNA polymerase III general transcription initiation factor activity
- term_id: GO:0006360
  label: transcription by RNA polymerase I
- term_id: GO:0006383
  label: transcription by RNA polymerase III
- term_id: GO:0003700
  label: DNA-binding transcription factor activity
- term_id: GO:0001216
  label: DNA-binding transcription activator activity
- term_id: GO:0001217
  label: DNA-binding transcription repressor activity
- term_id: GO:0006355
  label: regulation of DNA-templated transcription
- term_id: GO:0000785
  label: chromatin
- term_id: GO:0001059
  label: transcription by RNA polymerase IV
- term_id: GO:0001060
  label: transcription by RNA polymerase V
differences:
- prior_source: '[go-annotation#1720](https://github.com/geneontology/go-annotation/issues/1720) (open)'
  prior_said: Make "transcription, DNA-templated" do-not-annotate and always specify promoter type, including
    "transcription from bacterial-type RNA polymerase promoter"
  we_recommend: Specify the polymerase for eukaryotes; for bacteria use `GO:0006351`
  why: The proposed bacterial term (`GO:0001121`) no longer exists in GO
sources:
- kind: wiki
  title: Transcription jamboree
  url: https://wiki.geneontology.org/index.php/Transcription_jamboree
- kind: drive
  title: 2017 transcription guidelines
  url: https://drive.google.com/open?id=0B_c5g4FezmhfNENjNk5RbjJwQUk
date: '2026-11-15'
---

# TR-8. Use RNA polymerase II terms for eukaryotic protein-coding genes; name Pol I or III only when shown

## Decision

For a regulator of a eukaryotic protein-coding gene, use the RNA polymerase
II-specific terms (`GO:0000981`, `GO:0001228`, `GO:0001227`, `GO:0000978`, `GO:0006357`)
without requiring the paper to mention the polymerase. Use RNA polymerase I or III terms
(`GO:0001181`, `GO:0000995`, `GO:0006360`, `GO:0006383`) only when the paper identifies
those polymerases' templates. For bacteria, archaea, mitochondria and plastids, use the
terms without polymerase qualification (`GO:0003700`, `GO:0001216`, `GO:0001217`,
`GO:0006355`), or the organelle transcription terms.

## Context

The electronic transcription jamboree agreed that "for almost all protein
coding genes in eukaryotes ... you can confidently use the RNA Pol II terms even if the
paper doesn't explicitly mention that detail", with rare exceptions such as
trypanosome genes transcribed by Pol I
([wiki: Transcription jamboree](https://wiki.geneontology.org/index.php/Transcription_jamboree),
archived). The 2017 working group told curators to "always use regulation of RNA
polymerase II transcription terms when there is evidence that the transcription factor
regulates mRNA levels" ([Drive: 2017 transcription guidelines](https://drive.google.com/open?id=0B_c5g4FezmhfNENjNk5RbjJwQUk)).
The Pol II-specific dbTF term `GO:0000981` occurs in `GO:0000785` chromatin, which no
bacterial protein does.

## Application

Worked examples. A yeast zinc-cluster activator of a glucose-repressed gene:
`GO:0001228` with `has_input` the gene. A plant MYB activator of an anthocyanin gene:
`GO:0001228`. E. coli LacI: `GO:0001217` DNA-binding transcription repressor activity.
Plant RNA polymerase IV and V transcription (`GO:0001059`, `GO:0001060`) belongs to
siRNA-directed silencing, not to dbTF annotation.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0000981` DNA-binding transcription factor activity, RNA polymerase II-specific; `GO:0001228` DNA-binding transcription activator activity, RNA polymerase II-specific; `GO:0001227` DNA-binding transcription repressor activity, RNA polymerase II-specific; `GO:0000978` RNA polymerase II cis-regulatory region sequence-specific DNA binding; `GO:0006357` regulation of transcription by RNA polymerase II; `GO:0001181` RNA polymerase I general transcription initiation factor activity; `GO:0000995` RNA polymerase III general transcription initiation factor activity; `GO:0006360` transcription by RNA polymerase I; `GO:0006383` transcription by RNA polymerase III; `GO:0003700` DNA-binding transcription factor activity; `GO:0001216` DNA-binding transcription activator activity; `GO:0001217` DNA-binding transcription repressor activity; `GO:0006355` regulation of DNA-templated transcription; `GO:0000785` chromatin; `GO:0001059` transcription by RNA polymerase IV; `GO:0001060` transcription by RNA polymerase V |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [go-annotation#1720](https://github.com/geneontology/go-annotation/issues/1720) (open) | Make "transcription, DNA-templated" do-not-annotate and always specify promoter type, including "transcription from bacterial-type RNA polymerase promoter" | Specify the polymerase for eukaryotes; for bacteria use `GO:0006351` | The proposed bacterial term (`GO:0001121`) no longer exists in GO |

## Sources

- wiki: [Transcription jamboree](https://wiki.geneontology.org/index.php/Transcription_jamboree)
- drive: [2017 transcription guidelines](https://drive.google.com/open?id=0B_c5g4FezmhfNENjNk5RbjJwQUk)

<!-- END GENERATED -->
