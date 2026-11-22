---
id: PC-7
title: Accessory, structural and regulatory subunits get their own MF or none; do not give them `contributes_to`
  the complex's catalytic activity.
status: proposed
topic: PC
provenance: GOC_PLUS
provenance_note: '[GOC+] GOC states the principle; the "part in the mechanism" test for machines, and
  the narrowing of the ATP synthase example, are ours.'
aspects:
- C
- F
evidence_codes:
- TAS
go_terms:
- term_id: GO:1990756
  label: ubiquitin-like ligase-substrate adaptor activity
- term_id: GO:0030234
  label: enzyme regulator activity
- term_id: GO:0019887
  label: protein kinase regulator activity
- term_id: GO:0004679
  label: AMP-activated protein kinase activity
- term_id: GO:0001671
  label: ATPase activator activity
- term_id: GO:0060090
  label: molecular adaptor activity
- term_id: GO:0030674
  label: protein-macromolecule adaptor activity
- term_id: GO:0140756
  label: structural constituent of proteasome
- term_id: GO:0003735
  label: structural constituent of ribosome
- term_id: GO:0046933
  label: proton-transporting ATP synthase activity, rotational mechanism
- term_id: GO:0008121
  label: quinol-cytochrome-c reductase activity
- term_id: GO:0004298
  label: threonine-type endopeptidase activity
- term_id: GO:0004129
  label: cytochrome-c oxidase activity
differences:
- prior_source: '[wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) (reviewed
    2023)'
  prior_said: All components of ATP synthase are annotated `contributes_to GO:0046933`
  we_recommend: '`contributes_to` only for subunits whose part is in the mechanism; inhibitors and supernumerary
    subunits of unknown role get none (PC-7)'
  why: Consistent with the wiki's own "only the subunits required" sentence and with the 2026 OXPHOS GO-CAM
    discussion
open_questions:
- '**Schema text.** The `contributes_to_molecular_function` description in `gene_review.yaml` gives an
  accessory-subunit example that PC-7 rejects; revising it is a schema change for the maintainers.'
sources:
- kind: issue
  title: go-annotation#2760
  url: https://github.com/geneontology/go-annotation/issues/2760
- kind: issue
  title: go-annotation#3510
  url: https://github.com/geneontology/go-annotation/issues/3510
- kind: issue
  title: go-annotation#3283
  url: https://github.com/geneontology/go-annotation/issues/3283
- kind: drive
  title: Annotating activities of complexes and subcomplexes
  url: https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s
date: '2026-11-15'
---

# PC-7. Accessory, structural and regulatory subunits get their own MF or none; do not give them `contributes_to` the complex's catalytic activity.

## Decision

Accessory, structural and regulatory subunits get their own MF or none; do not give them `contributes_to` the complex's catalytic activity.

## Context

