from typing import Annotated

import doctyper

app = doctyper.Typer()


@app.command()
def main(name: Annotated[str, doctyper.Argument(envvar="AWESOME_NAME")] = "World"):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    app()
