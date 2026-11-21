---
id: ONT-5
title: A replacement in another aspect is a `consider`, never a `replaced_by`
status: proposed
topic: ONT
provenance: GOC_PLUS
provenance_note: '[GOC+]. The GOC has no written rule. A May 2026 ontology developers'' call found none
  in the documentation, considered that a cross-aspect `replaced_by` could be acceptable in principle,
  then concluded that `consider` is safer because automated replacement in GO-CAM models would need a
  relation change that only a curator can make ([Drive: Ontology Developers call 2026-05-11](https://drive.google.com/open?id=1LgDHGlk1SEX5fZ0DugEfs_YLPlMxvWmV)).
  We make that conclusion a rule.'
go_terms:
- term_id: GO:0099022
  obsolete: true
- term_id: GO:7770062
  label: vesicle membrane tethering activity
- term_id: GO:0099023
  label: vesicle tethering complex
- term_id: GO:0006418
  label: tRNA aminoacylation for protein translation
- term_id: GO:0070127
  label: tRNA aminoacylation for mitochondrial protein translation
- term_id: GO:0004813
  label: alanine-tRNA ligase activity
differences:
- prior_source: '[wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)'
  prior_said: '`replaced_by` when one term replaces the obsolete one; `consider` otherwise; no rule on
    aspect'
  we_recommend: Cross-aspect replacements are always `consider`
  why: Automated replacement cannot change the relation; a May 2026 call reached this view but did not
    document it ([ONT-5](ONT-5.md))
sources:
- kind: web
  title: VESICLE_TETHERING_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/VESICLE_TETHERING_OBSOLETION.html
- kind: repo
  title: ontology changes
  url: https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md
- kind: web
  title: AMINO_ACID_ACTIVATION_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/AMINO_ACID_ACTIVATION_OBSOLETION.html
- kind: drive
  title: Ontology Developers call 2026-05-11
  url: https://drive.google.com/open?id=1LgDHGlk1SEX5fZ0DugEfs_YLPlMxvWmV
date: '2026-11-15'
---

# ONT-5. A replacement in another aspect is a `consider`, never a `replaced_by`

## Decision

When a biological process is obsoleted because it described a molecular function (or the
reverse), the new term must be offered as `consider`. An annotation cannot be repointed
mechanically across aspects, because the gene-product-to-term relation changes too.

## Application

*Example.* GO obsoleted `GO:0099022` vesicle tethering and four children because tethering is
a binding activity, and minted `GO:7770062` vesicle membrane tethering activity. None of the
five carries a `replaced_by`; the MF is offered through `consider`, and each annotation needs
a curator to choose the transport process the activity is part of. `GO:0099023` vesicle
tethering complex is a cellular-component term and must not be used as the MF replacement
([VESICLE_TETHERING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/VESICLE_TETHERING_OBSOLETION.html),
[ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)). The same shape recurs across the
docking, ER–plasma membrane and mitochondrion–ER tethering obsoletions.

A within-aspect redirect and cross-aspect advice can coexist on one term: GO's tRNA-charging
obsoletions give each amino-acid-specific BP a `replaced_by` to the compartment-level BP
(`GO:0006418` or `GO:0070127`) and name the 1:1 MF (`GO:0004813` alanine-tRNA ligase
activity for the alanine term) in the comment
([AMINO_ACID_ACTIVATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/AMINO_ACID_ACTIVATION_OBSOLETION.html)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The GOC has no written rule. A May 2026 ontology developers' call found none in the documentation, considered that a cross-aspect `replaced_by` could be acceptable in principle, then concluded that `consider` is safer because automated replacement in GO-CAM models would need a relation change that only a curator can make ([Drive: Ontology Developers call 2026-05-11](https://drive.google.com/open?id=1LgDHGlk1SEX5fZ0DugEfs_YLPlMxvWmV)). We make that conclusion a rule. |
| Date | 2026-11-15 |
| GO terms | `GO:0099022`  (obsolete); `GO:7770062` vesicle membrane tethering activity; `GO:0099023` vesicle tethering complex; `GO:0006418` tRNA aminoacylation for protein translation; `GO:0070127` tRNA aminoacylation for mitochondrial protein translation; `GO:0004813` alanine-tRNA ligase activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term) | `replaced_by` when one term replaces the obsolete one; `consider` otherwise; no rule on aspect | Cross-aspect replacements are always `consider` | Automated replacement cannot change the relation; a May 2026 call reached this view but did not document it ([ONT-5](ONT-5.md)) |

## Sources

- web: [VESICLE_TETHERING_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/VESICLE_TETHERING_OBSOLETION.html)
- repo: [ontology changes](https://github.com/ai4curation/ai-gene-review/blob/main/docs/ontology_changes.md)
- web: [AMINO_ACID_ACTIVATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/AMINO_ACID_ACTIVATION_OBSOLETION.html)
- drive: [Ontology Developers call 2026-05-11](https://drive.google.com/open?id=1LgDHGlk1SEX5fZ0DugEfs_YLPlMxvWmV)

<!-- END GENERATED -->
