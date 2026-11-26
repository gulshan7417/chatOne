import pytest
from pydantic import ValidationError

from agent.graph.builder import build_graph


def graph_input(message: str) -> dict[str, str]:
    """Create a valid initial graph state."""

    return {
        "user_id": "gulshan",
        "thread_id": "thread_001",
        "message": message,
        "normalized_message": "",
        "request_type": "unclassified",
        "response": "",
    }


@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Hi agent",
        "Hey there",
        "Greetings agent",
    ],
)
def test_graph_routes_greetings(message: str) -> None:
    graph = build_graph()

    result = graph.invoke(graph_input(message))

    assert result["request_type"] == "greeting"
    assert result["response"] == "Hello! How can I help you?"


@pytest.mark.parametrize(
    "message",
    [
        "What is LangGraph?",
        "How does routing work?",
        "Can an agent call tools?",
    ],
)
def test_graph_routes_questions(message: str) -> None:
    graph = build_graph()

    result = graph.invoke(graph_input(message))

    assert result["request_type"] == "question"
    assert result["response"] == (
        f"Your question has been received: {message}"
    )


@pytest.mark.parametrize(
    "message",
    [
        "Build an agent",
        "LangGraph state",
        "Use a tool",
    ],
)
def test_graph_routes_unknown_requests(message: str) -> None:
    graph = build_graph()

    result = graph.invoke(graph_input(message))

    assert result["request_type"] == "unknown"
    assert result["response"] == (
        "I could not determine the request type. "
        "Please provide a greeting or a question ending with '?'."
    )


def test_graph_normalizes_before_classification() -> None:
    graph = build_graph()

    result = graph.invoke(
        graph_input("   What   is\nLangGraph?   ")
    )

    assert result["normalized_message"] == "What is LangGraph?"
    assert result["request_type"] == "question"


def test_graph_preserves_request_identity() -> None:
    graph = build_graph()

    result = graph.invoke(graph_input("Hello agent"))

    assert result["user_id"] == "gulshan"
    assert result["thread_id"] == "thread_001"


@pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        ("user_id", "../admin"),
        ("thread_id", "thread/001"),
        ("message", "   "),
    ],
)
def test_graph_rejects_invalid_input(
    field: str,
    invalid_value: str,
) -> None:
    graph = build_graph()
    data = graph_input("Hello agent")
    data[field] = invalid_value

    with pytest.raises(ValidationError):
        graph.invoke(data)