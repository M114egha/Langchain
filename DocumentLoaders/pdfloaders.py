from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")

documents = loader.load()    
"""Each Document has -> .page_content → the text of that page
                        .metadata → page number, source, and other info"""

print(f"Type of documents: {type(documents)}")
print(f"Number of pages: {len(documents)}")


