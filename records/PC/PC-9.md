---
id: PC-9
title: When the active subunit of a complex is not known, give no subunit the complex's MF; use CC membership
  and BP.
status: proposed
topic: PC
provenance: GOC
aspects:
- C
- F
go_terms:
- term_id: GO:0005515
  label: protein binding
sources:
- kind: wiki
  title: Contributes to
  url: https://wiki.geneontology.org/index.php/Contributes_to
- kind: drive
  title: GOC 2025-05 GO-CAM guidelines
  url: https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# PC-9. When the active subunit of a complex is not known, give no subunit the complex's MF; use CC membership and BP.

## Decision

When the active subunit of a complex is not known, give no subunit the complex's MF; use CC membership and BP.

## Context

"If a gene product is part of a complex and it is unknown which subunit is responsible for the
activity of the complex, do not annotate with a term from the Molecular Function branch"
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). In GO-CAM the
complex term is then the enabler with no parts listed, and no subunit MF is exported
([Drive: GOC 2025-05 GO-CAM guidelines](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE)).
Do not fill the gap with `GO:0005515` protein binding; the repo's protein-binding policy
removes bare protein binding as uninformative
([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md); `src/ai_gene_review/validation/protein_binding_policy.py`).
If the gap is a genuine biological unknown, record a `knowledge_gaps` entry with a
`suggested_experiments` partner.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0005515` protein binding |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [PC-9-E1](PC-9.examples.yaml): An archaeal AmoA row refined to the complex activity although the active subunit is unknown | Non-conformant | amoA enables GO:0004497 monooxygenase activity (IEA, GO_REF:0000043) |

## Sources

- wiki: [Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)
- drive: [GOC 2025-05 GO-CAM guidelines](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
