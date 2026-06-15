# Day 4: Meeting Agenda Generator Agent 🗓️

## 📝 The Challenge
**Agent Type**: LLM-Based | **Role**: Meeting Facilitator

**Build an AI agent that reads meeting notes and generates a structured agenda.**

In this challenge, you will create a Python script that reads a meeting brief from `meeting.txt`, sends it to an LLM, and outputs a clear agenda.

## 🎯 Objectives
1. **Ingest Data**: Read the meeting brief from `meeting.txt`.
2. **Process with LLM**:
   - Generate a meeting title.
   - Extract the objective.
   - Allocate total duration and time for each agenda item.
   - Assign owners and expected outcomes.
3. **Output**:
   - Save structured results to `agenda.json`.
   - Save a human-readable agenda to `agenda.txt`.

## 📂 Input Format (`meeting.txt`)
Example format:
```
Meeting Title: Q1 Product Planning
Objective: Decide priorities for Q1 roadmap and align teams
Duration: 60 minutes
Meeting Type: decision
Participants: Product, Engineering, Marketing
Constraints: Must decide top 3 features
```

## 💡 Hints
- Keep the model prompt strict so the output is valid JSON.
- Use a low temperature for consistent results.
- Handle any extra output formatting from the model when parsing JSON.

## 🏃 Run the Solution
```bash
python reference_solution.py
```
