---
id: QN-9
title: A NOT negates the term and all its descendants. Place it on the most general term the evidence
  excludes, and never on an ancestor of a term the gene product positively has.
status: proposed
topic: QN
provenance: GOC_PLUS
provenance_note: '[GOC+]. GOC states downward propagation. The placement procedure is ours. [wiki: Elements
  of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation); [go-annotation#1761](https://github.com/geneontology/go-annotation/issues/1761).'
go_terms:
- term_id: GO:0004672
  label: protein kinase activity
- term_id: GO:0004674
  label: protein serine/threonine kinase activity
- term_id: GO:1904161
  label: DNA synthesis involved in UV-damage excision repair
- term_id: GO:0000731
  label: DNA synthesis involved in DNA repair
- term_id: GO:0006303
  label: double-strand break repair via nonhomologous end joining
- term_id: GO:0006281
  label: DNA repair
- term_id: GO:0006289
  label: nucleotide-excision repair
- term_id: GO:0005544
  label: calcium-dependent phospholipid binding
- term_id: GO:0005543
  label: phospholipid binding
sources:
- kind: issue
  title: go-annotation#1761
  url: https://github.com/geneontology/go-annotation/issues/1761
- kind: wiki
  title: 16 December 2014 PAINT Conference Call
  url: https://wiki.geneontology.org/index.php/16_December_2014_PAINT_Conference_Call
- kind: repo
  title: action consistency
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md
- kind: wiki
  title: Elements of an annotation
  url: https://wiki.geneontology.org/index.php/Elements_of_an_annotation
date: '2026-11-15'
---

# QN-9. A NOT negates the term and all its descendants. Place it on the most general term the evidence excludes, and never on an ancestor of a term the gene product positively has.

## Decision

A NOT negates the term and all its descendants. Place it on the most general term the evidence excludes, and never on an ancestor of a term the gene product positively has.

## Context

"NOT enables GO:0004672 protein kinase activity" also means NOT GO:0004674 protein serine/threonine kinase activity (which `is_a` GO:0004672), and NOT every other child. A NOT placed too high therefore contradicts any positive annotation below it, even one from a different paper.

## Application

**Example (DNA polymerase alpha, [go-annotation#1761](https://github.com/geneontology/go-annotation/issues/1761)).** Human POLA1 (P09884) carried NOT rows to excision-repair processes (PMID:1730053, PMID:1508673) and also a NOT to the parent "DNA synthesis involved in DNA repair", while PMID:11470886 showed a role in double-strand break repair. GO:1904161 DNA synthesis involved in UV-damage excision repair `is_a` GO:0000731 DNA synthesis involved in DNA repair, and GO:0006303 double-strand break repair via nonhomologous end joining `is_a` GO:0006281 DNA repair. The NOT on the parent was the logical error. The fix moved the NOTs to the specific excision-repair children (GO:1904161, GO:0006289 nucleotide-excision repair) and kept the positive NHEJ annotation. Both papers stayed valid.

**Choosing the level.** Ask what the experiment excluded. A kinase-dead mutant shown to bind its substrate excludes catalysis (GO:0004672), not binding. A protein that keeps phospholipid binding but has lost calcium dependence gets NOT GO:0005544 calcium-dependent phospholipid binding while keeping GO:0005543 phospholipid binding. This is the Syt8 case from PAINT, PTHR10024 ([wiki: 16 December 2014 PAINT Conference Call](https://wiki.geneontology.org/index.php/16_December_2014_PAINT_Conference_Call)).

**Repo check.** The [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md) rules warn when a kept NOT row is on the same term as, or an ancestor of, a kept positive row. When it fired it found ARL6 NOT `cilium` against `axoneme`, DNM1L NOT `endoplasmic reticulum` against `endoplasmic reticulum membrane`, and APP NOT `dendrite` against `dendritic spine`.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. GOC states downward propagation. The placement procedure is ours. [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation); [go-annotation#1761](https://github.com/geneontology/go-annotation/issues/1761). |
| Date | 2026-11-15 |
| GO terms | `GO:0004672` protein kinase activity; `GO:0004674` protein serine/threonine kinase activity; `GO:1904161` DNA synthesis involved in UV-damage excision repair; `GO:0000731` DNA synthesis involved in DNA repair; `GO:0006303` double-strand break repair via nonhomologous end joining; `GO:0006281` DNA repair; `GO:0006289` nucleotide-excision repair; `GO:0005544` calcium-dependent phospholipid binding; `GO:0005543` phospholipid binding |

## Sources

- issue: [go-annotation#1761](https://github.com/geneontology/go-annotation/issues/1761)
- wiki: [16 December 2014 PAINT Conference Call](https://wiki.geneontology.org/index.php/16_December_2014_PAINT_Conference_Call)
- repo: [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)
- wiki: [Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)

<!-- END GENERATED -->
