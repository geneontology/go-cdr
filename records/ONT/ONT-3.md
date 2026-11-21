---
id: ONT-3
title: Treat `replaced_by` as a mechanical redirect that you must check
status: proposed
topic: ONT
provenance: GOC_PLUS
provenance_note: '[GOC+]. The GOC documents what `replaced_by` does; checking it per annotation, and flagging
  a wrong redirect upstream, is ours ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).'
go_terms:
- term_id: GO:0070680
  obsolete: true
- term_id: GO:0070981
  label: L-asparagine biosynthetic process
- term_id: GO:0070681
  label: glutaminyl-tRNAGln biosynthesis via transamidation
- term_id: GO:0043039
  label: tRNA aminoacylation
- term_id: GO:0036378
  obsolete: true
- term_id: GO:1901755
  label: vitamin D3 biosynthetic process
- term_id: GO:0042369
  label: vitamin D catabolic process
differences:
- prior_source: GOC tooling (Noctua, Protein2GO, GORULE:0000020)
  prior_said: Annotations to terms with `replaced_by` are updated automatically
  we_recommend: Accept the redirect only after checking it per annotation; flag wrong redirects upstream
  why: Redirects can leave the branch (`GO:0070680`) or misfit a subset (CYP24A1) ([ONT-3](ONT-3.md))
sources:
- kind: wiki
  title: Annotation Conf. Call 2023-04-18
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18
- kind: drive
  title: Automated Ontology Term Updates in Noctua
  url: https://drive.google.com/open?id=1QrKtMLMjBFoUaceh5UJX5IP_EtqMEx9igsqj_73DrFQ
- kind: wiki
  title: Obsoleting an Existing Ontology Term
  url: https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term
- kind: web
  title: OVER_ANNOTATION_PATTERNS
  url: https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html
- kind: web
  title: CALCITRIOL_BIOSYNTHESIS_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/CALCITRIOL_BIOSYNTHESIS_OBSOLETION.html
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# ONT-3. Treat `replaced_by` as a mechanical redirect that you must check

## Decision

`replaced_by` says the obsolete term and its target denote the same thing, and tools apply it
automatically. Accept it for your annotation only after checking that the target is in the
right branch for what the gene does. When it is not, record the correct term and flag the
`replaced_by` upstream.

## Context

Noctua and Protein2GO update terms with a `replaced_by` automatically, and QuickGO and AmiGO
repair such annotations on load; `consider` targets need curator review
([wiki: Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18),
[Drive: Automated Ontology Term Updates in Noctua](https://drive.google.com/open?id=1QrKtMLMjBFoUaceh5UJX5IP_EtqMEx9igsqj_73DrFQ)).
GORULE:0000020 repairs GAF rows the same way. Only one `replaced_by` is allowed per term
([wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)),
so a term whose annotations fell into distinct classes cannot be served by one redirect.

## Application

*Example (redirect leaves the branch).* `GO:0070680` asparaginyl-tRNAAsn biosynthesis via
transamidation is obsolete with `replaced_by` `GO:0070981` L-asparagine biosynthetic process
(both verified in the local build). The GatCAB transamidase makes Asn-tRNA(Asn), not free
asparagine. The obsolete term's own definition begins "A tRNA aminoacylation process", and its
glutaminyl twin `GO:0070681` is a subclass of `GO:0043039` tRNA aminoacylation (both checked in
the local build). For GatCAB genes the right term is `GO:0043039`, not the redirect
([OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html), pattern 9).

*Example (redirect right for most rows, not all).* `GO:0036378` calcitriol biosynthetic
process from calciol is replaced by `GO:1901755` vitamin D3 biosynthetic process, which GO
redefined so that calcitriol is its primary output. That fits the 25-hydroxylases and the
1α-hydroxylase. It does not obviously fit CYP24A1, whose product is the 24-hydroxylated
inactivation metabolite; `GO:0042369` vitamin D catabolic process may be the right home
([CALCITRIOL_BIOSYNTHESIS_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/CALCITRIOL_BIOSYNTHESIS_OBSOLETION.html)).

When you accept a redirect, record the `replaced_by` line and the release in your provenance,
and check whether repointing to a parent changes subsumption elsewhere (a module or GO-CAM on
the parent term may now subsume a sibling).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The GOC documents what `replaced_by` does; checking it per annotation, and flagging a wrong redirect upstream, is ours ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)). |
| Date | 2026-11-15 |
| GO terms | `GO:0070680`  (obsolete); `GO:0070981` L-asparagine biosynthetic process; `GO:0070681` glutaminyl-tRNAGln biosynthesis via transamidation; `GO:0043039` tRNA aminoacylation; `GO:0036378`  (obsolete); `GO:1901755` vitamin D3 biosynthetic process; `GO:0042369` vitamin D catabolic process |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| GOC tooling (Noctua, Protein2GO, GORULE:0000020) | Annotations to terms with `replaced_by` are updated automatically | Accept the redirect only after checking it per annotation; flag wrong redirects upstream | Redirects can leave the branch (`GO:0070680`) or misfit a subset (CYP24A1) ([ONT-3](ONT-3.md)) |

## Sources

- wiki: [Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18)
- drive: [Automated Ontology Term Updates in Noctua](https://drive.google.com/open?id=1QrKtMLMjBFoUaceh5UJX5IP_EtqMEx9igsqj_73DrFQ)
- wiki: [Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)
- web: [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)
- web: [CALCITRIOL_BIOSYNTHESIS_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/CALCITRIOL_BIOSYNTHESIS_OBSOLETION.html)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
