# 🎓 University FAQ Chatbot 
This Streamlit application is an AI-powered Campus Information Bot designed to provide students, faculty, and prospective applicants with instant, accurate university-related information. It automates the process of searching through 500+ pages of student handbooks, course catalogs, and campus policies, delivering reliable answers 24/7.

---

# 🚀 Features:
Research and retrieve course information, enrollment procedures, academic policies, housing details, financial aid, and campus facilities
Integrate academic calendar data and student services lookup for structured, real-time responses
Use semantic search with FAISS and HuggingFace embeddings for meaning-based question matching
Apply ScaleDown to compress university documentation by 75%, improving efficiency and reducing LLM token usage

---

# 🧠 Technologies Used

- Python
- Streamlit (Frontend UI)
- LangChain (RAG Pipeline)
- FAISS (Vector Database)
- HuggingFace Sentence Transformers (Embeddings)
- Groq LLaMA-3.1 Model (LLM)
- ScaleDown API (Context Compression)
- Pandas (CSV Data Processing)

---


# ⚙️ How to Get Started?

1. Clone the GitHub repository
```
git clone https://github.com/RuchitaGanguly/UniversityChatbot_IntelUnnati1.git
cd UniversityChatbot_IntelUnnati1
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Set up API Keys
Create a .env file and add:

GROQ_API_KEY

SCALEDOWN_API_KEY

4. Run the Streamlit App
```
streamlit run app.py
```
# 🤖 How it Works?

The Campus Information Bot consists of the following components:

Knowledge Base Builder
Processes 500+ university FAQs from CSV, generates semantic embeddings using HuggingFace, and stores them in a FAISS vector database.

Retriever + Compressor
Performs semantic search to find the most relevant FAQs and uses ScaleDown to compress context before sending it to the LLM.

Answer Generator
Uses Groq’s LLaMA-3.1 model to generate accurate, context-grounded responses strictly based on retrieved university data.

Streamlit Interface
Provides a clean chat interface for students to ask questions and receive instant 24/7 support.

