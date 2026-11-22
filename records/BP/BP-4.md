---
id: BP-4
title: When the mechanism is unknown, use `acts upstream of or within`, choose a sign, and choose the
  most proximal process
status: proposed
topic: BP
provenance: GOC_PLUS
provenance_note: '[GOC]. The review handling is [GOC+].'
aspects:
- P
go_terms:
- term_id: GO:0006915
  label: apoptotic process
- term_id: GO:0090200
  label: positive regulation of release of cytochrome c from mitochondria
related:
- BP-7
- QN-7
sources:
- kind: issue
  title: go-annotation#1517
  url: https://github.com/geneontology/go-annotation/issues/1517
- kind: wiki
  title: Annotation Relations
  url: https://wiki.geneontology.org/index.php/Annotation_Relations
- kind: drive
  title: Annotation relations – Guidelines for P2GO
  url: https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc
- kind: drive
  title: Regulation and causality & use of qualifiers in legacy annotations
  url: https://drive.google.com/open?id=1fmgRMOPel-8_7iIuMAkVDNGuxurUWTxJRdsZTgSeNRM
- kind: wiki
  title: Annotating from phenotypes
  url: https://wiki.geneontology.org/index.php/Annotating_from_phenotypes
- kind: repo
  title: docs/source_defects.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md
date: '2026-11-15'
---

# BP-4. When the mechanism is unknown, use `acts upstream of or within`, choose a sign, and choose the most proximal process

## Decision

**Statement.** If the evidence shows that the gene product affects a process but not how its activity relates to that process, annotate with `acts upstream of or within`. Use the positive- or negative-effect child whenever the direction is known, which it almost always is from a perturbation. Choose the most proximal process the data support, not the furthest readout. Making no annotation is acceptable when the only available term is organism-level (BP-7).

## Context

The relation was introduced at the 2017 Cambridge GOC meeting for this case ([go-annotation#1517](https://github.com/geneontology/go-annotation/issues/1517)). Both the wiki and the P2GO relation table tell curators to pick the signed child ([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations); [Drive: Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)). It is also the default BP relation: GORULE:0000061 assigns it when none is asserted ([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)). The 2017 Corvallis presentation argued that legacy BP annotations, made before relations existed, mean only "most likely upstream of, and possibly a participant in" ([Drive: Regulation and causality & use of qualifiers in legacy annotations](https://drive.google.com/open?id=1fmgRMOPel-8_7iIuMAkVDNGuxurUWTxJRdsZTgSeNRM)).

## Application

**Worked examples.**

- Human CHCHD10: mutant alleles inhibit apoptosis by preventing cytochrome c release. The wiki says the only valid annotation is `acts upstream of or within` GO:0006915 apoptotic process (here the negative-effect child), and explicitly not GO:0090200 positive regulation of release of cytochrome c from mitochondria ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)).
- *Dictyostelium* AbcA knockouts have sorocarp defects. The curator who proposed the relation gave this as the model case, `acts upstream of or within` sorocarp morphogenesis ([go-annotation#1517](https://github.com/geneontology/go-annotation/issues/1517)).

**In review.** An `involved_in` row supported only by a phenotype, with no mechanism, has the wrong relation. That does not make it a false claim. Correct the relation as structured data, following [QN-7](../QN/QN-7.md): mark the row `MODIFY`, say in `reason` that only the relation changes, and add a `NEW` row with the same term and `qualifier: acts_upstream_of_or_within` (with its sign where known). When a more proximal term exists, the `MODIFY` proposes it instead. Where the source should change its export, also record a source defect (`defect_type: WRONG_QUALIFIER`, see [docs/source_defects.md](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)). If the process is real but peripheral, the corrected row is non-core. Do not `REMOVE` a true claim because its relation was too strong.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC]. The review handling is [GOC+]. |
| Date | 2026-11-15 |
| Related | [BP-7](BP-7.md), [QN-7](../QN/QN-7.md) |
| GO terms | `GO:0006915` apoptotic process; `GO:0090200` positive regulation of release of cytochrome c from mitochondria |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [BP-4-E1](BP-4.examples.yaml): A nuclease's effect on antimicrobial gene expression kept as a signed upstream annotation | Conformant | nuc-1 acts_upstream_of_or_within_positive_effect GO:0002785 negative regulation of antimicrobial peptide production (IMP, PMID:26251453) |
| [BP-4-E2](BP-4.examples.yaml): An usher annotated as involved in cell adhesion from an adhesion-defect phenotype | Non-conformant | cupA3 involved_in GO:0007155 cell adhesion (IMP, PMID:11381121) |
| [BP-4-E3](BP-4.examples.yaml): A new upstream heat-response row without the sign its own evidence gives | Non-conformant | CnoX acts_upstream_of_or_within GO:0009408 response to heat (IMP, PMID:18657513) |

## Sources

- issue: [go-annotation#1517](https://github.com/geneontology/go-annotation/issues/1517)
- wiki: [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- drive: [Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- drive: [Regulation and causality & use of qualifiers in legacy annotations](https://drive.google.com/open?id=1fmgRMOPel-8_7iIuMAkVDNGuxurUWTxJRdsZTgSeNRM)
- wiki: [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
- repo: [docs/source_defects.md](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)

<!-- END GENERATED -->
