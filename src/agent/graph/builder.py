from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from agent.graph.nodes import (
    classify_request,
    handle_greeting,
    handle_question,
    handle_unknown,
    normalize_message,
)
from agent.graph.routes import route_request
from agent.graph.state import AgentState


def build_graph() -> CompiledStateGraph:
    """Construct and compile the conditionally routed agent graph."""

    builder = StateGraph(AgentState)

    builder.add_node("normalize_message", normalize_message)
    builder.add_node("classify_request", classify_request)
    builder.add_node("handle_greeting", handle_greeting)
    builder.add_node("handle_question", handle_question)
    builder.add_node("handle_unknown", handle_unknown)

    builder.add_edge(START, "normalize_message")
    builder.add_edge("normalize_message", "classify_request")

    builder.add_conditional_edges(
        "classify_request",
        route_request,
        {
            "greeting": "handle_greeting",
            "question": "handle_question",
            "unknown": "handle_unknown",
        },
    )

    builder.add_edge("handle_greeting", END)
    builder.add_edge("handle_question", END)
    builder.add_edge("handle_unknown", END)

    return builder.compile()