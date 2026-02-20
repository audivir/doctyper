import doctyper

app = doctyper.Typer()


@app.command()
def main(
    name: str,
    password: str = doctyper.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    ),
):
    print(f"Hello {name}. Doing something very secure with password.")
    print(f"...just kidding, here it is, very insecure: {password}")


if __name__ == "__main__":
    app()
