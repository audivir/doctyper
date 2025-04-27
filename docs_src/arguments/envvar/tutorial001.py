import doctyper


def main(name: str = doctyper.Argument("World", envvar="AWESOME_NAME")):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    doctyper.run(main)
