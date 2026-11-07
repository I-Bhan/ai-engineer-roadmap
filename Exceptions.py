
import json
from pathlib import Path

file = Path("invalid.json")
try:
    read2 = file.read_text(encoding="utf-8")
    text = json.loads(read2)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON format")
except PermissionError:
    print("Permission denied")

else:
    print(text)

finally:
    print("Document loading attempt finished.")