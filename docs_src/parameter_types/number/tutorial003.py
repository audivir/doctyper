import doctyper

app = doctyper.Typer()


@app.command()
def main(verbose: int = doctyper.Option(0, "--verbose", "-v", count=True)):
    print(f"Verbose level is {verbose}")


if __name__ == "__main__":
    app()
