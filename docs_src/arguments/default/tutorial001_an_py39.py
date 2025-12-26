from typing import Annotated

import doctyper

app = doctyper.Typer()


@app.command()
def main(name: Annotated[str, doctyper.Argument()] = "Wade Wilson"):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
