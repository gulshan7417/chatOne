from agent.graph.state import AgentState, RequestType


GREETING_WORDS = {
    "hello",
    "hi",
    "hey",
    "greetings",
}


def normalize_message(state: AgentState) -> dict[str, str]:
    """Normalize whitespace in the user's message."""

    normalized_message = " ".join(state.message.split())

    return {
        "normalized_message": normalized_message,
    }


def classify_request(state: AgentState) -> dict[str, RequestType]:
    """Classify the request using deterministic rules."""

    normalized_lower = state.normalized_message.lower()
    words = set(normalized_lower.split())

    if words.intersection(GREETING_WORDS):
        request_type: RequestType = "greeting"

    elif normalized_lower.endswith("?"):
        request_type = "question"

    else:
        request_type = "unknown"

    return {
        "request_type": request_type,
    }


def handle_greeting(state: AgentState) -> dict[str, str]:
    """Create a response for a greeting."""

    return {
        "response": "Hello! How can I help you?",
    }


def handle_question(state: AgentState) -> dict[str, str]:
    """Create a deterministic response for a question."""

    return {
        "response": (
            "Your question has been received: "
            f"{state.normalized_message}"
        ),
    }


def handle_unknown(state: AgentState) -> dict[str, str]:
    """Create a safe fallback response."""

    return {
        "response": (
            "I could not determine the request type. "
            "Please provide a greeting or a question ending with '?'."
        ),
    }