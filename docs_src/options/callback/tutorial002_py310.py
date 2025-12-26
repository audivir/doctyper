import doctyper

app = doctyper.Typer()


def name_callback(value: str):
    print("Validating name")
    if value != "Camila":
        raise doctyper.BadParameter("Only Camila is allowed")
    return value


@app.command()
def main(name: str | None = doctyper.Option(default=None, callback=name_callback)):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
