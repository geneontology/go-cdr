---
id: EV-2
title: Use IDA when the experiment measures the gene product's own activity, location or complex membership
  directly.
status: proposed
topic: EV
provenance: GOC
provenance_note: '[GOC] [wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29);
  [go-annotation#6468](https://github.com/geneontology/go-annotation/issues/6468).'
evidence_codes:
- IDA
- IPI
- IMP
- IEP
go_terms:
- term_id: GO:0005488
  label: binding
- term_id: GO:0005515
  label: protein binding
- term_id: GO:0004596
  label: protein-N-terminal amino-acid acetyltransferase activity
- term_id: GO:0051015
  label: actin filament binding
- term_id: GO:0004383
  label: guanylate cyclase activity
- term_id: GO:0006897
  label: endocytosis
- term_id: GO:0006914
  label: autophagy
related:
- EV-4
sources:
- kind: issue
  title: go-annotation#6468
  url: https://github.com/geneontology/go-annotation/issues/6468
- kind: paper
  title: PMID:21900231
  url: https://europepmc.org/article/MED/21900231
- kind: wiki
  title: IEP
  url: https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29
- kind: wiki
  title: IDA
  url: https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29
date: '2026-11-15'
---

# EV-2. Use IDA when the experiment measures the gene product's own activity, location or complex membership directly.

## Decision

Use IDA when the experiment measures the gene product's own activity, location or complex membership directly.

## Context

IDA (ECO:0000314) covers enzyme assays, in vitro reconstitution, immunolocalisation,
cell fractionation, and binding assays in which the partner cannot be given an
identifier (a nucleic acid, a lipid, actin filaments). IDA takes no WITH/FROM
(GORULE:0000017) and must not be used for `GO:0005488` binding or `GO:0005515`
protein binding (GORULE:0000003). Isolating a complex by pulling down a tagged
subunit is IDA for the complex (CC) term, because it assays the complex directly.

A protein expressed in a heterologous or overexpression system is still IDA when
the system is the vehicle for an assay of normal activity or location. The 2026
clarification ([go-annotation#6468](https://github.com/geneontology/go-annotation/issues/6468))
settled the boundary: overexpression used to measure a molecular function is IDA;
gain- or loss-of-function phenotypes used to infer a process are IMP
([EV-4](EV-4.md)).

## Application

*Examples.* `GO:0004596` protein-N-terminal amino-acid acetyltransferase activity
for NAA50 from enzyme kinetics ([PMID:21900231](https://europepmc.org/article/MED/21900231),
the IDA wiki example). `GO:0051015` actin filament binding for mouse Actn1 is IDA,
not IPI, because F-actin has no gene-product identifier. Rat guanylate cyclase GC-F
expressed in COS cells and assayed for `GO:0004383` guanylate cyclase activity is
IDA, not IEP ([wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29), PMID:7831337).

*Counter-example.* MGI annotated CREG1 (UniProtKB:O75629) to `GO:0006897`
endocytosis and `GO:0006914` autophagy as IDA from overexpression and knockdown
phenotypes. After #6468 these were recoded; process inferences from perturbation
phenotypes are IMP.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] [wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29); [go-annotation#6468](https://github.com/geneontology/go-annotation/issues/6468). |
| Date | 2026-11-15 |
| Related | [EV-4](EV-4.md) |
| Evidence codes | IDA, IPI, IMP, IEP |
| GO terms | `GO:0005488` binding; `GO:0005515` protein binding; `GO:0004596` protein-N-terminal amino-acid acetyltransferase activity; `GO:0051015` actin filament binding; `GO:0004383` guanylate cyclase activity; `GO:0006897` endocytosis; `GO:0006914` autophagy |

## Sources

- issue: [go-annotation#6468](https://github.com/geneontology/go-annotation/issues/6468)
- paper: [PMID:21900231](https://europepmc.org/article/MED/21900231)
- wiki: [IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29)
- wiki: [IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29)

<!-- END GENERATED -->
