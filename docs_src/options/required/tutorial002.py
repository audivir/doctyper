import doctyper


def main(name: str, lastname: str = doctyper.Option(default=...)):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    doctyper.run(main)
