# prompt_template.py

from langchain_core.prompts import PromptTemplate

def get_prompt_template():
    return PromptTemplate(
        template="""
Use the following context to answer the question. 
If you don't know the answer, just say "I don't know"—don't try to make up an answer.

Context:
{context}

Question: {question}
Answer:
""",
        input_variables=["context", "question"]
    )