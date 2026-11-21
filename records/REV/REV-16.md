---
id: REV-16
title: A miscitation is a defect in the citation, not in the biology; key it on the citation
status: proposed
topic: REV
provenance: NEW
provenance_note: '[NEW]. The GOC''s ticket guidelines ask for specifics and PMIDs in correction requests
  ([go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md));
  the citation-keyed register is ours.'
evidence_codes:
- IDA
differences:
- prior_source: '[MISCITATION_AUDIT](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATION_AUDIT.html)
    (internal) vs GOC ticket practice'
  prior_said: GOC tickets correct one row at a time
  we_recommend: Key citation defects on the citation, and check every gene that cites it
  why: One bad PMID is usually copied across paralogs and partners ([REV-16](REV-16.md))
sources:
- kind: web
  title: MISCITATION_AUDIT
  url: https://ai4curation.io/ai-gene-review/pages/projects/MISCITATION_AUDIT.html
- kind: repo
  title: reference curation
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/reference_curation.md
- kind: repo
  title: go-annotation CONTRIBUTING
  url: https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md
date: '2026-11-15'
---

# REV-16. A miscitation is a defect in the citation, not in the biology; key it on the citation

## Decision

When an annotation's reference resolves to a different paper (`WRONG_IDENTIFIER`) or the
right paper does not say what it is cited for (`MISCITED`), keep GOA's
`original_reference_id`, record the finding in `reference_review`, judge the claim on whatever
real evidence exists, and check where else the same citation is used.

## Context

Validators check that a title matches its PMID and that a quote occurs in the paper. A wrong
PMID imported together with its own title passes both. Bad citations are rarely confined to one
gene: they are copied across paralogs and complex partners. Seven of the twenty distinct
`WRONG_IDENTIFIER` citations in this repository's register affect more than one gene, and 26 of
27 such rows came from GOA rather than from reviews here ([MISCITATION_AUDIT](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATION_AUDIT.html)).

Failure modes seen: an off-by-one symbol (a `protein farnesylation` IDA on COX17 citing a COX10
paper; the term is wrong even for COX10, which farnesylates heme), paralog substitution
(ELOVL1, ELOVL2 and ELOVL3 citing a paper that cloned "HELO1", i.e. ELOVL5), symbol collision
(ADPRH citing a paper whose "ARH1" is a different gene), and wholly unrelated papers. Spread is
a triage queue, not a verdict: the ELOVL5 paper is correctly cited on ELOVL5.

For a deleted duplicate PMID, record the verified canonical identifier in
`reference_review.replacement` and quote the canonical paper under its own id. A fetch failure
alone establishes neither replacement nor retraction ([reference curation](https://github.com/ai4curation/ai-gene-review/blob/main/docs/reference_curation.md)).
When P2 contradicts a finding in P1, record it on P1's finding (`finding_review`, `DISPUTED` or
`OVERTURNED`) rather than condemning the whole paper.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW]. The GOC's ticket guidelines ask for specifics and PMIDs in correction requests ([go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)); the citation-keyed register is ours. |
| Date | 2026-11-15 |
| Evidence codes | IDA |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [MISCITATION_AUDIT](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATION_AUDIT.html) (internal) vs GOC ticket practice | GOC tickets correct one row at a time | Key citation defects on the citation, and check every gene that cites it | One bad PMID is usually copied across paralogs and partners ([REV-16](REV-16.md)) |

## Sources

- web: [MISCITATION_AUDIT](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATION_AUDIT.html)
- repo: [reference curation](https://github.com/ai4curation/ai-gene-review/blob/main/docs/reference_curation.md)
- repo: [go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)

<!-- END GENERATED -->
