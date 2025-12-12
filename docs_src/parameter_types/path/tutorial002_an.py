from pathlib import Path

import doctyper
from typing_extensions import Annotated

app = doctyper.Typer()


@app.command()
def main(
    config: Annotated[
        Path,
        doctyper.Option(
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ],
):
    text = config.read_text()
    print(f"Config file contents: {text}")


if __name__ == "__main__":
    app()
