---
id: IEA-12
title: 'Review actions: keep true general rows, remove wrong ones, never cite an IEA as evidence'
status: proposed
topic: IEA
provenance: GOC_PLUS
provenance_note: '[GOC] for retention; [GOC+] for the action mapping.'
evidence_codes:
- ISS
- IEA
go_terms:
- term_id: GO:0005829
  label: cytosol
- term_id: GO:0005737
  label: cytoplasm
- term_id: GO:1990904
  label: ribonucleoprotein complex
sources:
- kind: issue
  title: go-annotation#615
  url: https://github.com/geneontology/go-annotation/issues/615
- kind: issue
  title: go-annotation#1879
  url: https://github.com/geneontology/go-annotation/issues/1879
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: repo
  title: action consistency
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md
- kind: web
  title: TREEGRAFTER
  url: https://ai4curation.io/ai-gene-review/pages/projects/TREEGRAFTER.html
date: '2026-11-15'
---

# IEA-12. Review actions: keep true general rows, remove wrong ones, never cite an IEA as evidence

## Decision

A correct but general IEA is ACCEPT or KEEP_AS_NON_CORE (or MODIFY when the row's own evidence
supports a specific descendant), never REMOVE. REMOVE is for a demonstrably wrong mapping or rule
output, an over-propagation argued on biological grounds, a fallen premise, or a taxon violation.
Never quote an ARBA statement, an electronic `DR GO` line, a keyword or a protein name as support
for anything.

## Context

the GOA position since 2008 is that correct but uninformative electronic annotations are
retained, and redundancy filtering is a display problem ([go-annotation#615](https://github.com/geneontology/go-annotation/issues/615));
PomBase filters IEA, ISS and similar rows where non-HTP experimental support exists, and no group
filters experimental rows ([go-annotation#1879](https://github.com/geneontology/go-annotation/issues/1879)).
In this repository, rows sharing a term reinforce each other and must receive consistent actions;
REMOVE is never a deduplication tool ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md);
[action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)). ARBA-derived UniProt text,
submitter-imported text and electronic GO lines are unvetted predictions, and citing ARBA text for
an ARBA row is circular ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), "Quote UniProt for evidence"). The bar for
MODIFY is the row's own evidence: an InterPro2GO row from a generic GPCR signature supports only a
generic receptor term.

## Application

Worked example: TreeGrafter `GO:0005829` cytosol and `GO:0005737` cytoplasm rows on soluble
bacterial enzymes were first downgraded and, on re-review, moved to KEEP_AS_NON_CORE as true but
redundant ([TREEGRAFTER](https://ai4curation.io/ai-gene-review/pages/projects/TREEGRAFTER.html)). The keyword mapping to `GO:1990904` ribonucleoprotein complex, which a
curator found too broad to be useful, was kept by GOA because it is correct and informative for
genome-wide analyses in poorly annotated species ([go-annotation#615](https://github.com/geneontology/go-annotation/issues/615));
on a protein with no RNP association the same row would be wrong and removed.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for retention; [GOC+] for the action mapping. |
| Date | 2026-11-15 |
| Evidence codes | ISS, IEA |
| GO terms | `GO:0005829` cytosol; `GO:0005737` cytoplasm; `GO:1990904` ribonucleoprotein complex |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [IEA-12-E1](IEA-12.examples.yaml): TreeGrafter cytosol on a soluble bacterial polymerase kept as non-core | Conformant | dinB located_in GO:0005829 cytosol (IEA, GO_REF:0000118) |
| [IEA-12-E2](IEA-12.examples.yaml): A generic small-molecule binding parent kept after re-review | Conformant | ALB enables GO:0036094 small molecule binding (IEA, GO_REF:0000118) |

## Sources

- issue: [go-annotation#615](https://github.com/geneontology/go-annotation/issues/615)
- issue: [go-annotation#1879](https://github.com/geneontology/go-annotation/issues/1879)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- repo: [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)
- web: [TREEGRAFTER](https://ai4curation.io/ai-gene-review/pages/projects/TREEGRAFTER.html)

<!-- END GENERATED -->
