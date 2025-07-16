# 📄 PDF Parsing & Chatbot Project

A modular project to **parse PDF documents**, embed them, and interact with the content via a **question-answering chatbot**.

---

## 📁 Folder Structure

```
PdfParsing-QAChatbot/
│
├── .env                         # Gemini API key
├── test1.pdf                    # Sample PDF
├── requirements.txt             # Python dependencies
├── README.md                    # Documentation
│
├── chroma_db/                   # Chroma vector DB (auto-generated)
├── data/                        # Uploaded or parsed PDF files
├── outputs/                     # Logs or results (optional)
│
├── pdf_parsing/
│   ├── __init__.py
│   └── parser.py                # Load and parse PDF documents
│
├── chatbot/
│   ├── __init__.py
│   ├── splitter.py
│   ├── embedder.py
│   ├── storage.py
│   ├── prompt_template.py
│   ├── llm.py
│   └── retriever_chain.py
│
├── main.py     # Streamlit chatbot
```

└──

---

## ▶️ How to Run

### Streamlit App

```bash
streamlit run main.py
```

---

## ✨ Features

- Modular code: reusable components in `pdf_parsing/` and `chatbot/`
- Easy to plug in more LLMs
- ChromaDB vector store support
- Gemini 1.5 Flash integration
