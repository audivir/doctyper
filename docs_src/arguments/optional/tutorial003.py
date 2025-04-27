import doctyper


def main(name: str = doctyper.Argument(default=...)):
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
