---
id: PC-3
title: A gene product that binds a complex without being part of it gets `GO:0044877` protein-containing
  complex binding or a specific child, not `part_of` or `located_in` the complex.
status: proposed
topic: PC
provenance: GOC
aspects:
- C
- F
evidence_codes:
- IBA
go_terms:
- term_id: GO:0044877
  label: protein-containing complex binding
- term_id: GO:0022627
  label: cytosolic small ribosomal subunit
- term_id: GO:0043022
  label: ribosome binding
- term_id: GO:0043024
  label: ribosomal small subunit binding
sources:
- kind: wiki
  title: Located in
  url: https://wiki.geneontology.org/index.php/Located_in
- kind: drive
  title: Guidelines for P2GO
  url: https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc
- kind: wiki
  title: Guidelines for new Binding terms
  url: https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms
- kind: issue
  title: go-annotation#5574
  url: https://github.com/geneontology/go-annotation/issues/5574
date: '2026-11-15'
---

# PC-3. A gene product that binds a complex without being part of it gets `GO:0044877` protein-containing complex binding or a specific child, not `part_of` or `located_in` the complex.

## Decision

A gene product that binds a complex without being part of it gets `GO:0044877` protein-containing complex binding or a specific child, not `part_of` or `located_in` the complex.

## Context

`part_of` is the only CC relation for complex terms; `located_in` and `is_active_in` are for
cellular anatomical entities
([wiki: Located in](https://wiki.geneontology.org/index.php/Located_in);
[Drive: Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc),
which names complex binding for non-members). New subclasses of `GO:0044877` must correspond to
a complex term
([wiki: Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)).

## Application

*Example.* A fission yeast translation elongation factor carried an IBA `part_of`
`GO:0022627` cytosolic small ribosomal subunit propagated from a budding-yeast source. The
2024 fix removed `part_of`; GO's view was that ribosome binding, not membership, describes a
factor that delivers tRNA to the ribosome
([go-annotation#5574](https://github.com/geneontology/go-annotation/issues/5574);
`GO:0043022` ribosome binding, or `GO:0043024` ribosomal small subunit binding). Keeping a
`located_in` row to the ribosomal subunit, as one curator proposed, uses a relation that the
P2GO table excludes for complex terms.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | IBA |
| GO terms | `GO:0044877` protein-containing complex binding; `GO:0022627` cytosolic small ribosomal subunit; `GO:0043022` ribosome binding; `GO:0043024` ribosomal small subunit binding |

## Sources

- wiki: [Located in](https://wiki.geneontology.org/index.php/Located_in)
- drive: [Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- wiki: [Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)
- issue: [go-annotation#5574](https://github.com/geneontology/go-annotation/issues/5574)

<!-- END GENERATED -->
