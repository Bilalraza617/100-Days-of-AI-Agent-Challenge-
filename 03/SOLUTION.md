# Day 3 Solution: Calendar Conflict Detection Agent 📅

This document explains the logic used in `reference_solution.py`.

## 📝 Reasoning & Logic

This is a **rule-based agent**. It does not need an LLM. The workflow is:

1. Read the calendar CSV.
2. Convert the rows into structured event objects.
3. Sort events by start time.
4. Check neighboring events for overlap or missing buffer time.
5. Generate a structured conflict report.

## 🔍 Code Breakdown

### 1. Imports & Setup

The script uses the standard library only.

```python
import csv
import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List
```

### 2. Configuration

The priority map and buffer size define how the agent thinks.

```python
PRIORITY_MAP = {"low": 1, "medium": 2, "high": 3}
BUFFER_MINUTES = 10
```

### 3. Data Structure

Each row from the CSV is converted into an `Event` object.

```python
@dataclass
class Event:
    title: str
    start: datetime
    end: datetime
    priority: int
    event_type: str
    flexible: bool
```

### 4. Parsing Helpers

The helper functions convert raw strings into useful Python values.

```python
def parse_datetime(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d %H:%M")
```

### 5. Reading the Calendar

The CSV is read row by row and sorted by start time.

```python
def read_calendar(path="calendar.csv") -> List[Event]:
    ...
    return sorted(events, key=lambda e: e.start)
```

### 6. Conflict Detection

This is the core logic. Two events conflict if they overlap or if the gap between them is smaller than the configured buffer.

```python
overlap = a.end > b.start
no_buffer = (b.start - a.end) < timedelta(minutes=BUFFER_MINUTES)
```

Severity is based on priority. If either event is high priority, the conflict is marked `high`; otherwise it is `medium`.

### 7. Resolution Suggestions

The suggestion logic prefers moving the less important flexible event.

```python
if a.priority > b.priority and b.flexible:
    return f"Reschedule '{b.title}'"
```

### 8. Output Files

The script writes two outputs:

1. `conflicts.json` for structured data.
2. `conflicts.txt` for a readable summary.

## 🚀 How to Run

```bash
python reference_solution.py
```
