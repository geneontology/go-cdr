---
id: REV-17
title: Record upstream errors as structured source defects, addressed to whoever can fix them
status: proposed
topic: REV
provenance: GOC_PLUS
provenance_note: '[GOC+]. The GOC routes UniProt keyword and HAMAP issues to UniProt and GOA issues to
  GOA ([go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)),
  and asks curators to file tickets against other groups'' errors ([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).
  The structured record is ours.'
evidence_codes:
- IBA
- IBD
sources:
- kind: repo
  title: source defects
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md
- kind: repo
  title: go-annotation CONTRIBUTING
  url: https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md
- kind: wiki
  title: Tips
  url: https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations
date: '2026-11-15'
---

# REV-17. Record upstream errors as structured source defects, addressed to whoever can fix them

## Decision

When the error is in the source record, add a `source_defects` entry that names the defect
type, the responsible resource, the asserted and corrected values, a confidence and a
self-contained explanation. The review action says what this repository does; the defect says
what the source should do.

## Context

The resource is the group that can make the fix, which is usually not GOA:

| The fix changes... | Resource |
|---|---|
| a curated GAF row | the `assigned_by` group (MGI, TAIR, SGD, UniProt...) |
| the content of an InterPro2GO mapping or a signature description | `INTERPRO`, naming the mapping in `record` |
| GOA's application of a correct mapping (a 51-residue fragment that got the row) | `GOA_EBI` |
| a term on a PANTHER node propagated by TreeGrafter | `PANTHER` |
| a PAINT IBD/IBA assertion | `GO_CENTRAL` |
| a term's label, definition or placement | `GOC` |
| a GO-CAM activity | `GO_CAM`, with the activity id in `record` |

## Application

*Example.* A GO-CAM gave an H4K5 acetyltransferase activity `enabled_by` SCL27, a GRAS
protein that shares the alias HAM1 with the MYST acetyltransferase HAM1; the cited papers study
the MYST protein. The defect is `WRONG_GENE_PRODUCT`, `slot: enabled_by`, `REPOINT` from
AT2G45160 to AT5G64610, `cause: SYMBOL_COLLISION`, `confidence: CONFIRMED`
([source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)).

Typed causes make patterns countable: `OVER_PROPAGATION` (fix the node, not the inherited
rows), `SCOPE_OVER_REACH` (a mapping applied across a taxon boundary), `LABEL_WITHOUT_DEFINITION`,
`SPECULATION_AS_ASSERTION` ("may function as" became an assertion), and `PRACTICE_CHANGE` (a
dated cohort sharing one convention, fixable in bulk). The mapping-versus-row distinction has
been reopened repeatedly in practice; check the filing whenever the fix is a mapping, whatever
the row's `assigned_by` says.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The GOC routes UniProt keyword and HAMAP issues to UniProt and GOA issues to GOA ([go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)), and asks curators to file tickets against other groups' errors ([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)). The structured record is ours. |
| Date | 2026-11-15 |
| Evidence codes | IBA, IBD |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [REV-17-E1](REV-17.examples.yaml): SCL27 enabling an H4K5 acetyltransferase activity in a GO-CAM, repointed to HAM1 | Conformant | gomodel:67e5e74400000148 |
| [REV-17-E2](REV-17.examples.yaml): A GDSL esterase mapping on the pseudoenzyme MVP1 filed to InterPro, a MUTAGEN note to UniProt | Conformant | MVP1 enables GO:0016788 hydrolase activity, acting on ester bonds (IEA, GO_REF:0000002) |
| [REV-17-E3](REV-17.examples.yaml): An InterPro2GO qualifier defect on V-ATPase subunit A filed to UniProt | Non-conformant | vma-1 enables GO:0046961 proton-transporting ATPase activity, rotational mechanism (IEA, GO_REF:0000002) |
| [REV-16-E3](REV-16.examples.yaml): A true Pld4 exonuclease row removed because its paper did not show the activity (from [REV-16](REV-16.md)) | Non-conformant | Pld4 enables GO:0045145 single-stranded DNA 5'-3' DNA exonuclease activity (IMP, PMID:22102906) |
| [RS-5-E3](../RS/RS-5.examples.yaml): An InterPro-derived positive regulation of transcription on SVP flipped to negative (from [RS-5](../RS/RS-5.md)) | Non-conformant | SVP involved_in GO:0045944 positive regulation of transcription by RNA polymerase II (IEA, GO_REF:0000002) |

## Sources

- repo: [source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)
- repo: [go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)
- wiki: [Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)

<!-- END GENERATED -->
