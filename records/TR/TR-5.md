---
id: TR-5
title: Annotate coTF activity for locus-specific action through a dbTF, and protect proteins with a real
  DNA-binding domain from it
status: proposed
topic: TR
provenance: GOC_PLUS
provenance_note: '[GOC+]. The recruitment-chain reading is GOC expert practice stated in issues, not in
  the 2021 paper''s term definitions.'
aspects:
- F
- P
evidence_codes:
- IDA
go_terms:
- term_id: GO:0003712
  label: transcription coregulator activity
- term_id: GO:0003713
  label: transcription coactivator activity
- term_id: GO:0003714
  label: transcription corepressor activity
- term_id: GO:0000976
  label: transcription cis-regulatory region binding
- term_id: GO:0003700
  label: DNA-binding transcription factor activity
differences:
- prior_source: '[go-annotation#4000](https://github.com/geneontology/go-annotation/issues/4000)'
  prior_said: 'Two readings of coTF: any protein in a recruitment cascade, or only proteins directly recruited
    by a dbTF'
  we_recommend: Cascade reading, provided the chain is shown to start at a dbTF or at a mark it caused
  why: Matches [go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554) and the
    current GO:0003712 definition ("at a specific genomic locus")
- prior_source: '`GO:0000976` term text'
  prior_said: 'Definition: binding "to a specific sequence of DNA"; comment: "meant to also capture non-specific
    binding"'
  we_recommend: Use GO:0000976 for non-specific regulatory-region binding by coTFs, as the comment and
    [go-annotation#5743](https://github.com/geneontology/go-annotation/issues/5743) intend
  why: The definition and the comment contradict each other; we follow the usage guidance and flag the
    definition
open_questions:
- '**Strict versus cascade coTF.** Is the recruitment-chain reading of [TR-5](TR-5.md) the consortium
  position, or should GO:0003712 be reserved for proteins directly bound by a dbTF, with a new term for
  "co-coregulators"?'
sources:
- kind: issue
  title: go-annotation#4554
  url: https://github.com/geneontology/go-annotation/issues/4554
- kind: issue
  title: go-annotation#4000
  url: https://github.com/geneontology/go-annotation/issues/4000
- kind: issue
  title: go-annotation#2972
  url: https://github.com/geneontology/go-annotation/issues/2972
- kind: issue
  title: go-annotation#5743
  url: https://github.com/geneontology/go-annotation/issues/5743
date: '2026-11-15'
---

# TR-5. Annotate coTF activity for locus-specific action through a dbTF, and protect proteins with a real DNA-binding domain from it

## Decision

Annotate `GO:0003712` (or `GO:0003713`, `GO:0003714`) when the protein is recruited
to specific genes by a DNA-bound dbTF, or by reading a mark laid down at a
dbTF-specified locus, or by another coTF in such a chain, and changes their
transcription. For a protein with a characterised DNA-binding domain and DNA-binding
evidence, annotate coTF activity only with evidence that the regulatory effect does not
use its own DNA binding.

## Context

GO:0003712 is defined as modulating transcription "via binding to a
DNA-binding transcription factor at a specific genomic locus, either on its own or as
part of a complex", with the usage note that most coregulators do not bind DNA. The GOC
expert reading sets three recruitment routes (direct binding by a dbTF, reading a
histone mark, recruitment by another coTF) and declines to make separate
"coactivator-coactivator" terms ([go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554);
[go-annotation#4000](https://github.com/geneontology/go-annotation/issues/4000)). For Cdx2
and Pou5f1, both with characterised homeodomains and DNA-binding evidence, coTF
annotations based on protein–protein interaction were changed to dbTF: "To apply that
term you would need evidence that the activity does NOT involve DNA binding"
([go-annotation#2972](https://github.com/geneontology/go-annotation/issues/2972)).

## Application

Worked examples. RFXANK, a subunit of the RFX complex that binds the MHC class II X box,
had its dbTF activator row `MODIFY` to `GO:0003713` and its DNA-binding row `REMOVE`;
RFXAP likewise (`genes/human/RFXANK`). NOTCH1's intracellular domain activates targets in
complex with the DNA-binding RBPJ; its IDA rows to cis-regulatory DNA binding and dbTF
activator activity were removed by the curating group, leaving `GO:0003713`
([go-annotation#5743](https://github.com/geneontology/go-annotation/issues/5743)).

When a coTF binds DNA non-specifically as part of its mechanism, annotate
`GO:0000976` transcription cis-regulatory region binding (the term's comment admits
non-specific binding) alongside the coTF term, not `GO:0003700`
([go-annotation#5743](https://github.com/geneontology/go-annotation/issues/5743)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+]. The recruitment-chain reading is GOC expert practice stated in issues, not in the 2021 paper's term definitions. |
| Date | 2026-11-15 |
| Evidence codes | IDA |
| GO terms | `GO:0003712` transcription coregulator activity; `GO:0003713` transcription coactivator activity; `GO:0003714` transcription corepressor activity; `GO:0000976` transcription cis-regulatory region binding; `GO:0003700` DNA-binding transcription factor activity |

## Examples

| Example | Verdict | Subject |
|---|---|---|
| [TR-5-E1](TR-5.examples.yaml): An MBF subunit that reaches promoters through its DNA-binding partners | Non-conformant | cdc10 enables GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific (EXP, PMID:14648198) |
| [TR-5-E2](TR-5.examples.yaml): A plant coactivator recruited by methyl-DNA readers rather than by a dbTF | Contested | EIP9 enables GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific (IDA, PMID:30523112) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [go-annotation#4000](https://github.com/geneontology/go-annotation/issues/4000) | Two readings of coTF: any protein in a recruitment cascade, or only proteins directly recruited by a dbTF | Cascade reading, provided the chain is shown to start at a dbTF or at a mark it caused | Matches [go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554) and the current GO:0003712 definition ("at a specific genomic locus") |
| `GO:0000976` term text | Definition: binding "to a specific sequence of DNA"; comment: "meant to also capture non-specific binding" | Use GO:0000976 for non-specific regulatory-region binding by coTFs, as the comment and [go-annotation#5743](https://github.com/geneontology/go-annotation/issues/5743) intend | The definition and the comment contradict each other; we follow the usage guidance and flag the definition |

## Open questions

1. **Strict versus cascade coTF.** Is the recruitment-chain reading of [TR-5](TR-5.md) the consortium position, or should GO:0003712 be reserved for proteins directly bound by a dbTF, with a new term for "co-coregulators"?

## Sources

- issue: [go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554)
- issue: [go-annotation#4000](https://github.com/geneontology/go-annotation/issues/4000)
- issue: [go-annotation#2972](https://github.com/geneontology/go-annotation/issues/2972)
- issue: [go-annotation#5743](https://github.com/geneontology/go-annotation/issues/5743)

<!-- END GENERATED -->
