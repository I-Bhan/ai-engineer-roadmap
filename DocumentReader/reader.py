from pathlib import Path


def read_document(file):
    file = Path(file)
    read2 = file.read_text(encoding="utf-8")

    return read2