import doctyper


def main(in_prod: bool = doctyper.Option(True, " /--demo", " /-d")):
    if in_prod:
        print("Running in production")
    else:
        print("Running demo")


if __name__ == "__main__":
    doctyper.run(main)
