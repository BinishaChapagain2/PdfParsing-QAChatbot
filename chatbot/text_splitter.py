# text_splitter.py

from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_text_splitters():
    child_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    parent_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return parent_splitter, child_splitter