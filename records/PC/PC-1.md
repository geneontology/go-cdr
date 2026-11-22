---
id: PC-1
title: Annotate `part_of` a complex only with evidence that the complex exists as a stable unit and that
  this gene product is an intrinsic member.
status: proposed
topic: PC
provenance: GOC_PLUS
provenance_note: '[GOC+] GOC states this bar for term creation; extending it to annotation is ours. The
  IPI and IDA pages disagree on the code for complex isolation by co-IP (see Differences).'
aspects:
- C
- F
evidence_codes:
- IDA
- IPI
- IBA
- ISS
- ISO
go_terms:
- term_id: GO:0044877
  label: protein-containing complex binding
- term_id: GO:0034464
  label: BBSome
differences:
- prior_source: '[wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)'
  prior_said: Evidence bar (no simple IP, pull-down, colocalization or two-hybrid) stated for creating
    complex terms
  we_recommend: Same bar for annotating `part_of` (PC-1)
  why: A term-creation bar that does not apply to annotation lets binary hits become membership
- prior_source: '[wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29)
    vs [wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29)'
  prior_said: 'IPI page: complex annotations from co-IP or pull-down may use IPI with the bait in WITH;
    IDA page: tagged-subunit isolation of a complex is IDA, not IPI'
  we_recommend: IDA for isolation of the defined complex; IPI only for a binary interaction, which does
    not support `part_of` (PC-1)
  why: The two pages conflict; IDA matches what the assay shows
sources:
- kind: wiki
  title: Protein complexes
  url: https://wiki.geneontology.org/index.php/Protein_complexes
- kind: wiki
  title: IDA
  url: https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29
- kind: web
  title: HUMAN_BBSOME
  url: https://ai4curation.io/ai-gene-review/pages/projects/HUMAN_BBSOME.html
date: '2026-11-15'
---

# PC-1. Annotate `part_of` a complex only with evidence that the complex exists as a stable unit and that this gene product is an intrinsic member.

## Decision

Annotate `part_of` a complex only with evidence that the complex exists as a stable unit and that this gene product is an intrinsic member.

## Context

GO defines a protein-containing complex as a stable assembly of two or more macromolecules, at
least one a protein, whose parts function together. Its editors' page accepts stringent
purification followed by detection of the members, and lists as unacceptable on their own:
simple immunoprecipitation, pull-downs from cell extracts without further purification,
colocalization, two-hybrid screens, genetic interaction, and transient enzyme-substrate or
receptor-ligand pairs (unless the pair is needed to assemble a functional complex, as for
dimeric PDGF bridging two receptors)
([wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)).

That page was written to decide which complexes deserve GO terms. We apply the same bar to
annotating a gene product to an existing complex term:

| Evidence | Supports `part_of` the complex? | Code |
|---|---|---|
| Purified complex (tandem affinity, gradient, gel filtration) with the protein identified as a member | yes | IDA |
| Cryo-EM or crystal structure of the assembled complex containing the protein | yes; but a structure of a partial complex does not define the full membership | IDA |
| Immunoprecipitation of a tagged subunit that recovers the defined complex | yes | IDA ([wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29)) |
| Binary interaction with one known member (Y2H, pull-down, co-IP from extract) | no; it supports a binding MF, at most `GO:0044877` protein-containing complex binding if the partner is the complex | IPI |
| Co-localization with complex members | no | |
| Homology to a member shown experimentally in another species, with orthology of the protein checked | yes | ISS/ISO/IBA |

## Application

*Example.* The BBSome review set replaced dozens of bare `protein binding` IPI rows with
membership of `GO:0034464` BBSome for the eight core subunits, whose membership rests on
purification and cryo-EM of the octamer; the chaperonin-like MKKS, BBS10 and BBS12 were not
given BBSome membership, because they assemble the complex rather than belong to it
([HUMAN_BBSOME](https://ai4curation.io/ai-gene-review/pages/projects/HUMAN_BBSOME.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] GOC states this bar for term creation; extending it to annotation is ours. The IPI and IDA pages disagree on the code for complex isolation by co-IP (see Differences). |
| Date | 2026-11-15 |
| Evidence codes | IDA, IPI, IBA, ISS, ISO |
| GO terms | `GO:0044877` protein-containing complex binding; `GO:0034464` BBSome |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [PC-1-E1](PC-1.examples.yaml): A Ku70-binding protein from a two-hybrid screen annotated as a DNA-PK complex subunit | Non-conformant | ATP23 part_of GO:0005958 DNA-dependent protein kinase-DNA ligase 4 complex (NAS, PMID:10219089) |
| [PC-1-E2](PC-1.examples.yaml): Chaperonin recovered with bait proteins annotated to a generic complex | Non-conformant | HSPD1 part_of GO:0032991 protein-containing complex (IDA, PMID:21328542) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes) | Evidence bar (no simple IP, pull-down, colocalization or two-hybrid) stated for creating complex terms | Same bar for annotating `part_of` (PC-1) | A term-creation bar that does not apply to annotation lets binary hits become membership |
| [wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) vs [wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29) | IPI page: complex annotations from co-IP or pull-down may use IPI with the bait in WITH; IDA page: tagged-subunit isolation of a complex is IDA, not IPI | IDA for isolation of the defined complex; IPI only for a binary interaction, which does not support `part_of` (PC-1) | The two pages conflict; IDA matches what the assay shows |

## Sources

- wiki: [Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)
- wiki: [IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29)
- web: [HUMAN_BBSOME](https://ai4curation.io/ai-gene-review/pages/projects/HUMAN_BBSOME.html)

<!-- END GENERATED -->
