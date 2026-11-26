from typing import Literal

from agent.graph.state import AgentState


RouteName = Literal[
    "greeting",
    "question",
    "unknown",
]


def route_request(state: AgentState) -> RouteName:
    """Select the next node from the classified request type."""

    if state.request_type == "greeting":
        return "greeting"

    if state.request_type == "question":
        return "question"

    return "unknown"