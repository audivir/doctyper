import doctyper


def main(
    fullname: str = doctyper.Option(
        "Wade Wilson", show_default="Deadpoolio the amazing's name"
    ),
):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    doctyper.run(main)
