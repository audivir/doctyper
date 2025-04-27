from typing import Optional

import doctyper
import pytest
from doctyper.testing import CliRunner

runner = CliRunner()


def test_deprecation():
    app = doctyper.Typer()

    def add_command():
        @app.command()
        def cmd(
            opt: Optional[float] = doctyper.Option(
                3.14,
                is_flag=True,
                flag_value="42",
                help="Some wonderful number",
            ),
        ): ...  # pragma: no cover

    with pytest.warns(
        match="The 'is_flag' and 'flag_value' parameters are not supported by Typer"
    ):
        add_command()
