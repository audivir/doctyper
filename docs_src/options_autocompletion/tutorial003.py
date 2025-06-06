import doctyper

valid_names = ["Camila", "Carlos", "Sebastian"]


def complete_name(incomplete: str):
    completion = []
    for name in valid_names:
        if name.startswith(incomplete):
            completion.append(name)
    return completion


app = doctyper.Typer()


@app.command()
def main(
    name: str = doctyper.Option(
        "World", help="The name to say hi to.", autocompletion=complete_name
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
