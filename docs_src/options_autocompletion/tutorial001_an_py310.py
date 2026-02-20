from typing import Annotated

import doctyper

app = doctyper.Typer()


@app.command()
def main(
    name: Annotated[str, doctyper.Option(help="The name to say hi to.")] = "World",
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
