import doctyper
from rich import print

app = doctyper.Typer()


@app.command()
def main():
    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


if __name__ == "__main__":
    app()
