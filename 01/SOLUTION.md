# Day 1: Task Prioritization "Agent" - Solution

## 🧠 Step-by-Step Logic

The goal of this agent is to mimic a human project manager who looks at a list of tasks and decides what to do first. Here is the logic flow:

1.  **Input Parsing**:
    - The agent reads `tasks.csv` using Python's `csv` library.
    - It normalizes data (e.g., converts 'High', 'high', 'HIGH' to a standard integer score).
    - It parses natural dates (YYYY-MM-DD) into Python date objects.

2.  **Scoring Algorithm**:
    - We assign a numerical score to every task based on a weighted formula.
    - **Urgency (2.0x)**: How close is the deadline?
        - `Overdue` = Max score (5.0)
        - `Today` = Max score (5.0)
        - `Within 3 days` = High score (3.0)
        - `> 7 days` = Low score (1.0)
    - **Importance (3.0x)**: High (3), Medium (2), Low (1).
    - **Quick Win Bonus**: If a task takes <= 15 mins, we add a generic +1.0 point to encourage getting small things done.
    - **Blocked Penalty**: If `blocked=yes`, we subtract 5.0 points to ensure it doesn't appear in the "To Do" list.

3.  **Categorization**:
    - **TOP 3**: The highest scoring valid (unblocked) tasks.
    - **NEXT 5**: The next batch of tasks.
    - **UNBLOCK**: Any task marked as blocked.
    - **DEFER**: Tasks that are essentially "Low Urgency AND Low Importance".

4.  **Output Generation**:
    - The structured data is saved to `plan.json` for other agents/programs.
    - A human-readable summary is saved to `plan.txt`.

## 🤖 The "System Prompt" (Logic)

While this is a rule-based agent (no LLM), the "prompt" is effectively the scoring function:

```python
score = (WEIGHTS["urgency"] * urgency_score) + 
        (WEIGHTS["importance"] * impact_score) + 
        quickwin_bonus - 
        blocked_penalty
```

This formula dictates the agent's behavior. If you want the agent to value "Quick technical fixes" more, you would simply increase the `quickwin_bonus` weight.

## 📝 Code Snippets

### 1. Handling Fuzzy Effort Inputs
Humans enter effort in many ways ("15m", "L", "2h"). We normalize this:
```python
def parse_effort(s: str) -> int:
    # Handle T-shirt sizing
    if s.upper() in EFFORT_DEFAULTS_MIN:
        return EFFORT_DEFAULTS_MIN[s.upper()]
    
    # Handle "15m" or just "15"
    s = s.lower().replace("min", "").replace("m", "").strip()
    try:
        return int(s)
    except ValueError:
        return 45 # Default to Medium
```

### 2. The Decision Making (Reasoning)
The code generates a "reason" string so the user knows *why* a task was picked.
```python
def reason(task, breakdown):
    reasons = []
    if is_overdue(task): reasons.append("Overdue")
    if is_high_impact(task): reasons.append("High Impact")
    if is_quick_win(task): reasons.append("Quick Win")
    return ", ".join(reasons)
```

## ⚠️ Edge Case Handling

1.  **Missing Deadlines**: If a task has no deadline, we assign a low baseline urgency (0.5) so it doesn't get lost but isn't prioritized over urgent work.
2.  **Bad Data**: If a user enters "Huge" for effort (which isn't S/M/L) or a bad date, the system falls back to safe defaults (Medium effort, None date) rather than crashing.
3.  **Empty Files**: The script checks `if not tasks:` and prints a helpful message instead of crashing on an empty list processing.
