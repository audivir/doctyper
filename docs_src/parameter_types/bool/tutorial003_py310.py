import doctyper

app = doctyper.Typer()


@app.command()
def main(force: bool = doctyper.Option(False, "--force/--no-force", "-f/-F")):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    app()
