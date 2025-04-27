import doctyper


def callback():
    print("Running a command")


app = doctyper.Typer(callback=callback)


@app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
