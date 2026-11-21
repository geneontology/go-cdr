---
id: BP-2
title: Name the entity that performs the step; substrates and products are not participants unless they
  do some of the work
status: proposed
topic: BP
provenance: GOC_PLUS
provenance_note: '[GOC+]. The convention is GOC practice, and #211 states it for transport. The general
  test and the three-way exception (scaffold, cofactor, chemistry) are ours, from [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md).'
aspects:
- P
go_terms:
- term_id: GO:0006508
  label: proteolysis
- term_id: GO:0002003
  label: angiotensin maturation
- term_id: GO:0016486
  label: peptide hormone processing
- term_id: GO:0030070
  label: insulin processing
- term_id: GO:0034205
  label: amyloid-beta formation
- term_id: GO:0006590
  label: thyroid hormone generation
- term_id: GO:0042730
  label: fibrinolysis
- term_id: GO:0006956
  label: complement activation
- term_id: GO:0016540
  label: protein autoprocessing
related:
- BP-3
differences:
- prior_source: '[CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), [go-annotation#211](https://github.com/geneontology/go-annotation/issues/211)'
  prior_said: Substrates are not participants (no GO wiki page states this generally).
  we_recommend: 'General rule with three exceptions: scaffold, cofactor, chemistry (BP-2).'
  why: Fills a documentation gap. GO's corpus already follows the convention, but no written guideline
    exists.
- prior_source: '[FUNGAL_PHENOTYPES](https://ai4curation.io/ai-gene-review/pages/projects/FUNGAL_PHENOTYPES.html)
    vs [wiki: HMP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_(HMP))'
  prior_said: HMP is equivalent to IMP and allowed when the screen phenotype correlates well with the
    process.
  we_recommend: HTP growth phenotypes may corroborate or question an existing row. They should not create
    a new process annotation without a mechanism (BP-2).
  why: The HMP criteria assess screen quality, not participation. Necessity data from a perfect screen
    are still necessity data.
sources:
- kind: issue
  title: go-annotation#211
  url: https://github.com/geneontology/go-annotation/issues/211
- kind: issue
  title: go-annotation#2425
  url: https://github.com/geneontology/go-annotation/issues/2425
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
- kind: web
  title: FUNGAL_PHENOTYPES
  url: https://ai4curation.io/ai-gene-review/pages/projects/FUNGAL_PHENOTYPES.html
date: '2026-11-15'
---

# BP-2. Name the entity that performs the step; substrates and products are not participants unless they do some of the work

## Decision

**Statement.** Before annotating, or accepting, a process term on a substrate, precursor, product or other consumed entity, ask which gene product performs the step. If the answer is a different gene product, the term belongs to that one. The exceptions are substrates that contribute to the process themselves: by supplying a scaffold, acting as a cofactor, or carrying out the chemistry.

## Context

In process terms under GO:0006508 proteolysis and similar transformation processes, the participant is the agent of the transformation. GO's annotation corpus follows this convention almost everywhere, even though no wiki page states it. [go-annotation#211](https://github.com/geneontology/go-annotation/issues/211) states it for a transport case: process terms go to the gene products that facilitate the process, not to the cargo. [go-annotation#2425](https://github.com/geneontology/go-annotation/issues/2425) notes that GAF generation from GO-CAM pushed target molecules into process annotations, and proposes removing them.

## Application

**Worked examples.**

- **Not a participant.** Human AGT (angiotensinogen) is not annotated to GO:0002003 angiotensin maturation. GO:0002003 `is_a` GO:0016486 peptide hormone processing (verified), and it is annotated to the proteases that cleave angiotensinogen: REN, ACE, ACE2 and others. The comparator check (BP-3) confirms the convention. INS is absent from GO:0030070 insulin processing, POMC is absent from GO:0016486, and APP is absent from GO:0034205 amyloid-beta formation ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md); review `genes/human/AGT`).
- **Participants by exception.** Thyroglobulin carries GO:0006590 thyroid hormone generation because it supplies the tyrosyl residues and positions the coupling pair: the scaffold case. Fibrin(ogen) carries GO:0042730 fibrinolysis because fibrin is the template that accelerates tPA-mediated plasminogen activation: the cofactor case. C3 carries GO:0006956 complement activation because its own thioester forms the covalent bond to the target: the chemistry case. Autoprocessing is the limiting case, where the substrate is the enzyme (GO:0016540 protein autoprocessing).
- **Necessity data.** High-throughput fungal growth screens show many mutants failing on alternative carbon or nitrogen sources. Respiratory assembly factors fail on glycerol because they are needed for respiration, not because they act on glycerol. Such data may corroborate an existing pathway annotation, or flag one for a second look. They must not create one ([FUNGAL_PHENOTYPES](https://ai4curation.io/ai-gene-review/pages/projects/FUNGAL_PHENOTYPES.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The convention is GOC practice, and #211 states it for transport. The general test and the three-way exception (scaffold, cofactor, chemistry) are ours, from [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md). |
| Date | 2026-11-15 |
| Related | [BP-3](BP-3.md) |
| GO terms | `GO:0006508` proteolysis; `GO:0002003` angiotensin maturation; `GO:0016486` peptide hormone processing; `GO:0030070` insulin processing; `GO:0034205` amyloid-beta formation; `GO:0006590` thyroid hormone generation; `GO:0042730` fibrinolysis; `GO:0006956` complement activation; `GO:0016540` protein autoprocessing |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), [go-annotation#211](https://github.com/geneontology/go-annotation/issues/211) | Substrates are not participants (no GO wiki page states this generally). | General rule with three exceptions: scaffold, cofactor, chemistry (BP-2). | Fills a documentation gap. GO's corpus already follows the convention, but no written guideline exists. |
| [FUNGAL_PHENOTYPES](https://ai4curation.io/ai-gene-review/pages/projects/FUNGAL_PHENOTYPES.html) vs [wiki: HMP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_(HMP)) | HMP is equivalent to IMP and allowed when the screen phenotype correlates well with the process. | HTP growth phenotypes may corroborate or question an existing row. They should not create a new process annotation without a mechanism (BP-2). | The HMP criteria assess screen quality, not participation. Necessity data from a perfect screen are still necessity data. |

## Sources

- issue: [go-annotation#211](https://github.com/geneontology/go-annotation/issues/211)
- issue: [go-annotation#2425](https://github.com/geneontology/go-annotation/issues/2425)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)
- web: [FUNGAL_PHENOTYPES](https://ai4curation.io/ai-gene-review/pages/projects/FUNGAL_PHENOTYPES.html)

<!-- END GENERATED -->
