import re
import typing
from collections.abc import Sequence
from enum import Enum
from typing import TYPE_CHECKING, Any

import pytest
import typer
import typing_extensions
from typer._typing import Annotated, Callable, Literal
from typer.testing import CliRunner

if TYPE_CHECKING:
    from typing import Literal

runner = CliRunner()


def assert_run(
    args: Sequence[str],
    code: int,
    expected: str,
    func: Callable[..., None],
    regex: bool = True,
    stderr: bool = False,
) -> None:
    app = typer.SlimTyper()
    app.command()(func)
    result = runner.invoke(app, args)
    output = result.output
    print(output)
    assert result.exit_code == code
    if regex:
        assert re.search(expected, output)
    else:
        assert expected in output


def assert_help(expected: str, func: Callable[..., None]) -> None:
    assert_run(["--help"], 0, expected, func)


def test_slim_typer():
    app = typer.SlimTyper()

    assert isinstance(app, typer.Typer)
    assert not app.pretty_exceptions_enable
    assert not app._add_completion


def test_doc_argument():
    def main(arg: str):
        """Docstring.

        Args:
            arg: String Argument.
        """

    assert_help(r"arg\s+TEXT\s+String Argument\. \[required\]", main)


def test_doc_option():
    def main(opt: str = 1):
        """Docstring.

        Args:
            opt: String Option with Default.
        """

    assert_help(r"--opt\s+TEXT\s+String Option with Default\. \[default: 1\]", main)


def test_doc_flag():
    def main(flag: bool = True):
        """Docstring.

        Args:
            flag: Boolean Flag with Default.
        """

    assert_help(
        r"--flag\s+--no-flag\s+Boolean Flag with Default\. \[default: flag\]",
        main,
    )


def test_choices_help():
    def main(choice: Literal["a", "b"]):
        """Docstring.

        Args:
            choice: The valid choices.
        """

    assert_help(r"choice\s+CHOICE:\{a\|b\}\s+The valid choices\. \[required\]", main)


def test_choices_valid_value():
    def main(choice: Literal["a", "b"]):
        print(f"The choice was {choice!r}")

    assert_run(["b"], 0, "The choice was 'b'", main, regex=False)


def test_choices_other_type():
    def main(choice: Literal[1, 2]):
        print(f"The choice was {choice!r}")

    assert_run(["2"], 0, "The choice was 2", main, regex=False)


def test_choices_invalid_value():
    app = typer.SlimTyper()

    @app.command()
    def main(choice: Literal["a", "b"]): ...

    assert_run(
        ["c"],
        2,
        "Invalid value for 'CHOICE:{a|b}': 'c' is not one of 'a', 'b'.",
        main,
        regex=False,
        stderr=True,
    )


def test_choices_help_list():
    def main(choice: list[Literal["a", "b"]]):
        """Docstring.

        Args:
            choice: The valid choices.
        """

    assert_help(
        r"choice\s+CHOICE:\{a\|b\}\.\.\.\s+The valid choices\. \[required\]", main
    )


def test_choices_help_tuple():
    def main(choice: tuple[Literal["a", "b"], int]):
        """Docstring.

        Args:
            choice: Tuple with 'a'/'b' and an int.
        """

    assert_help(
        r"choice\s+CHOICE\.\.\.\s+Tuple with 'a'/'b' and an int\. \[required\]", main
    )


def test_choices_union():
    def main(choice: 'Literal["a"] | Literal["b"]'):
        """Docstring.

        Args:
            choice: The valid choices.
        """

    assert_help(r"choice\s+CHOICE:\{a\|b\}\s+The valid choices\. \[required\]", main)


def test_choices_union_error():
    def main(choice: 'Literal["a"] | str'): ...

    with pytest.raises(
        AssertionError, match="Typer Currently doesn't support Union types"
    ):
        assert_help("", main)


