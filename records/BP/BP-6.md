---
id: BP-6
title: Annotate the process the gene product acts in, not the readout that was measured
status: proposed
topic: BP
provenance: GOC
aspects:
- P
sources:
- kind: wiki
  title: Annotating from phenotypes
  url: https://wiki.geneontology.org/index.php/Annotating_from_phenotypes
- kind: drive
  title: GOC NYC 2018 QC group report
  url: https://drive.google.com/open?id=1cTLQGeV9aUiMvMgW5DxB8pNOARlMoNmmz7nqiyxXPg0
- kind: wiki
  title: Apoptosis Curation Manual
  url: https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual
- kind: web
  title: APOPTOSIS assay readouts
  url: https://ai4curation.io/ai-gene-review/pages/projects/APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.html
- kind: issue
  title: go-annotation#2469
  url: https://github.com/geneontology/go-annotation/issues/2469
- kind: issue
  title: go-annotation#2510
  url: https://github.com/geneontology/go-annotation/issues/2510
- kind: issue
  title: go-annotation#1886
  url: https://github.com/geneontology/go-annotation/issues/1886
- kind: wiki
  title: Guidelines for checkpoints
  url: https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints
- kind: issue
  title: go-annotation#1631
  url: https://github.com/geneontology/go-annotation/issues/1631
date: '2026-11-15'
---

# BP-6. Annotate the process the gene product acts in, not the readout that was measured

## Decision

**Statement.** Identify what was measured and what conclusion the authors drew. Then annotate the process closest to the gene product's activity that the evidence supports. Never annotate the assay readout as a process when the readout is a downstream marker of something else.

## Context

"Beware of read-outs" is long-standing GOC guidance. The wiki's example is DNA fragmentation, a readout for apoptosis that does not place the mutated gene in DNA catabolism ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). The QC group's reports repeat it as "annotate to the conclusion of the experiment, not the read-out" ([Drive: GOC NYC 2018 QC group report](https://drive.google.com/open?id=1cTLQGeV9aUiMvMgW5DxB8pNOARlMoNmmz7nqiyxXPg0)).

**Common readouts and what they do not show:**

| Readout | Tempting term | Why it fails | Source |
|---|---|---|---|
| TUNEL, annexin V, cleaved caspase-3, PARP cleavage | apoptotic signaling or its regulation | late endpoints of almost any death; annexin V marks PS exposure, which is not the gene's activity | [wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual); [APOPTOSIS assay readouts](https://ai4curation.io/ai-gene-review/pages/projects/APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.html) |
| cytochrome c release, MOMP | regulation of cytochrome c release / MOMP | "pretty much any apoptosis-inducing event will trigger MOMP" | [wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual) |
| mitochondrial membrane depolarisation | mitochondrion organization | readout of reduced mitochondrial activity | [go-annotation#2469](https://github.com/geneontology/go-annotation/issues/2469) |
| reduced DNA synthesis after siRNA | regulation of DNA replication | many cell-cycle blocks give the same result | [go-annotation#2510](https://github.com/geneontology/go-annotation/issues/2510) |
| cell size in a screen | regulation of cell size | indirect growth effects | [go-annotation#1886](https://github.com/geneontology/go-annotation/issues/1886) |
| checkpoint arrest in a mutant | checkpoint terms | arrest shows the checkpoint works; the mutated gene caused the damage | [wiki: Guidelines for checkpoints](https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints) |
| altered spindle pole body separation from nuclear envelope defects | SPB separation | indirect phenotype | [go-annotation#1631](https://github.com/geneontology/go-annotation/issues/1631) |

## Application

**Worked example.** Silencing human RPS19 produces condensed DNA, nuclear fragmentation and PARP cleavage. Curators decided not to annotate regulation of apoptosis, because RPS19's role in small-subunit biogenesis explains the death as an indirect effect ([wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |

## Sources

- wiki: [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
- drive: [GOC NYC 2018 QC group report](https://drive.google.com/open?id=1cTLQGeV9aUiMvMgW5DxB8pNOARlMoNmmz7nqiyxXPg0)
- wiki: [Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)
- web: [APOPTOSIS assay readouts](https://ai4curation.io/ai-gene-review/pages/projects/APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.html)
- issue: [go-annotation#2469](https://github.com/geneontology/go-annotation/issues/2469)
- issue: [go-annotation#2510](https://github.com/geneontology/go-annotation/issues/2510)
- issue: [go-annotation#1886](https://github.com/geneontology/go-annotation/issues/1886)
- wiki: [Guidelines for checkpoints](https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints)
- issue: [go-annotation#1631](https://github.com/geneontology/go-annotation/issues/1631)

<!-- END GENERATED -->
