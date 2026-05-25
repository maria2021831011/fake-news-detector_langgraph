from langgraph.graph import StateGraph, END
from state import AgentState
from src.agents.agents import analyzer, verifier, judge
from langchain_ollama import ChatOllama
from config import MODEL_NAME

llm = ChatOllama(model=MODEL_NAME)


def build_graph():

    def a(state):
        result = analyzer(llm, state)
        return {**state, **result}

    def v(state):
        result = verifier(llm, state)
        return {**state, **result}

    def j(state):
        result = judge(llm, state)
        return {**state, **result}

    graph = StateGraph(AgentState)

    graph.add_node("analyzer", a)
    graph.add_node("verifier", v)
    graph.add_node("judge", j)

    graph.set_entry_point("analyzer")

    graph.add_edge("analyzer", "verifier")
    graph.add_edge("verifier", "judge")
    graph.add_edge("judge", END)

    return graph.compile()