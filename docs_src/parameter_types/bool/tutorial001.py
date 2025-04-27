import doctyper


def main(force: bool = doctyper.Option(False, "--force")):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    doctyper.run(main)
