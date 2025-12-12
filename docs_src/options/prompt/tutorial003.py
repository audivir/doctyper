import doctyper

app = doctyper.Typer()


@app.command()
def main(
    project_name: str = doctyper.Option(..., prompt=True, confirmation_prompt=True),
):
    print(f"Deleting project {project_name}")


if __name__ == "__main__":
    app()
