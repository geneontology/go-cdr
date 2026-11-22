---
id: QN-5
title: Do not make new `colocalizes_with` annotations. When reviewing one, convert it to `is_active_in`
  or `located_in` if the evidence supports that, or remove it.
status: proposed
topic: QN
provenance: GOC_PLUS
provenance_note: '[GOC+]. GO deprecated the relation but published no conversion procedure; the table
  is ours. [wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with); [Drive:
  Reviewing colocalizes_with annotations (2023)](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o);
  [wiki: 31 Aug 2021 PAINT Conference Call](https://wiki.geneontology.org/index.php/31_Aug_2021_PAINT_Conference_Call)
  (IBA for GO:0005635 nuclear envelope that had been withheld only because of a `colocalizes_with` mismatch).'
evidence_codes:
- IBA
go_terms:
- term_id: GO:0005635
  label: nuclear envelope
related:
- QN-7
differences:
- prior_source: '[wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with)'
  prior_said: Deprecated, "existing annotations are under review"; no procedure
  we_recommend: Conversion table; no new rows
  why: GO gave no procedure, and reviewers meet these rows now
sources:
- kind: wiki
  title: Colocalizes with
  url: https://wiki.geneontology.org/index.php/Colocalizes_with
- kind: web
  title: ORGANELLES
  url: https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html
- kind: drive
  title: Reviewing colocalizes_with annotations (2023)
  url: https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o
- kind: wiki
  title: 31 Aug 2021 PAINT Conference Call
  url: https://wiki.geneontology.org/index.php/31_Aug_2021_PAINT_Conference_Call
date: '2026-11-15'
---

# QN-5. Do not make new `colocalizes_with` annotations. When reviewing one, convert it to `is_active_in` or `located_in` if the evidence supports that, or remove it.

## Decision

Do not make new `colocalizes_with` annotations. When reviewing one, convert it to `is_active_in` or `located_in` if the evidence supports that, or remove it.

## Context

Curators have read `colocalizes_with` in at least three ways: transient localisation, low assay resolution, and echoing a paper's wording ("X colocalizes with Y"). GO has marked it deprecated ([wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with), last reviewed 2018). The repo schema's enum still describes it as "weaker than located_in", which is a reading GO no longer endorses.

**Conversion.**

| What the evidence shows | Convert to |
|---|---|
| The product acts there, even transiently | `is_active_in` (use an extension or GO-CAM for timing) |
| The product is a resident there, activity not shown | `located_in` |
| The product passes through on the way to its site of action | Remove (not a location claim) |
| The paper says "colocalizes with marker M" as a localisation method | Judge the localisation itself and apply the rows above |
| Resolution too low to place it at the term's granularity | `located_in` a coarser term the assay can resolve (a root organelle is acceptable; see [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)) |

**Review action.** If the term is kept with a different relation, MODIFY the row and add a relation-only NEW row ([QN-7](QN-7.md)). If the location does not hold, REMOVE it.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. GO deprecated the relation but published no conversion procedure; the table is ours. [wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with); [Drive: Reviewing colocalizes_with annotations (2023)](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o); [wiki: 31 Aug 2021 PAINT Conference Call](https://wiki.geneontology.org/index.php/31_Aug_2021_PAINT_Conference_Call) (IBA for GO:0005635 nuclear envelope that had been withheld only because of a `colocalizes_with` mismatch). |
| Date | 2026-11-15 |
| Related | [QN-7](QN-7.md) |
| Evidence codes | IBA |
| GO terms | `GO:0005635` nuclear envelope |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [QN-5-E1](QN-5.examples.yaml): A colocalizes_with cytosol row accepted as the core location of a cytosolic enzyme | Non-conformant | HPR2 colocalizes_with GO:0005829 cytosol (IDA, PMID:30233632) |
| [QN-5-E2](QN-5.examples.yaml): A term refinement that deliberately preserves colocalizes_with | Non-conformant | EML1 colocalizes_with GO:0015630 microtubule cytoskeleton (IDA, PMID:24859200) |
| [QN-9-E1](QN-9.examples.yaml): A NOT on dendrite accepted beside a positive dendritic spine row (from [QN-9](QN-9.md)) | Non-conformant | APP NOT colocalizes_with GO:0030425 dendrite (IDA, PMID:17251419) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with) | Deprecated, "existing annotations are under review"; no procedure | Conversion table; no new rows | GO gave no procedure, and reviewers meet these rows now |

## Sources

- wiki: [Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with)
- web: [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)
- drive: [Reviewing colocalizes_with annotations (2023)](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o)
- wiki: [31 Aug 2021 PAINT Conference Call](https://wiki.geneontology.org/index.php/31_Aug_2021_PAINT_Conference_Call)

<!-- END GENERATED -->
