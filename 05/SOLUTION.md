# Day 5 Solution: Query-Answering Agent with RAG 🔍

This document explains the logic used in `reference_solution.py`.

## 📝 Reasoning & Logic

RAG (Retrieval-Augmented Generation) combines two steps:

1. **Retrieval**: Find relevant information from a knowledge base using embeddings.
2. **Generation**: Use an LLM to generate an answer grounded in the retrieved information.

## 🔍 Code Breakdown

### 1. Imports & Setup

The script uses NumPy for vector math and OpenAI for embeddings and chat.

```python
import json
import numpy as np
from openai import OpenAI
from datetime import date
```

### 2. Configuration

Define the embedding and chat models.

```python
EMBED_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4.1-mini"
```

### 3. Reading Notes

Notes are read from a text file, one per line.

```python
def read_notes(path="notes.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]
```

### 4. Embedding

Convert text into vectors using the embedding model.

```python
def embed_texts(texts):
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=texts
    )
    return [e.embedding for e in response.data]
```

### 5. Storing Knowledge

Store embeddings along with the original text.

```python
def store_knowledge(chunks, embeddings):
    records = []
    for text, emb in zip(chunks, embeddings):
        records.append({
            "text": text,
            "embedding": emb,
            "created": date.today().isoformat()
        })
    with open("knowledge.json", "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)
    return records
```

### 6. Cosine Similarity

Measure how similar two embeddings are.

```python
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

### 7. Retrieval

Find the top K most similar notes to a query.

```python
def retrieve(query, records, top_k=3):
    query_emb = embed_texts([query])[0]
    scored = []
    for r in records:
        score = cosine_similarity(query_emb, r["embedding"])
        scored.append((score, r["text"]))
    scored.sort(reverse=True)
    return [text for _, text in scored[:top_k]]
```

### 8. Generation

Use the LLM to answer the query based on retrieved notes.

```python
def answer_query(query, contexts):
    prompt = f"""
Answer the following question using ONLY the provided notes.
...
"""
    response = client.chat.completions.create(...)
    return response.choices[0].message.content
```

### 9. Main Workflow

1. Read and embed notes.
2. Store embeddings.
3. Prompt for a query.
4. Retrieve relevant notes.
5. Generate and display answer.

## 🚀 How to Run

```bash
python reference_solution.py
```
