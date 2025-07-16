# retriever_chain.py

from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain.vectorstores import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata
from chatbot.embedder import get_embedding_model
from chatbot.text_splitter import get_text_splitters
from chatbot.storage import get_vector_store
import os

def load_pdf(pdf_path):
    loader = UnstructuredPDFLoader(pdf_path, mode="paged", strategy='auto', encoding='utf-8')
    return loader.load()

def split_documents(docs):
    parent_splitter, child_splitter = get_text_splitters()
    parent_chunk = parent_splitter.split_documents(docs)
    return parent_chunk, child_splitter

def setup_retriever(parent_chunk, child_splitter, persist_directory="chroma_db"):
    store = InMemoryStore()
    
    # Child chunks
    child_docs = child_splitter.split_documents(parent_chunk)
    filtered_child_docs = filter_complex_metadata(child_docs)

    # Embedding model
    embeddings = get_embedding_model()

    # Vector store
    vector_store = get_vector_store(filtered_child_docs, embeddings, persist_directory)

    # Retriever
    retriever = ParentDocumentRetriever(
        vectorstore=vector_store,
        docstore=store,
        child_splitter=child_splitter,
    )

    # Add parent docs
    filtered_parent_chunk = filter_complex_metadata(parent_chunk)
    retriever.add_documents(filtered_parent_chunk)

    return retriever

def build_rag_chain(retriever):
    from chatbot.prompt_template import get_prompt_template
    from chatbot.llm import get_llm
    from langchain_core.output_parsers import StrOutputParser
    from langchain.schema.runnable import RunnableSequence

    prompt = get_prompt_template()

    # Model
    model = get_llm()

    parser = StrOutputParser()

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = RunnableSequence(
        {
            "context": retriever | format_docs,
            "question": lambda x: x
        },
        prompt,
        model,
        parser
    )
    return chain