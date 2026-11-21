---
id: PH-8
title: Ignore seed qualifiers except NOT; carry `contributes_to` only where the subunit's role is conserved
status: proposed
topic: PH
provenance: GOC_PLUS
provenance_note: '[GOC] for defaults; [GOC+] for the strip test and the seed-relation caveat.'
evidence_codes:
- IBA
- IBD
- ISS
- ISO
- ISA
go_terms:
- term_id: GO:0003899
  label: DNA-directed RNA polymerase activity
related:
- PH-2
differences:
- prior_source: '[wiki: 5 May 2020 PAINT call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)'
  prior_said: Seed qualifiers other than NOT are ignored; IBDs default to `involved_in`/`is_active_in`/`enables`.
  we_recommend: Keep the default, but check `acts_upstream_of_or_within` seeds for indirect evidence before
    placing a BP (PH-8).
  why: The default silently upgrades indirect seeds to direct claims.
- prior_source: '[go-annotation#1319](https://github.com/geneontology/go-annotation/issues/1319), [#5254](https://github.com/geneontology/go-annotation/issues/5254),
    [#3242](https://github.com/geneontology/go-annotation/issues/3242)'
  prior_said: '`contributes_to` propagates as made; should be documented.'
  we_recommend: Carry it only for distributed active sites; the row must read correctly if the qualifier
    is stripped (PH-8).
  why: Software strips qualifiers; peripheral subunits otherwise inherit catalytic activity.
sources:
- kind: wiki
  title: 5 May 2020 PAINT call
  url: https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call
- kind: issue
  title: go-annotation#5254
  url: https://github.com/geneontology/go-annotation/issues/5254
- kind: issue
  title: go-annotation#3242
  url: https://github.com/geneontology/go-annotation/issues/3242
- kind: issue
  title: go-annotation#1319
  url: https://github.com/geneontology/go-annotation/issues/1319
date: '2026-11-15'
---

# PH-8. Ignore seed qualifiers except NOT; carry `contributes_to` only where the subunit's role is conserved

## Decision

When judging whether an experimental row supports an IBD, ignore its gene-product-to-term
relation except NOT. IBDs default to `involved_in` (BP), `is_active_in` (CC) and `enables`
(MF). Use `contributes_to` on an IBD, ISS or ISO only when the seed carries it and the target
is a subunit of the same complex in which the activity is distributed. The annotation should
still read correctly if a consumer strips the qualifier.

## Context

the qualifier policy for GAF 2.2 is a 2020 PAINT decision
([wiki: 5 May 2020 PAINT call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)).
It means an `acts_upstream_of_or_within` seed can yield an `involved_in` IBA, which upgrades the
claim; the seed check in PH-2 is therefore where indirect evidence must be caught. PAINT
propagates the qualifier the primary annotation had and cannot add or remove it; where seeds
disagree the PAINT curator chooses ([go-annotation#5254](https://github.com/geneontology/go-annotation/issues/5254)).
Curators agreed that a `contributes_to` may be carried into an ISS/ISA, and that this should be
documented ([go-annotation#3242](https://github.com/geneontology/go-annotation/issues/3242)).
Peripheral RNA polymerase subunits are the cautionary case: `GO:0003899` DNA-directed RNA
polymerase activity with `contributes_to` is defensible on core subunits and doubtful on
Rpb4/7, which the enzyme does not need for catalysis ([go-annotation#1319](https://github.com/geneontology/go-annotation/issues/1319)).

## Application

Worked example: SPO11 might borrow `contributes_to` endonuclease activity from archaeal Top6A
by ISA. The PomBase view, which we adopt, is to use `contributes_to` only for distributed active
sites (polymerases, proteasome) and to prefer a regulator term or a weaker MF when the subunit
is known not to be catalytic ([go-annotation#3242](https://github.com/geneontology/go-annotation/issues/3242)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for defaults; [GOC+] for the strip test and the seed-relation caveat. |
| Date | 2026-11-15 |
| Related | [PH-2](PH-2.md) |
| Evidence codes | IBA, IBD, ISS, ISO, ISA |
| GO terms | `GO:0003899` DNA-directed RNA polymerase activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: 5 May 2020 PAINT call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call) | Seed qualifiers other than NOT are ignored; IBDs default to `involved_in`/`is_active_in`/`enables`. | Keep the default, but check `acts_upstream_of_or_within` seeds for indirect evidence before placing a BP (PH-8). | The default silently upgrades indirect seeds to direct claims. |
| [go-annotation#1319](https://github.com/geneontology/go-annotation/issues/1319), [#5254](https://github.com/geneontology/go-annotation/issues/5254), [#3242](https://github.com/geneontology/go-annotation/issues/3242) | `contributes_to` propagates as made; should be documented. | Carry it only for distributed active sites; the row must read correctly if the qualifier is stripped (PH-8). | Software strips qualifiers; peripheral subunits otherwise inherit catalytic activity. |

## Sources

- wiki: [5 May 2020 PAINT call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)
- issue: [go-annotation#5254](https://github.com/geneontology/go-annotation/issues/5254)
- issue: [go-annotation#3242](https://github.com/geneontology/go-annotation/issues/3242)
- issue: [go-annotation#1319](https://github.com/geneontology/go-annotation/issues/1319)

<!-- END GENERATED -->