def test_non_unique():
    def main(choice: Literal["1", 1]): ...

    with pytest.raises(ValueError, match="Literal values must be unique"):
        assert_help("", main)

    class OneEnum(Enum):
        ONE_STR = "1"
        ONE_INT = 1

    def main(choice: OneEnum): ...

    with pytest.raises(ValueError, match="Enum values must be unique"):
        assert_help("", main)


def test_choices_non_unique_case_dependent():
    def main(choice: Literal["a", "A"]): ...

    assert_help(r"choice\s+CHOICE:\{a\|A\}", main)

    def main(
        choice: Annotated[Literal["a", "A"], typer.Option(case_sensitive=False)],
    ): ...

    with pytest.raises(ValueError, match="Literal values must be unique"):
        assert_help("", main)

    class CaseEnum(Enum):
        A = "a"
        B = "A"

    def main(choice: CaseEnum): ...

    assert_help(r"choice\s+CHOICE:\{a\|A\}", main)

    def main(
        choice: Annotated[CaseEnum, typer.Option(case_sensitive=False)],
    ): ...

    with pytest.raises(ValueError, match="Enum values must be unique"):
        assert_help("", main)


def test_future_annotations():
    def main(
        opt: "str | None" = None,  # future annotation would convert str | None to "str | None"
    ): ...

    assert_help(r"--opt\s+TEXT\s+\[default: None\]", main)


def test_future_annotations_with_docstring():
    def main(
        opt: "str | None" = None,  # future annotation would convert str | None to "str | None"
    ):
        """Docstring.

        Args:
            opt: String Option with Default.
        """

    assert_help(r"--opt\s+TEXT\s+String Option with Default\. \[default: None\]", main)


def test_help_preference():
    def main(
        doc_opt: Annotated[str, typer.Option()] = "string",
        ann_opt: Annotated[
            str, typer.Option(help="String Option with Annotated Help.")
        ] = "string",
    ):  # future annotation would convert str | None to "str | None"
        """Docstring.

        Args:
            doc_opt: String Option with Docstring Help.
            ann_opt: Not shown in help.
        """

    assert_help(
        r"--doc-opt\s+TEXT\s+String Option with Docstring Help\. \[default: string\]",
        main,
    )
    assert_help(
        r"--ann-opt\s+TEXT\s+String Option with Annotated Help\. \[default: string\]",
        main,
    )


def test_custom_annotated():
    def main(
        opt: Annotated["str | None", typer.Option(show_default="Custom")] = None,
    ):  # future annotation would convert str | None to "str | None"
        """Docstring.

        Args:
            opt: String Option with Custom Default.
        """

    assert_help(
        r"--opt\s+TEXT\s+String Option with Custom Default\. \[default: \(Custom\)\]",
        main,
    )


@pytest.mark.parametrize(
    "type_",
    [
        pytest.param(
            typing_extensions.TypeAliasType, id="typing_extensions.TypeAliasType"
        ),
        pytest.param(
            getattr(typing, "TypeAliasType", None),
            marks=pytest.mark.skipif(
                not hasattr(typing, "TypeAliasType"),
                reason="TypeAliasType is not available",
            ),
            id="typing.TypeAliasType",
        ),
    ],
)
def test_typing_type_alias(type_: type[Any]):
    Alias = type_("Alias", Literal["a", "b"])

    def main(arg: Alias):
        """Docstring.

        Args:
            arg: Aliased argument.
        """

    assert_help(r"arg\s+ARG:{a\|b}\s+Aliased argument\. \[required\]", main)


def test_typing_annotated():
    def main(
        ann_arg: Annotated[str, typer.Argument(help="Annotated Argument.")],
    ): ...

    assert_help(
        r"ann_arg\s+TEXT\s+Annotated Argument\. \[required\]",
        main,
    )


def test_typing_literal():
    def main(choice: Literal["a", "b"]): ...  # noqa: F821

    assert_help(r"choice\s+CHOICE:\{a\|b\}\s+\[required\]", main)
