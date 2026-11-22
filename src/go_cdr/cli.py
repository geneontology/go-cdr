"""Command line for GO Consortium Decision Records: ``go-cdr build|validate|aigr-example``."""

from pathlib import Path
from typing import Optional

import typer
import yaml

from go_cdr.aigr import draft_example, find_rows
from go_cdr.records import build, validate

app = typer.Typer(help="GO Consortium Decision Records.", no_args_is_help=True)


@app.command("build")
def build_command(root: Path = typer.Option(Path("."), help="Repository root.")) -> None:
    """Regenerate derived blocks in the record files and the site data."""
    for path in build(root):
        typer.echo(f"updated {path}")


@app.command("validate")
def validate_command(
    root: Path = typer.Option(Path("."), help="Repository root."),
    check_terms: bool = typer.Option(False, help="Also check GO term labels against the GO build (needs oaklib)."),
) -> None:
    """Report schema errors, broken references and stale generated text."""
    errors = validate(root, check_terms=check_terms)
    for e in errors:
        typer.echo(e)
    if errors:
        raise typer.Exit(1)
    typer.echo("records OK")


@app.command("aigr-example")
def aigr_example_command(
    review: str = typer.Argument(..., help="Review file path relative to the ai-gene-review root."),
    index: Optional[int] = typer.Option(None, help="existing_annotations index; omit to list the rows."),
    term: Optional[str] = typer.Option(None, help="When listing, only rows for this GO term id."),
    aigr_root: Path = typer.Option(..., help="Root of an ai-gene-review checkout."),
    commit: str = typer.Option(..., help="ai-gene-review commit the checkout is at, for pinned links."),
) -> None:
    """Draft an example's subject and provenance from an AI Gene Review annotation row."""
    if index is None:
        for row in find_rows(aigr_root, review, term):
            typer.echo(f"{row['index']}\t{row['term']}\t{row['evidence']}\t{row['reference']}\t{row['action']}")
        return
    typer.echo(yaml.safe_dump(draft_example(aigr_root, review, index, commit), sort_keys=False, width=100))


if __name__ == "__main__":
    app()
