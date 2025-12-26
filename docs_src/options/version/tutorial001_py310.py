import doctyper

__version__ = "0.1.0"

app = doctyper.Typer()


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise doctyper.Exit()


@app.command()
def main(
    name: str = doctyper.Option("World"),
    version: bool | None = doctyper.Option(
        None, "--version", callback=version_callback
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
