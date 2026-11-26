from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


RequestType = Literal[
    "unclassified",
    "greeting",
    "question",
    "unknown",
]


class AgentState(BaseModel):
    """Shared state that flows through the LangGraph workflow."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
        validate_assignment=True,
    )

    user_id: str = Field(
        min_length=3,
        max_length=50,
        pattern=r"^[a-zA-Z0-9_-]+$",
    )

    thread_id: str = Field(
        min_length=3,
        max_length=100,
        pattern=r"^[a-zA-Z0-9_-]+$",
    )

    message: str = Field(
        min_length=1,
        max_length=4000,
    )

    normalized_message: str = Field(
        default="",
        max_length=4000,
    )

    request_type: RequestType = "unclassified"

    response: str = Field(
        default="",
        max_length=5000,
    )