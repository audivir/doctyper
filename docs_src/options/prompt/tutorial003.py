import doctyper


def main(
    project_name: str = doctyper.Option(..., prompt=True, confirmation_prompt=True),
):
    print(f"Deleting project {project_name}")


if __name__ == "__main__":
    doctyper.run(main)
