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
    embeddings,
    collection_name="job_descriptions",
    
):


    texts = df["Job Description"].fillna("").tolist()
    ids = [str(i) for i in df.index]

    
    client = chromadb.PersistentClient(
    path="../data/chromadb/chroma_db"
)
    

    collection = client.get_or_create_collection(
    name=collection_name
        )

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=df[['role', 'salary_clean', 'Rating', 'company_name', 'location', 'Headquarters', 'Size', 'founded', 'Type of ownership', 'Industry', 'Sector', 'revenue_clean', 'competitors']].to_dict(orient='records')
    )

    return client
