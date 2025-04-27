import doctyper


def main(
    name: str = doctyper.Argument(
        "Wade Wilson", help="Who to greet", show_default="Deadpoolio the amazing's name"
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    doctyper.run(main)
