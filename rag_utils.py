from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()
collection = client.create_collection("books")


def store_books(books):
    for book in books:
        embedding = model.encode(book.description).tolist()
        collection.add(
            documents=[book.description],
            embeddings=[embedding],
            ids=[str(book.id)]
        )


def query_books(question):
    query_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    return results['documents'][0]