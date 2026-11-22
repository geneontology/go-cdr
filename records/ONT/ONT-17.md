---
id: ONT-17
title: When an annotation violates a constraint, decide which of the two is wrong
status: proposed
topic: ONT
provenance: GOC_PLUS
provenance_note: '[GOC+]. The filtering behaviour is GOC; requiring a reviewer to decide which side is
  wrong is ours.'
evidence_codes:
- IBA
- IEA
go_terms:
- term_id: GO:0007179
  label: transforming growth factor beta receptor signaling pathway
differences:
- prior_source: '[Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)
    (GORULE:0000013)'
  prior_said: Experimental violations reported, kept; non-experimental filtered
  we_recommend: 'Filtering is not a fix: record the node or mapping defect; for experimental violations
    decide whether the constraint or the term choice is wrong'
  why: 5 of 21 violated constraints looked too narrow in one re-examination ([ONT-17](ONT-17.md))
sources:
- kind: drive
  title: Taxon Constraints for Signaling Pathways
  url: https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg
- kind: web
  title: RAR_MISANNOTATION
  url: https://ai4curation.io/ai-gene-review/pages/projects/RAR_MISANNOTATION.html
date: '2026-11-15'
---

# ONT-17. When an annotation violates a constraint, decide which of the two is wrong

## Decision

A non-experimental annotation that violates a taxon constraint is removed, and the cause is
fixed at its source (the PAINT node, the InterPro2GO mapping, the orthology projection). An
experimental annotation that violates one is examined: if the organism really performs the
function, the constraint is too narrow and should be corrected; if not, the annotation is wrong
in its choice of term.

## Context

GORULE:0000013 checks constraints. Non-experimental violations are filtered from GO products;
experimental violations are reported to the assigning group and left in place; NOT annotations
are exempt ([Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)).
Filtering hides the error from users without fixing the node or mapping that made it, so a
reviewer should still record the source defect.

*Constraint too narrow.* A re-examination of rare-in-lineage annotations found 38 that break an
existing constraint. Of the 21 terms involved, 14 were annotation errors and 5 constraints
looked too narrow: glutamate-gated calcium channel activity and plasma membrane repair are
restricted to Metazoa although plant GLR3.3 and SYT1 do these things; cholesterol binding is
`never_in` Fungi although CAP proteins bind sterols; sperm axoneme assembly is Metazoa-only
although *Selaginella* makes flagellate sperm ([RAR_MISANNOTATION](https://ai4curation.io/ai-gene-review/pages/projects/RAR_MISANNOTATION.html)).

*Annotation wrong.* Histone deacetylase activity on *B. subtilis* AcuC (`never_in` Bacteria)
and nuclear mRNA decapping on bacterial RppH proteins (`only_in` Eukaryota) arrived by IBA from
nodes placed too deep. TreeGrafter adds a further route: it grafts unreviewed proteins onto
PAINT nodes without a taxon check, so one node placed too deep becomes many IEA rows
([RAR_MISANNOTATION](https://ai4curation.io/ai-gene-review/pages/projects/RAR_MISANNOTATION.html)).

*A real case where both are partly right.* In 2023, 33 *C. elegans* annotations to
`GO:0007179` transforming growth factor beta receptor signaling pathway were flagged as
violations, although worms have TGF-beta superfamily ligands and receptors. The problem is a
pathway term named after one receptor subfamily in a family whose subfamilies do not map neatly
onto GO's terms ([Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)).
Such cases need an ontology fix, not a choice between deleting the worm rows and deleting the
constraint.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The filtering behaviour is GOC; requiring a reviewer to decide which side is wrong is ours. |
| Date | 2026-11-15 |
| Evidence codes | IBA, IEA |
| GO terms | `GO:0007179` transforming growth factor beta receptor signaling pathway |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [ONT-17-E1](ONT-17.examples.yaml): An inflammatory response IBA on a mosquito Toll receptor removed for a Vertebrata constraint | Conformant | TOLL9 involved_in GO:0006954 inflammatory response (IBA, GO_REF:0000033) |
| [ONT-17-E2](ONT-17.examples.yaml): A bacterial flagellar regulator's experimental row on a cilium motility term | Conformant | fleQ involved_in GO:2000155 positive regulation of cilium-dependent cell motility (IMP, PMID:12218010) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg) (GORULE:0000013) | Experimental violations reported, kept; non-experimental filtered | Filtering is not a fix: record the node or mapping defect; for experimental violations decide whether the constraint or the term choice is wrong | 5 of 21 violated constraints looked too narrow in one re-examination ([ONT-17](ONT-17.md)) |

## Sources

- drive: [Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)
- web: [RAR_MISANNOTATION](https://ai4curation.io/ai-gene-review/pages/projects/RAR_MISANNOTATION.html)

<!-- END GENERATED -->
