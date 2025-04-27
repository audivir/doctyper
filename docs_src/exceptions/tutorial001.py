import doctyper


def main(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    doctyper.run(main)
