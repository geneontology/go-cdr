---
id: PH-3
title: Use high-throughput seeds and single seeds only with an independent second line
status: proposed
topic: PH
provenance: GOC_PLUS
provenance_note: '[GOC+]. Resolves a standing disagreement between curators who want a two-seed rule and
  PAINT curators who reject one; we side with neither and condition on the term.'
evidence_codes:
- HTP
- IBA
- IBD
- ISS
- ISO
- ISA
differences:
- prior_source: FlyBase position in [go-annotation#2382](https://github.com/geneontology/go-annotation/issues/2382),
    [#3413](https://github.com/geneontology/go-annotation/issues/3413)
  prior_said: IBDs should need more than one supporting gene.
  we_recommend: Single seeds allowed with an independent second line; single-seed BP needs a direct MF/CC
    link (PH-3).
  why: PAINT curators and PomBase rejected a blanket rule in the same threads; failures concentrate on
    loosely linked BP, so we condition on the term.
sources:
- kind: wiki
  title: PAINT annotation guidelines
  url: https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines
- kind: issue
  title: go-annotation#1775
  url: https://github.com/geneontology/go-annotation/issues/1775
- kind: issue
  title: go-annotation#2382
  url: https://github.com/geneontology/go-annotation/issues/2382
- kind: issue
  title: go-annotation#2219
  url: https://github.com/geneontology/go-annotation/issues/2219
- kind: issue
  title: go-annotation#3413
  url: https://github.com/geneontology/go-annotation/issues/3413
date: '2026-11-15'
---

# PH-3. Use high-throughput seeds and single seeds only with an independent second line

## Decision

An IBD may rest on one seed gene or on HTP evidence when at least one independent line
agrees: a domain or active site consistent with the MF, a coherent MF-BP-CC set for the clade,
or unannotated literature in another lineage. A BP propagated from a single seed needs a
direct, mechanistic link to an MF or CC already placed on the same node.

## Context

the PAINT guideline already allows single-paper and HTP seeds with supporting data,
and notes that identical annotations from one paper in several species are not independent
([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)).
The HTP working group allowed HTP-evidenced rows to seed ISS/ISA/ISO/IBA with case-by-case
review ([go-annotation#1775](https://github.com/geneontology/go-annotation/issues/1775)).
Disputes about single seeds cluster on loosely connected BP terms such as "receptor
localization to synapse" or neuronal identity ([go-annotation#2382](https://github.com/geneontology/go-annotation/issues/2382),
[go-annotation#2219](https://github.com/geneontology/go-annotation/issues/2219)), while
single-seed MF on a conserved ribosomal or ubiquitin-ligase subunit is uncontroversial. The
rule targets the failing case without forbidding the sound one.

## Application

Worked example: SAP18 (PTHR13082) carried a corepressor IBD that FlyBase and PomBase curators
first read as a single-entity transfer. The PAINT curator's reply cited repression data for
human and *Arabidopsis* SAP18 outside GO, which is exactly the independent second line this
rule asks for; the residual question was whether fungi had lost the activity
([go-annotation#3413](https://github.com/geneontology/go-annotation/issues/3413)). Literature
outside GO counts, but the IBD's evidence box should cite it so that reviewers can see it.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. Resolves a standing disagreement between curators who want a two-seed rule and PAINT curators who reject one; we side with neither and condition on the term. |
| Date | 2026-11-15 |
| Evidence codes | HTP, IBA, IBD, ISS, ISO, ISA |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| FlyBase position in [go-annotation#2382](https://github.com/geneontology/go-annotation/issues/2382), [#3413](https://github.com/geneontology/go-annotation/issues/3413) | IBDs should need more than one supporting gene. | Single seeds allowed with an independent second line; single-seed BP needs a direct MF/CC link (PH-3). | PAINT curators and PomBase rejected a blanket rule in the same threads; failures concentrate on loosely linked BP, so we condition on the term. |

## Sources

- wiki: [PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)
- issue: [go-annotation#1775](https://github.com/geneontology/go-annotation/issues/1775)
- issue: [go-annotation#2382](https://github.com/geneontology/go-annotation/issues/2382)
- issue: [go-annotation#2219](https://github.com/geneontology/go-annotation/issues/2219)
- issue: [go-annotation#3413](https://github.com/geneontology/go-annotation/issues/3413)

<!-- END GENERATED -->
