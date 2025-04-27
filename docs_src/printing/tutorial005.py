import doctyper


def main(good: bool = True):
    message_start = "everything is "
    if good:
        ending = doctyper.style("good", fg=doctyper.colors.GREEN, bold=True)
    else:
        ending = doctyper.style("bad", fg=doctyper.colors.WHITE, bg=doctyper.colors.RED)
    message = message_start + ending
    doctyper.echo(message)


if __name__ == "__main__":
    doctyper.run(main)
