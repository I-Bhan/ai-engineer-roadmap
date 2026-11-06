from Toolkit import *
from pathlib import Path

folder = Path("Documents/")
file= folder.glob("*.txt")
output=Path("processed/")
output.mkdir(parents=True, exist_ok=True)
processed_count=0
for fil in file:
    contents = fil.read_text(encoding="utf-8")
    contents = clean_text(contents)
    count_contents = count_words(contents)
    output_file = output / fil.name
    output_file.write_text(contents,encoding="utf-8")
    processed_count += 1
    print(contents)
    print(f"{fil.name}: {count_contents}")
print(f"Total Files Processed: {processed_count}")
