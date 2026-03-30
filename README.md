# 🤖 LLM Document Q&A System (RAG)

An AI-powered application that allows users to upload PDF documents and ask questions based on their content using Retrieval-Augmented Generation (RAG).

---

## 📌 Project Overview

This project demonstrates how to build an end-to-end **Generative AI application** using:

- Natural Language Processing (NLP)
- Embedding Models
- Vector Databases (FAISS)
- Semantic Search

The system extracts text from uploaded PDF documents, processes it into smaller chunks, and retrieves the most relevant information to answer user queries.

---

## 🚀 Features

- 📂 Upload any PDF document  
- 📄 Automatic text extraction  
- ✂️ Intelligent text chunking  
- 🔍 Semantic search using embeddings  
- ⚡ Fast similarity search using FAISS  
- 🤖 Context-based question answering  
- ⚠️ Detects unrelated questions  
- 🎯 Clean and concise answers  

---

## 🏗️ Architecture

The system follows a **Retrieval-Augmented Generation (RAG)** pipeline:

1. **Document Ingestion**
   - Upload PDF
   - Extract raw text using PyPDF

2. **Text Processing**
   - Clean text (remove noise, newlines)
   - Split into smaller chunks

3. **Embedding Generation**
   - Convert text chunks into vectors using Sentence Transformers

4. **Vector Storage**
   - Store embeddings in FAISS index for fast retrieval

5. **Query Processing**
   - Convert user query into embedding
   - Find most similar document chunks

6. **Answer Generation**
   - Extract relevant sentence from retrieved chunk
   - Return concise answer

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Frontend/UI:** Streamlit  
- **NLP Model:** Sentence Transformers (`all-MiniLM-L6-v2`)  
- **Vector Database:** FAISS  
- **PDF Processing:** PyPDF  
- **Libraries:** NumPy  

---

## 📂 Project Structure
LLM-Document-QA-RAG/
│── app.py
│── requirements.txt
│── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
git clone https://github.com/geetha-sandhya/LLM-Document-QA-RAG.git

cd LLM-Document-QA-RAG

---

### 2️⃣ Install dependencies
pip install -r requirements.txt

---

### 3️⃣ Run the application
streamlit run app.py

---

## 💡 Example Use Case

- Students can quickly understand concepts from notes  
- Professionals can extract insights from reports  
- Researchers can query large documents easily  

---

## ⚠️ Limitations

- Answers depend on document quality  
- PDF text extraction may introduce minor noise  
- Not a fully generative model (retrieval-based system)  

---

## 🔮 Future Improvements

- Integrate Large Language Models (LLMs) for better answers  
- Improve text cleaning and preprocessing  
- Add support for multiple documents  
- Deploy as a web application  

---

## 👩‍💻 Author

**Geetha Sandhya**  
B.Tech (3rd Year)  
Aspiring Machine Learning Engineer  

---

## ⭐ Conclusion

This project demonstrates practical implementation of:
- Machine Learning concepts  
- NLP techniques  
- Generative AI workflows  

It showcases the ability to build scalable AI solutions combining **data processing, embeddings, and retrieval systems**.

---