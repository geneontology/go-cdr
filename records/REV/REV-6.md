---
id: REV-6
title: Catalytic rows on pseudoenzymes, substrates and accessory subunits
status: proposed
topic: REV
provenance: GOC_PLUS
provenance_note: '[GOC+]. The `contributes_to` convention and the ban on IPI for catalytic activity (GORULE:0000007,
  [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)) are GOC; the pseudoenzyme
  handling is ours ([CONTESTED_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/CONTESTED_FUNCTION.html),
  [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html),
  patterns 3 and 8).'
evidence_codes:
- IDA
- IPI
- TAS
- IEA
go_terms:
- term_id: GO:0016491
  label: oxidoreductase activity
- term_id: GO:0051213
  label: dioxygenase activity
- term_id: GO:0032454
  label: histone H3K9 demethylase activity
- term_id: GO:0006468
  label: protein phosphorylation
- term_id: GO:0003924
  label: GTPase activity
- term_id: GO:0004129
  label: cytochrome-c oxidase activity
related:
- REV-8
- REV-14
sources:
- kind: web
  title: CONTESTED_FUNCTION
  url: https://ai4curation.io/ai-gene-review/pages/projects/CONTESTED_FUNCTION.html
- kind: web
  title: TOP_NOTS
  url: https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html
- kind: issue
  title: go-annotation#2131
  url: https://github.com/geneontology/go-annotation/issues/2131
- kind: web
  title: OVER_ANNOTATION_PATTERNS
  url: https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html
date: '2026-11-15'
---

# REV-6. Catalytic rows on pseudoenzymes, substrates and accessory subunits

## Decision

Remove electronic catalytic rows when the protein lacks the catalytic machinery. Read
"is phosphorylated" and "stimulates the activity of" as the opposite of "has the activity".
Give a complex's catalytic activity only to the subunit that carries the active site.

## Context

Domain signatures predict activity from fold, and folds outlive catalysis. Three shapes recur:

- *Pseudoenzymes.* A JmjC, P450, thiolase or HKD fold whose active-site residues are gone.
  Fission yeast Epe1 carries IEA rows for `GO:0016491` oxidoreductase activity and
  `GO:0051213` dioxygenase activity from its JmjC domain; its iron-binding triad is
  non-canonical and no demethylation has been detected, so the electronic rows are `REMOVE`
  ([CONTESTED_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/CONTESTED_FUNCTION.html)). Its two PomBase experimental rows for
  `GO:0032454` histone H3K9 demethylase activity are `UNDECIDED`, not `REMOVE`, because they
  rest on in vivo genetics the reviewer cannot fully re-read ([REV-8](REV-8.md)).
- *Substrate read as enzyme.* Human CREB1 carries an IDA for `GO:0006468` protein
  phosphorylation; CREB1 is phosphorylated by kinases and is not one. RASA1 carries a TAS for
  `GO:0003924` GTPase activity; it stimulates Ras GTPase activity and has none itself
  ([TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html), Tier 1).
- *Accessory subunit given the complex's activity.* SURF1, a cytochrome oxidase assembly
  factor, carries an IEA for `GO:0004129` cytochrome-c oxidase activity. The activity
  belongs to the catalytic subunits; non-catalytic partners get `contributes_to` at most, and
  assembly factors get nothing ([protein-complexes.md](../PC/README.md)).

An experimental row of the substrate kind (CREB1) can be removed despite its code, because the
error is in the reading of the result, not in the result: the paper shows CREB1 phosphorylated,
which no one disputes. Say so in the reason, and quote the paper.

Where the absent activity is likely to be re-predicted, propose a NOT ([REV-14](REV-14.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The `contributes_to` convention and the ban on IPI for catalytic activity (GORULE:0000007, [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)) are GOC; the pseudoenzyme handling is ours ([CONTESTED_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/CONTESTED_FUNCTION.html), [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html), patterns 3 and 8). |
| Date | 2026-11-15 |
| Related | [REV-8](REV-8.md), [REV-14](REV-14.md) |
| Evidence codes | IDA, IPI, TAS, IEA |
| GO terms | `GO:0016491` oxidoreductase activity; `GO:0051213` dioxygenase activity; `GO:0032454` histone H3K9 demethylase activity; `GO:0006468` protein phosphorylation; `GO:0003924` GTPase activity; `GO:0004129` cytochrome-c oxidase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [REV-6-E1](REV-6.examples.yaml): Epe1 JmjC oxidoreductase IEA removed on its non-canonical iron site | Conformant | Epe1 enables GO:0016491 oxidoreductase activity (IEA, GO_REF:0000043) |
| [REV-6-E2](REV-6.examples.yaml): A protein phosphorylation IDA on CREB1 removed because CREB1 is the substrate | Conformant | CREB1 acts_upstream_of_or_within GO:0006468 protein phosphorylation (IDA, PMID:8798441) |
| [REV-6-E3](REV-6.examples.yaml): Cytochrome-c oxidase activity removed from the assembly factor SURF1 | Conformant | SURF1 enables GO:0004129 cytochrome-c oxidase activity (IEA, GO_REF:0000107) |
| [REV-8-E1](REV-8.examples.yaml): Epe1 H3K9 demethylase IDA left UNDECIDED rather than removed (from [REV-8](REV-8.md)) | Conformant | Epe1 enables GO:0032454 histone H3K9 demethylase activity (IDA, PMID:25838386) |
| [REV-17-E2](REV-17.examples.yaml): A GDSL esterase mapping on the pseudoenzyme MVP1 filed to InterPro, a MUTAGEN note to UniProt (from [REV-17](REV-17.md)) | Conformant | MVP1 enables GO:0016788 hydrolase activity, acting on ester bonds (IEA, GO_REF:0000002) |

## Sources

- web: [CONTESTED_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/CONTESTED_FUNCTION.html)
- web: [TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html)
- issue: [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)
- web: [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)

<!-- END GENERATED -->
