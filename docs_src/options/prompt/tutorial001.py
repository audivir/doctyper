import doctyper

app = doctyper.Typer()


@app.command()
def main(name: str, lastname: str = doctyper.Option(..., prompt=True)):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    app()
