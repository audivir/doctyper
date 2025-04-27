import doctyper


def main():
    delete = doctyper.confirm("Are you sure you want to delete it?")
    if not delete:
        print("Not deleting")
        raise doctyper.Abort()
    print("Deleting it!")


if __name__ == "__main__":
    doctyper.run(main)
