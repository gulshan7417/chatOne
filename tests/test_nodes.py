import pytest
from agent.graph.state import AgentState, RequestType
from agent.graph.nodes import (
    classify_request,
    handle_greeting,
    handle_question,
    handle_unknown,
    normalize_message,
)
from agent.graph.state import AgentState


def create_state(
    message: str,
    normalized_message: str = "",
    request_type: RequestType = "unclassified",
) -> AgentState:
    return AgentState(
        user_id="gulshan",
        thread_id="thread_001",
        message=message,
        normalized_message=normalized_message,
        request_type=request_type,
        response="",
    )


def test_normalize_message() -> None:
    state = create_state("  Explain   LangGraph\nstate  ")

    update = normalize_message(state)

    assert update == {
        "normalized_message": "Explain LangGraph state",
    }


@pytest.mark.parametrize(
    ("message", "expected_type"),
    [
        ("Hello agent", "greeting"),
        ("Hi there", "greeting"),
        ("What is LangGraph?", "question"),
        ("Build an agent", "unknown"),
    ],
)
def test_classify_request(
    message: str,
    expected_type: str,
) -> None:
    state = create_state(
        message=message,
        normalized_message=message,
    )

    update = classify_request(state)

    assert update["request_type"] == expected_type


def test_handle_greeting() -> None:
    state = create_state(
        message="Hello",
        normalized_message="Hello",
        request_type="greeting",
    )

    update = handle_greeting(state)

    assert update["response"] == "Hello! How can I help you?"


def test_handle_question() -> None:
    state = create_state(
        message="What is LangGraph?",
        normalized_message="What is LangGraph?",
        request_type="question",
    )

    update = handle_question(state)

    assert update["response"] == (
        "Your question has been received: What is LangGraph?"
    )


def test_handle_unknown() -> None:
    state = create_state(
        message="Build an agent",
        normalized_message="Build an agent",
        request_type="unknown",
    )

    update = handle_unknown(state)

    assert "could not determine" in update["response"]