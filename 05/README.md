# Day 5: Query-Answering Agent with RAG

Welcome to Day 5 of the **100 Days of Agentic AI Challenge**!

## 📌 Overview

**Agent Type**: 🤖 Retrieval-Augmented Generation (RAG)
**Role**: 🔍 Knowledge Assistant

In this challenge, you will build a **Query-Answering Agent** that reads a knowledge base (notes), embeds them semantically, and answers user questions using the most relevant notes.

## 🛠️ The Assignment

Your detailed instructions, requirements, and logic goals are in **[TASK.md](./TASK.md)**.
👉 **[Go to TASK.md to start the challenge!](./TASK.md)**

## 💡 Solution

Once you've tried it yourself (or if you get stuck), check out:

- **[SOLUTION.md](./SOLUTION.md)**: For the logic and reasoning.
- **[reference_solution.py](./reference_solution.py)**: For the working code.

## 🏃 Run the Solution

You can run the reference solution to generate embeddings and query the knowledge base:

```bash
python reference_solution.py
```

This will read `notes.txt`, generate embeddings, save them to `knowledge.json`, and prompt for a query.
