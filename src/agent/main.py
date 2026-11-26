from pydantic import ValidationError

from agent.graph.builder import build_graph
from agent.schemas import AgentRequest


def main() -> None:
    raw_input = {
        "user_id": "gulshan",
        "thread_id": "thread_001",
        "message": "What is LangGraph?",
    }

    try:
        request = AgentRequest.model_validate(raw_input)
        graph = build_graph()

        result = graph.invoke(
            {
                **request.model_dump(),
                "normalized_message": "",
                "request_type": "unclassified",
                "response": "",
            }
        )

        print("Graph execution successful")
        print(f"Normalized message: {result['normalized_message']}")
        print(f"Request type: {result['request_type']}")
        print(f"Response: {result['response']}")

    except ValidationError as error:
        print("Input validation failed")
        print(error)


if __name__ == "__main__":
    main()