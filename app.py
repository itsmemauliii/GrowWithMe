import streamlit as st
import openai
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

# Streamlit UI
st.set_page_config(page_title="Data Science Chatbot", layout="wide")
st.title("🤖 AI Chatbot for Data Science Queries")
st.write("Ask any questions related to Data Science, Machine Learning, and Coding!")

# Load and preprocess data (custom dataset for RAG)
data = """
Machine learning is a field of artificial intelligence that focuses on teaching computers to learn patterns from data.
Overfitting occurs when a model learns the training data too well and fails to generalize to unseen data.
Python is a widely used programming language for data science due to its rich ecosystem of libraries.
Pandas is used for data manipulation, while Matplotlib and Seaborn are used for data visualization.
"""
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
documents = text_splitter.split_text(data)

# Create FAISS Vector Store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_texts(documents, embeddings)

# Create chatbot with memory
llm = ChatOpenAI(model_name="gpt-4")
retriever = vector_store.as_retriever()
memory = ConversationBufferMemory(memory_key="chat_history")

qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

# Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me anything about Data Science...")
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    response = qa_chain.run({"question": user_input, "chat_history": st.session_state.messages})

    with st.chat_message("assistant"):
        st.markdown(response)

    # Store messages in session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": response})
