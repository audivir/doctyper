import doctyper


def main(config: doctyper.FileText = doctyper.Option(..., mode="a")):
    config.write("This is a single line\n")
    print("Config line written")


if __name__ == "__main__":
    doctyper.run(main)
