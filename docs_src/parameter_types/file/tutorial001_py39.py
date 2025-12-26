import doctyper

app = doctyper.Typer()


@app.command()
def main(config: doctyper.FileText = doctyper.Option(...)):
    for line in config:
        print(f"Config line: {line}")


if __name__ == "__main__":
    app()
