---
id: REV-2
title: Choose the action by what it says about the claim
status: proposed
topic: REV
provenance: NEW
provenance_note: '[NEW]. The GOC''s curation tools offer keep, edit, delete and NOT; the graded vocabulary
  is this repository''s ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).'
go_terms:
- term_id: GO:0016020
  label: membrane
differences:
- prior_source: GOC curation tools (Noctua, Protein2GO)
  prior_said: Keep, edit, delete, or add NOT
  we_recommend: A graded vocabulary that separates false, over-reaching, broad, peripheral and undecidable
  why: '"Delete" conflates distinct judgements; the distinction matters for upstream feedback ([REV-2](REV-2.md))'
sources:
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# REV-2. Choose the action by what it says about the claim

## Decision

Each action is a distinct statement. Use the one whose statement you can defend, and make
the `reason` argue that statement and no other.

## Context

| Action | What it asserts | Typical evidence |
|---|---|---|
| `ACCEPT` | True, and part of the gene's core function | Direct evidence, coherent with the whole picture |
| `KEEP_AS_NON_CORE` | True and as precise as warranted, but peripheral | Developmental or pleiotropic roles, real secondary activities |
| `MODIFY` | The idea is right; this row's own evidence supports a better term | A paper that names the ligand; a sign error (`positive` vs `negative regulation`) |
| `MARK_AS_OVER_ANNOTATED` | Not false, but beyond what the evidence supports | An in vitro activity of unknown relevance; a phenotype read as a process |
| `TOO_GENERAL` | True but uninformative, because a specific asserted term entails it | `GO:0016020` membrane beside an accepted specific membrane term |
| `REMOVE` | Unlikely to be true | Contradicted function; demonstrably wrong mapping; over-propagation |
| `UNDECIDED` | Cannot judge with the evidence available | Inaccessible full text; genuinely conflicting data |

Two failure modes recur. The first is an action that contradicts its own reason: `ACCEPT` or
`KEEP_AS_NON_CORE` on a row whose reason argues the term is too general. The second is using
`REMOVE` for "I prefer another row" or "true but vague". Neither is a judgement about truth.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW]. The GOC's curation tools offer keep, edit, delete and NOT; the graded vocabulary is this repository's ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)). |
| Date | 2026-11-15 |
| GO terms | `GO:0016020` membrane |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [REV-2-E1](REV-2.examples.yaml): ATP binding kept as non-core, with the reason saying why it is not TOO_GENERAL | Conformant | LPXK enables GO:0005524 ATP binding (IEA, GO_REF:0000002) |
| [REV-2-E2](REV-2.examples.yaml): A membrane row kept as non-core while the reason calls it uninformative | Non-conformant | LYM2 located_in GO:0016020 membrane (TAS, PMID:12068095) |
| [REV-4-E2](REV-4.examples.yaml): DAF-16 cytoplasm rows accepted although the cytoplasmic pool is the inactive one (from [REV-4](REV-4.md)) | Non-conformant | daf-16 located_in GO:0005737 cytoplasm (IEA, GO_REF:0000044) |
| [REV-5-E3](REV-5.examples.yaml): Wound healing from a scratch assay kept as non-core on FGF1 (from [REV-5](REV-5.md)) | Non-conformant | FGF1 involved_in GO:0042060 wound healing (IDA, PMID:16756958) |
| [RS-2-E3](../RS/RS-2.examples.yaml): Positive regulation of cell division kept on the kinetochore subunit SPC24 (from [RS-2](../RS/RS-2.md)) | Non-conformant | SPC24 acts_upstream_of_or_within GO:0051781 positive regulation of cell division (IMP, PMID:29356153) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| GOC curation tools (Noctua, Protein2GO) | Keep, edit, delete, or add NOT | A graded vocabulary that separates false, over-reaching, broad, peripheral and undecidable | "Delete" conflates distinct judgements; the distinction matters for upstream feedback ([REV-2](REV-2.md)) |

## Sources

- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
