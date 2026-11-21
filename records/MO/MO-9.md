---
id: MO-9
title: On the host side, annotate participation in defence to the most specific defence or immune term
  the evidence supports, and keep response-to and susceptibility separate.
status: proposed
topic: MO
provenance: GOC_PLUS
go_terms:
- term_id: GO:0038187
  label: pattern recognition receptor activity
- term_id: GO:0002221
  label: pattern recognition receptor signaling pathway
- term_id: GO:0045087
  label: innate immune response
- term_id: GO:0140374
  label: antiviral innate immune response
- term_id: GO:0042742
  label: defense response to bacterium
- term_id: GO:0050829
  label: defense response to Gram-negative bacterium
- term_id: GO:0050830
  label: defense response to Gram-positive bacterium
- term_id: GO:0050832
  label: defense response to fungus
- term_id: GO:0051607
  label: defense response to virus
- term_id: GO:0061844
  label: antimicrobial humoral immune response mediated by antimicrobial peptide
- term_id: GO:0045071
  label: negative regulation of viral genome replication
- term_id: GO:0009617
  label: response to bacterium
- term_id: GO:0009615
  label: response to virus
- term_id: GO:0140546
  label: defense response to symbiont
differences:
- prior_source: '[Drive: Combined multiorg + immune system process call 2021-11-22](https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so)'
  prior_said: Left open whether immune system process is a system process; suggested unicellular defence
    is defence, not immunity.
  we_recommend: Use defence terms for prokaryotes; immune terms for animals and plants as GO defines them
    (MO-9).
  why: '`GO:0045087` innate immune response is now a subclass of `GO:0140546` defense response to symbiont,
    so defence groups both.'
sources:
- kind: web
  title: PLANT_FUNGAL_INTERACTIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/PLANT_FUNGAL_INTERACTIONS.html
- kind: drive
  title: Combined multiorg + immune system process call 2021-11-22
  url: https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so
- kind: wiki
  title: Immunology Revisions
  url: https://wiki.geneontology.org/index.php/Immunology_Revisions
- kind: web
  title: INNATE_IMMUNITY
  url: https://ai4curation.io/ai-gene-review/pages/projects/INNATE_IMMUNITY.html
date: '2026-11-15'
---

# MO-9. On the host side, annotate participation in defence to the most specific defence or immune term the evidence supports, and keep response-to and susceptibility separate.

## Decision

On the host side, annotate participation in defence to the most specific defence or immune term the evidence supports, and keep response-to and susceptibility separate.

## Context

Use this ladder:

1. **Recognition and signalling components** take the receptor or signalling
   MF and the pathway BP: `GO:0038187` pattern recognition receptor activity,
   `GO:0002221` pattern recognition receptor signaling pathway, `GO:0045087`
   innate immune response or a child such as `GO:0140374` antiviral innate
   immune response.
2. **Effectors** that act on the microbe take the defence term for the target
   class: `GO:0042742` defense response to bacterium (or `GO:0050829`/
   `GO:0050830` for Gram-negative/Gram-positive), `GO:0050832` defense response
   to fungus, `GO:0051607` defense response to virus; for antimicrobial
   peptides, `GO:0061844` antimicrobial humoral immune response mediated by
   antimicrobial peptide.
3. **Direct restriction factors** acting on a viral step take the host-side
   regulation term (`GO:0045071` negative regulation of viral genome
   replication).
4. **Transcriptional induction alone** supports at most `GO:0009617` response
   to bacterium or `GO:0009615` response to virus, and in reviews is
   non-core.
5. **A susceptibility factor** whose loss increases resistance is a negative
   regulator: `defense response` becomes negative regulation of defense
   response, not defense response.

Use "immune response" terms for organisms with an immune system as GO defines
it; for bacteria and archaea (CRISPR, restriction-modification, abortive
infection) use defence terms. In the current ontology, `GO:0045087` innate
immune response is a subclass of `GO:0140546` defense response to symbiont,
so defence is the grouping term and nothing is lost.

## Application

*Example.* MLO in barley and Arabidopsis MLO2 had `defense response` rows;
both reviews changed the sign to negative regulation of defense response,
because loss of MLO gives powdery mildew resistance
([PLANT_FUNGAL_INTERACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PLANT_FUNGAL_INTERACTIONS.html)). Genes known
only from infection phenotypes (LYM2, CYP79B2) did not get `defense response to
fungus`; genes that do part of the work (CYP71B15 making camalexin, ABCG36
exporting it) did.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| GO terms | `GO:0038187` pattern recognition receptor activity; `GO:0002221` pattern recognition receptor signaling pathway; `GO:0045087` innate immune response; `GO:0140374` antiviral innate immune response; `GO:0042742` defense response to bacterium; `GO:0050829` defense response to Gram-negative bacterium; `GO:0050830` defense response to Gram-positive bacterium; `GO:0050832` defense response to fungus; `GO:0051607` defense response to virus; `GO:0061844` antimicrobial humoral immune response mediated by antimicrobial peptide; `GO:0045071` negative regulation of viral genome replication; `GO:0009617` response to bacterium; `GO:0009615` response to virus; `GO:0140546` defense response to symbiont |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: Combined multiorg + immune system process call 2021-11-22](https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so) | Left open whether immune system process is a system process; suggested unicellular defence is defence, not immunity. | Use defence terms for prokaryotes; immune terms for animals and plants as GO defines them (MO-9). | `GO:0045087` innate immune response is now a subclass of `GO:0140546` defense response to symbiont, so defence groups both. |

## Sources

- web: [PLANT_FUNGAL_INTERACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PLANT_FUNGAL_INTERACTIONS.html)
- drive: [Combined multiorg + immune system process call 2021-11-22](https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so)
- wiki: [Immunology Revisions](https://wiki.geneontology.org/index.php/Immunology_Revisions)
- web: [INNATE_IMMUNITY](https://ai4curation.io/ai-gene-review/pages/projects/INNATE_IMMUNITY.html)

<!-- END GENERATED -->
