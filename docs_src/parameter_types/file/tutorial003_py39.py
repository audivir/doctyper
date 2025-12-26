import doctyper

app = doctyper.Typer()


@app.command()
def main(file: doctyper.FileBinaryRead = doctyper.Option(...)):
    processed_total = 0
    for bytes_chunk in file:
        # Process the bytes in bytes_chunk
        processed_total += len(bytes_chunk)
        print(f"Processed bytes total: {processed_total}")


if __name__ == "__main__":
    app()
