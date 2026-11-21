---
id: LIT-4
title: 'Weigh localisation data by what was localised: endogenous protein in its native cell outranks
  a tagged, overexpressed construct.'
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC+] — the IDA page accepts overexpression as an assay system; the ranking and the
  transit rule come from [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html).'
evidence_codes:
- IDA
go_terms:
- term_id: GO:0005743
  label: mitochondrial inner membrane
- term_id: GO:0005789
  label: endoplasmic reticulum membrane
open_questions:
- Should the GOC adopt an explicit localisation-evidence ranking (LIT-4), and should overexpressed localisation
  require a compartment marker to support IDA at all?
sources:
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
date: '2026-11-15'
---

# LIT-4. Weigh localisation data by what was localised: endogenous protein in its native cell outranks a tagged, overexpressed construct.

## Decision

Weigh localisation data by what was localised: endogenous protein in its native cell outranks a tagged, overexpressed construct.

## Context

A localisation result supports a CC term at the resolution of the assay. Rank the
evidence:

1. endogenous protein, specific antibody or knock-in tag, native cell type, with a
   compartment marker;
2. tagged protein at near-endogenous level, with a marker;
3. overexpressed tagged protein, with a marker;
4. overexpressed protein described by shape alone ("perinuclear", "resembling the
   Golgi");
5. a crude fraction not checked for contaminating compartments.

Levels 1-3 can support the organelle term. Level 4 supports nothing beyond the
cell. Level 5 is the subject of [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html): a
"mitochondrial" fraction not checked for an ER marker cannot separate mitochondria
from mitochondria-associated ER membranes. A sub-compartment
(`GO:0005743` mitochondrial inner membrane, `GO:0005789` endoplasmic reticulum
membrane) needs an assay that resolves it or two independent lines that agree.

Overexpression creates specific artefacts. Saturated targeting machinery leaves
protein in the ER, and mutant or misfolded protein is retained there. A secreted or
plasma-membrane protein seen in the ER is in transit, not resident; its ER row is
non-core only with direct evidence on the endogenous protein, otherwise
over-annotated. In the ORGANELLES audit CABP2's Golgi row rested on overexpressed
CaBP2 "resembling the Golgi apparatus", while all marker work in the paper was on
CaBP7/8; CERKL's ER rows all came from overexpressed tagged constructs.

Being located somewhere does not mean acting there. Whether to use `located_in`
or `is_active_in` is a CC question ([cellular-component.md](../CC/README.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] — the IDA page accepts overexpression as an assay system; the ranking and the transit rule come from [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html). |
| Date | 2026-11-15 |
| Evidence codes | IDA |
| GO terms | `GO:0005743` mitochondrial inner membrane; `GO:0005789` endoplasmic reticulum membrane |

## Open questions

1. Should the GOC adopt an explicit localisation-evidence ranking (LIT-4), and should overexpressed localisation require a compartment marker to support IDA at all?

## Sources

- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)

<!-- END GENERATED -->
