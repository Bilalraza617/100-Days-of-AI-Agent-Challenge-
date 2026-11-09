# Day 6 Solution: Daily Goal Reflection Agent 🌱

This guide explains the approach used in `reference_solution.py`.

## 🧠 Approach

The agent uses an LLM to turn a short daily log into a structured reflection. It keeps two responsibilities separate:

1. **Evidence**: The goals, progress, blockers, and notes supplied in `goals.txt`.
2. **Reflection**: A summary, goal statuses, and next steps grounded only in that evidence.

The prompt asks for a fixed JSON shape and explicitly prohibits inventing progress or causes. The script parses the model response, checks the required fields and status values, and only then saves the result.

## 🔍 Main Steps

### 1. Load configuration and input

`python-dotenv` loads `OPENAI_API_KEY` from `.env`. The script reads `goals.txt` as UTF-8 text and stops with a clear error if the file is missing, empty, or the API key is not set.

### 2. Request a structured reflection

The agent sends the log to `gpt-4.1-mini` using JSON response mode. Its response includes:

- A concise summary and wins
- A status and next step for every goal
- Evidence-based observations and suggested priorities
- A reflection question and supportive encouragement

### 3. Validate and save

The script checks that the response contains the expected fields, text lists, and allowed goal statuses. It writes the validated object to `reflection.json` and renders the same information as `reflection.txt`.

## 🔐 Setup

Create `.env` from `.env.example` and add your API key. Keep `.env` private; do not commit it.

Install dependencies if they are not already available:

```bash
uv pip install openai python-dotenv
```

## 🚀 Run

From the `06` directory:

```bash
python reference_solution.py
```

Edit `goals.txt` before each run. The two output files are generated in the same directory.
