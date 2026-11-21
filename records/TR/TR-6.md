---
id: TR-6
title: Separate GTFs from coTFs by where they are recruited, and annotate GTFs to transcription itself
status: proposed
topic: TR
provenance: GOC
aspects:
- F
- P
evidence_codes:
- IBA
go_terms:
- term_id: GO:0006351
  label: DNA-templated transcription
- term_id: GO:0003713
  label: transcription coactivator activity
- term_id: GO:0016251
  label: RNA polymerase II general transcription initiation factor activity
sources:
- kind: issue
  title: go-annotation#4554
  url: https://github.com/geneontology/go-annotation/issues/4554
- kind: issue
  title: go-annotation#2853
  url: https://github.com/geneontology/go-annotation/issues/2853
- kind: issue
  title: go-annotation#2933
  url: https://github.com/geneontology/go-annotation/issues/2933
date: '2026-11-15'
---

# TR-6. Separate GTFs from coTFs by where they are recruited, and annotate GTFs to transcription itself

## Decision

A protein recruited through core promoter elements (TATA box, initiator) to act at
every promoter of its polymerase is a GTF: annotate the polymerase-specific GTF activity
and the transcription BP, not regulation of transcription. A protein recruited through
gene-specific elements by a dbTF is a coTF, even if it is also a subunit of a GTF in
another context. Use `GO:0006351` DNA-templated transcription and its children only for
RNA polymerase subunits and GTFs.

## Context

"If the protein(complex) recruitment happens via the core promoter elements
(TATA box, initiator, etc) then it is a GTF. Via the other (gene-specific elements)
located in the promoter/enhancer, then it is a cofactor"
([go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554)). GO
decided that GTFs are core machinery annotated to transcription, not to its regulation
([go-annotation#2853](https://github.com/geneontology/go-annotation/issues/2853)), and
that the transcription term and children are for RNA polymerase and GTFs only, with
other annotations moved to regulation terms
([go-annotation#2933](https://github.com/geneontology/go-annotation/issues/2933); the
review is still open). The ontology makes the GTF terms part of transcription.

## Application

Worked examples. S. pombe Taf11, a TFIID subunit, had an IBA to `GO:0003713`
transcription coactivator activity; it was filtered and annotated to `GO:0016251` RNA
polymerase II general transcription initiation factor activity
([go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554)). Some
TFIID subunits also belong to coactivator complexes (SAGA); those take a coTF term only
from experiments showing dbTF-directed recruitment. Mediator subunits are coactivators
by definition: GO:0003713's definition names "the Mediator complex, which bridges
sequence-specific DNA binding transcription factors and RNA polymerase".

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | IBA |
| GO terms | `GO:0006351` DNA-templated transcription; `GO:0003713` transcription coactivator activity; `GO:0016251` RNA polymerase II general transcription initiation factor activity |

## Sources

- issue: [go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554)
- issue: [go-annotation#2853](https://github.com/geneontology/go-annotation/issues/2853)
- issue: [go-annotation#2933](https://github.com/geneontology/go-annotation/issues/2933)

<!-- END GENERATED -->
