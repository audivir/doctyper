import doctyper


def main(name: str = "World"):
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
