---
id: MF-1
title: Assert an MF only for an activity the gene product itself performs
status: proposed
topic: MF
provenance: GOC
aspects:
- F
go_terms:
- term_id: GO:0060090
  label: molecular adaptor activity
- term_id: GO:0004679
  label: AMP-activated protein kinase activity
- term_id: GO:0019887
  label: protein kinase regulator activity
- term_id: GO:0000030
  label: mannosyltransferase activity
sources:
- kind: wiki
  title: Enables
  url: https://wiki.geneontology.org/index.php/Enables
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: wiki
  title: Contributes to
  url: https://wiki.geneontology.org/index.php/Contributes_to
- kind: wiki
  title: Guidelines for new Molecular Functions
  url: https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions
date: '2026-11-15'
---

# MF-1. Assert an MF only for an activity the gene product itself performs

## Decision

Use `enables` for an activity the gene product carries out, alone or as the
responsible subunit of a complex. Do not use an MF term to record a process role, a
phenotype, an interaction partner's activity, or an activity the protein merely
supports.

## Context

`enables` is the default MF relation and is reserved for "gene products
that mediate a Molecular Function"; accessory subunits "should not be annotated to a
Molecular Function in which they do not directly participate" and usually take
`GO:0060090` molecular adaptor activity or a regulator term instead
([wiki: Enables](https://wiki.geneontology.org/index.php/Enables)). A gene product that
is necessary for an activity is not thereby its performer; the same distinction
governs BP `involved_in` ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), "Do not add what curators
deliberately declined to add").

## Application

Worked example. In the AMP-activated protein kinase, PRKAA1 is the catalytic subunit
and enables `GO:0004679` AMP-activated protein kinase activity. PRKAG1 binds AMP/ADP and
stabilises the activation loop; it is annotated to `GO:0019887` protein kinase
regulator activity and does *not* contribute to the kinase activity
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). In the
PIGM–PIGX mannosyltransferase, only PIGM enables `GO:0000030` mannosyltransferase
activity, although PIGX is required.

Where the responsible subunit of a complex is unknown, make no MF annotation; capture
the complex membership (CC) and the process (BP)
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). The
`contributes_to` qualifier is reserved for irreducible molecular machines; see
[protein-complexes.md](../PC/README.md).


<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0060090` molecular adaptor activity; `GO:0004679` AMP-activated protein kinase activity; `GO:0019887` protein kinase regulator activity; `GO:0000030` mannosyltransferase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [MF-1-E1](MF-1.examples.yaml): Kinase activity removed from a cyclin regulatory subunit | Conformant | CCNE1 enables GO:0016301 kinase activity (IEA, GO_REF:0000107) |
| [MF-1-E2](MF-1.examples.yaml): GTPase activity removed from a G beta subunit despite an IDA row | Conformant | GNB1 enables GO:0003924 GTPase activity (IDA, PMID:1543505) |
| [MF-14-E1](MF-14.examples.yaml): The RCK regulatory subunit of a potassium transporter given a regulator term (from [MF-14](MF-14.md)) | Conformant | khtT enables GO:0008324 monoatomic cation transmembrane transporter activity (IEA, GO_REF:0000002) |
| [MF-14-E2](MF-14.examples.yaml): A PP2A B subunit kept as contributes_to the phosphatase activity (from [MF-14](MF-14.md)) | Non-conformant | PPP2R2A contributes_to GO:0004721 phosphoprotein phosphatase activity (IDA, PMID:30595372) |

## Sources

- wiki: [Enables](https://wiki.geneontology.org/index.php/Enables)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- wiki: [Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)
- wiki: [Guidelines for new Molecular Functions](https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions)

<!-- END GENERATED -->
