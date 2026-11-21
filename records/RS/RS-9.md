---
id: RS-9
title: 'Receptors, G proteins and second-messenger enzymes: annotate the specific pathway the evidence
  shows, with the right coupling and sign'
status: proposed
topic: RS
provenance: GOC_PLUS
provenance_note: '[GOC+]. The PDE convention is a 2025 PAINT working decision (minutes), not yet a published
  guideline.'
aspects:
- P
go_terms:
- term_id: GO:0004941
  label: beta2-adrenergic receptor activity
- term_id: GO:0004930
  label: G protein-coupled receptor activity
- term_id: GO:0007189
  label: adenylate cyclase-activating G protein-coupled receptor signaling pathway
- term_id: GO:0007193
  label: adenylate cyclase-inhibiting G protein-coupled receptor signaling pathway
- term_id: GO:0007200
  label: phospholipase C-activating G protein-coupled receptor signaling pathway
- term_id: GO:0019933
  obsolete: true
- term_id: GO:0141156
  label: cAMP/PKA signal transduction
- term_id: GO:0045879
  label: negative regulation of smoothened signaling pathway
- term_id: GO:0007224
  label: smoothened signaling pathway
differences:
- prior_source: '[Drive: PAINT signaling minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM)'
  prior_said: 'Working decision: PDEs are negative regulation of cAMP pathways; cAMP-mediated signaling
    to be obsoleted.'
  we_recommend: Adopted (RS-9).
  why: 'Fills a gap: no published guideline covered second-messenger degraders.'
sources:
- kind: drive
  title: PAINT signaling annotation – meeting minutes, 2025
  url: https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM
- kind: issue
  title: go-annotation#1691
  url: https://github.com/geneontology/go-annotation/issues/1691
- kind: web
  title: LIGANDS_IN_SIGNALING
  url: https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html
- kind: web
  title: GPCR
  url: https://ai4curation.io/ai-gene-review/pages/projects/GPCR.html
- kind: web
  title: REGULATION_SIGN
  url: https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html
date: '2026-11-15'
---

# RS-9. Receptors, G proteins and second-messenger enzymes: annotate the specific pathway the evidence shows, with the right coupling and sign

## Decision

Statement.

## Context

- Receptors: annotate the most specific receptor activity the ligand and mechanism support (for example GO:0004941 beta2-adrenergic receptor activity rather than GO:0004930 G protein-coupled receptor activity, when the row's own evidence names the ligand). Annotate the matching pathway.
- G proteins: annotate coupling pathway terms (GO:0007189, GO:0007193, GO:0007200 phospholipase C-activating G protein-coupled receptor signaling pathway) from direct evidence on the Gα class, not from family membership.
- Second-messenger enzymes: annotate an adenylate cyclase that makes the second messenger of a GPCR pathway to that pathway. Annotate an enzyme that destroys the second messenger, such as a phosphodiesterase, to negative regulation of the pathway.
- Inhibitory receptors: a receptor whose ligand switches its activity off, such as Patched, is annotated to regulation of the pathway, with the sign the receptor exerts. Smoothened carries the pathway term.

**Rationale.** The 2025 PAINT signalling minutes record the plan to obsolete GO:0019933 cAMP-mediated signaling and GO:0141156 cAMP/PKA signal transduction, with members re-annotated to GO:0007189. The same minutes place PKA in the pathway and propose PDEs as negative regulation ([Drive: PAINT signaling annotation – meeting minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM)). GO:0019933 is obsolete in the current release. The 2017 review asked curators to rehouse "regulation of adenylate cyclase activity" and "regulation of cAMP biosynthesis" rows on GPCRs to the AC-activating or AC-inhibiting pathway terms ([go-annotation#1691](https://github.com/geneontology/go-annotation/issues/1691)). In the ligand survey, PTCH1 and Drosophila ptc carry only regulation terms ([LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html)). The Gs/Gi split is the commonest source of family-level sign errors ([GPCR](https://ai4curation.io/ai-gene-review/pages/projects/GPCR.html); [REGULATION_SIGN](https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html)).

## Application

**Worked example.** PTCH1 restrains Smoothened until Hedgehog binds. Annotate PTCH1 to GO:0045879 negative regulation of smoothened signaling pathway, and Smoothened to GO:0007224 smoothened signaling pathway.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The PDE convention is a 2025 PAINT working decision (minutes), not yet a published guideline. |
| Date | 2026-11-15 |
| GO terms | `GO:0004941` beta2-adrenergic receptor activity; `GO:0004930` G protein-coupled receptor activity; `GO:0007189` adenylate cyclase-activating G protein-coupled receptor signaling pathway; `GO:0007193` adenylate cyclase-inhibiting G protein-coupled receptor signaling pathway; `GO:0007200` phospholipase C-activating G protein-coupled receptor signaling pathway; `GO:0019933`  (obsolete); `GO:0141156` cAMP/PKA signal transduction; `GO:0045879` negative regulation of smoothened signaling pathway; `GO:0007224` smoothened signaling pathway |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: PAINT signaling minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM) | Working decision: PDEs are negative regulation of cAMP pathways; cAMP-mediated signaling to be obsoleted. | Adopted (RS-9). | Fills a gap: no published guideline covered second-messenger degraders. |

## Sources

- drive: [PAINT signaling annotation – meeting minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM)
- issue: [go-annotation#1691](https://github.com/geneontology/go-annotation/issues/1691)
- web: [LIGANDS_IN_SIGNALING](https://ai4curation.io/ai-gene-review/pages/projects/LIGANDS_IN_SIGNALING.html)
- web: [GPCR](https://ai4curation.io/ai-gene-review/pages/projects/GPCR.html)
- web: [REGULATION_SIGN](https://ai4curation.io/ai-gene-review/pages/projects/REGULATION_SIGN.html)

<!-- END GENERATED -->
