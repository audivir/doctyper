import subprocess
import sys

import doctyper
from doctyper.testing import CliRunner

from docs_src.arguments.optional import tutorial002 as mod

runner = CliRunner()

app = doctyper.Typer()
app.command()(mod.main)


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "[OPTIONS] [NAME]" in result.output


def test_call_no_arg():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Hello World!" in result.output


def test_call_arg():
    result = runner.invoke(app, ["Camila"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
