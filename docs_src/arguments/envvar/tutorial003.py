import doctyper


def main(
    name: str = doctyper.Argument("World", envvar="AWESOME_NAME", show_envvar=False),
):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    doctyper.run(main)
