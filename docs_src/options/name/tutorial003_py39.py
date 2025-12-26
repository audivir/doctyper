import doctyper

app = doctyper.Typer()


@app.command()
def main(user_name: str = doctyper.Option(..., "-n")):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    app()
