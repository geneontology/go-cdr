---
id: PH-9
title: Record a loss with IKR or IRD, and choose IKR when a key residue explains it
status: proposed
topic: PH
provenance: NEW
provenance_note: '[GOC] for the codes; [GOC+] for "prefer IKR" and the seed-in-clade check; [NEW] for
  the requirement to name the residues (PANTHER does not publish them, see [PANTHER_IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/PANTHER_IBA_REVIEW.html)).'
evidence_codes:
- IDA
- IBA
- IBD
- IKR
- IRD
go_terms:
- term_id: GO:0004252
  label: serine-type endopeptidase activity
- term_id: GO:0042026
  label: protein refolding
differences:
- prior_source: '[wiki: IRD](https://wiki.geneontology.org/index.php/Inferred_from_Rapid_Divergence%28IRD%29)
    (2018)'
  prior_said: IRD "implies a NOT annotation"; example is a gene-level NOT row citing a TAIR communication.
  we_recommend: IRD lives on internal nodes and creates no gene rows; prefer IKR when a residue explains
    the loss; check the loss clade for seeds (PH-9).
  why: Current PAINT data contain no gene-level IRD rows; the wiki example no longer matches the data
    ([IRD_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html)). The IRD
    page's three empty sections should be filled.
- prior_source: '[wiki: IKR](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29)'
  prior_said: '`WITH/FROM` must indicate the lacking residues via an alignment, domain or rule id.'
  we_recommend: Also name the residues in the review or ticket (PH-9).
  why: PANTHER does not publish which residues an IKR used, so a domain id alone is not checkable.
sources:
- kind: wiki
  title: PAINT annotation guidelines
  url: https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines
- kind: wiki
  title: IKR
  url: https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29
- kind: web
  title: IRD_EVIDENCE
  url: https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html
- kind: issue
  title: go-annotation#2109
  url: https://github.com/geneontology/go-annotation/issues/2109
- kind: web
  title: PANTHER_IBA_REVIEW
  url: https://ai4curation.io/ai-gene-review/pages/projects/PANTHER_IBA_REVIEW.html
date: '2026-11-15'
---

# PH-9. Record a loss with IKR or IRD, and choose IKR when a key residue explains it

## Decision

When members below an annotated node have lost the function, record the loss. Use IKR when
the loss is explained by missing key residues and say which residues. Use IRD for divergence
with no residue explanation. Before placing either, check that the loss clade does not contain
a seed of the IBD it blocks.

## Context

losses are part of the GOC design ([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines);
[wiki: IKR](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29)), but
the two codes behave very differently downstream. An IKR produces a NOT|IBA on every
descendant, which users can see. An IRD sits only on the internal node in PAINT's `IBD.gaf` and
produces nothing for the genes below it: GOA holds no IRD rows, and none of PAINT's NOT|IBA leaf
rows comes from an IRD alone ([IRD_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html)). A curator who knows the
residue therefore loses information by using IRD, which is the point of the PAINT team's
preference for IKR when a catalytic residue is missing
([go-annotation#2109](https://github.com/geneontology/go-annotation/issues/2109)). The IKR page
requires a `WITH/FROM` naming the alignment, domain or rule when the reference is a GO_REF, and
warns that families have exceptions: WNK1 lacks the canonical catalytic Lys yet is active
because another Lys substitutes ([wiki: IKR](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29)).
When a paper both shows the missing site and assays inactivity, make both NOT IKR and NOT IDA.

## Application

Worked example: rat HPT matches the peptidase S1 domain but has lost the catalytic triad, so it
carries NOT `GO:0004252` serine-type endopeptidase activity by IKR with `InterPro:IPR000126` in
`WITH/FROM` ([wiki: IKR](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29)).
Counter-example: the fungal IRD that blocks `GO:0042026` protein refolding on PTHR19375
(PTN001065099) is right for SSB and SSZ1, which fold nascent chains, and wrong for SSA, because
yeast SSA1 is itself a seed of the blocked IBD and has two refolding IDA rows. The repo verdict
is `LOSS_TOO_BROAD`, with the request to move the IRD onto the SSB/SSZ1 branch
([IRD_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html)). Of 19 contested IRDs adjudicated in the repo, 12
looked wrong and 2 too broad, and in six of the 19 the loss clade contained a seed of the IBD
it blocked; that sample is biased towards conflicts and is not an error rate.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW] [GOC] for the codes; [GOC+] for "prefer IKR" and the seed-in-clade check; [NEW] for the requirement to name the residues (PANTHER does not publish them, see [PANTHER_IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/PANTHER_IBA_REVIEW.html)). |
| Date | 2026-11-15 |
| Evidence codes | IDA, IBA, IBD, IKR, IRD |
| GO terms | `GO:0004252` serine-type endopeptidase activity; `GO:0042026` protein refolding |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: IRD](https://wiki.geneontology.org/index.php/Inferred_from_Rapid_Divergence%28IRD%29) (2018) | IRD "implies a NOT annotation"; example is a gene-level NOT row citing a TAIR communication. | IRD lives on internal nodes and creates no gene rows; prefer IKR when a residue explains the loss; check the loss clade for seeds (PH-9). | Current PAINT data contain no gene-level IRD rows; the wiki example no longer matches the data ([IRD_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html)). The IRD page's three empty sections should be filled. |
| [wiki: IKR](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29) | `WITH/FROM` must indicate the lacking residues via an alignment, domain or rule id. | Also name the residues in the review or ticket (PH-9). | PANTHER does not publish which residues an IKR used, so a domain id alone is not checkable. |

## Sources

- wiki: [PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)
- wiki: [IKR](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29)
- web: [IRD_EVIDENCE](https://ai4curation.io/ai-gene-review/pages/projects/IRD_EVIDENCE.html)
- issue: [go-annotation#2109](https://github.com/geneontology/go-annotation/issues/2109)
- web: [PANTHER_IBA_REVIEW](https://ai4curation.io/ai-gene-review/pages/projects/PANTHER_IBA_REVIEW.html)

<!-- END GENERATED -->
