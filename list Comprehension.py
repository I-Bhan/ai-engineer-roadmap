documents = [
    {"id": 1, "name": "contract.pdf", "pages": 12},
    {"id": 2, "name": "image.png", "pages": 1},
    {"id": 3, "name": "report.pdf", "pages": 25},
    {"id": 4, "name": "notes.txt", "pages": 3},
    {"id": 5, "name": "agreement.pdf", "pages": 8}
]


result = [document for document in documents if document["name"].endswith(".pdf")]
result_5 = [document for document in documents if document["pages"]>5]
result_all= [document["name"] for document in documents ]
result_12 = [document["name"] for document in documents if document["name"].endswith(".pdf") and document["pages"]>5]
print(result)
print(result_5)
print(result_all)
print(result_12)
