---
id: AE-3
title: 'Use `has_input` for the specific, physiologically relevant molecular target that the term does
  not already name: a substrate, a binding partner, a target gene, or the gene product a regulator acts
  on.'
status: proposed
topic: AE
provenance: GOC
provenance_note: '[GOC]; the FXN worked example is ours.'
evidence_codes:
- IDA
- IPI
go_terms:
- term_id: GO:0004143
  label: ATP-dependent diacylglycerol kinase activity
- term_id: GO:0004674
  label: protein serine/threonine kinase activity
- term_id: GO:0005515
  label: protein binding
- term_id: GO:0005488
  label: binding
- term_id: GO:0008047
  label: enzyme activator activity
- term_id: GO:0004396
  label: hexokinase activity
sources:
- kind: wiki
  title: Annotation Conf. Call 2020-02-04
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04
- kind: wiki
  title: Contributes to
  url: https://wiki.geneontology.org/index.php/Contributes_to
- kind: drive
  title: GP2term and extensions (2021)
  url: https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc
- kind: issue
  title: go-annotation#2584
  url: https://github.com/geneontology/go-annotation/issues/2584
- kind: wiki
  title: Has input
  url: https://wiki.geneontology.org/index.php/Has_input
- kind: wiki
  title: Annotating binding
  url: https://wiki.geneontology.org/index.php/Annotating_binding
- kind: issue
  title: go-annotation#2076
  url: https://github.com/geneontology/go-annotation/issues/2076
date: '2026-11-15'
---

# AE-3. Use `has_input` for the specific, physiologically relevant molecular target that the term does not already name: a substrate, a binding partner, a target gene, or the gene product a regulator acts on.

## Decision

What to capture.

## Context

- Enzyme substrates more specific than the term. Human DGKA `enables` GO:0004143 ATP-dependent diacylglycerol kinase activity, `has_input` 1-O-palmityl-2-acetyl-sn-glycerol (CHEBI:75936 in the wiki example), IDA, PMID:22627129.
- Protein substrates. Human CDC7 phosphorylates MCM2 (PMID:15668232): GO:0004674 protein serine/threonine kinase activity `has_input` MCM2.
- Binding partners. Use the specific binding child when one exists. Otherwise use GO:0005515 protein binding or GO:0005488 binding with `has_input` the partner. Since the 2020 decision, chemical binding is annotated as GO:0005488 binding `has_input` the ChEBI entity rather than by requesting a new precomposed binding term ([wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)).
- Target genes of transcription regulators, on both the MF and the "regulation of transcription" BP row. Standard annotations are not linked, so an input stated on the MF cannot be inferred for the BP.
- The regulated gene product of a regulator activity. In `genes/human/FXN` the reviewed annotation of FXN `enables` GO:0008047 enzyme activator activity carries `has_input`(UniProtKB:Q9Y697, cysteine desulfurase NFS1) from PMID:38627381. That is the pattern the wiki gives for regulatory subunits ([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to), regulatory and catalytic subunits).

**What not to capture.**

- An input already in the term label or definition (GO:0004396 hexokinase activity `has_input` D-hexose).
- Currency metabolites: ATP for a kinase, NAD+ for a dehydrogenase. GO keeps only the reaction participants that carry the biological specificity, unlike Rhea, which lists them all ([Drive: GP2term and extensions (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc)).
- Cofactors and metal ions, and the "X" of an "X-dependent" activity (calcium for a calcium-dependent kinase).
- Assay analogues and artificial substrates. The input is the biological one.
- Sequence Ontology terms ([go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584)).

**`has_input` versus `with/from`.** `with/from` names the sequence that supports the evidence. `has_input` names the physiological target. A mouse protein shown to bind the human orthologue of its partner gets IPI `with`(human partner) and `has_input`(mouse partner) ([wiki: Has input](https://wiki.geneontology.org/index.php/Has_input); [wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).

**Direct contact is not required.** An enzyme assay implies contact with the substrate, and no separate interaction assay is needed. The 2018-2020 has_direct_input review ended with a single relation for both cases ([go-annotation#2076](https://github.com/geneontology/go-annotation/issues/2076)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC]; the FXN worked example is ours. |
| Date | 2026-11-15 |
| Evidence codes | IDA, IPI |
| GO terms | `GO:0004143` ATP-dependent diacylglycerol kinase activity; `GO:0004674` protein serine/threonine kinase activity; `GO:0005515` protein binding; `GO:0005488` binding; `GO:0008047` enzyme activator activity; `GO:0004396` hexokinase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [AE-3-E1](AE-3.examples.yaml): Target genes named on the regulation-of-transcription BP row as well as on the MF row | Conformant | LMX1B involved_in GO:0045944 positive regulation of transcription by RNA polymerase II (ISS, GO_REF:0000024) |
| [AE-3-E2](AE-3.examples.yaml): The GTPase acted on, recorded as has_input on a GEF activity | Conformant | ARHGEF16 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:20679435) |
| [AE-3-E3](AE-3.examples.yaml): Substrate and products that the enzyme term's definition already names | Non-conformant | GALC enables GO:0004336 galactosylceramidase activity (IDA, PMID:8281145) |
| [AE-2-E1](AE-2.examples.yaml): One has_input group per target gene on a transcription factor activity (from [AE-2](AE-2.md)) | Conformant | LMX1B enables GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific (ISS, GO_REF:0000024) |
| [AE-4-E2](AE-4.examples.yaml): Water recorded as an output of a peroxidase (from [AE-4](AE-4.md)) | Non-conformant | LPO enables GO:0004601 peroxidase activity (IDA, PMID:6295491) |
| [AE-8-E1](AE-8.examples.yaml): An activator activity part_of heme biosynthesis, with the matching BP row from the same paper (from [AE-8](AE-8.md)) | Conformant | FXN enables GO:0008047 enzyme activator activity (IDA, PMID:15123683) |
| [AE-11-E3](AE-11.examples.yaml): An enzyme row that also asserts it is causally upstream of its substrate's activity (from [AE-11](AE-11.md)) | Non-conformant | AASDHPPT enables GO:0008897 holo-[acyl-carrier-protein] synthase activity (IDA, PMID:19933275) |
| [AE-12-E2](AE-12.examples.yaml): A substrate extension authored onto IBA, IEA and ISS GEF rows (from [AE-12](AE-12.md)) | Non-conformant | DOCK11 enables GO:0005085 guanyl-nucleotide exchange factor activity (IBA, GO_REF:0000033) |
| [AE-14-E1](AE-14.examples.yaml): A protease row accepted with its substrate, process and location extensions checked (from [AE-14](AE-14.md)) | Conformant | LONP1 enables GO:0004176 ATP-dependent peptidase activity (IDA, PMID:37327776) |

## Sources

- wiki: [Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)
- wiki: [Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)
- drive: [GP2term and extensions (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc)
- issue: [go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584)
- wiki: [Has input](https://wiki.geneontology.org/index.php/Has_input)
- wiki: [Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)
- issue: [go-annotation#2076](https://github.com/geneontology/go-annotation/issues/2076)

<!-- END GENERATED -->
