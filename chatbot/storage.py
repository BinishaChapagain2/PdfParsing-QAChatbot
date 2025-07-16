# storage.py

from langchain.vectorstores import Chroma
from chatbot.embedder import get_embedding_model

def get_vector_store(documents, embeddings, persist_directory):
    return Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_name="my_collection"
    )