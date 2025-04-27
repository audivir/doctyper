import doctyper


def main(username: str):
    if username == "root":
        print("The root user is reserved")
        raise doctyper.Abort()
    print(f"New user created: {username}")


if __name__ == "__main__":
    doctyper.run(main)
