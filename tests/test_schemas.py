import pytest
from pydantic import ValidationError

from agent.schemas import AgentRequest


def valid_request_data() -> dict[str, str]:
    """Return fresh valid data for each test."""

    return {
        "user_id": "gulshan",
        "thread_id": "thread_001",
        "message": "Explain LangGraph state.",
    }


def test_valid_agent_request() -> None:
    request = AgentRequest.model_validate(valid_request_data())

    assert request.user_id == "gulshan"
    assert request.thread_id == "thread_001"
    assert request.message == "Explain LangGraph state."


def test_surrounding_whitespace_is_removed() -> None:
    data = valid_request_data()
    data["message"] = "   Explain LangGraph state.   "

    request = AgentRequest.model_validate(data)

    assert request.message == "Explain LangGraph state."


@pytest.mark.parametrize(
    "invalid_user_id",
    [
        "../admin",
        "user name",
        "user@example.com",
        "ab",
        "user/123",
    ],
)
def test_invalid_user_id_is_rejected(invalid_user_id: str) -> None:
    data = valid_request_data()
    data["user_id"] = invalid_user_id

    with pytest.raises(ValidationError):
        AgentRequest.model_validate(data)


@pytest.mark.parametrize(
    "invalid_thread_id",
    [
        "../thread",
        "thread 001",
        "id",
        "thread/001",
    ],
)
def test_invalid_thread_id_is_rejected(invalid_thread_id: str) -> None:
    data = valid_request_data()
    data["thread_id"] = invalid_thread_id

    with pytest.raises(ValidationError):
        AgentRequest.model_validate(data)


@pytest.mark.parametrize(
    "invalid_message",
    [
        "",
        " ",
        "     ",
    ],
)
def test_empty_message_is_rejected(invalid_message: str) -> None:
    data = valid_request_data()
    data["message"] = invalid_message

    with pytest.raises(ValidationError):
        AgentRequest.model_validate(data)


def test_message_over_maximum_length_is_rejected() -> None:
    data = valid_request_data()
    data["message"] = "a" * 4001

    with pytest.raises(ValidationError):
        AgentRequest.model_validate(data)


def test_message_at_maximum_length_is_accepted() -> None:
    data = valid_request_data()
    data["message"] = "a" * 4000

    request = AgentRequest.model_validate(data)

    assert len(request.message) == 4000


def test_unexpected_field_is_rejected() -> None:
    data: dict[str, object] = valid_request_data()
    data["is_admin"] = True

    with pytest.raises(ValidationError):
        AgentRequest.model_validate(data)


def test_invalid_assignment_is_rejected() -> None:
    request = AgentRequest.model_validate(valid_request_data())

    with pytest.raises(ValidationError):
        request.message = ""


def test_model_serializes_to_expected_dictionary() -> None:
    request = AgentRequest.model_validate(valid_request_data())

    assert request.model_dump() == valid_request_data()