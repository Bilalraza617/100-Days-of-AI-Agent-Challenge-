import os, uuid, time
from dataclasses import dataclass, field
from typing import Dict, Any, List
from dotenv import load_dotenv
from openai import OpenAI
 
load_dotenv()
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Explain the importance of fast language models",
            model="groq/compound",
        )

print("Response:", response.choices[0].text.strip())
 
def chat(system:str, user:str, temp:float=0):
    r = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        temperature=temp,
        messages=[{"role":"system","content":system},
                  {"role":"user","content":user}]
    )
    return r.choices[0].message.content.strip()
 
@dataclass
class Message:
    sender: str
    content: str
    ts: float = field(default_factory=time.time)
 
@dataclass
class Blackboard:
    data: Dict[str, Any] = field(default_factory=dict)
    log: List[Message] = field(default_factory=list)
    def write(self, msg: Message): self.log.append(msg)
    def update(self, **kwargs): self.data.update(kwargs)

    # ----------------

ROLE_RESEARCHER = (
"Role: Researcher. Read the task & propose 3 concise facts or sources "
"to inform a solution. Output as bullet points. No final answer."
)
 
ROLE_PLANNER = (
"Role: Planner. Read the latest facts and propose an ordered plan with 3–5 steps. "
"State assumptions and risks briefly."
)
 
ROLE_CRITIC = (
"Role: Critic. Review the plan for gaps, conflicts, or missing data. "
"Return 2–3 actionable improvements. No final answer."
)
 
ROLE_SINGLE = (
"You are a single agent acting as Researcher, Planner, and Critic at once. "
"Given the task, produce facts, a plan, then self-critique with improvements."
)


# -------------------

class BaseAgent:
    def __init__(self, name:str, role:str): self.name, self.role = name, role
    def act(self, task:str, bb:Blackboard)->Message:
        context = (
            f"Task:\n{task}\n\nBlackboard:\n{bb.data}\n\n"
            f"Conversation so far:\n" +
            "\n".join([f"- {m.sender}: {m.content[:200]}" for m in bb.log[-6:]])
        )
        out = chat(system=self.role, user=context)
        return Message(sender=self.name, content=out)
 
researcher = BaseAgent("Researcher", ROLE_RESEARCHER)
planner    = BaseAgent("Planner",    ROLE_PLANNER)
critic     = BaseAgent("Critic",     ROLE_CRITIC)
single     = BaseAgent("Solo",       ROLE_SINGLE)

# -----------------------

def summarize_last(msgs: List[Message], role:str)->str:
    if not msgs: return ""
    joined = "\n".join([m.content for m in msgs[-2:]])
    return chat(system=f"Summarize for {role}.", user=joined)
 
def multi_agent_run(task:str, rounds:int=1)->Blackboard:
    bb = Blackboard(data={"task": task, "facts":[], "plan":"","critique":""})
    for r in range(rounds):
        # Researcher
        m1 = researcher.act(task, bb); bb.write(m1)
        bb.update(facts=bb.data.get("facts", []) + [m1.content])
 
        # Planner proposes
        ctx = summarize_last(bb.log, "Planner")
        m2 = planner.act(task + "\n\nContext:\n" + ctx, bb); bb.write(m2)
        bb.update(plan=m2.content)
 
        # Critic reviews
        ctx = summarize_last(bb.log, "Critic")
        m3 = critic.act(task + "\n\nContext:\n" + ctx, bb); bb.write(m3)
        bb.update(critique=m3.content)
 
        # Planner revises
        ctx = summarize_last(bb.log, "Planner")
        m4 = planner.act(task + "\n\nRevise plan per critique:\n" + ctx, bb); bb.write(m4)
        bb.update(plan=m4.content, round=r+1)
    return bb

# -----------------------

def single_agent_run(task:str)->Blackboard:
    bb = Blackboard(data={"task":task})
    m = single.act(task, bb); bb.write(m)
    bb.update(final=m.content)
    return bb

# -----------------------

TASK = ("Design a 3-email outreach sequence for a B2B AI tool targeting "
        "healthcare analytics leaders. Include subject lines and a clear CTA each.")
 
bb_multi  = multi_agent_run(TASK, rounds=1)
bb_single = single_agent_run(TASK)
 
print("\n=== MULTI-AGENT (final plan) ===\n", bb_multi.data.get("plan",""))
print("\n=== MULTI-AGENT (critique) ===\n", bb_multi.data.get("critique",""))
print("\n=== SINGLE-AGENT ===\n", bb_single.data.get("final",""))

# ---------------------

comparison_prompt = f"""
Compare two outputs for the same task.
 
[Multi-agent Plan]
{bb_multi.data.get('plan','')}
 
[Single-agent Output]
{bb_single.data.get('final','')}
 
Score each (1–5) on Coverage, Quality, Diversity, and provide a 3-sentence verdict.
"""
print("\n=== AUTO EVAL ===\n", chat("You are a fair evaluator.", comparison_prompt))