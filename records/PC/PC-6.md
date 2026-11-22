---
id: PC-6
title: Use `contributes_to` only when no single subunit has the activity and the activity is that of an
  irreducible molecular machine, and give it only to the subunits whose part is in the mechanism.
status: proposed
topic: PC
provenance: GOC
aspects:
- C
- F
go_terms:
- term_id: GO:0003878
  label: ATP citrate synthase activity
- term_id: GO:0008177
  label: succinate dehydrogenase (quinone) activity
- term_id: GO:0046933
  label: proton-transporting ATP synthase activity, rotational mechanism
- term_id: GO:0046961
  label: proton-transporting ATPase activity, rotational mechanism
- term_id: GO:0003899
  label: DNA-directed RNA polymerase activity
- term_id: GO:0001671
  label: ATPase activator activity
- term_id: GO:0001055
  obsolete: true
related:
- PC-7
sources:
- kind: wiki
  title: Annotation Relations
  url: https://wiki.geneontology.org/index.php/Annotation_Relations
- kind: wiki
  title: Contributes to
  url: https://wiki.geneontology.org/index.php/Contributes_to
- kind: issue
  title: go-annotation#6414
  url: https://github.com/geneontology/go-annotation/issues/6414
- kind: issue
  title: go-annotation#3616
  url: https://github.com/geneontology/go-annotation/issues/3616
- kind: issue
  title: go-annotation#3865
  url: https://github.com/geneontology/go-annotation/issues/3865
- kind: web
  title: SDH_GP2TERM_CONTRIBUTES_TO
  url: https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html
date: '2026-11-15'
---

# PC-6. Use `contributes_to` only when no single subunit has the activity and the activity is that of an irreducible molecular machine, and give it only to the subunits whose part is in the mechanism.

## Decision

Use `contributes_to` only when no single subunit has the activity and the activity is that of an irreducible molecular machine, and give it only to the subunits whose part is in the mechanism.

## Context

GO's definition: `contributes_to` links a gene product to an MF executed by a complex "in which
the Molecular Function cannot be ascribed to an individual subunit of that complex. Only the
complex subunits required for the Molecular Function are annotated"
([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)).
Being part of a complex is not sufficient
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). The cases:

| Case | Example | Who gets `contributes_to` |
|---|---|---|
| Composite active site built from residues of several subunits | ATP citrate lyase of *Chlorobaculum tepidum* (`GO:0003878`); ABC half-transporter heterodimers; thiocyanate hydrolase | every subunit contributing residues |
| Compound activity of the whole complex, a multi-step reaction no subunit performs | succinate dehydrogenase (quinone) activity `GO:0008177` for SDHA, SDHB, SDHC, SDHD ([go-annotation#6414](https://github.com/geneontology/go-annotation/issues/6414)) | each subunit in the reaction path |
| Coupled molecular machine | `GO:0046933` proton-transporting ATP synthase activity, rotational mechanism; `GO:0046961` proton-transporting ATPase activity, rotational mechanism for V-ATPase ([go-annotation#3616](https://github.com/geneontology/go-annotation/issues/3616)) | catalytic, rotor, stator and channel subunits (see PC-7 for others) |
| Polymerase catalytic core | nuclear RNA polymerases: the core subunits contribute to `GO:0003899` DNA-directed RNA polymerase activity; subunits outside the core do not | core only |
| Cofactor-dependent composite ATPase | torsins and their activators ([go-annotation#3865](https://github.com/geneontology/go-annotation/issues/3865)) | the ATPase may take `contributes_to`; the activator takes `GO:0001671` ATPase activator activity |

Ask the checklist question for each subunit separately. If the answer to "can the activity
occur without this subunit?" is yes, it does not contribute.

## Application

*Example.* SDHB, SDHC and SDHD reviews in the repo carry a structured `qualifier:
contributes_to` row on `GO:0008177`. Where GOA still ships `enables`, the review marks the GOA
row `MODIFY` and adds a paired `NEW` `contributes_to` row, the pattern the validator accepts
until GOA catches up ([SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html)).

A wiki example gives `contributes_to` on `GO:0001055` RNA polymerase II activity; that term is
now obsolete, so the example should be read with `GO:0003899`.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Related | [PC-7](PC-7.md) |
| GO terms | `GO:0003878` ATP citrate synthase activity; `GO:0008177` succinate dehydrogenase (quinone) activity; `GO:0046933` proton-transporting ATP synthase activity, rotational mechanism; `GO:0046961` proton-transporting ATPase activity, rotational mechanism; `GO:0003899` DNA-directed RNA polymerase activity; `GO:0001671` ATPase activator activity; `GO:0001055`  (obsolete) |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [PC-6-E1](PC-6.examples.yaml): SDHB given enables on the whole-complex succinate:quinone reaction | Non-conformant | SDHB enables GO:0008177 succinate dehydrogenase (quinone) activity (IMP, PMID:26925370) |
| [PC-6-E2](PC-6.examples.yaml): The catalytic A subunit of V-ATPase contributes to the rotary activity | Conformant | TFP1 contributes_to GO:0046961 proton-transporting ATPase activity, rotational mechanism (IBA, GO_REF:0000033) |

## Sources

- wiki: [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- wiki: [Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)
- issue: [go-annotation#6414](https://github.com/geneontology/go-annotation/issues/6414)
- issue: [go-annotation#3616](https://github.com/geneontology/go-annotation/issues/3616)
- issue: [go-annotation#3865](https://github.com/geneontology/go-annotation/issues/3865)
- web: [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html)

<!-- END GENERATED -->
