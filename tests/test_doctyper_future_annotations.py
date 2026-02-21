from __future__ import annotations

import re

import typer
from typer.testing import CliRunner

runner = CliRunner()


def test_future_annotations():
    app = typer.Typer(show_none_defaults=True)

    @app.command()
    def main(opt: str | None = None): ...

    result = runner.invoke(app, ["--help"])
    assert re.search(r"--opt\s+TEXT\s+\[default: None\]", result.stdout)
