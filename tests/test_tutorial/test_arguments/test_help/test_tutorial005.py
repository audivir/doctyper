import subprocess
import sys

import doctyper
from doctyper.testing import CliRunner

from docs_src.arguments.help import tutorial005 as mod

runner = CliRunner()

app = doctyper.Typer()
app.command()(mod.main)


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "[OPTIONS] [NAME]" in result.output
    assert "Arguments" in result.output
    assert "Who to greet" in result.output
    assert "[default: (Deadpoolio the amazing's name)]" in result.output


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
