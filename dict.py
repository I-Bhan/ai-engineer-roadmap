documents = [
    {
        "id": 1,
        "name": "contract.pdf",
        "pages": 12,
        "status": "processed"
    },
    {
        "id": 2,
        "name": "report.txt",
        "pages": 5,
        "status": "pending"
    },
    {
        "id": 3,
        "name": "agreement.pdf",
        "pages": 8,
        "status": "pending"
    }
]

while True:
    print(f"""===== Document Metadata Manager =====

            1. Add Document
            2. Search Document
            3. Update Document Status
            4. Delete Document
            5. Show All Documents
            6. Exit""")
    index = input("Choose an option:")
    id_exists=False
    match index:
        case "1":
            id_5=int(input("Enter document id :"))
            name=str(input("Enter document name:"))
            pages=int(input("Enter document pages:"))
            for document in documents:
                if document["id"] == id_5:
                 id_exists=True
                 break
            if id_exists:
                print("Document id is already in database")
            else:
                 documents.append({"id": id_5, "name": name, "pages": pages, "status": "pending"})



        case "2":
            id_2=int(input("Enter document id :"))
            for document in documents:
                 if document["id"] == id_2:
                   print(document["name"])
                   break
            else:
                print("Document not found!")
                

        case "3":
            id_1=int(input("Enter document id :"))
            for document in documents:
                if document["id"] == id_1:
                    document["status"] = "processed"
                    print(document["status"])
                    break
        case "4":
            id_3=int(input("Enter document id :"))
            for document in documents:
                if document["id"] == id_3:
                    documents.remove(document)



        case "5":
            for document in documents:
                print(document)
        case "6":
            break
        case _:
            print("Invalid option")




