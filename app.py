import streamlit as st
import ollama
from utils import (
    extract_text_from_pdf,
    chunk_text,
    build_faiss_index,
    retrieve_top_chunks,
    generate_linkedin_summary,
    call_ollama
)

import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

text = ""


st.set_page_config(page_title="Ask Your Resume", layout="centered")
st.title("📄 Ask Your Resume – Powered by Ollama")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "index" not in st.session_state:
    st.session_state.index = None
if "chunks" not in st.session_state:
    st.session_state.chunks = None

# Upload and process file
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
if uploaded_file and st.session_state.index is None:
    with st.spinner("🔍 Extracting text from resume..."):
        text = extract_text_from_pdf(uploaded_file)
        if not text.strip():
            st.error("No readable text found in PDF.")
            st.stop()
        st.success("✅ Resume text extracted.")

    with st.spinner("📚 Chunking and indexing your resume..."):
        chunks = chunk_text(text)
        index, _ = build_faiss_index(chunks)
        st.session_state.chunks = chunks
        st.session_state.index = index
        st.success("✅ Resume indexed and ready!")

# Display chat history
for i, (q, a) in enumerate(st.session_state.chat_history):
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        st.markdown(a)

# Chat input
query = st.chat_input("💬 Ask something about your resume")
if query and st.session_state.index is not None:
    with st.chat_message("user"):
        st.markdown(query)

    with st.spinner("🤖 Thinking..."):
        try:
            top_chunks = retrieve_top_chunks(query, st.session_state.chunks, st.session_state.index)
            context = "\n\n".join(top_chunks)

            prompt = f"Based on the resume content below, answer the question:\n\n{context}\n\nQuestion: {query}"

            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response['message']['content']

            with st.chat_message("assistant"):
                st.markdown(answer)

            st.session_state.chat_history.append((query, answer))

        except Exception as e:
            st.error(f"Something went wrong with Ollama: {e}")



