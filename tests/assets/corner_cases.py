import doctyper

app = doctyper.Typer()


@app.command(context_settings={"auto_envvar_prefix": "TEST"})
def main(
    name: str = doctyper.Option("John", hidden=True),
    lastname: str = doctyper.Option("Doe", "/lastname", show_default="Mr. Doe"),
    age: int = doctyper.Option(lambda: 42, show_default=True),
):
    """
    Say hello.
    """
    print(f"Hello {name} {lastname}, it seems you have {age}")


if __name__ == "__main__":
    app()
