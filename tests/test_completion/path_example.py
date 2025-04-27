from pathlib import Path

import doctyper

app = doctyper.Typer()


@app.command()
def f(p: Path):
    print(p)


if __name__ == "__main__":
    app()
