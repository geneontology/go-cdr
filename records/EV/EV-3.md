---
id: EV-3
title: Use IPI only with the partner's identifier in WITH/FROM, and only for binding, complex or interaction-dependent
  terms; never for catalytic activity.
status: proposed
topic: EV
provenance: NEW
provenance_note: '[GOC] for the WITH/FROM and catalytic rules ([wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29),
  [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)); [NEW] for the restriction
  on non-binding terms.'
evidence_codes:
- IDA
- IPI
- IMP
go_terms:
- term_id: GO:0003824
  label: catalytic activity
- term_id: GO:0044877
  label: protein-containing complex binding
- term_id: GO:0019901
  label: protein kinase binding
- term_id: GO:0045296
  label: cadherin binding
- term_id: GO:0004860
  label: protein kinase inhibitor activity
- term_id: GO:0030674
  label: protein-macromolecule adaptor activity
- term_id: GO:0005515
  label: protein binding
differences:
- prior_source: '[wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29)'
  prior_said: IPI may support any MF except catalytic, or any BP, because the partner is involved
  we_recommend: IPI supports binding, complex and (with an activity assay) regulator/adaptor terms; BP
    only alongside evidence placing the product's own activity in the process (EV-3)
  why: Interaction with a process component shows association, not participation
open_questions:
- Should IPI to non-binding terms be formally restricted (EV-3), and should GORULE:0000007's catalytic
  ban extend to transporter activity, where binding is equally uninformative about transport?
sources:
- kind: issue
  title: go-annotation#2349
  url: https://github.com/geneontology/go-annotation/issues/2349
- kind: issue
  title: go-annotation#2131
  url: https://github.com/geneontology/go-annotation/issues/2131
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: paper
  title: PMID:19590578
  url: https://europepmc.org/article/MED/19590578
- kind: web
  title: MISCITATIONS
  url: https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html
- kind: repo
  title: source defects
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md
- kind: wiki
  title: IPI
  url: https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29
date: '2026-11-15'
---

# EV-3. Use IPI only with the partner's identifier in WITH/FROM, and only for binding, complex or interaction-dependent terms; never for catalytic activity.

## Decision

Use IPI only with the partner's identifier in WITH/FROM, and only for binding, complex or interaction-dependent terms; never for catalytic activity.

## Context

IPI (ECO:0000353) is a direct assay in which the partner is known and has a stable
identifier (gene, protein, RNA, ComplexPortal complex). The identifier is
mandatory (GORULE:0000018). Independent partners are separated by pipes; partners
required simultaneously by commas
([go-annotation#2349](https://github.com/geneontology/go-annotation/issues/2349)).
IPI must not support `GO:0003824` catalytic activity or any is_a descendant
(GORULE:0000007). Enzyme regulator terms are outside that ban; the scope was
narrowed deliberately in [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131).
A complex co-precipitated through a tagged or antibody-targeted subunit may be
recorded as IPI with that subunit in WITH/FROM for a `GO:0044877`
protein-containing complex binding term.

**Our sharpening: when IPI may support a non-binding term.** The wiki allows IPI
for any MF (except catalytic) or BP when the gene product "interacts with another
entity that was shown experimentally to be involved in that process." That is
guilt by association, and it reproduces the necessity-versus-participation error
the repository warns against ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), "Do not add what
curators deliberately declined to add"). We restrict it. IPI may support:

1. a specific binding term naming the partner class (`GO:0019901` protein kinase
   binding, `GO:0045296` cadherin binding);
2. a complex term, when the interaction is the evidence of membership;
3. a regulator or adaptor MF (`GO:0004860` protein kinase inhibitor activity,
   `GO:0030674` protein-macromolecule adaptor activity) only when the same paper
   also shows the binding changes the partner's activity or bridges two named
   partners (record that assay too, usually as IDA);
4. a BP term only as part of a set: the interaction plus an IMP or IDA in the same
   paper that places the gene product's own activity in the process.

A co-immunoprecipitation with a process component, alone, supports at most the
specific binding term.

## Application

*Examples.* ZBP1 has an IPI row from [PMID:19590578](https://europepmc.org/article/MED/19590578)
whose WITH/FROM is UniProtKB:Q13601 (KRR1, a ribosome biogenesis factor); the
partner in the paper is RIPK1 (Q13546). GRID1 has two IPI rows with
UniProtKB:P68871, haemoglobin beta, a classic affinity-purification contaminant
([MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html)). In both, the reference is sound and the
WITH/FROM is wrong. Record such rows as source defects (`defect_type: WRONG_WITH_FROM`, see
[source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)), not as reference problems.

Bare `GO:0005515` protein binding from IPI is uninformative. The repository policy
removes it, or modifies it to a specific term the paper supports
(`src/ai_gene_review/validation/protein_binding_policy.py`). The wiki's
requirement for a reciprocal protein-binding row on the partner predates that
policy and should not drive new curation.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] [GOC] for the WITH/FROM and catalytic rules ([wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29), [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)); [NEW] for the restriction on non-binding terms. |
| Date | 2026-11-15 |
| Evidence codes | IDA, IPI, IMP |
| GO terms | `GO:0003824` catalytic activity; `GO:0044877` protein-containing complex binding; `GO:0019901` protein kinase binding; `GO:0045296` cadherin binding; `GO:0004860` protein kinase inhibitor activity; `GO:0030674` protein-macromolecule adaptor activity; `GO:0005515` protein binding |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) | IPI may support any MF except catalytic, or any BP, because the partner is involved | IPI supports binding, complex and (with an activity assay) regulator/adaptor terms; BP only alongside evidence placing the product's own activity in the process (EV-3) | Interaction with a process component shows association, not participation |

## Open questions

1. Should IPI to non-binding terms be formally restricted (EV-3), and should GORULE:0000007's catalytic ban extend to transporter activity, where binding is equally uninformative about transport?

## Sources

- issue: [go-annotation#2349](https://github.com/geneontology/go-annotation/issues/2349)
- issue: [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- paper: [PMID:19590578](https://europepmc.org/article/MED/19590578)
- web: [MISCITATIONS](https://ai4curation.io/ai-gene-review/pages/projects/MISCITATIONS.html)
- repo: [source defects](https://github.com/ai4curation/ai-gene-review/blob/main/docs/source_defects.md)
- wiki: [IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29)

<!-- END GENERATED -->
