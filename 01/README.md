# Task Prioritization Tool

A simple task manager that reads tasks from a CSV file, prioritizes them based on urgency, impact, and effort, and generates a structured plan in JSON and TXT formats.

## Features

- **Input**: Reads from `tasks.csv` (columns: title, description, deadline, effort, impact, blocked, tags).
- **Smart Scoring**: Calculates priority scores based on:
  - Urgency (deadline proximity)
  - Importance (low/medium/high)
  - Quick Wins (effort <= 15 mins)
  - Blocking Status (penalties for blocked tasks)
- **Categorization**:
  - **TOP 3**: Highest priority executable tasks.
  - **NEXT 5**: Subsequent high-priority tasks.
  - **UNBLOCK**: Tasks that are currently blocked.
  - **DEFER**: Low urgency and low impact tasks.
- **Output**: Generates `plan.json` (detailed machine-readable) and `plan.txt` (human-readable summary).

## Requirements

- Python 3.x

## Project Structure

- `agent.py`: Main logic script.
- `tasks.csv`: Input file containing your tasks.
- `plan.json`: Generated output (detailed).
- `plan.txt`: Generated output (summary).

## How to Use

1. **Prepare your tasks**: Create or edit `tasks.csv` with the following headers:
   `title,description,deadline,effort,impact,blocked,tags`

   Example content for `tasks.csv`:
   ```csv
   title,description,deadline,effort,impact,blocked,tags
   Fix bug,Urgent fix,2026-01-25,15,high,no,work
   Plan meeting,,2026-02-01,M,medium,yes,personal
   ```

2. **Run the script**:
   ```bash
   python agent.py
   ```

3. **View the results**: Check the console output or open `plan.txt` / `plan.json`.

## Configuration

You can tweak the scoring logic in `agent.py`:
- `EFFORT_DEFAULTS_MIN`: Definitions for S/M/L durations.
- `IMPACT_MAP`: Score values for low/medium/high.
- `WEIGHTS`: Multipliers for urgency, importance, etc.
