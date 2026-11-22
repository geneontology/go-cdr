---
id: IEA-9
title: Judge a rule by its condition sets, as conjunctions, against the experimental record
status: proposed
topic: IEA
provenance: GOC_PLUS
provenance_note: '[GOC+]. The receipts requirements are this repository''s ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md),
  "Reviewing rules").'
evidence_codes:
- IBA
sources:
- kind: repo
  title: 'docs: rule review receipts'
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/rule_review_receipts.md
- kind: drive
  title: ARBA notes for curators
  url: https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz
- kind: drive
  title: Rule-based systems in GOA, 2025
  url: https://drive.google.com/open?id=1_XLWtDWUzR0A-u8TTE3OoZa46XpHgICo
- kind: web
  title: ARBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/ARBA_REVIEW.html
- kind: issue
  title: go-annotation#6018
  url: https://github.com/geneontology/go-annotation/issues/6018
- kind: drive
  title: Including IBA in ARBA training
  url: https://drive.google.com/open?id=1eIC-6mENH1bQoHsjDuaXu52IlXm5PyCD
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# IEA-9. Judge a rule by its condition sets, as conjunctions, against the experimental record

## Decision

Review a UniRule or ARBA rule by reading every condition set it serves, each as the conjunction
of all its conditions including taxon. A rule is wrong only if it annotates a protein that lacks
the function, has an obsolete consequent, or has been withdrawn. Rule size, generality, redundancy
and low recall are not errors. Before calling a protein a false positive, check its experimental
annotations to the term and its descendants.

## Context

an audit of 78 ARBA rule reviews in November 2026 found about 45 verdicts unsupported by
their own evidence; the commonest errors were treating rule size as evidence (the "limit of 12
condition sets" is a default in an analysis tool), verdicts on conditions never recorded, judging
signatures one at a time, mislabelled InterPro ids, and "false positives" that were experimentally
annotated ([docs: rule review receipts](https://github.com/ai4curation/ai-gene-review/blob/main/docs/rule_review_receipts.md)). ARBA's "100%
confidence" means only that every Swiss-Prot entry matching the condition carried the annotation
in training: missing negative examples, excluded HAMAP/PROSITE-ProRule annotations and errors in
templates all pass through, and signatures carry no taxon constraint of their own, so they can
"leak" into lineages where the function does not exist
([Drive: ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz)).
UniRule and ARBA apply GO taxon constraints during validation and prefer precision over recall
([Drive: Rule-based systems in GOA, 2025](https://drive.google.com/open?id=1_XLWtDWUzR0A-u8TTE3OoZa46XpHgICo)).

## Application

Worked examples: ARBA00090718 assigns (S)-2-hydroxyglutarate dehydrogenase activity to SerA-family
proteins, which make the (R) enantiomer, so the *P. putida* serA row was removed and the rule review
proposes deprecation. ARBA00089174 assigns adaptive thermogenesis from PM20D1 FunFams across
Eukaryota; the fission-yeast cps1 row was removed and the rule review restricts it to mammals
([ARBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/ARBA_REVIEW.html); [go-annotation#6018](https://github.com/geneontology/go-annotation/issues/6018)).
Including IBA rows in ARBA training removed many high-level and do-not-annotate predictions as
well as over-annotations such as ARBA00084588, which added endocrine pancreas development to
proteins matching one FunFam in vertebrates
([Drive: Including IBA in ARBA training](https://drive.google.com/open?id=1eIC-6mENH1bQoHsjDuaXu52IlXm5PyCD)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The receipts requirements are this repository's ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), "Reviewing rules"). |
| Date | 2026-11-15 |
| Evidence codes | IBA |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-9-E1](IEA-9.examples.yaml): Fission-yeast Cps1 inherits adaptive thermogenesis from an older ARBA condition set | Non-conformant | SPAC24C9.08 involved_in GO:1990845 adaptive thermogenesis (IEA, GO_REF:0000117) |
| [IEA-9-E2](IEA-9.examples.yaml): An ARBA rule upheld by reading its single condition set as a conjunction | Conformant | ARBA |
| [IEA-4-E2](IEA-4.examples.yaml): A withdrawn ARBA rule whose only consequent is an obsolete term (from [IEA-4](IEA-4.md)) | Non-conformant | ARBA |

## Sources

- repo: [docs: rule review receipts](https://github.com/ai4curation/ai-gene-review/blob/main/docs/rule_review_receipts.md)
- drive: [ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz)
- drive: [Rule-based systems in GOA, 2025](https://drive.google.com/open?id=1_XLWtDWUzR0A-u8TTE3OoZa46XpHgICo)
- web: [ARBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/ARBA_REVIEW.html)
- issue: [go-annotation#6018](https://github.com/geneontology/go-annotation/issues/6018)
- drive: [Including IBA in ARBA training](https://drive.google.com/open?id=1eIC-6mENH1bQoHsjDuaXu52IlXm5PyCD)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
