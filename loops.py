

documents = [
    "contract.pdf",
    "image.png",
    "report.txt",
    "notes.docx",
    "agreement.pdf",
    "photo.jpg"
]


while True:
    print(f"""
 1. Process Documents
 2. Exit""")
    number = int(input("Choose an option: "))
    if number == 1:
        ejected_count = 0
        accepted_count = 0
        for i in documents:
           if i.lower().endswith((".txt",".pdf")):
              accepted_count += 1
              print( i,"is Accepted ")
           else:
             ejected_count += 1
             continue


        print(f"""
        Total Accepted: {accepted_count} 
        Total Rejected: {ejected_count} """)
    if number==2:
     print("Goodbye")
     break







