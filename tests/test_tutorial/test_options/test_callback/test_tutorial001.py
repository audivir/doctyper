import subprocess
import sys

import doctyper
from doctyper.testing import CliRunner

from docs_src.options.callback import tutorial001 as mod

runner = CliRunner()

app = doctyper.Typer()
app.command()(mod.main)


def test_1():
    result = runner.invoke(app, ["--name", "Camila"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.output


def test_2():
    result = runner.invoke(app, ["--name", "rick"])
    assert result.exit_code != 0
    assert "Invalid value for '--name'" in result.output
    assert "Only Camila is allowed" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
