---
id: REV
title: Reviewing existing annotations
record_kind: guideline
applies_to:
- contributing_group
status: proposed
differences:
- prior_source: '`ActionEnum` docstring for `TOO_GENERAL` (repo schema)'
  prior_said: Term true but entailed by a more specific asserted term
  we_recommend: Same, narrowed to terms imprecise on their own (membrane); a respectable term such as
    GPCR activity is kept
  why: Two reviews read the docstring in opposite ways; earlier reviews are not retroactively defective
    ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md))
- prior_source: '[wiki: QCQA call 2018-03-20](https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20)'
  prior_said: Need "a list of blacklisted papers and retractions"
  we_recommend: A periodic retraction scan with citation-site attribution, separating retraction, expression
    of concern and erratum
  why: A blacklist cannot tell a reference-list citation from an annotation's sole evidence ([RETRACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/RETRACTIONS.html))
open_questions:
- Should the GOC adopt a graded review vocabulary in its tools (at least separating "false" from "true
  but uninformative"), so that review outcomes can be fed back without collapsing to delete?
- 'GORULE:0000022: should annotations whose only evidence is a retracted paper be filtered, flagged, or
  left to the assigning group? We recommend flag-and-review.'
- How should a reviewer express "the term is right, but the evidence code understates species-specific
  experimental evidence"? This repository's tooling cannot record it as `NEW`, and the GAF has no upgrade
  mechanism.
- Should NOT annotations be proposed systematically for pseudoenzymes whose active-site loss is structurally
  established, even without a published negative assay?
- 'Display versus annotation for highly annotated genes: if the annotation set is correct but overwhelming,
  is the fix a better review or a better display? The 2024 sessions left this open.'
- Should IBA rows that duplicate a gene's own experimental annotation be shown to users, given that they
  are correct by construction?
date: '2026-11-15'
---

# Reviewing existing annotations: GO annotation guidelines


**In brief:**

- A review judges claims about the gene product, not evidence rows. Rows that share a term
  are one claim; their actions must agree, and `REMOVE` is never a way to deduplicate them.
- Pick the action by what it says about the claim: `REMOVE` means "probably false", `MODIFY`
  means "this row's own evidence supports a better term", `MARK_AS_OVER_ANNOTATED` means
  "goes beyond the evidence", `KEEP_AS_NON_CORE` means "true, precise, peripheral".
- Do not overrule an experimental annotation whose full text you have not read. Use
  `UNDECIDED`, and never infer "wrong gene" from a cached title or abstract.
- Necessity is not participation. Being required for a process, consumed by it, or measured
  by its assay does not make a gene product part of it.
- When the error lives upstream (wrong gene, wrong paper, wrong mapping, retracted source),
  record it as a structured source defect addressed to whoever can fix it.
- Every row's reasoning must be specific to that term and backed by a verbatim quote from an
  independent source; boilerplate and self-citation of the GOA file are not review.

## Scope


This document covers the audit of an existing body of GO annotations for one gene product:
the GOA/MOD rows, PAINT IBA rows, electronic rows and NOT rows that a curator inherits. It
says how to classify each row, how to keep the classification consistent, when to defer, and
how to record problems that need fixing at the source. It also covers consortium review
tickets (obsoletion-driven and rule-driven reviews in the `go-annotation` tracker) and the GO
rules (gorules) that run on every load.

It does not repeat the term-choice rules for each aspect; those live in
[molecular-function.md](../MF/README.md), [biological-process.md](../BP/README.md),
[cellular-component.md](../CC/README.md) and the other sibling documents. Ontology
change (obsoletion, merges, term requests, taxon constraints) is in
[ontology-change-and-taxa.md](../ONT/README.md). How to read a phylogenetic
inference before challenging it is in [phylogenetic-propagation.md](../PH/README.md),
and pipeline-specific failure modes are in [electronic-annotation.md](../IEA/README.md).

The action vocabulary used throughout (`ACCEPT`, `KEEP_AS_NON_CORE`, `MODIFY`,
`MARK_AS_OVER_ANNOTATED`, `TOO_GENERAL`, `REMOVE`, `UNDECIDED`, `NEW`) is the
`ActionEnum` of this repository's review schema. A GOC curator working in Noctua or
Protein2GO has fewer verbs (keep, edit, delete, add NOT), but the distinctions below still
decide which of those to do.

## Principles


**GO is a model of current knowledge, not an archive.** The GOC's own best-practice page
says curators should not hesitate to remove older annotations that conflict with what is now
known ([wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).
A review is the place where that happens deliberately, one claim at a time.

**Evidence codes are not quality scores.** The consortium said so explicitly in 2007 and
removed the code hierarchy ([Drive: evCode-summary (archived)](https://drive.google.com/open?id=1qZm_e_wnfu_yUAg7qbwrJpYwyRRNqD_7)).
An IEA can be right and an IDA can be wrong. A review weighs what each row asserts and what
supports it, then reaches one verdict per claim.

**The reviewer sees less than the curator did.** Experimental annotations were made from full
text; a reviewer often has only an abstract. Humility about what you cannot see is a rule,
not a courtesy ([REV-8](REV-8.md)).

**Errors propagate, so fix them at the source.** A wrong seed annotation or mapping is copied
by PAINT, Ensembl Compara, InterPro2GO and ARBA. The 2018 QC call argued that error fixing
should be treated like fixing software bugs, because one fix can clear many species at once
([wiki: QCQA call 2018-03-20](https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20)).
A review that only cleans its own file leaves the cause in place.

**A review must be auditable.** Another curator should be able to read one row's reason and
quote and reach, or dispute, the same verdict.

## Records

<!-- BEGIN GENERATED RECORD INDEX -->

| Id | Record | Status | Provenance |
|---|---|---|---|
| [REV-1](REV-1.md) | Judge the claim, not the row; rows sharing a term get consistent actions | proposed | [GOC+] |
| [REV-2](REV-2.md) | Choose the action by what it says about the claim | proposed | [NEW] |
| [REV-3](REV-3.md) | A correct but general term is `MODIFY` only when this row's evidence supports the specific term | proposed | [NEW] |
| [REV-4](REV-4.md) | Separate core from peripheral before deciding anything else | proposed | [GOC+] |
| [REV-5](REV-5.md) | The conclusion, not the assay; the direct role, not its downstream effects | proposed | [GOC] |
| [REV-6](REV-6.md) | Catalytic rows on pseudoenzymes, substrates and accessory subunits | proposed | [GOC+] |
| [REV-7](REV-7.md) | Measured activity is not automatically function | proposed | [GOC+] |
| [REV-8](REV-8.md) | Do not overrule an experimental curator from evidence you have not seen | proposed | [NEW] |
| [REV-9](REV-9.md) | Challenge an electronic or phylogenetic row by arguing with its source | proposed | [GOC+] |
| [REV-10](REV-10.md) | Necessity is not participation | proposed | [NEW] |
| [REV-11](REV-11.md) | `NEW` is the one action that manufactures a claim; hold it to a higher bar | proposed | [GOC+] |
| [REV-12](REV-12.md) | An ND row is a statement about the literature | proposed | [GOC+] |
| [REV-13](REV-13.md) | Remove bare protein binding; look for the informative function behind it | proposed | [GOC+] |
| [REV-14](REV-14.md) | A NOT must exclude the function; propose NOTs where errors will recur | proposed | [GOC+] |
| [REV-15](REV-15.md) | A retraction is a source failure; scope the response to the evidence line | proposed | [GOC+] |
| [REV-16](REV-16.md) | A miscitation is a defect in the citation, not in the biology; key it on the citation | proposed | [NEW] |
| [REV-17](REV-17.md) | Record upstream errors as structured source defects, addressed to whoever can fix them | proposed | [GOC+] |
| [REV-18](REV-18.md) | Every row needs term-specific reasoning and independent, verbatim support | proposed | [NEW] |
| [REV-19](REV-19.md) | Know what the gorules already enforce, and do not mistake passing them for review | proposed | [GOC] |
| [REV-20](REV-20.md) | An obsoletion-driven review ticket is a review of claims, not a find-and-replace | proposed | [GOC] |

<!-- END GENERATED RECORD INDEX -->

## Decision aid


Work through these in order for each row; stop at the first that applies.

| Question | If yes |
|---|---|
| Is the term bare `GO:0005515`? | `REMOVE` under the policy; propose an informative MF if evidence allows ([REV-13](REV-13.md)) |
| Is it an ND on a root term? | Apply [REV-12](REV-12.md): `ACCEPT` with search cited, or stale |
| Is it a NOT? | Keep only if the result excludes the function ([REV-14](REV-14.md)) |
| Is the gene the substrate, cargo, target or a non-catalytic subunit? | `REMOVE` or `MARK_AS_OVER_ANNOTATED` ([REV-6](REV-6.md), [REV-10](REV-10.md)) |
| Experimental row, and you lack the full text or the abstract is about another gene? | `UNDECIDED` or defer-`ACCEPT`; never "wrong gene" ([REV-8](REV-8.md)) |
| Is the claim contradicted by better evidence? | `REMOVE`; propose NOT if pipelines will re-predict it |
| Electronic/IBA row outside the clade or signature scope where it holds? | `REMOVE`; record the source defect at the node or mapping ([REV-9](REV-9.md), [REV-17](REV-17.md)) |
| Does the term name an assay readout or a downstream effect? | `MARK_AS_OVER_ANNOTATED` ([REV-5](REV-5.md)) |
| Assayed activity of doubtful physiological relevance? | Tiers in [REV-7](REV-7.md) |
| True, but this row's evidence supports a specific descendant? | `MODIFY` with that descendant ([REV-3](REV-3.md)) |
| True, imprecise on its own, and a specific asserted term entails it? | `TOO_GENERAL` |
| True, as precise as warranted, and part of the core? | `ACCEPT` |
| True, as precise as warranted, peripheral? | `KEEP_AS_NON_CORE` |
| Is the reference retracted or miscited? | Act on the citation first ([REV-15](REV-15.md), [REV-16](REV-16.md)), then judge the claim on the remaining evidence |

Then check the set: same-term rows consistent, no positive term kept beside a NOT on it or an
ancestor, every `MODIFY` replacement supported by that row's evidence, core functions matching
the `ACCEPT` rows.

## Common errors


| Error | Example | Fix |
|---|---|---|
| `REMOVE` used to deduplicate | IEA removed beside an accepted IDA on the same term | Same action family on all rows ([REV-1](REV-1.md)) |
| `REMOVE` on a true but broad term | `GO:0016787` hydrolase activity removed beside a specific phospholipase term | `MODIFY` if the row's evidence supports the child; otherwise keep ([REV-3](REV-3.md)) |
| Action contradicts reason | `ACCEPT` with a reason saying the term is too general | Change the action to match the argument |
| Overruling the curator from a title | IDA called a paralog mix-up because the cached abstract names the paralog | `UNDECIDED` ([REV-8](REV-8.md)) |
| Substrate given the enzyme's process | angiotensinogen proposed for angiotensin maturation | Name who performs the step ([REV-10](REV-10.md)) |
| "Is phosphorylated" read as kinase activity | CREB1 protein phosphorylation IDA | `REMOVE`, quote the paper ([REV-6](REV-6.md)) |
| Assembly factor given the complex activity | SURF1 cytochrome-c oxidase activity | `REMOVE`; consider NOT |
| Retraction triggers wholesale removal | every row on a gene removed after one notice | Scope to the evidence line ([REV-15](REV-15.md)) |
| Mapping defect filed against GOA | IPR mapping scope filed as `GOA_EBI` with no `record` | `INTERPRO`, name the mapping ([REV-17](REV-17.md)) |
| Boilerplate reasoning | same reason and placeholder quote on 200 rows | Re-review row by row ([REV-18](REV-18.md)) |
| Citing the GOA file as support | `supported_by` pointing at `GENE-goa.tsv` | Quote the paper or record behind the row |
| Stale ND removed because an IBA exists | ND on MF removed "as an IBA now covers MF" | `ACCEPT`; IBA is not literature on the gene ([REV-12](REV-12.md)) |
| Uninformative tissue CC on a shuttling factor | cytoplasm rows on an inactive cytoplasmic pool | `MARK_AS_OVER_ANNOTATED` ([REV-4](REV-4.md)) |

## Reading list


**GO wiki**

- [wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) (reviewed 2025-11)
- [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) (flagged for review)
- [wiki: GO Central (GOC) QC Procedure](https://wiki.geneontology.org/index.php/GO_Central_%28GOC%29_QC_Procedure)
- [wiki: Annotation Conf. Call 2024-03-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12) (do-not-annotate subsets)
- [wiki: Annotation Conf. Call 2023-12-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-12-12) (retractions)
- [wiki: Ontology meeting 2023-12-11](https://wiki.geneontology.org/index.php/Ontology_meeting_2023-12-11) (GORULE:0000022 on hold)
- [wiki: QCQA call 2018-03-20](https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20)
- [wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)

**GO Consortium Drive**

- [Drive: GOC 2023-10 / GO rules update](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI)
- [Drive: GOC 2024-05 / GO rules](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)
- [Drive: GOC 2023-04 / Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)
- [Drive: GOC Fall 2024 / Highly annotated genes, C. elegans daf-16](https://drive.google.com/open?id=1YhRirPCkc9Pl0gOC3Mhc5Zn0VK8SGHEOO-BeI6pwAGk)
- [Drive: GOC Fall 2024 / Highly annotated genes, MTOR](https://drive.google.com/open?id=1Ha8AyFN9WndsT6UPPUnMYawzdn-dnqCG)
- [Drive: IEA WG 2025-10 / Mechanisms for decreasing erroneous & overkill of annotations](https://drive.google.com/open?id=10xAYIWTCFyN2bzxBnijErWf9CTsuX5N4jBI7GVLB9KM) (suggestions, not adopted rules)
- [Drive: old GOC minutes / evCode-summary](https://drive.google.com/open?id=1qZm_e_wnfu_yUAg7qbwrJpYwyRRNqD_7) (archived, 2007)

**GitHub issues and files (geneontology/go-annotation)**

- [go-annotation#1324](https://github.com/geneontology/go-annotation/issues/1324) (assay-artefact activity)
- [go-annotation#1519](https://github.com/geneontology/go-annotation/issues/1519) (non-physiological EC mappings)
- [go-annotation#1940](https://github.com/geneontology/go-annotation/issues/1940) (`colocalizes_with` on complexes)
- [go-annotation#2097](https://github.com/geneontology/go-annotation/issues/2097) (no PAINT protein binding)
- [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131) (GORULE:0000007)
- [go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584) (`occurs_at` review)
- [go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)
- [go-annotation issue template: annotation review for obsoletion](https://github.com/geneontology/go-annotation/blob/master/.github/ISSUE_TEMPLATE/annotation-review-for-obsoletion.md)

**Repository pages**

- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) (review guidelines, curator deference, NEW bar, ND, IBA, references)
- [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)
- [source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)
- [reference curation](https://github.com/ai4curation/ai-gene-review/blob/main/docs/reference_curation.md)
- [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)
- [REVIEW_QUALITY_AUDIT](https://ai4curation.io/ai-gene-review/pages/projects/REVIEW_QUALITY_AUDIT.html)
- [RETRACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/RETRACTIONS.html)
- [MISCITATION_AUDIT](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATION_AUDIT.html)
- [CONTESTED_FUNCTION](https://ai4curation.io/ai-gene-review/pages/projects/CONTESTED_FUNCTION.html)
- [TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html)
- [RAR_MISANNOTATION](https://ai4curation.io/ai-gene-review/pages/projects/RAR_MISANNOTATION.html)
- [TAXON_PATHWAY_VARIANCE](https://ai4curation.io/ai-gene-review/pages/projects/TAXON_PATHWAY_VARIANCE.html)
- [ORGANELLES](https://ai4curation.io/ai-gene-review/pages/projects/ORGANELLES.html)

GO term ids and labels were checked against the local `sqlite:obo:go` build (2026-11-03); the
subclass claim for `GO:0002003` under `GO:0016486` was checked with `runoak ancestors`.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| `ActionEnum` docstring for `TOO_GENERAL` (repo schema) | Term true but entailed by a more specific asserted term | Same, narrowed to terms imprecise on their own (membrane); a respectable term such as GPCR activity is kept | Two reviews read the docstring in opposite ways; earlier reviews are not retroactively defective ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)) |
| [wiki: QCQA call 2018-03-20](https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20) | Need "a list of blacklisted papers and retractions" | A periodic retraction scan with citation-site attribution, separating retraction, expression of concern and erratum | A blacklist cannot tell a reference-list citation from an annotation's sole evidence ([RETRACTIONS](https://ai4curation.io/ai-gene-review/pages/projects/RETRACTIONS.html)) |

## Open questions

1. Should the GOC adopt a graded review vocabulary in its tools (at least separating "false" from "true but uninformative"), so that review outcomes can be fed back without collapsing to delete?
2. GORULE:0000022: should annotations whose only evidence is a retracted paper be filtered, flagged, or left to the assigning group? We recommend flag-and-review.
3. How should a reviewer express "the term is right, but the evidence code understates species-specific experimental evidence"? This repository's tooling cannot record it as `NEW`, and the GAF has no upgrade mechanism.
4. Should NOT annotations be proposed systematically for pseudoenzymes whose active-site loss is structurally established, even without a published negative assay?
5. Display versus annotation for highly annotated genes: if the annotation set is correct but overwhelming, is the fix a better review or a better display? The 2024 sessions left this open.
6. Should IBA rows that duplicate a gene's own experimental annotation be shown to users, given that they are correct by construction?

<!-- END GENERATED -->
