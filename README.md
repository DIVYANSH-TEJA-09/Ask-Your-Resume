# Ask-Your-Resume
**Ask Your Resume** is an AI-powered web app that allows you to interact with your resume using natural language queries. Built with Streamlit, FAISS, and Ollama, it transforms your static resume into an intelligent, searchable chatbot powered by local LLMs.
---
## ✨ Features
- Upload your resume in `.pdf` format.
  <p align='center'>
    <img src="images/Interface_Resume.png",alt='upload' width=600>
  </p>
- Extracts and chunks resume text for better searchability.
  <p align='center'>
    <img src="images/Upload_Resume.png",alt='chunking' width=600>
  </p>
- Uses FAISS for semantic similarity search.
- Local language generation with **LLaMA 3 via Ollama**.
- Ask questions like:
  - "What are my technical skills?"
  - "Where did I intern?"
  - "List my certifications."
- 🔁 Maintains chat session state (ask follow-ups).

  ---
## 🧠 How It Works

1. **Upload Resume**: Choose your `.pdf` resume file.
2. **Text Extraction**: Extracts readable text using `pdfplumber` or `PyMuPDF`.
3. **Chunking & Embedding**: Splits content into smaller parts and embeds with sentence transformers.
4. **Vector Indexing**: Uses FAISS to store and search vectorized resume chunks.
5. **Natural Language Query**: Your question + context → LLaMA 3 via `ollama`.
6. **Response Generation**: Returns a context-aware answer.
   <p align='center'>
    <img src="images/Thinking.png",alt='thinks' width=600>
  </p>
  <br>  
  <br>  
  <p align='center'>
    <img src="images/Reply.png",alt='response1' width=600>
  </p>
<br>
<br>
<p align='center'>
    <img src="images/reply2.png",alt='response2' width=600>
  </p>  


## 📦 Tech Stack

1. Frontend: Streamlit
2. Backend     : Python, Ollama (LLaMA3)
3. NLP Engine  : Retrieval-Augmented Generation (RAG)
4. Embeddings  : Sentence Transformers or Gemini-compatible
5. Search Index: FAISS
6.   PDF Parsing:pdfplumber

## 📁 Project Structure
Ask your Resume
- app.py
- utils.py
- requirements.txt
- README.md
- resumes
    - sample resumes

## 🛠 Installation & Setup
Step 1: Clone the repo (run in terminal)
<br>
<br>
git clone  https://github.com/DIVYANSH-TEJA-09/Ask-Your-Resume  
cd ask-your-resume
<br>
<br>
Step 2: Create a virtual environment
<br>
<br>
python -m venv .venv  
source .venv/bin/activate    # macOS/Linux  
.venv\Scripts\activate       # Windows  
<br>
<br>  
Step 3: Install Python dependencies  
<br>
<br>
pip install -r requirements.txt
<br>
<br>
## 🦙 How to Install Ollama & LLaMA 3
Step 4: Install Ollama
- Visit https://ollama.com and download the app for your OS:

- macOS: brew install ollama

- Windows: Download the installer from the website

- Linux:(run)
  <br>
  <br>
  curl -fsSL https://ollama.com/install.sh | sh
  <br>
  <br>
  - Then run the Ollama server:
  <br>
  <br>
  ollama serve
<br>
<br>
Step 5: Download and Run LLaMA 3
To download and run the LLaMA 3 model:
<br>
<br>
ollama run llama3
<br>
<br>
Wait for it to pull the model (~4–8GB depending on the version). Once downloaded, Ollama will keep the model ready for all future use.
## Sample Questions to Ask
- What tools do I know?

- Where did I intern?

- List my certifications.

- What's my academic background?

- Generate a LinkedIn-style summary.

- Compare with a reference resume.