The 2020 Complex Working Group: do not annotate subunits that do not participate in the MF with
`contributes_to`; adaptors, structural roles and regulatory roles have their own MF terms, and
a subunit can be left without an MF. Later tickets applied this to non-catalytic E3 subunits
(substrate adaptors such as F-box proteins take `GO:1990756` ubiquitin-like ligase-substrate
adaptor activity; [go-annotation#2760](https://github.com/geneontology/go-annotation/issues/2760)),
to non-catalytic transporter subunits (ATPase activator and adaptor terms;
[go-annotation#3510](https://github.com/geneontology/go-annotation/issues/3510)), and to
non-catalytic complex members generally (enzyme regulator or protein-RNA adaptor terms;
[go-annotation#3283](https://github.com/geneontology/go-annotation/issues/3283)).

| Subunit role | MF to consider | Example |
|---|---|---|
| Regulatory | `GO:0030234` enzyme regulator activity or a child, with `has_input` the catalytic subunit | PRKAG1 `GO:0019887` protein kinase regulator activity; PRKAA1 `enables` `GO:0004679` AMP-activated protein kinase activity |
| Activator of an ATPase | `GO:0001671` ATPase activator activity | torsin activators |
| Adaptor or bridge | `GO:0060090` molecular adaptor activity; `GO:0030674` protein-macromolecule adaptor activity; `GO:1990756` | F-box and DCAF substrate receptors |
| Structural | a "structural constituent of X" term | PSMA1 `GO:0140756` structural constituent of proteasome; ribosomal proteins `GO:0003735` |
| Unknown | no MF; CC and BP only | many OXPHOS supernumerary subunits |

**The ATP synthase and OXPHOS case.** The Contributes_to wiki says all components of ATP
synthase contribute to `GO:0046933`. The 2026 GO-CAM discussion of OXPHOS complexes I, III and
IV took a narrower view: catalytic-core subunits contribute to the activity, while
supernumerary subunits, which are eukaryote-specific with stabilising, regulatory or assembly
roles, do not
([Drive: Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s)).
We apply that narrower view to every coupled machine: a subunit `contributes_to` only if its
part is in the mechanism (a catalytic site, an electron-relay group, a substrate or quinone
site, the rotor, the stator or the proton channel). An inhibitor (ATP5IF1) gets regulator terms;
a supernumerary subunit of unknown role gets no MF.

## Application

*Examples of the error in the repo.* UQCRC1 is described in its own review as "a non-catalytic
structural core subunit" that "does not directly participate in the Q-cycle redox chemistry",
yet its core `molecular_function` is `GO:0008121` quinol-cytochrome-c reductase activity.
PSMA1's core function carries `contributes_to_molecular_function: GO:0004298`, although the
proteasome pilot concluded that threonine-type endopeptidase activity "should stay with PSMB5
and other catalytic beta subunits"; its `GO:0140756` structural MF is the right core. COX4I1,
a regulatory supernumerary subunit, has a TAS `enables GO:0004129` cytochrome-c oxidase activity
row ACCEPTed with a reason arguing for `contributes_to`. Each should be revised under this rule.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] GOC states the principle; the "part in the mechanism" test for machines, and the narrowing of the ATP synthase example, are ours. |
| Date | 2026-11-15 |
| Evidence codes | TAS |
| GO terms | `GO:1990756` ubiquitin-like ligase-substrate adaptor activity; `GO:0030234` enzyme regulator activity; `GO:0019887` protein kinase regulator activity; `GO:0004679` AMP-activated protein kinase activity; `GO:0001671` ATPase activator activity; `GO:0060090` molecular adaptor activity; `GO:0030674` protein-macromolecule adaptor activity; `GO:0140756` structural constituent of proteasome; `GO:0003735` structural constituent of ribosome; `GO:0046933` proton-transporting ATP synthase activity, rotational mechanism; `GO:0008121` quinol-cytochrome-c reductase activity; `GO:0004298` threonine-type endopeptidase activity; `GO:0004129` cytochrome-c oxidase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [PC-7-E1](PC-7.examples.yaml): A structural cytochrome-c oxidase subunit given the oxidase activity | Non-conformant | COX7B enables GO:0004129 cytochrome-c oxidase activity (TAS, PMID:8382530) |
| [PC-7-E2](PC-7.examples.yaml): A regulatory phosphorylase kinase subunit given the holoenzyme's kinase activity | Non-conformant | PHKA2 enables GO:0004689 phosphorylase kinase activity (IEA, GO_REF:0000117) |
| [PC-7-E3](PC-7.examples.yaml): A cofactor-free Complex I subunit with contributes_to in its core functions | Contested | The `core_functions` entry of the human NDUFA5 review: `molecular_function` `GO:0005198` structural molecule activity and `contributes_to_molecular_function` `GO:0008137` NADH dehydrogenase (ubiquinone) activity, for a non-catalytic accessory subunit that carries no redox cofactor. |
| [PC-4-E2](PC-4.examples.yaml): Complex I activity on an accessory subunit from a cDNA sequencing paper (from [PC-4](PC-4.md)) | Non-conformant | NDUFA2 enables GO:0008137 NADH dehydrogenase (ubiquinone) activity (NAS, PMID:9878551) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) (reviewed 2023) | All components of ATP synthase are annotated `contributes_to GO:0046933` | `contributes_to` only for subunits whose part is in the mechanism; inhibitors and supernumerary subunits of unknown role get none (PC-7) | Consistent with the wiki's own "only the subunits required" sentence and with the 2026 OXPHOS GO-CAM discussion |

## Open questions

1. **Schema text.** The `contributes_to_molecular_function` description in `gene_review.yaml` gives an accessory-subunit example that PC-7 rejects; revising it is a schema change for the maintainers.

## Sources

- issue: [go-annotation#2760](https://github.com/geneontology/go-annotation/issues/2760)
- issue: [go-annotation#3510](https://github.com/geneontology/go-annotation/issues/3510)
- issue: [go-annotation#3283](https://github.com/geneontology/go-annotation/issues/3283)
- drive: [Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s)

<!-- END GENERATED -->
