import doctyper


def main(user_name: str = doctyper.Option(..., "--name")):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    doctyper.run(main)
