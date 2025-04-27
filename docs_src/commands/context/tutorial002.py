import doctyper

app = doctyper.Typer()


@app.command()
def create(username: str):
    print(f"Creating user: {username}")


@app.command()
def delete(username: str):
    print(f"Deleting user: {username}")


@app.callback(invoke_without_command=True)
def main():
    """
    Manage users in the awesome CLI app.
    """
    print("Initializing database")


if __name__ == "__main__":
    app()
