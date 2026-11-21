# Groups and sign-off

One YAML file per contributing group or pipeline (`groups/<ID>.yaml`, a `Group` in
`src/go_cdr/schema/go_cdr.yaml`). Each group edits only its own file.

A sign-off names a `target`, either one record (`MOU-3`) or a whole chapter (`MOU`), and a
`signoff_status`. (The values are not YES/NO because YAML reads those as booleans.)

| Status | Meaning |
|---|---|
| `AGREED` (yes) | The group agrees and complies. |
| `DECLINED` (no) | The group does not agree, or does not comply. |
| `NOT_APPLICABLE` | The record does not apply to the group's work. |
| `IN_PROGRESS` | The group agrees and is working towards compliance, or is still deciding. |

A record-level sign-off overrides the group's chapter-level one. A record with neither is
shown as "no response". A chapter's `applies_to` says which kind of group signs off on it:
contributing groups sign off on guidelines and the MOU, pipelines on the pipeline rubrics.

**Every group here is invented** (`demo: true`) to show how the site works. Delete them
before real sign-off begins; the real list of GO groups lives in
[go-site `metadata/groups.yaml`](https://github.com/geneontology/go-site/blob/master/metadata/groups.yaml).
