import re
from typing import Literal

import doctyper
import pytest
from doctyper.testing import CliRunner

runner = CliRunner()


def test_slim_typer():
    app = doctyper.SlimTyper()

    assert isinstance(app, doctyper.Typer)
    assert not app.pretty_exceptions_enable
    assert not app._add_completion


def test_doc_argument():
    app = doctyper.SlimTyper()

    @app.command()
    def main(arg: str):
        """Docstring.

        Args:
            arg: String Argument.
        """

    result = runner.invoke(app, ["--help"])
    assert re.search(r"arg\s+TEXT\s+String Argument\. \[required\]", result.stdout)


def test_doc_option():
    app = doctyper.SlimTyper()

    @app.command()
    def main(opt: str = 1):
        """Docstring.

        Args:
            opt: String Option with Default.
        """

    result = runner.invoke(app, ["--help"])
    assert re.search(
        r"--opt\s+TEXT\s+String Option with Default\. \[default: 1\]", result.stdout
    )


def test_doc_flag():
    app = doctyper.SlimTyper()

    @app.command()
    def main(flag: bool = True):
        """Docstring.

        Args:
            flag: Boolean Flag with Default.
        """

    result = runner.invoke(app, ["--help"])
    assert re.search(
        r"--flag\s+--no-flag\s+Boolean Flag with Default\. \[default: flag\]",
        result.stdout,
    )


def test_choices_help():
    app = doctyper.SlimTyper()

    @app.command()
    def main(choice: Literal["a", "b"]):
        """Docstring.

        Args:
            choice: The valid choices.
        """

    result = runner.invoke(app, ["--help"])
    assert re.search(
        r"choice\s+CHOICE:\{a\|b\}\s+The valid choices\. \[required\]",
        result.stdout,
    )


def test_choices_non_string():
    app = doctyper.SlimTyper()

    @app.command()
    def main(choice: Literal[1, 2]): ...

    with pytest.raises(TypeError, match="Literal values must be strings"):
        runner.invoke(app, ["--help"])


def test_choices_valid_value():
    app = doctyper.SlimTyper()

    @app.command()
    def main(choice: Literal["a", "b"]):
        print("The choice was", choice)

    result = runner.invoke(app, ["b"])
    assert result.exit_code == 0
    assert "The choice was b" in result.stdout


def test_choices_invalid_value():
    app = doctyper.SlimTyper()

    @app.command()
    def main(choice: Literal["a", "b"]): ...

    result = runner.invoke(app, ["c"])
    assert result.exit_code == 2
    assert (
        "Invalid value for 'CHOICE:{a|b}': 'c' is not one of 'a', 'b'." in result.stdout
    )
