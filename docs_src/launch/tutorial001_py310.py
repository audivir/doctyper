import doctyper

app = doctyper.Typer()


@app.command()
def main():
    print("Opening Typer's docs")
    doctyper.launch("https://typer.tiangolo.com")


if __name__ == "__main__":
    app()
