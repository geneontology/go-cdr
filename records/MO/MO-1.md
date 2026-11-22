---
id: MO-1
title: Annotate each organism's gene products with the terms written from that organism's side.
status: proposed
topic: MO
provenance: GOC_PLUS
go_terms:
- term_id: GO:0052041
  label: symbiont-mediated suppression of host programmed cell death
- term_id: GO:0046718
  label: symbiont entry into host cell
- term_id: GO:0051607
  label: defense response to virus
- term_id: GO:0045071
  label: negative regulation of viral genome replication
- term_id: GO:0035738
  label: venom-mediated perturbation of biological process
- term_id: GO:0044793
  label: host-mediated suppression of viral proces
- term_id: GO:0140740
  label: ADP-riboxanase-[protein] activity
- term_id: GO:0030430
  label: host cell cytoplasm
- term_id: GO:0004197
  label: cysteine-type endopeptidase activity
- term_id: GO:0070269
  label: pyroptotic inflammatory response
sources:
- kind: drive
  title: Interspecies interaction - level of granularity
  url: https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E
- kind: issue
  title: go-annotation#3814
  url: https://github.com/geneontology/go-annotation/issues/3814
- kind: issue
  title: go-annotation#2720
  url: https://github.com/geneontology/go-annotation/issues/2720
date: '2026-11-15'
---

# MO-1. Annotate each organism's gene products with the terms written from that organism's side.

## Decision

Annotate each organism's gene products with the terms written from that organism's side.

## Context

Before choosing a term, decide which organism's gene product does the step,
then use the term family for that side:

| Who acts | On whom | Term family | Example |
|---|---|---|---|
| Symbiont | host process | symbiont-mediated perturbation / suppression / activation of host X; effector-mediated ... | `GO:0052041` symbiont-mediated suppression of host programmed cell death |
| Symbiont | own life cycle in host | viral process children; symbiont entry into host | `GO:0046718` symbiont entry into host cell |
| Host | symbiont | defence response to X; host-mediated suppression of symbiont process; regulation of viral process | `GO:0051607` defense response to virus; `GO:0045071` negative regulation of viral genome replication |
| Venom component | another organism | venom-mediated ... | `GO:0035738` venom-mediated perturbation of biological process |

Host-side regulation terms (`GO:0045071` negative regulation of viral genome
replication, `GO:0044793` host-mediated suppression of viral process) are
legitimate for host restriction factors: they describe the host acting on the
virus.

## Application

*Example.* In GO-CAM `62b4ffe300002385`, *Shigella flexneri* OspC3
(UniProtKB:A0A0H2US87) enables `GO:0140740` ADP-riboxanase-[protein] activity
with `has input` human CASP4 (UniProtKB:P49662), occurs in `GO:0030430` host
cell cytoplasm, and is part of `GO:0052041`; its activity directly negatively
regulates CASP4 `GO:0004197` cysteine-type endopeptidase activity, which is
part of host `GO:0070269` pyroptotic inflammatory response. CASP4 gets no
symbiont term.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| GO terms | `GO:0052041` symbiont-mediated suppression of host programmed cell death; `GO:0046718` symbiont entry into host cell; `GO:0051607` defense response to virus; `GO:0045071` negative regulation of viral genome replication; `GO:0035738` venom-mediated perturbation of biological process; `GO:0044793` host-mediated suppression of viral proces; `GO:0140740` ADP-riboxanase-[protein] activity; `GO:0030430` host cell cytoplasm; `GO:0004197` cysteine-type endopeptidase activity; `GO:0070269` pyroptotic inflammatory response |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [MO-1-E1](MO-1.examples.yaml): A fungal effector given the symbiont-side immune-suppression term | Conformant | PIT2 GO:0140403 effector-mediated suppression of host innate immune response (IMP, PMID:23459172) |
| [MO-1-E2](MO-1.examples.yaml): A bacterial host factor annotated to the phage's own transcription process | Non-conformant | PSPPH_4093 acts_upstream_of_or_within_positive_effect GO:0039696 RNA-templated viral transcription (IDA, PMID:18836083) |

## Sources

- drive: [Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E)
- issue: [go-annotation#3814](https://github.com/geneontology/go-annotation/issues/3814)
- issue: [go-annotation#2720](https://github.com/geneontology/go-annotation/issues/2720)

<!-- END GENERATED -->
