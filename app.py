import os
import streamlit as st
import requests
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# Page Configuration
st.set_page_config(page_title="University FAQ Chatbot 🎓")
st.title("🎓 University FAQ Chatbot")
 
# Load Environment Variables
load_dotenv()
SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")

# Load Vector Database (Cached)
@st.cache_resource
def load_vectorstore():
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    db = FAISS.load_local(
        "faiss_db",
        embedding,
        allow_dangerous_deserialization=True
    )
    return db

db = load_vectorstore()

# Load Groq LLM (Optimized)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    max_tokens=125,    
    temperature=0.2   
)

# Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
query = st.chat_input("Ask a question about university...")

if query:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    docs = db.similarity_search(query, k=2)
    context = "\n".join([doc.page_content for doc in docs])

    compressed_context = context

    if SCALEDOWN_API_KEY:
        try:
            headers = {
                "x-api-key": SCALEDOWN_API_KEY,
                "Content-Type": "application/json"
            }

            response = requests.post(
                "https://api.scaledown.xyz/compress/raw/",
                headers=headers,
                json={
                    "context": context,
                    "prompt": query,
                    "model": "llama-3.1-8b-instant",
                    "scaledown": {"rate": "auto"}
                },
                timeout=15
            )

            if response.status_code == 200:
                compressed_context = response.json().get(
                    "compressed_prompt", context
                )

        except Exception:
            compressed_context = context

    final_prompt = f"""
You are a university assistant.

Answer ONLY using the context.
If answer is not clearly found, say:
"Please contact the university office."

Keep answer under 5 lines.

Context:
{compressed_context}

Question: {query}
"""
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(final_prompt)
            bot_reply = response.content
            st.markdown(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )