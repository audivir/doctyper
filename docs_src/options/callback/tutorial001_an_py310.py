from typing import Annotated

import doctyper

app = doctyper.Typer()


def name_callback(value: str):
    if value != "Camila":
        raise doctyper.BadParameter("Only Camila is allowed")
    return value


@app.command()
def main(name: Annotated[str | None, doctyper.Option(callback=name_callback)] = None):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
