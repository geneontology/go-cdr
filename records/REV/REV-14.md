---
id: REV-14
title: A NOT must exclude the function; propose NOTs where errors will recur
status: proposed
topic: REV
provenance: GOC_PLUS
provenance_note: '[GOC+]. The IEA working group lists NOT-aware logic blocks as a desirable pipeline mechanism
  ([Drive: Mechanisms for decreasing erroneous & overkill of annotations](https://drive.google.com/open?id=10xAYIWTCFyN2bzxBnijErWf9CTsuX5N4jBI7GVLB9KM));
  the exclusion test is ours.'
evidence_codes:
- IEA
go_terms:
- term_id: GO:0005929
  label: cilium
differences:
- prior_source: '[TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html) and GOC
    practice'
  prior_said: NOT annotations are made from published negative results
  we_recommend: 'Also review existing NOTs: a failure to detect is not exclusion, and 11 of 295 NOTs here
    were overturned'
  why: A weak NOT blocks correct positive annotations ([REV-14](REV-14.md))
sources:
- kind: web
  title: TOP_NOTS
  url: https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html
- kind: drive
  title: Taxon Constraints for Signaling Pathways
  url: https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg
- kind: drive
  title: Mechanisms for decreasing erroneous & overkill of annotations
  url: https://drive.google.com/open?id=10xAYIWTCFyN2bzxBnijErWf9CTsuX5N4jBI7GVLB9KM
date: '2026-11-15'
---

# REV-14. A NOT must exclude the function; propose NOTs where errors will recur

## Decision

Keep an existing NOT only when its negative result rules the function out, not when it
merely failed to detect it. Where a review removes a pipeline-predicted activity the protein
demonstrably lacks, consider proposing a NOT, since only a NOT stops the prediction from
returning.

## Application

*Example.* ARL3 carried `NOT|located_in` `GO:0005929` cilium from an overexpression screen of
tagged GTPases in serum-starved cells. That showed tagged ARL3 is not enriched in cilia under
one condition; ARL3-GTP is made inside the cilium by its ciliary GEF, and endogenous ARL3
stains cilia. The NOT was removed ([TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html), NOT_NOTs section).

`REMOVE` on a NOT row doubts the negative claim without asserting the positive one, so removing
both a term and its NOT is consistent. `TOO_GENERAL` is never used on a NOT: a NOT on a broad
term is the strongest negative claim. GO taxon constraints do not apply to NOT annotations
([Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)).
The NOT candidates from pseudoenzymes and "is phosphorylated" misreadings (DnaJ proteins and
ATP binding, UEV domains and E2 activity) are listed in [TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html); none has
yet been verified and submitted. See [qualifiers-and-negation.md](../QN/README.md).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The IEA working group lists NOT-aware logic blocks as a desirable pipeline mechanism ([Drive: Mechanisms for decreasing erroneous & overkill of annotations](https://drive.google.com/open?id=10xAYIWTCFyN2bzxBnijErWf9CTsuX5N4jBI7GVLB9KM)); the exclusion test is ours. |
| Date | 2026-11-15 |
| Evidence codes | IEA |
| GO terms | `GO:0005929` cilium |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [REV-14-E1](REV-14.examples.yaml): ARL3 NOT cilium removed because the negative result does not exclude | Conformant | ARL3 NOT located_in GO:0005929 cilium (IDA, PMID:17646400) |
| [REV-14-E2](REV-14.examples.yaml): A NOT galactokinase row on GLCAK1 kept: galactose tested, below 0.1% of GlcA | Conformant | GLCAK1 NOT enables GO:0004335 galactokinase activity (IDA, PMID:19951951) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html) and GOC practice | NOT annotations are made from published negative results | Also review existing NOTs: a failure to detect is not exclusion, and 11 of 295 NOTs here were overturned | A weak NOT blocks correct positive annotations ([REV-14](REV-14.md)) |

## Sources

- web: [TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html)
- drive: [Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)
- drive: [Mechanisms for decreasing erroneous & overkill of annotations](https://drive.google.com/open?id=10xAYIWTCFyN2bzxBnijErWf9CTsuX5N4jBI7GVLB9KM)

<!-- END GENERATED -->
