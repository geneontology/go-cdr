---
id: CAM-3
title: The enabler is the gene product that performs the activity; use a complex as enabler only for an
  emergent activity, and never the root complex term.
status: proposed
topic: CAM
provenance: GOC_PLUS
provenance_note: '[GOC] for the three cases and the export table; [GOC+] for the ban on `GO:0032991` (asked
  but not settled in the 2025 deck) and for limiting `has part` to contributing subunits (the deck''s
  Case 4 flags the problem but gives no rule).'
go_terms:
- term_id: GO:0032991
  label: protein-containing complex
- term_id: GO:0031464
  label: Cul4A-RING E3 ubiquitin ligase complex
- term_id: GO:1990756
  label: ubiquitin-like ligase-substrate adaptor activity
- term_id: GO:0045254
  label: pyruvate dehydrogenase complex
- term_id: GO:0004739
  label: pyruvate dehydrogenase (acetyl-transferring) activity
- term_id: GO:0004742
  label: dihydrolipoyllysine-residue acetyltransferase activity
- term_id: GO:0004148
  label: dihydrolipoyl dehydrogenase (NADH) activity
related:
- CAM-6
differences:
- prior_source: '[Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)'
  prior_said: When no single subunit carries the activity, the complex is the enabler and each gene product
    has a `part of` relation to the activity.
  we_recommend: Complex enabler with `has part` only for contributing subunits, or no `has part` when
    the active subunit is unknown (CAM-3).
  why: Supersedes the earlier form; matches the 2025 rules and their export mapping.
- prior_source: '[Drive: GO-CAM modelling calls, 2022-02-15](https://drive.google.com/open?id=1rA1RiHst8e9tulY0zeua96WJSG2lKNS9VFWhDCWW2Ps)'
  prior_said: Proposed `GO:0032991` "or children" as allowed complex enablers.
  we_recommend: Never the root term (CAM-3).
  why: The 2025 deck asks whether the root should be disallowed; an enabler of "some complex" says nothing
    about who acts.
- prior_source: '[gocam-curation complexes reference](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/complexes.md)
    (repo)'
  prior_said: 'Case 3, shared activity: "represent the relevant contributing subunits".'
  we_recommend: Represent the complex as enabler with the contributing subunits as `has part` (CAM-3).
  why: The repo phrasing could be read as one node per subunit, which would export `enables` for each.
sources:
- kind: web
  title: PROTEIN_COMPLEX_FUNCTIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html
- kind: drive
  title: 2025 GO-CAM guidelines for protein-containing complexes
  url: https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE
- kind: drive
  title: Contributes_to (2021 GOC)
  url: https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks
- kind: drive
  title: GO-CAM modelling calls 2020-2022
  url: https://drive.google.com/open?id=1rA1RiHst8e9tulY0zeua96WJSG2lKNS9VFWhDCWW2Ps
date: '2026-11-15'
---

# CAM-3. The enabler is the gene product that performs the activity; use a complex as enabler only for an emergent activity, and never the root complex term.

## Decision

The enabler is the gene product that performs the activity; use a complex as enabler only for an emergent activity, and never the root complex term.

## Context

Apply the 2025 consortium rules for complexes in this order:

1. If a subunit performs the activity, that subunit is the enabler. Assign
   functions to the other subunits whose activity is known and link them in a
   causal flow (substrate adaptor, scaffold, catalytic subunit). Leave out
   subunits whose activity is unknown; their membership belongs in standard
   CC annotations to the complex term.
2. If several subunits are needed to form the active unit (a shared active
   site, a ligand pocket built from two chains, a heteromeric channel), the
   enabler is the most specific GO protein-containing complex term, with
   `has part` naming only the subunits that contribute.
3. If the active subunit is unknown, the complex term is the enabler and no
   `has part` is added.

Never use `GO:0032991` protein-containing complex itself as an enabler. If no
complex term of the right granularity exists, request one.

*Rationale.* The export depends on the case. Case 1 yields `GP enables MF`
for the active subunit. Case 2 is meant to yield `contributes_to` rows for each
`has part` member (not yet implemented in 2025). Case 3 yields no MF row at
all. A model that lists every member of a complex as `has part` will, once
case 2 export works, give the catalytic function to structural and accessory
subunits, which is exactly the over-annotation the complex working group set
out to stop ([PROTEIN_COMPLEX_FUNCTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html)).

## Application

*Example.* Case 1 in the 2025 deck: in the `GO:0031464` Cul4A-RING E3
ubiquitin ligase complex, DCAF12 enables `GO:1990756` ubiquitin-like
ligase-substrate adaptor activity, with the substrate as input, and the export
is "DCAF12 enables ubiquitin ligase-substrate adaptor activity". The cullin and
RING subunits get their own activities in the flow. For the pyruvate
dehydrogenase complex (`GO:0045254`), the three catalytic components each have
their own function (`GO:0004739` pyruvate dehydrogenase (acetyl-transferring)
activity, `GO:0004742` dihydrolipoyllysine-residue acetyltransferase activity,
`GO:0004148` dihydrolipoyl dehydrogenase (NADH) activity), linked by
`provides input for` because the lipoyl intermediate is protein-bound
(CAM-6).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the three cases and the export table; [GOC+] for the ban on `GO:0032991` (asked but not settled in the 2025 deck) and for limiting `has part` to contributing subunits (the deck's Case 4 flags the problem but gives no rule). |
| Date | 2026-11-15 |
| Related | [CAM-6](CAM-6.md) |
| GO terms | `GO:0032991` protein-containing complex; `GO:0031464` Cul4A-RING E3 ubiquitin ligase complex; `GO:1990756` ubiquitin-like ligase-substrate adaptor activity; `GO:0045254` pyruvate dehydrogenase complex; `GO:0004739` pyruvate dehydrogenase (acetyl-transferring) activity; `GO:0004742` dihydrolipoyllysine-residue acetyltransferase activity; `GO:0004148` dihydrolipoyl dehydrogenase (NADH) activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA) | When no single subunit carries the activity, the complex is the enabler and each gene product has a `part of` relation to the activity. | Complex enabler with `has part` only for contributing subunits, or no `has part` when the active subunit is unknown (CAM-3). | Supersedes the earlier form; matches the 2025 rules and their export mapping. |
| [Drive: GO-CAM modelling calls, 2022-02-15](https://drive.google.com/open?id=1rA1RiHst8e9tulY0zeua96WJSG2lKNS9VFWhDCWW2Ps) | Proposed `GO:0032991` "or children" as allowed complex enablers. | Never the root term (CAM-3). | The 2025 deck asks whether the root should be disallowed; an enabler of "some complex" says nothing about who acts. |
| [gocam-curation complexes reference](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/complexes.md) (repo) | Case 3, shared activity: "represent the relevant contributing subunits". | Represent the complex as enabler with the contributing subunits as `has part` (CAM-3). | The repo phrasing could be read as one node per subunit, which would export `enables` for each. |

## Sources

- web: [PROTEIN_COMPLEX_FUNCTIONS](https://ai4curation.io/ai-gene-review/pages/projects/PROTEIN_COMPLEX_FUNCTIONS.html)
- drive: [2025 GO-CAM guidelines for protein-containing complexes](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE)
- drive: [Contributes_to (2021 GOC)](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks)
- drive: [GO-CAM modelling calls 2020-2022](https://drive.google.com/open?id=1rA1RiHst8e9tulY0zeua96WJSG2lKNS9VFWhDCWW2Ps)

<!-- END GENERATED -->
