"""Command line for GO Consortium Decision Records: ``go-cdr build|validate``."""

from pathlib import Path

import typer

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


if __name__ == "__main__":
    app()
