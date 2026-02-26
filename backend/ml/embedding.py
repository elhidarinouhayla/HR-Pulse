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


