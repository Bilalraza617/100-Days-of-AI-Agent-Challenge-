import os
from dotenv import load_dotenv
from openai import OpenAI
 
load_dotenv()
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("GEMINI_API_BASE_URL")
)
 
def ask(prompt, show=True):
    resp = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role":"user","content":prompt}]
    )
    ans = resp.choices[0].message.content
    if show: print(ans)
    return ans
# Step 3: Baseline vs CoT — Math (15 min)
q = "A farmer has 17 sheep. All but 9 run away. How many are left?"
 
print("\n--- Baseline ---")
ask(q)
 
print("\n--- With CoT ---")
ask(q + "\n\nThink step by step before giving the final answer.")
# 👉 Compare: baseline often guesses, CoT reliably walks through steps → correct = 9.

# Step 4: Logic Puzzle (15 min)
q = """If John is taller than Mary, and Mary is taller than Sam, 
who is the shortest?"""
 
print("\n--- Baseline ---")
ask(q)
 
print("\n--- With CoT ---")
ask(q + "\n\nReason step by step before answering.")
# Observe: CoT makes the model explicitly compare pairs before concluding.

# Step 5: Commonsense Story (15 min)
q = """Alice put her laptop in her backpack. 
Then she went to school. 
Where is the laptop most likely now?"""
 
print("\n--- Baseline ---")
ask(q)
 
print("\n--- With CoT ---")
ask(q + "\n\nExplain your reasoning step by step.")
# Step 6: Structured CoT Output (10 min)
# Guide the model to format its reasoning:

prompt = """
Solve: A train leaves at 3pm going 60 mph. 
Another leaves at 4pm going 90 mph. 
When will the faster train catch up?
 
Answer format:
Reasoning:
Final Answer:
"""
print(ask(prompt))
# Great for agents that need to parse the Final Answer separately from reasoning.

# Step 7: Mini-Project (15–20 min)
# Build a small evaluator function:

tasks = [
    "What is 23*17?",
    "If it rains, the ground gets wet. It is raining. What can we conclude?",
    "A red ball is in the box. The box is tipped over. Where is the ball?"
]
 
for t in tasks:
    print("\nQ:", t)
    baseline = ask(t, show=False)
    cot = ask(t + "\nThink step by step.", show=False)
    print("Baseline:", baseline.strip())
    print("CoT:", cot.strip())
# 👉 Compare side by side — you’ll see CoT reduces errors and hallucinations.

# ✅ By completing this lab, you’ve seen CoT in action across math, logic, and commonsense tasks. This sets the stage for more advanced reasoning methods like ReAct (Lab 2) and planning loops (Lab 3).