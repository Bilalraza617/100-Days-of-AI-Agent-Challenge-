# Day 5: Query-Answering Agent with RAG 🔍

## 📝 The Challenge

**Agent Type**: RAG | **Role**: Knowledge Assistant

**Build an agent that reads a knowledge base, embeds it, and answers questions grounded in those notes.**

In this challenge, you will create a Python script that reads notes from `notes.txt`, converts them into semantic embeddings, stores them, retrieves relevant notes based on a query, and uses an LLM to generate an answer.

## 🎯 Objectives

1. **Ingest Data**: Read notes from `notes.txt` (one note per line).
2. **Embed**: Use OpenAI's embedding model to convert notes into vectors.
3. **Store**: Save embeddings to `knowledge.json` for later retrieval.
4. **Retrieve**: When given a query, find the most semantically similar notes.
5. **Generate**: Send the retrieved notes to an LLM along with the query to generate an answer.

## 📂 Input Format (`notes.txt`)

One note per line. Example:

```
AI agents are autonomous systems that can plan, reason, and act toward goals.
Vector databases allow semantic search by storing embeddings instead of keywords.
RAG systems combine retrieval with generation to produce grounded responses.
```

## 💡 Hints

- Use cosine similarity to rank embeddings.
- Retrieve the top K (e.g., 3) most similar notes.
- Pass those notes to the LLM as context.
- The LLM should only use the provided notes to answer.

## 🏃 Run the Solution

```bash
python reference_solution.py
```
