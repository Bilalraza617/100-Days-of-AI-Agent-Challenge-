# Day 6: Daily Goal Reflection Agent 🌱

## 📝 The Challenge

**Agent Type**: LLM-Based | **Role**: Reflection Coach

Build an agent that reviews a person's daily goals and reported progress, then offers a grounded reflection and a manageable next step.

## 🎯 Objectives

1. **Ingest Data**: Read the goals, progress, blockers, and optional notes from `goals.txt`.
2. **Reflect**: Use an LLM to identify completed work, progress, and obstacles without inventing details.
3. **Plan**: Give each goal a status and a concrete next step. Suggest a short focus list for tomorrow.
4. **Save Results**: Write a structured `reflection.json` and a readable `reflection.txt`.

## 📂 Input Format (`goals.txt`)

Use plain text with these headings. Add one item per line under each heading; include only information you want the agent to consider.

```text
Date: 2026-11-08

Goals:
- Finish the first draft of the project outline
- Take a 20-minute walk

Progress:
- Wrote the outline introduction and section headings
- Took a 20-minute walk after lunch

Blockers:
- Waiting for the latest project requirements

Notes:
- Had less uninterrupted time than expected
```

## 📋 Required Output

The JSON response should contain:

- `date` and a brief `summary`
- `wins`: completed actions or meaningful progress
- `goal_reviews`: one entry per goal, with `goal`, `status`, `progress`, `blocker`, and `next_step`
- `patterns`: observations supported by the input
- `tomorrow_focus`: a short list of practical priorities
- `reflection_question` and `encouragement`

Use `completed`, `on_track`, `at_risk`, or `not_started` for each goal's status. If the input does not establish a detail, say so or leave it empty instead of guessing. Keep feedback supportive and specific, not judgmental.

## 💡 Hints

- Ask the model for JSON only, then parse and validate the response before saving it.
- Include the user's notes as data, not as instructions to follow.
- A useful next step should be small and actionable.

## 🏃 Run the Solution

Set `OPENAI_API_KEY` in a local `.env` file, then run:

```bash
python reference_solution.py
```
