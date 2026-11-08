from processor import clean_text,count_words
from pathlib import Path
from reader import read_document
from storage import save_document
folder = Path("Documents/")
file= folder.glob("*.txt")
output=Path("processed/")
output.mkdir(parents=True, exist_ok=True)
processed_count=0
for fil in file:
    contents = read_document(fil)
    contents = clean_text(contents)
    count_contents = count_words(contents)
    saved_path=save_document( output / fil.name,contents)
    processed_count += 1
    print(contents)
    print(f"{fil.name}: {count_contents}")
    print(f"Saved: {saved_path}")
print(f"Total Files Processed: {processed_count}")
