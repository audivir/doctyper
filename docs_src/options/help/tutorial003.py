import doctyper

app = doctyper.Typer()


@app.command()
def main(fullname: str = doctyper.Option("Wade Wilson", show_default=False)):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    app()
