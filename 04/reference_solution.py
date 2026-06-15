import json
import os
from datetime import date
from openai import OpenAI
from dotenv import load_dotenv
 
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
 
SYSTEM_PROMPT = """
You are a Meeting Agenda Generator Agent.
 
Your job is to generate a clear, time-boxed meeting agenda.
 
Rules:
- Agenda must fit within the provided duration
- Focus on the meeting objective
- Include time allocation for each item
- Identify decision points where applicable
- Return ONLY valid JSON with this schema:
 
{
  "meeting_title": "",
  "objective": "",
  "total_duration_minutes": 0,
  "agenda": [
    {
      "topic": "",
      "time_minutes": 0,
      "owner": "",
      "outcome": ""
    }
  ]
}
"""
 
def read_input(path="meeting.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
 

def generate_agenda(meeting_text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": meeting_text}
        ],
        temperature=0.3
    )
    content = response.choices[0].message.content
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        cleaned = content.strip().strip('`')
        return json.loads(cleaned)
 

def save_outputs(data):
    with open("agenda.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
 
    with open("agenda.txt", "w", encoding="utf-8") as f:
        f.write(f"Meeting Agenda ({date.today()})\n")
        f.write("=" * 45 + "\n\n")
        f.write(f"Title: {data.get('meeting_title', '')}\n")
        f.write(f"Objective: {data.get('objective', '')}\n")
        f.write(f"Duration: {data.get('total_duration_minutes', 0)} minutes\n\n")
 
        for i, item in enumerate(data.get("agenda", []), 1):
            f.write(f"{i}. {item.get('topic', '')} ({item.get('time_minutes', 0)} min)\n")
            f.write(f"   Owner: {item.get('owner', '')}\n")
            f.write(f"   Outcome: {item.get('outcome', '')}\n\n")
 

def main():
    meeting_text = read_input()
    agenda = generate_agenda(meeting_text)
    save_outputs(agenda)
    print("Meeting agenda generated successfully.")
    print(json.dumps(agenda, indent=2))
 

if __name__ == "__main__":
    main()
