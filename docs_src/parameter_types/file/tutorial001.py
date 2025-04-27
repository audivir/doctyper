import doctyper


def main(config: doctyper.FileText = doctyper.Option(...)):
    for line in config:
        print(f"Config line: {line}")


if __name__ == "__main__":
    doctyper.run(main)
