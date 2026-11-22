---
id: REV-8
title: Do not overrule an experimental curator from evidence you have not seen
status: proposed
topic: REV
provenance: NEW
provenance_note: '[NEW]. GOC guidance tells curators to remove annotations based on invalidated hypotheses
  and to file a ticket against another group''s errors ([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations));
  it does not address reviewers working without full text. Our rule adds the restraint ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).'
evidence_codes:
- IDA
- IPI
- IMP
- IGI
related:
- REV-6
differences:
- prior_source: '[wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)'
  prior_said: Remove annotations based on invalidated hypotheses; GO is not an archive
  we_recommend: Same, but a reviewer without full text must not remove experimental rows on suspicion;
    use `UNDECIDED`
  why: Many cached sources are abstract-only, and titles often foreground a paralog that the figures do
    not ([REV-8](REV-8.md))
- prior_source: '[Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)
    (GORULE:0000013)'
  prior_said: Experimental violations are reported and kept
  we_recommend: A reviewer may call an experimental row wrong when the definition or constraint excludes
    the organism, after checking the constraint is not too narrow
  why: The error is then a term choice, not a reading of data ([REV-8](REV-8.md), [ONT-17](../ONT/ONT-17.md))
sources:
- kind: web
  title: RAR_MISANNOTATION
  url: https://ai4curation.io/ai-gene-review/pages/projects/RAR_MISANNOTATION.html
- kind: wiki
  title: Tips
  url: https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations
- kind: repo
  title: CLAUDE.md
  url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
date: '2026-11-15'
---

# REV-8. Do not overrule an experimental curator from evidence you have not seen

## Decision

Never `REMOVE` an experimental row, or call it "wrong gene", "paralog mix-up" or "name
confusion", because the cached title or abstract is about something else. If you cannot verify
the evidence, use `UNDECIDED`; if the function is clearly right for the gene, `ACCEPT` and
defer.

## Context

Curators who made an IDA, IMP, IGI or IPI read the full text. Many of this repository's
cached publications are abstract-only, and a paper's title often foregrounds one gene or a
paralog while the figures also assay the gene in question. Before asserting mis-attribution,
check the GO term's definition (an apparent mismatch is often a reading error: `G protein
activity` covers small GTPases) and the organism actually stated in the abstract. Reserve
confident "this paper is about organism X" caveats for cases the cached text states outright.

`REMOVE` on an experimental row remains correct in three cases: the function is contradicted
by later evidence; the row misreads an uncontested result ([REV-6](REV-6.md), CREB1); or the
term's definition or a taxon constraint excludes the organism, which makes the error a term
choice rather than a reading of data. The RAR re-examination applied exactly this split to 958
kingdom-level candidates: 379 experimental rows were deferred to the curator and only those
excluded by definition or constraint were called wrong
([RAR_MISANNOTATION](https://ai4curation.io/ai-gene-review/pages/projects/RAR_MISANNOTATION.html)).

A deferral is not silence. Record why you could not decide and what would decide it (the
figure you could not see, the experiment that is missing).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [NEW]. GOC guidance tells curators to remove annotations based on invalidated hypotheses and to file a ticket against another group's errors ([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)); it does not address reviewers working without full text. Our rule adds the restraint ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)). |
| Date | 2026-11-15 |
| Related | [REV-6](REV-6.md) |
| Evidence codes | IDA, IPI, IMP, IGI |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [REV-8-E1](REV-8.examples.yaml): Epe1 H3K9 demethylase IDA left UNDECIDED rather than removed | Conformant | Epe1 enables GO:0032454 histone H3K9 demethylase activity (IDA, PMID:25838386) |
| [REV-8-E2](REV-8.examples.yaml): Galactokinase IMP on GalT removed where the abstract names the galK knockout | Conformant | galT enables GO:0004335 galactokinase activity (IMP, PMID:18263746) |
| [REV-8-E3](REV-8.examples.yaml): A swarming-motility IMP removed because the cached title is about FlgM | Non-conformant | swrD involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:25313396) |
| [REV-6-E1](REV-6.examples.yaml): Epe1 JmjC oxidoreductase IEA removed on its non-canonical iron site (from [REV-6](REV-6.md)) | Conformant | Epe1 enables GO:0016491 oxidoreductase activity (IEA, GO_REF:0000043) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) | Remove annotations based on invalidated hypotheses; GO is not an archive | Same, but a reviewer without full text must not remove experimental rows on suspicion; use `UNDECIDED` | Many cached sources are abstract-only, and titles often foreground a paralog that the figures do not ([REV-8](REV-8.md)) |
| [Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg) (GORULE:0000013) | Experimental violations are reported and kept | A reviewer may call an experimental row wrong when the definition or constraint excludes the organism, after checking the constraint is not too narrow | The error is then a term choice, not a reading of data ([REV-8](REV-8.md), [ONT-17](../ONT/ONT-17.md)) |

## Sources

- web: [RAR_MISANNOTATION](https://ai4curation.io/ai-gene-review/pages/projects/RAR_MISANNOTATION.html)
- wiki: [Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
- repo: [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)

<!-- END GENERATED -->
