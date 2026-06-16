import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="./memory_db"
)

collection = client.get_or_create_collection(
    name="user_memory"
)
def save_memory(text):

    chunks = create_chunks(text)

    for chunk in chunks:

        embedding = model.encode(
            chunk
        )

        collection.add(
            ids=[
                str(
                    collection.count()+1
                )
            ],
            documents=[
                chunk
            ],
            embeddings=[
                embedding.tolist()
            ]
        )
def retrieve_memory(query):

    if collection.count() == 0:
        return []

    query_embedding = model.encode(query)

    results = collection.query(
    query_embeddings=[
        query_embedding.tolist()
    ],
    n_results=5
    )

    print(results) 

    return results["documents"][0]
def create_chunks(
    text,
    chunk_size=150
):

    chunks = []

    for i in range(
        0,
        len(text),
        chunk_size
    ):

        chunks.append(
            text[i:i+chunk_size]
        )

    return chunks
def show_all_memories():
    return collection.get()["documents"]
