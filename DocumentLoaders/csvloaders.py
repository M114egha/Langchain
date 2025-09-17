from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("sample.csv") 

data = loader.load()

print(f"Type of data object: {type(data)}")
print(f"Number of rows: {len(data)}\n")


for i , row in  enumerate(data):
    print("row+1")
    print("row.page_content")
