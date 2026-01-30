# Day 2: Email Summarization Agent 📧

## 📝 The Challenge
**Agent Type**: LLM-Based | **Role**: AI Assistant

**Build an AI Agent that reads an email and extracts the key info so you don't have to.**

In this challenge, you will step up from rule-based logic to **LLM-based intelligence**. You will use an LLM (like Gemini or OpenAI) to "read" a text file containing an email and output a structured summary.

## 🎯 Objectives
1.  **Ingest Data**: Read the content of `email.txt`.
2.  **Process with LLM**: Send the content to an AI model with a system prompt that asks for:
    -   A 2-3 sentence summary.
    -   Key points (bullet points).
    -   Action items (who needs to do what).
    -   Deadlines and Urgency.
3.  **Structured Output**:
    -   Parse the LLM's response into JSON.
    -   Save it to `summary.json`.
    -   (Optional) Generate a human-readable `summary.txt`.

## 📂 Input Format (`email.txt`)
A simple text file with an email body. Example:
```text
Subject: Project Timeline Update
Hi team,
The client has requested that the initial prototype be delivered by March 10...
```

## 🛠️ Required Libraries
You will likely need:
-   `openai` (compatible with Gemini) or `google-generativeai`
-   `python-dotenv` (to manage API keys securely)

## 💡 Hints
-   **System Prompt**: This is the most important part. You need to tell the AI *exactly* what schema to return. "Return ONLY valid JSON..." is a powerful instruction.
-   **JSON Parsing**: LLMs sometimes wrap code in \`\`\`json blocks. Make sure your code can handle that.

## 🏃 Run the Solution
If you get stuck, check `SOLUTION.md` for the logic breakdown or run the reference solution:
```bash
python reference_solution.py
```
