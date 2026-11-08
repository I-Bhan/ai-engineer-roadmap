from pathlib import Path

def save_document(file,contents):
    file=Path(file)
    file.write_text(contents,encoding="utf-8")
    return file