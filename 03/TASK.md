# Day 3: Calendar Conflict Detection Agent 📅

## 📝 The Challenge

**Agent Type**: Rule-Based | **Role**: Calendar Manager

**Build a rule-based agent that scans a calendar and flags meeting conflicts.**

In this challenge, you will create a Python script that reads calendar events, compares their time ranges, and produces a clear conflict report.

## 🎯 Objectives

1.  **Ingest Data**: Read events from a CSV file (`calendar.csv`).
2.  **Analyze**:
    - Sort events by start time.
    - Detect overlapping events.
    - Detect events that are too close together with less than the buffer window.
    - Suggest a resolution based on priority and flexibility.
3.  **Output**:
    - Generate a `conflicts.json` file with structured results.
    - Generate a `conflicts.txt` summary for humans.

## 📂 Input Format (`calendar.csv`)

Your script should expect a CSV with these columns:

- `title`: Event name
- `start_time`: `YYYY-MM-DD HH:MM`
- `end_time`: `YYYY-MM-DD HH:MM`
- `priority`: `low`, `medium`, or `high`
- `type`: Event category such as `meeting`, `focus`, or `personal`
- `flexible`: `yes` or `no`

## 💡 Hints

- Compare each event with the next event after sorting by start time.
- Treat overlaps and missing buffer time as separate conflict types.
- Use flexibility and priority to decide which event should be moved first.

## 🏃 Run the Solution

If you get stuck, check `SOLUTION.md` for the logic breakdown or run the reference solution:

```bash
python reference_solution.py
```
