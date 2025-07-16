import streamlit as st
from chatbot.retriever_chain import load_pdf, split_documents, setup_retriever, build_rag_chain
from dotenv import load_dotenv
import os

st.set_page_config(page_title="RAG PDF Q&A", layout="centered")
st.title("📄 PDF Q&A Chatbot using RAG")

# Initialize session state
if 'chain' not in st.session_state:
    st.session_state.chain = None

# Upload PDF in sidebar
uploaded_file = st.sidebar.file_uploader("Upload a PDF", type="pdf")
if uploaded_file:
    with open("data/test1.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.sidebar.success("PDF uploaded successfully!")

    # Run RAG pipeline
    with st.spinner("Processing PDF..."):
        docs = load_pdf("data/test1.pdf")
        parent_chunk, child_splitter = split_documents(docs)
        retriever = setup_retriever(parent_chunk, child_splitter)
        chain = build_rag_chain(retriever)
        st.session_state.chain = chain
    st.success("Ready to answer questions!")

# Question input
if st.session_state.chain:
    question = st.text_input("Ask a question about the document:")
    if question:
        with st.spinner("Thinking..."):
            response = st.session_state.chain.invoke(question)
        st.markdown(f"**Answer:** {response}")
