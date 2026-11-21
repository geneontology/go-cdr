# GO Consortium Decision Records

default:
    @just --list

# Install dependencies
install:
    uv sync --all-extras

# Regenerate derived blocks in the records and the site data
build:
    uv run go-cdr build

# Check records and groups; add --check-terms to check GO labels (downloads GO)
[positional-arguments]
validate *ARGS:
    uv run go-cdr validate "$@"

# Run tests (including doctests), type checks and lint
test:
    uv run pytest
    uv run mypy src tests
    uv run ruff check src tests scripts

# Build, then serve the browser at http://127.0.0.1:8000/site/
serve port="8000": build
    uv run python -m http.server {{port}} --bind 127.0.0.1
