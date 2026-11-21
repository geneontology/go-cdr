---
id: QN-2
title: Use `contributes_to` only when no single subunit, or smaller subset of subunits, can be said to
  carry out the activity. Annotate every catalytic-core subunit this way, and no accessory subunit.
status: proposed
topic: QN
provenance: GOC_PLUS
provenance_note: '[GOC+]. The test restates the wiki. The sharpening is the accessory-subunit alternative
  and the "unknown subunit, no MF" branch, which the wiki states but which annotators often skip. [wiki:
  Contributes to](https://wiki.geneontology.org/index.php/Contributes_to); [wiki: Enables](https://wiki.geneontology.org/index.php/Enables);
  [Drive: Contributes_to (GOC 2021)](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks);
  [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html).'
go_terms:
- term_id: GO:0004129
  label: cytochrome-c oxidase activity
- term_id: GO:0060090
  label: molecular adaptor activity
- term_id: GO:0098772
  label: molecular function regulator activity
- term_id: GO:0030234
  label: enzyme regulator activity
- term_id: GO:0008177
  label: succinate dehydrogenase (quinone) activity
- term_id: GO:0000104
  label: succinate dehydrogenase activity
- term_id: GO:0046933
  label: proton-transporting ATP synthase activity, rotational mechanism
- term_id: GO:0003878
  label: ATP citrate synthase activity
- term_id: GO:0000030
  label: mannosyltransferase activity
- term_id: GO:0003924
  label: GTPase activity
sources:
- kind: wiki
  title: Contributes to
  url: https://wiki.geneontology.org/index.php/Contributes_to
- kind: web
  title: TOP_NOTS
  url: https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html
- kind: issue
  title: go-annotation#6414
  url: https://github.com/geneontology/go-annotation/issues/6414
- kind: web
  title: SDH_GP2TERM_CONTRIBUTES_TO
  url: https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html
- kind: wiki
  title: Enables
  url: https://wiki.geneontology.org/index.php/Enables
- kind: drive
  title: Contributes_to (GOC 2021)
  url: https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks
date: '2026-11-15'
---

# QN-2. Use `contributes_to` only when no single subunit, or smaller subset of subunits, can be said to carry out the activity. Annotate every catalytic-core subunit this way, and no accessory subunit.

## Decision

Use `contributes_to` only when no single subunit, or smaller subset of subunits, can be said to carry out the activity. Annotate every catalytic-core subunit this way, and no accessory subunit.

## Context

`contributes_to` exists for "irreducible molecular machines" ([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). Being part of a complex is not enough. Applied too freely, `contributes_to` gives every structural or regulatory subunit its complex's catalytic activity, a pattern the repo's [TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html) worklist finds repeatedly (assembly factors such as SURF1 carrying GO:0004129 cytochrome-c oxidase activity).

**The test** (three questions, adapted from the wiki checklist):

1. Is the activity a property of the complex and not of one subunit? If one subunit has it alone, that subunit `enables` it and the others get no annotation to that term.
2. Is this subunit part of the active unit? Look for a shared active site, an essential core role, or a rotary or channel mechanism that needs the subunit. A regulatory, assembly or scaffolding subunit is not part of the active unit. Give it its own activity instead (GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity or a child, GO:0030234 enzyme regulator activity) together with `part_of` the complex.
3. Is it unknown which subunit carries the activity? Then make no MF annotation to any subunit. Annotate the complex membership (CC) and the process (BP).

## Application

**Examples.**

- *Succinate dehydrogenase.* No subunit catalyses the whole succinate-to-quinone reaction, so SDHA, SDHB, SDHC and SDHD each `contributes_to` GO:0008177 succinate dehydrogenase (quinone) activity. That is the agreed outcome of [go-annotation#6414](https://github.com/geneontology/go-annotation/issues/6414), worked in the repo's [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html). The parent GO:0000104 succinate dehydrogenase activity needs a separate judgement, because the flavoprotein SDHA can run the succinate half-reaction alone. `enables` GO:0000104 may be right for SDHA and wrong for the other three.
- *ATP synthase.* Every subunit of the F1, F0 and stator sectors `contributes_to` GO:0046933 proton-transporting ATP synthase activity, rotational mechanism ([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)).
- *ATP citrate lyase* from *Chlorobaculum tepidum*: both subunits supply active-site residues, neither is active alone, and both `contributes_to` GO:0003878 ATP citrate synthase activity.
- *Not contributes_to.* In the PIGM-PIGX complex only PIGM `enables` GO:0000030 mannosyltransferase activity. PIGX is required but has no activity of its own. eIF2gamma `enables` GO:0003924 GTPase activity, and eIF2alpha and eIF2beta get no GTPase annotation at all.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The test restates the wiki. The sharpening is the accessory-subunit alternative and the "unknown subunit, no MF" branch, which the wiki states but which annotators often skip. [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to); [wiki: Enables](https://wiki.geneontology.org/index.php/Enables); [Drive: Contributes_to (GOC 2021)](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks); [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html). |
| Date | 2026-11-15 |
| GO terms | `GO:0004129` cytochrome-c oxidase activity; `GO:0060090` molecular adaptor activity; `GO:0098772` molecular function regulator activity; `GO:0030234` enzyme regulator activity; `GO:0008177` succinate dehydrogenase (quinone) activity; `GO:0000104` succinate dehydrogenase activity; `GO:0046933` proton-transporting ATP synthase activity, rotational mechanism; `GO:0003878` ATP citrate synthase activity; `GO:0000030` mannosyltransferase activity; `GO:0003924` GTPase activity |

## Sources

- wiki: [Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)
- web: [TOP_NOTS](https://ai4curation.io/ai-gene-review/pages/projects/TOP_NOTS.html)
- issue: [go-annotation#6414](https://github.com/geneontology/go-annotation/issues/6414)
- web: [SDH_GP2TERM_CONTRIBUTES_TO](https://ai4curation.io/ai-gene-review/pages/projects/SDH_GP2TERM_CONTRIBUTES_TO.html)
- wiki: [Enables](https://wiki.geneontology.org/index.php/Enables)
- drive: [Contributes_to (GOC 2021)](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks)

<!-- END GENERATED -->
