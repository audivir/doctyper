import os
import subprocess
import sys

import doctyper
from doctyper.testing import CliRunner

from docs_src.options.callback import tutorial003 as mod

runner = CliRunner()

app = doctyper.Typer()
app.command()(mod.main)


def test_1():
    result = runner.invoke(app, ["--name", "Camila"])
    assert result.exit_code == 0
    assert "Validating name" in result.output
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


def test_completion():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL003.PY_COMPLETE": "complete_bash",
            "COMP_WORDS": "tutorial003.py --",
            "COMP_CWORD": "1",
        },
    )
    assert "--name" in result.stdout
