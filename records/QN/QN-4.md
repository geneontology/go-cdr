---
id: QN-4
title: Use `is_active_in` only when the evidence places the activity, not just the protein, in the location.
  Otherwise use `located_in`.
status: proposed
topic: QN
provenance: GOC_PLUS
provenance_note: '[GOC+]. [wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in);
  [wiki: Located in](https://wiki.geneontology.org/index.php/Located_in); [Drive: Reviewing colocalizes_with
  annotations (2023)](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o).'
go_terms:
- term_id: GO:0012505
  label: endomembrane system
- term_id: GO:0005829
  label: cytosol
- term_id: GO:0005635
  label: nuclear envelope
sources:
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
- kind: repo
  title: action consistency
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md
- kind: wiki
  title: Is active in
  url: https://wiki.geneontology.org/index.php/Is_active_in
- kind: wiki
  title: Located in
  url: https://wiki.geneontology.org/index.php/Located_in
- kind: drive
  title: Reviewing colocalizes_with annotations (2023)
  url: https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o
date: '2026-11-15'
---

# QN-4. Use `is_active_in` only when the evidence places the activity, not just the protein, in the location. Otherwise use `located_in`.

## Decision

Use `is_active_in` only when the evidence places the activity, not just the protein, in the location. Otherwise use `located_in`.

## Context

`is_active_in` is defined by the property chain `enables o occurs_in`. It is the stronger claim and the one GO-CAM needs. A GFP fusion or a proteomics hit supports `located_in`. An activity assay on a purified compartment, or a function that only makes sense on one side of a membrane (a matrix enzyme whose substrate exists only in the matrix), supports `is_active_in`.

**Rule detail.** A protein seen in transit (secretory proteins in the ER, receptors passing through the endomembrane system) is not active there. Do not use `is_active_in` for transit compartments, and use `located_in` for them only when the repo's organelle rules allow it ([ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html), rule 7: "transit is not residence"). The 2023 Padua breakout drew the same line for `colocalizes_with` rows on GO:0012505 endomembrane system: receptors trafficked through the endomembrane system and not active there should not have that localisation captured.

**Entailment** (as used by the repo's [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md) checks): `is_active_in` X entails `located_in` X, and `part_of` complex entails `located_in` the complex's location. `located_in` entails neither.

## Application

**Example.** CED-3 `is_active_in` GO:0005829 cytosol, because the caspase acts there ([wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in)). If a protein is also seen at GO:0005635 nuclear envelope by immunofluorescence and no activity is shown there, that row is `located_in` at most.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. [wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in); [wiki: Located in](https://wiki.geneontology.org/index.php/Located_in); [Drive: Reviewing colocalizes_with annotations (2023)](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o). |
| Date | 2026-11-15 |
| GO terms | `GO:0012505` endomembrane system; `GO:0005829` cytosol; `GO:0005635` nuclear envelope |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [QN-4-E1](QN-4.examples.yaml): A lipid-synthesizing enzyme is active in the membrane its substrate lives in | Conformant | cdsA is_active_in GO:0005886 plasma membrane (IBA, GO_REF:0000033) |
| [QN-4-E2](QN-4.examples.yaml): An ortholog-transferred is_active_in kept although the review says it overstates the evidence | Non-conformant | vms1 is_active_in GO:0005789 endoplasmic reticulum membrane (ISO, GO_REF:0000024) |
| [QN-5-E1](QN-5.examples.yaml): A colocalizes_with cytosol row accepted as the core location of a cytosolic enzyme (from [QN-5](QN-5.md)) | Non-conformant | HPR2 colocalizes_with GO:0005829 cytosol (IDA, PMID:30233632) |
| [QN-7-E3](QN-7.examples.yaml): A wrong is_active_in relation handled by marking the term over-annotated (from [QN-7](QN-7.md)) | Non-conformant | rho-1 is_active_in GO:0005829 cytosol (IBA, GO_REF:0000033) |

## Sources

- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)
- repo: [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)
- wiki: [Is active in](https://wiki.geneontology.org/index.php/Is_active_in)
- wiki: [Located in](https://wiki.geneontology.org/index.php/Located_in)
- drive: [Reviewing colocalizes_with annotations (2023)](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o)

<!-- END GENERATED -->
