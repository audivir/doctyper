from typing import Annotated

import doctyper

app = doctyper.Typer()


@app.command()
def main(force: Annotated[bool, doctyper.Option("--force")] = False):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    app()
