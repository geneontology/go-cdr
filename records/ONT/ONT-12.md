---
id: ONT-12
title: Do not request terms that GO has decided not to have
status: proposed
topic: ONT
provenance: GOC_PLUS
provenance_note: '[GOC+]. This departs from the older downstream-process guideline, which encouraged requests
  such as "BMP signaling involved in cardiac cell differentiation" ([wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)).'
go_terms:
- term_id: GO:0030369
  obsolete: true
- term_id: GO:0061678
  label: Entner-Doudoroff pathway
differences:
- prior_source: '[wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)
    (flagged "to be reviewed")'
  prior_said: Request "X involved in Y" terms to describe downstream involvement
  we_recommend: Never request them; annotate X and model Y
  why: GO has since obsoleted most such terms and lists the rest for obsoletion ([ONT-12](ONT-12.md))
sources:
- kind: web
  title: INVOLVED_IN_PRECOMPOSITION
  url: https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html
- kind: drive
  title: GO rules 2024
  url: https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM
- kind: wiki
  title: Annotation Conf. Call 2020-02-04
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04
- kind: wiki
  title: Obsoleting an Existing Ontology Term
  url: https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term
- kind: wiki
  title: Species-Specific Terms
  url: https://wiki.geneontology.org/index.php/Species-Specific_Terms
- kind: web
  title: AMINO_ACID_ACTIVATION_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/AMINO_ACID_ACTIVATION_OBSOLETION.html
- kind: web
  title: ICAM3_RECEPTOR_ACTIVITY_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/ICAM3_RECEPTOR_ACTIVITY_OBSOLETION.html
- kind: web
  title: ENTNER_DOUDOROFF_OBSOLETION
  url: https://ai4curation.io/ai-gene-review/pages/projects/ENTNER_DOUDOROFF_OBSOLETION.html
- kind: web
  title: OVER_ANNOTATION_PATTERNS
  url: https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html
- kind: wiki
  title: Annotating downstream processes
  url: https://wiki.geneontology.org/index.php/Annotating_downstream_processes
date: '2026-11-15'
---

# ONT-12. Do not request terms that GO has decided not to have

## Decision

Do not request precomposed "X involved in Y" terms, chemical-specific binding terms,
regulation-of-molecular-function process terms, single-step processes that restate an MF,
terms named for an assay or a phenotype, terms named for a taxon, or substrate-specific
processes whose substrate is already carried by an MF.

## Context

Each class has a current alternative:

| Don't request | Do instead | Basis |
|---|---|---|
| "X involved in Y" | Annotate X; carry Y in GO-CAM or (in GAF) a `part_of` extension | 1,265 such terms already obsoleted, 883 with a GO-CAM comment ([INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)); scheduled for obsoletion ([Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)) |
| "<chemical> binding" | `binding` with `has_input` the ChEBI entity | [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04) |
| "regulation of <MF>" processes | The regulator's own MF (enzyme regulator, adaptor) and the regulated process | do-not-annotate and scheduled obsoletion ([Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)) |
| Single-step processes ("protein methylation") | The MF that performs the step | as above |
| Assay or phenotype terms | The process the assay measures | GO obsoletion reasons list ([wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)) |
| Taxon-named subclasses | Subclasses distinguished by structure, composition or mechanism; a taxon constraint if needed | [wiki: Species-Specific Terms](https://wiki.geneontology.org/index.php/Species-Specific_Terms) |
| Substrate-specific BP restating an MF ("alanyl-tRNA aminoacylation") | The generic BP plus the specific MF | [AMINO_ACID_ACTIVATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/AMINO_ACID_ACTIVATION_OBSOLETION.html) |
| A ligand-named receptor activity with several unrelated receptors | The receptors' own activities with the ligand as input | `GO:0030369` ICAM-3 receptor activity obsoleted ([ICAM3_RECEPTOR_ACTIVITY_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/ICAM3_RECEPTOR_ACTIVITY_OBSOLETION.html)) |
| A pathway-variant term distinguished only by intermediates | The parent pathway term, with variants in GO-CAM | Entner–Doudoroff sub-pathways retired to `GO:0061678` ([ENTNER_DOUDOROFF_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/ENTNER_DOUDOROFF_OBSOLETION.html)) |

The test behind the last two rows is the one in [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)
pattern 9: ask what the specific term would assert that its parent and the gene's other
annotations do not. If the answer is a fact already carried in another aspect, the term adds
nothing. Specificity that no other aspect carries (compartment, for example) remains legitimate.

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. This departs from the older downstream-process guideline, which encouraged requests such as "BMP signaling involved in cardiac cell differentiation" ([wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)). |
| Date | 2026-11-15 |
| GO terms | `GO:0030369`  (obsolete); `GO:0061678` Entner-Doudoroff pathway |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [ONT-12-E1](ONT-12.examples.yaml): A proposed "phosphomannomutase activity involved in GDP-mannose biosynthetic process" | Non-conformant | GO:0004615 phosphomannomutase activity |
| [ONT-12-E2](ONT-12.examples.yaml): A proposed "positive regulation of base-excision repair glycosylase activity" | Non-conformant | A `proposed_new_terms` entry in the DDB1 review, "positive regulation of base-excision repair glycosylase activity", for the UV-DDB complex stimulating BER glycosylases in trans. |
| [ONT-12-E3](ONT-12.examples.yaml): Merged GTPase-specific GEF terms not re-requested for a RhoA-specific GEF | Conformant | GO:0005089 |
| [ONT-2-E1](ONT-2.examples.yaml): GTPase-specific GEF terms confirmed merged in three services, with QuickGO's behaviour noted (from [ONT-2](ONT-2.md)) | Conformant | GO:0005089 |
| [ONT-14-E1](ONT-14.examples.yaml): A missing RhoA-specific GEF term filed as a knowledge gap (from [ONT-14](ONT-14.md)) | Non-conformant | A `knowledge_gaps` entry in the ARHGEF19 review with `gap_kind: [ONTOLOGY]`: the protein is a RhoA exchange factor, and not a Rac1 or Cdc42 one, but this "cannot be stated in a GO term". |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) (flagged "to be reviewed") | Request "X involved in Y" terms to describe downstream involvement | Never request them; annotate X and model Y | GO has since obsoleted most such terms and lists the rest for obsoletion ([ONT-12](ONT-12.md)) |

## Sources

- web: [INVOLVED_IN_PRECOMPOSITION](https://ai4curation.io/ai-gene-review/pages/projects/INVOLVED_IN_PRECOMPOSITION.html)
- drive: [GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)
- wiki: [Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)
- wiki: [Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)
- wiki: [Species-Specific Terms](https://wiki.geneontology.org/index.php/Species-Specific_Terms)
- web: [AMINO_ACID_ACTIVATION_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/AMINO_ACID_ACTIVATION_OBSOLETION.html)
- web: [ICAM3_RECEPTOR_ACTIVITY_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/ICAM3_RECEPTOR_ACTIVITY_OBSOLETION.html)
- web: [ENTNER_DOUDOROFF_OBSOLETION](https://ai4curation.io/ai-gene-review/pages/projects/ENTNER_DOUDOROFF_OBSOLETION.html)
- web: [OVER_ANNOTATION_PATTERNS](https://ai4curation.io/ai-gene-review/pages/projects/OVER_ANNOTATION_PATTERNS.html)
- wiki: [Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)

<!-- END GENERATED -->
