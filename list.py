documents = [
    "contract.pdf",
    "report.txt",
    "agreement.pdf"
]

while True:
    print(f"""
    ===== Document Queue Manager =====

    1. Add Document
    2. Remove Document
    3. Search Document
    4. Show All Documents
    5. Count Documents
    6. Exit""")
    choose=input("Choose an option:")
    match choose:
        case "1":
            new=str(input("Enter Document Name:"))
            if new in documents:
                print("Document already exists!")
            else:
                documents.append(new)
                print("Document added successfully!")
        case "2":
            remove=str(input("Enter Document Name:"))
            if remove in documents:
             documents.remove(remove)
            else:
                print("Document not found!")
        case "3":
            search = input("Enter Document Name:")
            if search in documents:
                print("Document found!")
                print(search)
            else:
                print("Document not found!")
        case "4":
            if len(documents)==0 :
                print("No documents found!")
            else:
                for i in documents:
                    print(i)
        case "5":
          print(len(documents))

        case "6":
            break
        case _:
            print("Invalid choice!")

