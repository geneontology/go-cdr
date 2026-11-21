---
id: EV-6
title: Use IEP only for biological process terms, only from normal expression, and only when the gene
  product's job is the response itself.
status: proposed
topic: EV
provenance: GOC_PLUS
provenance_note: '[GOC] for the BP and normal-expression restrictions ([wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29),
  GORULE:0000006); [GOC+] for the agency test ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html);
  [go-annotation#2025](https://github.com/geneontology/go-annotation/issues/2025)).'
evidence_codes:
- IDA
- IMP
- IEP
go_terms:
- term_id: GO:0009408
  label: response to heat
- term_id: GO:0009410
  label: response to xenobiotic stimulus
- term_id: GO:0007507
  label: heart development
- term_id: GO:0030855
  label: epithelial cell differentiation
sources:
- kind: paper
  title: GO best-practices paper
  url: https://europepmc.org/article/MED/23842463
- kind: web
  title: IEP project
  url: https://ai4curation.io/ai-gene-review/pages/projects/IEP.html
- kind: paper
  title: PMID:21492153
  url: https://europepmc.org/article/MED/21492153
- kind: wiki
  title: IEP
  url: https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29
- kind: issue
  title: go-annotation#2025
  url: https://github.com/geneontology/go-annotation/issues/2025
date: '2026-11-15'
---

# EV-6. Use IEP only for biological process terms, only from normal expression, and only when the gene product's job is the response itself.

## Decision

Use IEP only for biological process terms, only from normal expression, and only when the gene product's job is the response itself.

## Context

IEP (ECO:0000270) infers involvement in a process from the timing or place of the
gene's own expression. GORULE:0000006 restricts it to BP. Overexpression and
ectopic expression are never IEP; they are IDA or IMP. The wiki asks for high-level
terms and warns "Use this code with caution!"; the [GO best-practices paper](https://europepmc.org/article/MED/23842463)
says "response to" terms are for products "required for the response to occur."

The [IEP project](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html) found that reviewers accepted only 22.5% of IEP
rows and kept 55.6% as non-core. The characteristic row is true but peripheral.
We therefore make the agency test explicit: *does the gene product exist for this
process, or is its abundance modulated by it?*

- **Annotate (core is fine):** effectors whose deployment is the response:
  heat-shock chaperones to `GO:0009408` response to heat (worm/hsp-16.2,
  ECOLI/DnaK); infection-induced immune effectors; clock components whose
  oscillating expression is the mechanism.
- **Annotate as non-core, or not at all:** constitutive enzymes induced by many
  insults. rat/Gstt1 collected four `response to X` terms from four induction
  papers for one glutathione transferase; the informative row is
  `GO:0009410` response to xenobiotic stimulus once, not the catalogue.
- **Do not annotate:** developmental time-courses read as tissue-building roles
  (rat/Ckmt2 rising after birth does not make creatine kinase part of
  `GO:0007507` heart development); regulon membership (ECOLI/arnF is induced by
  iron through BasS-BasR but does not handle iron); a signalling hub annotated as
  a responder to each stimulus it drives (ARATH/PIF3); one differential screen
  yielding one term for N genes ([PMID:21492153](https://europepmc.org/article/MED/21492153)
  gave eight unrelated genes `GO:0030855` epithelial cell differentiation).

When reviewing, keep the induction observation and judge the term: the usual
action is KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED, with REMOVE reserved for a
process of a different functional class. The wiki's own example of primate
IRF2BPL annotated to "development of secondary female sexual characteristics" from
pubertal induction would fail our agency test unless the activation data the wiki
mentions are annotated in their own right.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] [GOC] for the BP and normal-expression restrictions ([wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29), GORULE:0000006); [GOC+] for the agency test ([IEP](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html); [go-annotation#2025](https://github.com/geneontology/go-annotation/issues/2025)). |
| Date | 2026-11-15 |
| Evidence codes | IDA, IMP, IEP |
| GO terms | `GO:0009408` response to heat; `GO:0009410` response to xenobiotic stimulus; `GO:0007507` heart development; `GO:0030855` epithelial cell differentiation |

## Sources

- paper: [GO best-practices paper](https://europepmc.org/article/MED/23842463)
- web: [IEP project](https://ai4curation.io/ai-gene-review/pages/projects/IEP.html)
- paper: [PMID:21492153](https://europepmc.org/article/MED/21492153)
- wiki: [IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29)
- issue: [go-annotation#2025](https://github.com/geneontology/go-annotation/issues/2025)

<!-- END GENERATED -->
