import doctyper


def main():
    person_name = doctyper.prompt("What's your name?")
    print(f"Hello {person_name}")


if __name__ == "__main__":
    doctyper.run(main)
