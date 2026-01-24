# Day 1: Task Prioritization "Agent" - Detailed Solution

This document provides a **line-by-line explanation** of the `reference_solution.py` code.

---

### 1. Imports
We start by importing standard Python libraries needed for data handling.
```python
import csv
import json
import argparse
import sys
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Dict, Optional, Tuple
```
-   `csv`: Determines how to read the `tasks.csv` input file.
-   `json`: Used to save the output in a structured format (`plan.json`).
-   `argparse`, `sys`: Used for Command Line Interface (CLI) arguments and system exit codes.
-   `dataclasses`, `typing`, `datetime`: Modern Python features for type safety and clean data structures.

---

### 2. Configuration (The "Brain")
These constants define how the agent "thinks".
```python
EFFORT_DEFAULTS_MIN = {"S": 15, "M": 45, "L": 90}
IMPACT_MAP = {"low": 1, "medium": 2, "high": 3}

WEIGHTS = {
    "urgency": 2.0,
    "importance": 3.0,
    "quickwin_bonus": 1.0,
    "blocked_penalty": 5.0,
}
```
-   `EFFORT_DEFAULTS_MIN`: Converts T-shirt sizes (S/M/L) into minutes.
-   `WEIGHTS`: This is the most critical part. It tells the agent what is more important.
    -   `importance: 3.0` vs `urgency: 2.0`: This agent prefers Important tasks over Urgent ones.
    -   `blocked_penalty: 5.0`: A large penalty to ensure we don't pick blocked tasks.

---

### 3. Data Structure
We define a `Task` object to keep our code clean. Instead of dealing with raw dictionary keys like `row['title']`, we use `task.title`.
```python
@dataclass
class Task:
    title: str
    description: str
    deadline: Optional[date]
    effort_min: int
    impact: int
    blocked: bool
    tags: List[str]
```

---

### 4. Helper Functions (The Tools)

#### Parsing Dates
Converts string "2025-01-24" into a real Python date object. Handles errors gracefully.
```python
def parse_date(s: str) -> Optional[date]:
    s = (s or "").strip()
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None
```

#### Parsing Effort
Handles messy human input like "15m", "15", "M", or "Small".
```python
def parse_effort(s: str) -> int:
    s = (s or "").strip()
    if not s: return EFFORT_DEFAULTS_MIN["M"]
    
    # Handle S/M/L
    if s.upper() in EFFORT_DEFAULTS_MIN:
        return EFFORT_DEFAULTS_MIN[s.upper()]
        
    # Handle "15m" -> 15
    s = s.lower().replace("min", "").replace("m", "").strip()
    try:
        val = int(s)
        return max(5, val) # Minimum 5 minutes
    except ValueError:
        return EFFORT_DEFAULTS_MIN["M"] # Safe Fallback
```

---

### 5. Scoring Logic (The Core Algorithm)

#### Calculating Urgency
Returns a score from 0.0 to 5.0 based on how close the deadline is.
```python
def urgency_score(days_left: Optional[int]) -> float:
    if days_left is None: return 0.5   # No deadline = low urgency
    if days_left < 0: return 5.0       # Overdue = Max urgency
    if days_left == 0: return 5.0      # Today = Max urgency
    if days_left <= 3: return 3.0      # Soon
    if days_left <= 7: return 2.0      # This week
    return 1.0                         # Later
```

#### The Master Formula
Combines all factors into a single `score`.
```python
def compute_score(task: Task) -> Tuple[float, Dict[str, float]]:
    dleft = days_until(task.deadline)
    urg = urgency_score(dleft)
    imp = float(task.impact)
    
    # Bonuses and Penalties
    qwb = quickwin_bonus(task.effort_min) * WEIGHTS["quickwin_bonus"]
    bpen = WEIGHTS["blocked_penalty"] if task.blocked else 0.0

    # THE FORMULA
    score = (WEIGHTS["urgency"] * urg) + \
            (WEIGHTS["importance"] * imp) + \
            qwb - bpen
            
    return score, {...} # Returns breakdown for debugging
```

---

### 6. Main Logic

#### Reading Tasks
Iterates through the CSV row by row and blindly creates `Task` objects.
```python
def read_tasks(path: str) -> List[Task]:
    # ... standard csv reading ...
    # Uses helper functions to clean data immediately upon reading
    deadline = parse_date(row.get("deadline"))
    effort_min = parse_effort(row.get("effort"))
    # ...
```

#### Building the Plan
This is where the sorting happens.
```python
def build_plan(tasks: List[Task]) -> Dict:
    # 1. Score every task
    scored = []
    for t in tasks:
        s, breakdown = compute_score(t)
        scored.append((t, s, breakdown))

    # 2. SORTING:
    # - Primary: Score (Descending)
    # - Secondary: Effort (Ascending) -> Tie-breaker: do the smaller task first
    scored.sort(key=lambda x: (-x[1], x[0].effort_min))

    # 3. Categorize
    unblocked = [x for x in scored if not x[0].blocked]
    blocked = [x for x in scored if x[0].blocked]
    
    # Take top 3
    top3 = unblocked[:TOP3_COUNT]
    
    # ... logic for next5 and defer ...
```

---

### 7. Execution
Standard Python boilerplate to run the script.
```python
def main():
    # CLI Argument Parsing
    parser = argparse.ArgumentParser(...)
    # ... setup args ...

    # Error Catching
    try:
        tasks = read_tasks(args.input)
    except FileNotFoundError:
        print("Error: Input file not found...")
        sys.exit(1)

    # Core Execution
    plan = build_plan(tasks)
    
    # Output
    # ... saves to json and txt ...
```
