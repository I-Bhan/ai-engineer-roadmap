import json
from pathlib import Path



documents = [
    {"id": 1, "name": "contract.txt", "status": "processed"},
    {"id": 2, "name": "report.txt", "status": "pending"},
    {"id": 3, "name": "notes.txt", "status": "pending"}
]

file = Path("documents.json")
readle=file.read_text(encoding="utf-8")
docu_loads=json.loads(readle)
print(docu_loads)
id_docu=int(input("Enter Document ID:"))
for doc in docu_loads:
    if doc["id"] == id_docu:
        doc["status"]="processed"
        file.write_text(json.dumps(docu_loads, indent=4))
        print("document found")
        print("Document Name:", doc["name"])
        print("Document Status:", doc["status"])
        break
else:
 print("Not found")
