# Day 4 Solution: Meeting Agenda Generator Agent 🗓️

This document explains the logic used in `reference_solution.py`.

## 📝 Reasoning & Logic
This is an LLM-based agent. The workflow is:
1. Read the meeting brief from `meeting.txt`.
2. Use a strict system prompt to ask the model for valid JSON.
3. Parse the JSON response.
4. Save both structured and readable outputs.

## 🔍 Code Breakdown

### 1. Imports & Setup
The script uses standard Python libraries plus the OpenAI client.
```python
import json
import os
from datetime import date
from openai import OpenAI
from dotenv import load_dotenv
```

### 2. Client Initialization
Load API keys from environment variables so credentials stay out of code.
```python
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
```

### 3. System Prompt
We define a precise prompt so the model returns exactly the JSON schema we expect.

### 4. Reading Input
The meeting brief is loaded from `meeting.txt`.

### 5. Calling the LLM
We send the system prompt and user meeting text to the model and parse the returned JSON.

### 6. Saving Output
The same data is written to:
- `agenda.json`
- `agenda.txt`

## 🚀 How to Run
```bash
python reference_solution.py
```
