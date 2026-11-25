# LangGraph Enterprise Agent

A secure, production-oriented AI agent built step by step using:

- Python
- Pydantic
- LangGraph
- Tool calling
- RAG
- Model Context Protocol
- SQLite
- FastAPI
- React

## Development principles

1. Build one feature at a time.
2. Validate external data using Pydantic.
3. Test every feature before continuing.
4. Never commit secrets.
5. Apply least-privilege access to tools.
6. Create a Git checkpoint after every completed step.

## Current status

Step 1: Development environment and repository setup.
## Step 2: Pydantic validation

Implemented:

- Python `src` package structure
- `AgentRequest` input schema
- String length and identifier constraints
- Rejection of unexpected fields
- Whitespace normalization
- Assignment validation
- Valid and invalid input checks