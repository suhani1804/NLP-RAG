# ⚡ Smart Grid NLP RAG System

## 🚀 Overview

This project implements a **production-oriented NLP pipeline with Retrieval-Augmented Generation (RAG)** to analyze smart grid data (logs, incidents) and answer domain-specific queries.

It combines **modern NLP research concepts** with a lightweight, scalable architecture.

---

## 🧠 Key Features

* 🔍 Semantic Search using **MiniLM embeddings**
* 📊 Efficient retrieval with **FAISS vector database**
* 🧩 Advanced re-ranking using **MMR (Maximal Marginal Relevance)**
* 🤖 Context-aware answer generation using **LLM (OpenAI)**
* ⚙️ Synthetic **smart grid dataset generator**
* 📈 Evaluation metrics (Precision@K, MRR, Faithfulness)

---

## 🏗️ Architecture

```
User Query
   ↓
Embedding (MiniLM)
   ↓
FAISS Vector Search (Top-K)
   ↓
MMR Re-ranking
   ↓
Context Selection
   ↓
LLM (RAG)
   ↓
Final Answer
```

---

## 📁 Project Structure

```
smart-grid-rag/
│
├── app.py              # CLI entrypoint
├── rag_core.py         # NLP + retrieval logic
├── llm.py              # LLM interaction
├── evaluator.py        # evaluation metrics
├── data_generator.py   # synthetic dataset generator
├── config.py
├── data/
└── requirements.txt
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup

Set your OpenAI API key:

```bash
export OPENAI_API_KEY=your_api_key
```

Windows:

```bash
set OPENAI_API_KEY=your_api_key
```

---

## ▶️ Run the Project

```bash
python data_generator.py
python app.py
```

---

## 💡 Example Queries

* Why did transformer fail?
* What is voltage sag?
* How to fix overload?
* What causes breaker trip?

---

## 📊 Evaluation Metrics

* Precision@K
* Mean Reciprocal Rank (MRR)
* Faithfulness Score
* Custom RAG Score

---

## 🧪 Future Improvements

* API deployment (FastAPI)
* Web UI (Streamlit)
* Real-time data ingestion
* ColBERT-style token interaction

---

## 📌 Tech Stack

* Python
* sentence-transformers (MiniLM)
* FAISS
* OpenAI API

---

## 🤝 Contribution

Feel free to fork and enhance this project!

---
