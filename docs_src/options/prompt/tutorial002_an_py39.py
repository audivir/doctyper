from typing import Annotated

import doctyper

app = doctyper.Typer()


@app.command()
def main(
    name: str,
    lastname: Annotated[str, doctyper.Option(prompt="Please tell me your last name")],
):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    app()
