import doctyper

app = doctyper.Typer()


@app.command()
def main(
    name: str = doctyper.Option(..., "--name", "-n"),
    formal: bool = doctyper.Option(False, "--formal", "-f"),
):
    if formal:
        print(f"Good day Ms. {name}.")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    app()
