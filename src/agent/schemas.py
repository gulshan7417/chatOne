from pydantic import BaseModel, ConfigDict, Field


class AgentRequest(BaseModel):
    """Validated input received by the AI agent."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
        validate_assignment=True,
    )

    user_id: str = Field(
        min_length=3,
        max_length=50,
        pattern=r"^[a-zA-Z0-9_-]+$",
        description="Safe identifier for the user",
    )

    thread_id: str = Field(
        min_length=3,
        max_length=100,
        pattern=r"^[a-zA-Z0-9_-]+$",
        description="Conversation thread identifier",
    )

    message: str = Field(
        min_length=1,
        max_length=4000,
        description="User message sent to the agent",
    )