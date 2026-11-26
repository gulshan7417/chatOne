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
## Step 4: Deterministic LangGraph workflow

Implemented:

- Pydantic-based graph state
- Message-normalization node
- Deterministic response node
- START and END graph edges
- Graph compilation and invocation
- Automated graph execution tests
- Invalid graph input tests

Current workflow:

```text
START → normalize_message → create_response → END

## Step 5: Conditional graph routing

Implemented:

- Deterministic request classification
- Greeting, question, and unknown request types
- LangGraph conditional edges
- Dedicated response nodes for each route
- Safe fallback routing
- Unit tests for nodes and routing
- Integration tests for every graph branch

Current workflow:

```text
START
  ↓
normalize_message
  ↓
classify_request
  ├── greeting → handle_greeting ─┐
  ├── question → handle_question ├──→ END
  └── unknown  → handle_unknown ──┘