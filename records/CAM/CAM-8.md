---
id: CAM-8
title: Use a "directly" relation only between successive activities of different gene products, where
  the upstream activity acts on the downstream enabler; route small-molecule effects through the molecule.
status: proposed
topic: CAM
provenance: GOC_PLUS
go_terms:
- term_id: GO:0098772
  label: molecular function regulator activity
- term_id: GO:0004708
  label: MAP kinase kinase activity
- term_id: GO:0004707
  label: MAP kinase activity
- term_id: GO:0061501
  label: 2',3'-cyclic GMP-AMP synthase activity
differences:
- prior_source: '[wiki: Directly positively regulates](https://wiki.geneontology.org/index.php/Directly_positively_regulates)
    (2023) vs [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)'
  prior_said: The relation page allows a direct edge when the upstream activity makes or degrades a small-molecule
    regulator. The 2020 call fixed "directly" as direct physical interaction, with a reasoner rule that
    infers binding.
  we_recommend: Route small-molecule effects through the molecule (`has output`, `is small molecule activator/inhibitor
    of`); no direct protein-to-protein edge (CAM-8).
  why: The two sources conflict; a direct edge under the reasoner rule asserts a binding that did not
    happen.
sources:
- kind: wiki
  title: Directly positively regulates (reviewed 2023)
  url: https://wiki.geneontology.org/index.php/Directly_positively_regulates
- kind: wiki
  title: Annotation Conf. Call 2020-02-04
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04
- kind: drive
  title: Regulation Notes, 2020 GO-CAM Jamboree
  url: https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40
- kind: issue
  title: go-annotation#1979
  url: https://github.com/geneontology/go-annotation/issues/1979
- kind: repo
  title: gocam-curation causal-relations reference
  url: https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/causal-relations.md
date: '2026-11-15'
---

# CAM-8. Use a "directly" relation only between successive activities of different gene products, where the upstream activity acts on the downstream enabler; route small-molecule effects through the molecule.

## Decision

Use a "directly" relation only between successive activities of different gene products, where the upstream activity acts on the downstream enabler; route small-molecule effects through the molecule.

## Context

A direct regulation edge requires all of the following:

1. No activity intervenes between the two.
2. The upstream activity acts on the enabler of the downstream activity
   (phosphorylation, cleavage, binding that changes its state), so the
   downstream gene product is the upstream activity's `has input`.
3. The two activities have different enablers.
4. The mechanism is known. A knockdown phenotype, an epistasis result or a
   co-immunoprecipitation does not establish it.

If an enzyme regulates another activity by making or destroying a small
molecule, do not draw a direct edge between the two proteins. Write the
enzyme's `has output` ChEBI term and link that molecule to the downstream
activity with `is small molecule activator of` or `is small molecule inhibitor
of`. If the molecule is not in ChEBI, use `indirectly positively/negatively
regulates`.

A compound function within one gene product (ligand binding that switches on a
kinase domain) is one node with the compound MF term, not two nodes joined by a
direct edge.

*Rationale.* In GO, "directly" means direct physical interaction, and the
reasoner uses that meaning: an MF that directly regulates another MF is
inferred to be a `GO:0098772` molecular function regulator activity, and the
pair is inferred to bind. A direct edge from cGAS to STING would therefore
assert that the two proteins bind, which is not the mechanism (the enzyme makes
a second messenger). The February 2020 annotation call restricted direct
relations to activities of different gene products for the same reason. The
2023 relation page allows "directly" for small-molecule effects, which
conflicts with the reasoner rule; routing the effect through the molecule
satisfies both.

## Application

*Example.* In the EGF-MAPK example on the relation's wiki page, each MAP
kinase kinase activity (`GO:0004708`) directly positively regulates the MAP
kinase activity (`GO:0004707`) of its substrate. (The page cites model
`6348a65d00001727`; the cached model with that id is now a REG3A
inflammation model, so cite models by content as well as id.) For cGAS, `GO:0061501` 2',3'-cyclic GMP-AMP
synthase activity `has output` cGAMP, and cGAMP is the small-molecule activator
of STING's activity.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| GO terms | `GO:0098772` molecular function regulator activity; `GO:0004708` MAP kinase kinase activity; `GO:0004707` MAP kinase activity; `GO:0061501` 2',3'-cyclic GMP-AMP synthase activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [CAM-8-E1](CAM-8.examples.yaml): A MAPKK directly activating its cognate p38 MAPK | Conformant | gomodel:568b0f9600000284 |
| [CAM-8-E2](CAM-8.examples.yaml): Protein kinase D drawn as directly activating p38 with the mechanism unknown | Non-conformant | gomodel:568b0f9600000284 |
| [CAM-8-E3](CAM-8.examples.yaml): A cholesterol-esterifying enzyme drawn as directly inhibiting a viral fusion protein | Non-conformant | gomodel:6796b94c00004996 |
| [CAM-2-E1](CAM-2.examples.yaml): Calmodulin drawn as two nodes, calcium binding directly activating its own kinase-activator node (from [CAM-2](CAM-2.md)) | Non-conformant | gomodel:62b4ffe300004489 |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Directly positively regulates](https://wiki.geneontology.org/index.php/Directly_positively_regulates) (2023) vs [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04) | The relation page allows a direct edge when the upstream activity makes or degrades a small-molecule regulator. The 2020 call fixed "directly" as direct physical interaction, with a reasoner rule that infers binding. | Route small-molecule effects through the molecule (`has output`, `is small molecule activator/inhibitor of`); no direct protein-to-protein edge (CAM-8). | The two sources conflict; a direct edge under the reasoner rule asserts a binding that did not happen. |

## Sources

- wiki: [Directly positively regulates (reviewed 2023)](https://wiki.geneontology.org/index.php/Directly_positively_regulates)
- wiki: [Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)
- drive: [Regulation Notes, 2020 GO-CAM Jamboree](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)
- issue: [go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979)
- repo: [gocam-curation causal-relations reference](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/gocam-curation/references/causal-relations.md)

<!-- END GENERATED -->
