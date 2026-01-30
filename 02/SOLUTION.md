# Day 2 Solution: Email Summarization Agent 🧠

This document provides a **line-by-line explanation** of the `reference_solution.py` code.

---

## 📝 Reasoning & Logic
Unlike Day 1 (Rule-Based), this agent uses a **Large Language Model (LLM)**.
1.  **Ingestion**: Reads raw text.
2.  **Prompting**: Instructs the LLM to extract specific fields.
3.  **Inference**: Generates structured JSON from unstructured text.
4.  **Parsing**: Converts the LLM output into a Python dictionary.

---

## 🔍 Code Breakdown

### 1. Imports & Setup
We use `openai` (which works with Gemini via Google's compatibility layer) and `dotenv` for security.
```python
import json
import os
from datetime import date
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Load env vars from .env
```

### 2. Client Initialization
We connect to the API using the key stored in our environment.
```python
api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
) 
```

### 3. The System Prompt (The "Brain")
This is the most critical part. We tell the AI **who it is** and **exactly what format** we wait.
```python
SYSTEM_PROMPT = """
You are an Email Summarization Agent.

Your job:
1. Summarize the email in 2–3 sentences
2. Extract key points
3. Extract action items (who should do what)
4. Identify deadlines
5. Classify urgency: Low, Medium, or High

Return ONLY valid JSON with this schema:
{ ... }
"""
```
**Why JSON?**
Using JSON allows us to reliably parse the answer in Python. If we just asked for a "summary", we couldn't easily separate the deadlines from the action items programmatically.

### 4. Reading Input
A simple helper to read the file.
```python
def read_email(path="email.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
```

### 5. calling the LLM
We send the `email_text` (User) and `SYSTEM_PROMPT` (System) to the model.
```python
def summarize_email(email_text):
    response = client.chat.completions.create(
        model="gemini-2.0-flash-exp",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": email_text}
        ],
        temperature=0.2 # Low temperature = More factual/consistent
    )
    return json.loads(response.choices[0].message.content)
```
*   `json.loads(...)`: This converts the string output (e.g., `"{ 'summary': ... }"`) into a real Python dictionary.

### 6. Saving Output
We save the data in two formats:
1.  **JSON**: For machines/databases.
2.  **TXT**: A pretty-printed report for humans.
```python
def save_outputs(data):
    # Save JSON
    with open("summary.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    # Save Human Report
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Email Summary ({date.today()})\n")
        # ... writing fields ...
```

---

## 🛡️ Edge Case Handling

1.  **Empty File**: If `email.txt` is empty, the LLM will hallucinate.
    *   *Fix*: Add `if not email_text: return` in `main()`.
2.  **Bad JSON**: If the LLM adds text before/after the JSON.
    *   *Fix*: Use a JSON repair library or a stricter prompt.
3.  **API Errors**: If the internet is down or key is invalid.
    *   *Fix*: Wrap `summarize_email` in a `try/except` block.

## 🚀 How to Run
```bash
python reference_solution.py
```
