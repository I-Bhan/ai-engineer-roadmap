import json
from pathlib import Path

file = Path("document.json")
read1=file.read_text(encoding="utf-8")
text=json.loads(read1)

text["status"]="reviewed"
text["reviewed_by"]="AI Engineer"
print(text)
file.write_text(json.dumps(text,indent=4))