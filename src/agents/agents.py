from langchain_core.messages import SystemMessage, HumanMessage
from src.tools.tools import web_search

# ---------------- ANALYZER ----------------
def analyzer(llm, state):
    return llm.invoke([
        SystemMessage(content="Summarize the claim briefly."),
        HumanMessage(content=state["claim"])
    ]).content


# ---------------- VERIFIER ----------------
def verifier(llm, state):
    claim = state["claim"]
    web_data = web_search(claim)

    prompt = f"""
You are a fact verifier.

Use ONLY this evidence:
{web_data}

Claim:
{claim}

Return:
- Evidence Summary
- Supporting facts
- Contradictions
- Risk level
"""

    return llm.invoke(prompt).content


# ---------------- JUDGE ----------------
def judge(llm, state):
    claim = state["claim"]
    evidence = state["evidence"]

    prompt = f"""
You are a strict fact-checking system.

RULES:
- Use ONLY given evidence
- Do NOT use outside knowledge
- If evidence supports claim → TRUE
- If contradicts → FALSE
- If unclear → UNCERTAIN

Claim: {claim}

Evidence:
{evidence}

Return format:
Verdict:
Confidence (0-100):
Reason (short):
"""

    return llm.invoke(prompt).content