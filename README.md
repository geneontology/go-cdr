# GO Consortium Decision Records (go-cdr)

One record per decision of the Gene Ontology Consortium, in the manner of architecture
decision records (ADRs), with sign-off by the groups each decision applies to.

There are three kinds of record:

| Kind | Chapter | Signed off by |
|---|---|---|
| **Commitment**: an obligation of the memorandum of understanding (MOU) between GO Central and contributing groups | [`records/MOU`](records/MOU/README.md) | contributing groups |
| **Rubric**: a criterion annotation pipelines are judged by | [`records/PIPE`](records/PIPE/README.md) | pipelines |
| **Guideline**: how to annotate (16 chapters, 274 records) | e.g. [`records/MF`](records/MF/README.md) | contributing groups |

Everything is a **draft** (`status: proposed`). The guidelines were drafted by AI from an
inventory of about 22,000 GO wiki pages, Drive documents, GitHub issues and papers
([how](docs/origin.md), [inventory](sources/SOURCES.md)), and no curator has reviewed them
yet. The MOU records follow the October 2026 MOU draft; the rubrics follow the pipeline
rubrics proposed at the GOC meeting in Cambridge, 2025.

**The groups in [`groups/`](groups/README.md) are invented** (`demo: true`) to show how
sign-off works. Delete them before real sign-off begins.

## Layout

```
records/<CHAPTER>/README.md   chapter: what kind of records, who signs off (frontmatter: Chapter)
records/<CHAPTER>/<ID>.md     one record (frontmatter: Record)
groups/<GROUP>.yaml           a contributing group or pipeline and its sign-offs (Group)
src/go_cdr/schema/go_cdr.yaml LinkML schema for all three
site/index.html               static browser (reads site/data.js, built, not committed)
docs/origin.md                how the guidelines were drafted
sources/                      the source inventory behind the guidelines
scripts/migrate_from_aigr.py  one-off import from ai4curation/ai-gene-review
```

A record's body has three parts: **Decision**, **Context** (why) and **Application**
(worked examples). Its frontmatter holds the metadata: status, provenance (`GOC` restates
GOC guidance, `GOC_PLUS` sharpens it, `NEW` is new), requirement level for commitments and
rubrics, GO terms and evidence codes, related and superseding records, the checks that
enforce it, differences from prior guidance, open questions, sources and curator reviews.

## Working with records

```bash
just install      # uv sync
just build        # regenerate the derived blocks in records and site/data.js
just validate     # schema, cross-references, sign-off targets, stale text
just validate --check-terms   # also check GO ids and labels (downloads GO via oaklib)
just test         # pytest (with doctests), mypy, ruff
just serve        # build, then browse http://127.0.0.1:8000/site/
```

Edit the frontmatter, never the block between the `BEGIN GENERATED` and `END GENERATED`
markers; `just build` rewrites it, and `just validate` (run in CI) fails if it is stale.

To sign off, a group edits only its own `groups/<ID>.yaml`: each sign-off names a record
(`MOU-3`) or a whole chapter (`MOU`) and a status (`AGREED`, `DECLINED`, `NOT_APPLICABLE`,
`IN_PROGRESS`). A record-level sign-off overrides a chapter-level one.

## Examples

A record can have worked examples, in `records/<CHAPTER>/<ID>.examples.yaml` next to it. Each
example has a verdict: `CONFORMANT` (follows the record), `NON_CONFORMANT` (breaks it, with the
fix) or `CONTESTED` (disputed, linked to one of the record's open questions or to a discussion).
An example's subject is not always an annotation: it can be a GO-CAM, a protein family, a GO
term, a pipeline configuration or a described practice. The first examples were drafted from
[AI Gene Review](https://github.com/monarch-initiative/ai-gene-review) and link to the review they
came from; their verdicts are not yet reviewed by curators. See
[docs/examples-brief.md](docs/examples-brief.md) for how to write one, and
`go-cdr aigr-example` to copy an annotation's identifiers from a review file.

Examples serve a similar purpose to the cases in
[go-bench](https://github.com/ai4curation/go-bench) and are synced there by hand for now.

## Site

The browser filters records by kind, chapter, status, provenance, requirement level,
sign-off, aspect and evidence code, and shows a sign-off matrix per chapter and per group.
CI deploys it to GitHub Pages from `main`, at https://geneontology.github.io/go-cdr/.
Run `just serve` to browse a local build.

## License

Content is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), as
for other GO Consortium data.
