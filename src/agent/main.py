from pydantic import ValidationError

from agent.schemas import AgentRequest


def create_agent_request(data: dict) -> AgentRequest:
    """Validate raw input before it enters the agent workflow."""
    return AgentRequest.model_validate(data)


def main() -> None:
    invalid_data = {
        "user_id": "../admin",
        "thread_id": "thread_001",
        "message": "   ",
        "is_admin": True,
    }

    try:
        request = create_agent_request(invalid_data)

        print("Validation successful")
        print(request.model_dump())

    except ValidationError as error:
        print("Validation failed")
        print(error)


if __name__ == "__main__":
    main()
