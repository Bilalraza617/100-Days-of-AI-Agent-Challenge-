# Day 1: Task Prioritization Agent 📋

## 📝 The Challenge
**Agent Type**: Rule-Based | **Role**: Project Manager

**Build a Rule-Based "Agent" that organizes your messy to-do list.**

In this challenge, you will create a Python script that acts as a **Task Prioritization Agent**. It should read a list of tasks, understand their context (deadlines, difficulty, importance), and produce a clear, prioritized "Battle Plan" for the day.

## 🎯 Objectives
1.  **Ingest Data**: Read tasks from a CSV file (`tasks.csv`).
2.  **Analyze**:
    - Calculate a "priority score" for each task.
    - Weigh factors like **Deadlines** (Urgency) vs. **Impact** (Importance).
    - Identify "Quick Wins" (tasks < 15 mins).
    - Filter out "Blocked" tasks.
3.  **Output**:
    - Generate a `plan.txt` summary showing the **Top 3** tasks to focus on.
    - Generate a `plan.json` for potential future use.

## 📂 Input Format (`tasks.csv`)
Your script should expect a CSV with these columns:
- `title`: What is the task?
- `deadline`: YYYY-MM-DD
- `effort`: "S", "M", "L" OR minutes (e.g., "15m")
- `impact`: "low", "medium", "high"
- `blocked`: "yes"/"no"

## 💡 Hints
- You don't need an LLM for this! Simple `if/else` logic and weighting formulas are powerful forms of "Agentic" reasoning.
- Think about how *you* prioritize. Do you do the hardest thing first? Or the most urgent? Encapsulate that logic in code.

## 🏃 Run the Solution
If you get stuck, check `SOLUTION.md` for the logic breakdown or run the reference solution:
```bash
python reference_solution.py
```
