from langgraph.graph import StateGraph, END
from state import AgentState
from src.agents.agents import analyzer, verifier, judge
from langchain_ollama import ChatOllama
from config import MODEL_NAME

llm = ChatOllama(model=MODEL_NAME)


def build_graph():
    graph = StateGraph(AgentState)

    def a(state):
        return {"analysis": analyzer(llm, state)}

    def v(state):
        return {"evidence": verifier(llm, state)}

    def j(state):
        return {"verdict": judge(llm, state)}

    graph.add_node("analyzer", a)
    graph.add_node("verifier", v)
    graph.add_node("judge", j)

    graph.set_entry_point("analyzer")

    graph.add_edge("analyzer", "verifier")
    graph.add_edge("verifier", "judge")
    graph.add_edge("judge", END)

    return graph.compile()


graph = build_graph()