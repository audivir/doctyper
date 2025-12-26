import doctyper
from rich.prompt import Prompt

app = doctyper.Typer()


@app.command()
def main():
    name = Prompt.ask("Enter your name :sunglasses:")
    print(f"Hey there {name}!")


if __name__ == "__main__":
    app()
