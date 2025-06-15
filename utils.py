# utils.py

import pdfplumber
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

def chunk_text(text, chunk_size=100):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def build_faiss_index(chunks):
    embeddings = embedder.encode(chunks).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embeddings

def retrieve_top_chunks(query, chunks, index):
    query_embedding = embedder.encode([query]).astype("float32")
    D, I = index.search(query_embedding, k=3)
    return [chunks[i] for i in I[0]]

from fpdf import FPDF



def call_ollama(prompt, model="llama3"):
    import ollama
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

def generate_linkedin_summary(resume_text: str, llm_callback) -> tuple[str, str]:
    import os

    prompt = (
        "You are a professional career advisor. Based on the following resume content, "
        "generate a concise, compelling LinkedIn-style summary:\n\n"
        f"{resume_text}"
    )

    summary = llm_callback(prompt)

    # Generate PDF from summary
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)

    output_path = os.path.join("outputs", "linkedin_summary.pdf")
    os.makedirs("outputs", exist_ok=True)
    pdf.output(output_path)

    return summary, output_path
