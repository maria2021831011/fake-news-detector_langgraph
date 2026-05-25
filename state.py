from typing import TypedDict

class AgentState(TypedDict):
    claim: str
    analysis: str
    evidence: str
    verdict: str
    confidence: int