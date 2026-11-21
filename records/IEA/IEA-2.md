---
id: IEA-2
title: A signature mapping must hold for every member of the entry
status: proposed
topic: IEA
provenance: NEW
provenance_note: '[NEW]. Departs from the enzyme-mapping policy in go-annotation#385.'
go_terms:
- term_id: GO:0005524
  label: ATP binding
- term_id: GO:0006468
  label: protein phosphorylation
- term_id: GO:0006801
  label: superoxide metabolic process
- term_id: GO:0019430
  label: removal of superoxide radicals
- term_id: GO:0046961
  label: proton-transporting ATPase activity, rotational mechanism
- term_id: GO:0006754
  label: ATP biosynthetic process
- term_id: GO:0008564
  label: protein-exporting ATPase activity
differences:
- prior_source: InterPro curator in [go-annotation#385](https://github.com/geneontology/go-annotation/issues/385)
    (2007)
  prior_said: Enzyme mappings are not removed because a family has a few catalytically inactive members;
    inactive members are annotated manually.
  we_recommend: A mapping must hold for every member; move catalytic terms to site or active-site entries,
    or to rules (IEA-2).
  why: Manual negation of pseudo-enzymes does not happen at scale; site entries now make the narrower
    mapping possible. Reflects the later InterPro direction in [PMID:22301074](https://europepmc.org/article/MED/22301074)
    and [#2921](https://github.com/geneontology/go-annotation/issues/2921).
sources:
- kind: paper
  title: PMID:22301074
  url: https://europepmc.org/article/MED/22301074
- kind: issue
  title: go-annotation#2921
  url: https://github.com/geneontology/go-annotation/issues/2921
- kind: issue
  title: go-annotation#385
  url: https://github.com/geneontology/go-annotation/issues/385
- kind: wiki
  title: InterPro2GO session 2011
  url: https://wiki.geneontology.org/index.php/InterPro2GO_Session_October_4th_2011
- kind: web
  title: INTERPRO
  url: https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html
date: '2026-11-15'
---

# IEA-2. A signature mapping must hold for every member of the entry

## Decision

Map a GO term to an InterPro entry (or any signature) only if every protein the signature
matches has the function. When a term is true for a subset, place it on a narrower entry (a
subfamily, a site entry, an active-site entry) or in a rule that can require a site, exclude a
domain or restrict a taxon. Do not keep an enzyme mapping on a family because "most" members are
active.

## Context

the InterPro protocol already avoids mapping whole-protein function to a domain and
avoids large, uncharacterised families ([PMID:22301074](https://europepmc.org/article/MED/22301074);
[go-annotation#2921](https://github.com/geneontology/go-annotation/issues/2921)). A 2007 InterPro
reply stated the opposite policy for enzymes: catalytic mappings are not removed because a family
has a few inactive members, and those members must be annotated manually
([go-annotation#385](https://github.com/geneontology/go-annotation/issues/385)). That policy pushes
the cost onto every downstream user and leaves pseudo-enzymes with false IEAs that nobody has time
to negate. Since 2011 the same problem has been discussed for the protein kinase domain and
tribbles pseudokinases ([wiki: InterPro2GO session 2011](https://wiki.geneontology.org/index.php/InterPro2GO_Session_October_4th_2011)).
Site-level entries now make the narrower mapping possible.

## Application

Worked examples (proposals in [INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html), not yet adopted by InterPro):

- `IPR000719` (Protein kinase domain) maps `GO:0005524` ATP binding and `GO:0006468` protein
  phosphorylation. Pseudokinases match the domain. The kinase ATP-binding-site entry `IPR017441`
  and the active-site entries `IPR008271` and `IPR008266` already carry the terms for members with
  the motifs, so the domain-level mappings can go.
- `IPR001424` (Cu/Zn superoxide dismutase domain) maps `GO:0006801` superoxide metabolic process,
  which copper-chaperone members do not perform. UniRule UR000000113 selects canonical Cu/Zn SODs
  and excludes CCS, but assigns only an EC number; the request is to remove the domain mapping and
  add `GO:0019430` removal of superoxide radicals to the rule, plus separate cover for fungal
  Cu-only SODs.
- `IPR013380` (Type 3 secretion system ATPase SctN) maps `GO:0046961` proton-transporting ATPase
  activity, rotational mechanism and `GO:0006754` ATP biosynthetic process. SctN is a soluble
  protein-exporting ATPase with no Fo partner: the terms are wrong for every member, so this is a
  plain removal, with `GO:0008564` protein-exporting ATPase activity as a candidate addition.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW]. Departs from the enzyme-mapping policy in go-annotation#385. |
| Date | 2026-11-15 |
| GO terms | `GO:0005524` ATP binding; `GO:0006468` protein phosphorylation; `GO:0006801` superoxide metabolic process; `GO:0019430` removal of superoxide radicals; `GO:0046961` proton-transporting ATPase activity, rotational mechanism; `GO:0006754` ATP biosynthetic process; `GO:0008564` protein-exporting ATPase activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| InterPro curator in [go-annotation#385](https://github.com/geneontology/go-annotation/issues/385) (2007) | Enzyme mappings are not removed because a family has a few catalytically inactive members; inactive members are annotated manually. | A mapping must hold for every member; move catalytic terms to site or active-site entries, or to rules (IEA-2). | Manual negation of pseudo-enzymes does not happen at scale; site entries now make the narrower mapping possible. Reflects the later InterPro direction in [PMID:22301074](https://europepmc.org/article/MED/22301074) and [#2921](https://github.com/geneontology/go-annotation/issues/2921). |

## Sources

- paper: [PMID:22301074](https://europepmc.org/article/MED/22301074)
- issue: [go-annotation#2921](https://github.com/geneontology/go-annotation/issues/2921)
- issue: [go-annotation#385](https://github.com/geneontology/go-annotation/issues/385)
- wiki: [InterPro2GO session 2011](https://wiki.geneontology.org/index.php/InterPro2GO_Session_October_4th_2011)
- web: [INTERPRO](https://ai4curation.io/ai-gene-review/pages/projects/INTERPRO.html)

<!-- END GENERATED -->
