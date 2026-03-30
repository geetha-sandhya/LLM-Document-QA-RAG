import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Page config
st.set_page_config(page_title="LLM Document Q&A", layout="wide")

# Title
st.markdown("""
# 🤖 LLM Document Q&A System (RAG)

### 🔍 Ask Questions from Your Documents using AI

Upload a PDF and ask questions.

---
""")

# Upload file
uploaded_file = st.file_uploader("📂 Upload your PDF document", type="pdf")

# Load model (only once)
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# Extract and clean text from PDF
def extract_text(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            page_text = page_text.replace("\n", " ")
            text += page_text + " "
    return text

# Split text into chunks
def split_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Main logic
if uploaded_file:

    st.success("📄 Document uploaded successfully!")

    with st.spinner("📄 Processing document..."):
        text = extract_text(uploaded_file)
        chunks = split_text(text)

        embeddings = model.encode(chunks)
        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(embeddings))

    st.success("✅ Document processed! Ask your question below.")

    query = st.text_input("💬 Enter your question:")

    if query:
        with st.spinner("🤖 Searching answer..."):

            query_embedding = model.encode([query])
            distances, indices = index.search(np.array(query_embedding), k=3)

            # Check if question is relevant
            if distances[0][0] > 1.5:
                st.warning("⚠️ This question is not related to the document. Please ask based on your PDF.")
            else:
                best_chunk = chunks[indices[0][0]]

                # Clean chunk text
                best_chunk = best_chunk.replace("\n", " ")
                best_chunk = best_chunk.replace("  ", " ")

                # Extract only first meaningful sentence
                sentences = best_chunk.split(". ")
                filtered = [s for s in sentences if len(s.strip()) > 20]

                clean_answer = filtered[0] if filtered else best_chunk

                st.markdown("### 🤖 AI Answer")
                st.info(clean_answer.strip())

# Footer
st.markdown("---")
st.markdown("⚡ Built as part of Machine Learning & Generative AI Project")