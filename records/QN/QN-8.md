---
id: QN-8
title: Make a NOT annotation only when an experiment tested for the property and found it absent, or when
  the key residues for it are lost (IKR), and only when a reader would otherwise expect the property.
status: proposed
topic: QN
provenance: NEW
provenance_note: '[GOC] for the core rule; [NEW] for the explicit IEP exclusion. [wiki: Elements of an
  annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation); [go-annotation#3](https://github.com/geneontology/go-annotation/issues/3);
  [go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237); [NOT_ANNOTATION_USAGE](https://ai4curation.io/ai-gene-review/pages/projects/NOT_ANNOTATION_USAGE.html).'
evidence_codes:
- IMP
- IEP
- IKR
go_terms:
- term_id: GO:0000719
  label: photoreactive repair
- term_id: GO:0004672
  label: protein kinase activity
- term_id: GO:1903412
  label: response to bile acid
open_questions:
- '**Proposing NOT in a review.** The repo has no structured way to propose a new NOT annotation, since
  `NEW` adds positive claims. Should the schema allow `NEW` with `negated: true` under the [QN-8](QN-8.md)
  bar, or should NOT proposals stay in TOP_NOTS?'
sources:
- kind: issue
  title: go-annotation#2237
  url: https://github.com/geneontology/go-annotation/issues/2237
- kind: wiki
  title: Elements of an annotation
  url: https://wiki.geneontology.org/index.php/Elements_of_an_annotation
- kind: web
  title: NOT_ANNOTATION_USAGE
  url: https://ai4curation.io/ai-gene-review/pages/projects/NOT_ANNOTATION_USAGE.html
- kind: issue
  title: go-annotation#3
  url: https://github.com/geneontology/go-annotation/issues/3
date: '2026-11-15'
---

# QN-8. Make a NOT annotation only when an experiment tested for the property and found it absent, or when the key residues for it are lost (IKR), and only when a reader would otherwise expect the property.

## Decision

Make a NOT annotation only when an experiment tested for the property and found it absent, or when the key residues for it are lost (IKR), and only when a reader would otherwise expect the property.

## Context

The NOT qualifier is for absence that has been shown. Negative and inconclusive results do not show absence. The problem has been on record since go-annotation issue #3 (2003): a curator annotated NOT Golgi-to-vacuole transport because a mutant showed no missorting of one cargo, which means "not required for this assay", not "not involved". The documentation contradicted itself for another fifteen years. It suggested NOT for "our favorite protein is not found in the nucleus" until that example was removed in 2019 ([go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237)). The current wiki states the rule plainly ([wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation), reviewed 2026-03).

**Supports a NOT:**

- An activity assay on adequate protein that detects no activity where the family predicts one, ideally with a positive control. Example: CRY2 NOT GO:0000719 photoreactive repair, where a photolyase homologue lacks repair activity ([NOT_ANNOTATION_USAGE](https://ai4curation.io/ai-gene-review/pages/projects/NOT_ANNOTATION_USAGE.html)). Another: COQ8B NOT GO:0004672 protein kinase activity, because the family "lacks canonical protein kinase activity in trans" (PMID:27499294, cited in `genes/human/COQ8B`).
- Loss of catalytic residues established phylogenetically, using IKR (ECO:0000320 phylogenetic determination of loss of key residues evidence used in manual assertion). An IKR row must be a NOT (gorule-0000042).
- An antimicrobial-killing assay negative for one class of target, for a peptide active against another class. These are close to activity negatives.

**Does not support a NOT:**

- "Not required for" a process (knockout has no phenotype): redundancy and assay sensitivity are the usual explanations.
- "Not detected in" a location in a localisation experiment that found the protein elsewhere ([wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)).
- Expression unchanged after a stimulus: IEP evidence never supports a NOT. The repo audit found 169 IEP-only NOT rows in GOA, 82% of them "NOT response to..." terms ([NOT_ANNOTATION_USAGE](https://ai4curation.io/ai-gene-review/pages/projects/NOT_ANNOTATION_USAGE.html)).
- An abundance result. FGFR4 NOT GO:1903412 response to bile acid (IMP, PMID:19085950) rests only on bile acid not changing FGFR4 protein level. The repo review REMOVEs it.
- Absence that nobody expected. A NOT that rules out a property no reader would have assumed adds nothing.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] [GOC] for the core rule; [NEW] for the explicit IEP exclusion. [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation); [go-annotation#3](https://github.com/geneontology/go-annotation/issues/3); [go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237); [NOT_ANNOTATION_USAGE](https://ai4curation.io/ai-gene-review/pages/projects/NOT_ANNOTATION_USAGE.html). |
| Date | 2026-11-15 |
| Evidence codes | IMP, IEP, IKR |
| GO terms | `GO:0000719` photoreactive repair; `GO:0004672` protein kinase activity; `GO:1903412` response to bile acid |

## Open questions

1. **Proposing NOT in a review.** The repo has no structured way to propose a new NOT annotation, since `NEW` adds positive claims. Should the schema allow `NEW` with `negated: true` under the [QN-8](QN-8.md) bar, or should NOT proposals stay in TOP_NOTS?

## Sources

- issue: [go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237)
- wiki: [Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)
- web: [NOT_ANNOTATION_USAGE](https://ai4curation.io/ai-gene-review/pages/projects/NOT_ANNOTATION_USAGE.html)
- issue: [go-annotation#3](https://github.com/geneontology/go-annotation/issues/3)

<!-- END GENERATED -->
