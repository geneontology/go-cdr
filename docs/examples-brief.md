# Writing examples for GO Consortium Decision Records

This is the brief used to draft the first examples from AI Gene Review. It is kept so that
anyone adding examples later follows the same rules.

## What an example is

Each record (`records/<CH>/<ID>.md`) may have a sibling file `records/<CH>/<ID>.examples.yaml`:

```yaml
record: MF-5
examples:
- id: MF-5-E1                # <record>-E<n>, numbered from 1 within the file
  title: Short noun phrase saying what the case is
  verdict: NON_CONFORMANT     # CONFORMANT | NON_CONFORMANT | CONTESTED
  subject: {...}              # what the example is about (below)
  explanation: |              # Markdown: why the verdict follows from the record
  fix: |                      # NON_CONFORMANT only, required there: the conformant version
  see_also: [EV-3]            # other records the case also bears on (optional)
  open_question: 2            # CONTESTED only: 1-based number of the record's open question
  discussion: https://...     # CONTESTED only: issue/PR/thread URL (one of these two is required)
  derived_from:               # pinned URL(s) of what the example was taken from
  - https://github.com/monarch-initiative/ai-gene-review/blob/<commit>/genes/...#L123
```

The schema is `src/go_cdr/schema/go_cdr.yaml` (classes `ExampleSet`, `Example`, `Subject`).

### Subjects

| `subject_kind` | Required slots | Typical source in ai-gene-review |
|---|---|---|
| `annotation` | `gene` (`gene_id`, `symbol`), `term` (`term_id`, `label`), `evidence_code`; plus `qualifier`, `reference`, `taxon`, `negated`, `extension` when known | `genes/<org>/<GENE>/<GENE>-ai-review.yaml`, `existing_annotations[i]` |
| `gocam` | `model` (`gomodel:<id>`), and a `description` of the fragment | `gocams/<id>/<id>-src.yaml` and `-review.yaml` |
| `family` | `family` (`PANTHER:PTHR…` or `PANTHER:PTN…`), `description` | `interpro/panther/<PTHR>/<PTHR>-review.yaml` |
| `term` | `term` | `proposed_new_terms`, ontology-gap discussions, obsolete-term handling |
| `pipeline_config` | `pipeline` (e.g. `InterPro2GO`, `ARBA`, `UniRule`), `refs` (rule or mapping ids) | `rules/arba/`, `rules/unirule/`, InterPro2GO discussions in reviews |
| `other` | `description` | practices and workflows |

Every kind may also carry `description` (Markdown) and `refs` (CURIEs or URLs).

## Rules

1. **Copy identifiers, never type them.** For annotation subjects, generate the subject with:

   ```bash
   uv run go-cdr aigr-example <review path> --aigr-root <AIGR> --commit <COMMIT>            # list rows
   uv run go-cdr aigr-example <review path> --index N --aigr-root <AIGR> --commit <COMMIT>  # draft one
   ```

   and paste its `subject` and `derived_from` unchanged (drop `aigr_review`, which is there for
   you to read). For other kinds, copy ids from the source file and pin `derived_from` to the
   same commit, with a `#L<line>` anchor where it helps. A term id in a `fix` must come from the
   source (e.g. the review's `proposed_replacement_terms`) with its label as written there.
2. **The record decides the verdict, not the AI review.** Read the record's Decision, Context and
   Application. A REMOVE or MODIFY in a review is NON_CONFORMANT only if the reason it gives is
   the record's reason; an ACCEPT is CONFORMANT only if the row is a case the record actually
   speaks to. If the review's reasoning contradicts the record, the example is either CONTESTED
   (and says so) or not an example.
3. **Explanations are attributed and specific.** Say what was judged and why, in two to five
   sentences, naming the evidence the review relied on ("The review found the IBA seeded only by
   …"). Do not claim more than the source says. Say "the review" for the AI Gene Review; never
   present its judgment as a consortium ruling.
4. **CONTESTED needs a real anchor.** Use `open_question: N` when the case bears on one of the
   record's own open questions, or `discussion:` with an issue or PR URL you have checked exists
   (`gh issue view <n> -R monarch-initiative/ai-gene-review`). Good contested cases: an `UNDECIDED`
   row the record does not settle, a row where two reviews or a reviewer and a curator disagreed,
   a case the record's open question names.
5. **Prefer variety.** Aim for at least one example per record where a good case exists, ideally
   one of each verdict, from different organisms and evidence codes. Two to three per record is
   plenty. A record with no honest example gets none: say so in your report.
6. **Use `see_also`** when a case also illustrates another record; put the example under the record
   it illustrates best.
7. Write only `*.examples.yaml` files in your chapters. Do not run `go-cdr build` and do not edit
   records. Check your files with `uv run go-cdr validate 2>&1 | grep -E 'records/(CH1|CH2)/'`; ignore
   "generated text is stale" lines (the coordinator rebuilds) and errors in other chapters.
