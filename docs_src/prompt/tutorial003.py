import doctyper


def main():
    delete = doctyper.confirm("Are you sure you want to delete it?", abort=True)
    print("Deleting it!")


if __name__ == "__main__":
    doctyper.run(main)
