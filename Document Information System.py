document_name=input("Please enter your document name:" )
num_pages=int(input("Enter number of pages:"))
file_size=float(input("Enter file size (MB):"))
processed = input("Is document processed? (y/n): ").lower() == "y"

if not (document_name.lower().endswith(".txt") or document_name.lower().endswith(".pdf" )):
    print(f"""
    Result: Rejected
    Reason: Unsupported file type""")
elif file_size > 10:
    print(f"""
    Result: Rejected
    Reason: File exceeds 10 MB 
    """)
elif file_size <= 0 :
    print(f"""
    Result: Rejected
    Reason: File size must be greater than 0
    """)
else:
    print(f"""
    Result: Accepted
    """)





print(f"""
    Your document name is: {document_name} 
    document pages: {num_pages}
    pages of size: {file_size} MB
    processed: {processed}""")