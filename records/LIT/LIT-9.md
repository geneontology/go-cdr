---
id: LIT-9
title: Read what the paper reports as negative; never annotate a negative control or a failed assay as
  a positive.
status: proposed
topic: LIT
provenance: GOC_PLUS
provenance_note: '[GOC+]. GO documentation does not address negative controls; the rule comes from [MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html).'
evidence_codes:
- EXP
- IDA
go_terms:
- term_id: GO:0006068
  label: ethanol catabolic process
- term_id: GO:0003841
  label: 1-acylglycerol-3-phosphate O-acyltransferase activity
related:
- LIT-13
sources:
- kind: web
  title: miscitation project
  url: https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html
- kind: paper
  title: PMID:23207770
  url: https://europepmc.org/article/MED/23207770
- kind: paper
  title: PMID:21878620
  url: https://europepmc.org/article/MED/21878620
- kind: repo
  title: source defects
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md
date: '2026-11-15'
---

# LIT-9. Read what the paper reports as negative; never annotate a negative control or a failed assay as a positive.

## Decision

Read what the paper reports as negative; never annotate a negative control or a failed assay as a positive.

## Context

Two seed cases in the [miscitation project](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html) are positive
annotations from negative results:

- **SULT1B1**, `GO:0006068` ethanol catabolic process (IDA), from
  [PMID:23207770](https://europepmc.org/article/MED/23207770). The abstract names
  four ethanol-sulfating enzymes among eleven tested; SULT1B1 is one of the eleven
  and not one of the four. The cache is abstract-only, so the review marks the row
  over-annotated rather than removing it ([LIT-13](LIT-13.md)).
- **PNPLA3**, `GO:0003841` 1-acylglycerol-3-phosphate O-acyltransferase activity
  (EXP), from [PMID:21878620](https://europepmc.org/article/MED/21878620), which
  found no transfer to lysophosphatidic acid with a positive control in place. The
  quote passes the verbatim check; the row asserts the reverse of the result. With a
  NOT qualifier the citation would be impeccable.

A clear negative from a direct assay supports a NOT annotation
([qualifiers-and-negation.md](../QN/README.md)); record the error in an
existing positive row as a `MISSING_NEGATION` source defect
([source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)). When one paper finds an
activity and another does not (PMID:22560221 against PMID:21878620 for PNPLA3),
the claim is contested; grade the pair `DISPUTED` and keep both visible.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. GO documentation does not address negative controls; the rule comes from [MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html). |
| Date | 2026-11-15 |
| Related | [LIT-13](LIT-13.md) |
| Evidence codes | EXP, IDA |
| GO terms | `GO:0006068` ethanol catabolic process; `GO:0003841` 1-acylglycerol-3-phosphate O-acyltransferase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [LIT-9-E1](LIT-9.examples.yaml): Ethanol catabolism for a sulfotransferase the paper did not find active | Non-conformant | SULT1B1 involved_in GO:0006068 ethanol catabolic process (IDA, PMID:23207770) |
| [LIT-9-E2](LIT-9.examples.yaml): A positive acyltransferase row citing the paper that found no activity | Non-conformant | PNPLA3 enables GO:0003841 1-acylglycerol-3-phosphate O-acyltransferase activity (EXP, PMID:21878620) |

## Sources

- web: [miscitation project](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html)
- paper: [PMID:23207770](https://europepmc.org/article/MED/23207770)
- paper: [PMID:21878620](https://europepmc.org/article/MED/21878620)
- repo: [source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)

<!-- END GENERATED -->
