from typing import List

import doctyper

valid_completion_items = [
    ("Camila", "The reader of books."),
    ("Carlos", "The writer of scripts."),
    ("Sebastian", "The type hints guy."),
]


def complete_name(ctx: doctyper.Context, incomplete: str):
    names = ctx.params.get("name") or []
    for name, help_text in valid_completion_items:
        if name.startswith(incomplete) and name not in names:
            yield (name, help_text)


app = doctyper.Typer()


@app.command()
def main(
    name: List[str] = doctyper.Option(
        ["World"], help="The name to say hi to.", autocompletion=complete_name
    ),
):
    for n in name:
        print(f"Hello {n}")


if __name__ == "__main__":
    app()
