from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key="YOUR_KEY")

texts = ["I love apples", "I eat oranges", "Physiscs is my favourite "]


vectors = [embeddings.embed_query(t) for t in texts]


db = FAISS.from_texts(texts, embeddings)


results = db.similarity_search("I like fruits", k=2)
print(results)
