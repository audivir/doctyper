import subprocess
import sys
from pathlib import Path

import doctyper
from doctyper.testing import CliRunner

from docs_src.parameter_types.file import tutorial002_an as mod

runner = CliRunner()

app = doctyper.Typer()
app.command()(mod.main)


def test_main(tmpdir):
    config_file = Path(tmpdir) / "config.txt"
    if config_file.exists():  # pragma: no cover
        config_file.unlink()
    result = runner.invoke(app, ["--config", f"{config_file}"])
    text = config_file.read_text()
    config_file.unlink()
    assert result.exit_code == 0
    assert "Config written" in result.output
    assert "Some config written by the app" in text


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
