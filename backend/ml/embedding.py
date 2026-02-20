from sentence_transformers import SentenceTransformer
import numpy as np
import chromadb
from chromadb.config import Settings



def load_embedding_model():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model



def generate_embedding(model, texts):

    return model.encode(texts)




def normalize_embeddings(embeddings):

    embeddings_nor = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    return embeddings_nor



def save_chroma(
          df,
    texts,
    embeddings,
    ids,
    collection_name="job_descriptions",
    persist_directory="../data/chromadb/chroma_db"
):
    
    client = chromadb.Client(
        Settings(
            persist_directory=persist_directory,
            anonymized_telemetry=False
        )
    )

    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}
    )

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=df.to_dict(orient="records")
    )

    client.persist()

   
