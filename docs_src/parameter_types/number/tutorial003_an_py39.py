from typing import Annotated

import doctyper

app = doctyper.Typer()


@app.command()
def main(verbose: Annotated[int, doctyper.Option("--verbose", "-v", count=True)] = 0):
    print(f"Verbose level is {verbose}")


if __name__ == "__main__":
    app()
