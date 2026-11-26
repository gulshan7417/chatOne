import pytest

from agent.graph.routes import route_request
from agent.graph.state import AgentState, RequestType


def create_state(request_type: RequestType  ) -> AgentState:
    return AgentState(
        user_id="gulshan",
        thread_id="thread_001",
        message="Test message",
        normalized_message="Test message",
        request_type=request_type,
        response="",
    )


@pytest.mark.parametrize(
    ("request_type", "expected_route"),
    [
        ("greeting", "greeting"),
        ("question", "question"),
        ("unknown", "unknown"),
        ("unclassified", "unknown"),
    ],
)
def test_route_request(
    request_type: RequestType,
    expected_route: str,
) -> None:
    state = create_state(request_type)

    route = route_request(state)

    assert route == expected_route