import json
import os
from datetime import date
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
 
api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )  
 
SYSTEM_PROMPT = """
You are an Email Summarization Agent.
 
Your job:
1. Summarize the email in 2–3 sentences
2. Extract key points
3. Extract action items (who should do what)
4. Identify deadlines
5. Classify urgency: Low, Medium, or High
 
Return ONLY valid JSON with this schema:
 
{
  "summary": "",
  "key_points": [],
  "action_items": [],
  "deadlines": [],
  "urgency": ""
}
"""
 
def read_email(path="email.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
 
def summarize_email(email_text):
    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": email_text}
        ],
        temperature=0.2
    )
    return json.loads(response.choices[0].message.content)
 
def save_outputs(data):
    with open("summary.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
 
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Email Summary ({date.today()})\n")
        f.write("=" * 40 + "\n\n")
        f.write("SUMMARY:\n")
        f.write(data["summary"] + "\n\n")
 
        f.write("KEY POINTS:\n")
        for p in data["key_points"]:
            f.write(f"- {p}\n")
 
        f.write("\nACTION ITEMS:\n")
        for a in data["action_items"]:
            f.write(f"- {a}\n")
 
        f.write("\nDEADLINES:\n")
        for d in data["deadlines"]:
            f.write(f"- {d}\n")
 
        f.write(f"\nURGENCY: {data['urgency']}\n")
 
def main():
    email_text = read_email()
    result = summarize_email(email_text)
    save_outputs(result)
    print("Email summarized successfully.")
    print(result)
 
if __name__ == "__main__":
    main()