import re
import sys
from typing import TYPE_CHECKING

import doctyper
import pytest
from doctyper._typing import Annotated, Literal, TypeAliasType
from doctyper.testing import CliRunner

if TYPE_CHECKING:
    from typing import Literal

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


@pytest.mark.skipif(sys.version_info < (3, 8), reason="Literal is not available")
def test_choices_typing_literal():
    from typing import Literal as _Literal

    app = doctyper.SlimTyper()

    @app.command()
    def main(choice: _Literal["a", "b"]): ...

    result = runner.invoke(app, ["--help"])
    assert re.search(
        r"choice\s+CHOICE:\{a\|b\}\s+\[default: None\] \[required\]",
        result.stdout,
    )


# TODO: why is there a default value?


def test_choices_typing_ext_literal():
    from typing_extensions import Literal as _Literal

    app = doctyper.SlimTyper()

    @app.command()
    def main(choice: _Literal["a", "b"]): ...

    result = runner.invoke(app, ["--help"])
    assert re.search(
        r"choice\s+CHOICE:\{a\|b\}\s+\[default: None\] \[required\]",
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


def test_future_annotations():
    app = doctyper.SlimTyper()

    @app.command()
    def main(
        opt: "str | None" = None,  # future annotation would convert str | None to "str | None"
    ):
        """Docstring.

        Args:
            opt: String Option with Default.
        """

    result = runner.invoke(app, ["--help"])
    assert re.search(
        r"--opt\s+TEXT\s+String Option with Default\. \[default: None\]", result.stdout
    )


def test_help_preference():
    app = doctyper.SlimTyper()

    @app.command()
    def main(
        doc_opt: Annotated[str, doctyper.Option()] = "string",
        ann_opt: Annotated[
            str, doctyper.Option(help="String Option with Annotated Help.")
        ] = "string",
    ):  # future annotation would convert str | None to "str | None"
        """Docstring.

        Args:
            doc_opt: String Option with Docstring Help.
            ann_opt: Not shown in help.
        """

    result = runner.invoke(app, ["--help"])
    assert re.search(
        r"--doc-opt\s+TEXT\s+String Option with Docstring Help\. \[default: string\]",
        result.stdout,
    )
    assert re.search(
        r"--ann-opt\s+TEXT\s+String Option with Annotated Help\. \[default: string\]",
        result.stdout,
    )


def test_custom_annotated():
    app = doctyper.SlimTyper()

    @app.command()
    def main(
        opt: Annotated["str | None", doctyper.Option(show_default="Custom")] = None,
    ):  # future annotation would convert str | None to "str | None"
        """Docstring.

        Args:
            opt: String Option with Custom Default.
        """

    result = runner.invoke(app, ["--help"])
    assert re.search(
        r"--opt\s+TEXT\s+String Option with Custom Default\. \[default: \(Custom\)\]",
        result.stdout,
    )


def test_type_alias():
    app = doctyper.SlimTyper()
    Alias = TypeAliasType("Alias", Literal["a", "b"])

    @app.command()
    def main(arg: Alias):
        """Docstring.

        Args:
            arg: Aliased argument.
        """

    # TODO: automatically use the aliased name as metavar?

    result = runner.invoke(app, ["--help"])
    assert re.search(
        r"arg\s+ARG:{a\|b}\s+Aliased argument\. \[required\]", result.stdout
    )
