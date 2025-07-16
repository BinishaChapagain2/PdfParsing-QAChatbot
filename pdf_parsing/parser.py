from langchain_community.document_loaders import UnstructuredPDFLoader

def load_pdf(path: str):
    loader = UnstructuredPDFLoader(path, mode="paged", strategy='auto', encoding='utf-8')
    docs = loader.load()
    return docs