# Product Description: LLM2Deck

## Overview
LLM2Deck is an advanced, automated system for generating high-quality Anki flashcards using Large Language Models (LLMs). The core philosophy of the project is to leverage **parallel generation** from multiple LLM sources to create diverse, comprehensive, and accurate study materials, which are then synthesized into a single, cohesive deck.

## Core Architectural Constraint
**Generic OpenAI-Compatible Provider Interface**:
To ensure maximum flexibility and future-proofing, the system must not rely on hardcoded SDKs for specific AI providers (e.g., Anthropic, Cerebras, Google, etc.). Instead, the entire architecture must be built around a **single, generic OpenAI-compatible API client**.

- **Extensibility via Configuration**: Support for different providers (Cerebras, OpenRouter, Canopywave, local models, etc.) is achieved strictly through configuration (YAML). Users define the `base_url`, `api_key`, and model parameters for each provider in the config file. The system treats them all uniformly.
- **No Vendor Lock-in**: The codebase remains clean of vendor-specific logic.

## Key Functionalities

### 1. Parallel Generation & Synthesis
The generation pipeline consists of three distinct stages:
1.  **Parallel Generation**: The system sends the same prompt/question to multiple configured LLM providers simultaneously. This captures different teaching styles, nuances, and solution approaches.
2.  **Combination (The "Combiner")**: A designated "smart" model (configurable) receives the outputs from all generators. Its task is to synthesize these inputs into a single, high-quality set of flashcards, removing redundancies and resolving conflicts.
3.  **Formatting (The "Formatter")**: An optional final step where a model dedicated to structure ensures the output is valid, parseable JSON, adhering to the required schema.

### 2. Flexible Input Sources
- **Subject-Based Generation**: Built-in support for structured subjects (e.g., LeetCode, Computer Science, Physics) with specialized prompting strategies.
- **Document Ingestion**: The ability to ingest arbitrary documents (Markdown, Text, HTML) from a directory structure. The system treats folders as deck hierarchies and files as source material for card generation.

### 3. Output Formats
- **Anki Packages (.apkg)**: Generates ready-to-import Anki files with support for:
    - Hierarchical Decks (e.g., `LeetCode::Dynamic Programming::Problem Name`).
    - Rich styling (Markdown rendering, code blocks).
    - Metadata tagging (difficulty, topic, card type).
- **Archival JSON**: Stores raw generated data for future processing or merging.
- **Markdown Export**: Converts cards to human-readable Markdown files.

### 4. Operational Reliability
- **Resumability**: If a run is interrupted or fails, the system can resume from the exact point of failure, skipping already processed items.
- **Caching**: Aggressive caching of LLM responses to prevent redundant API calls and save costs.
- **Cost Estimation & Budgeting**:
    - **Pre-run Estimation**: Calculates expected token usage and cost based on the number of questions and provider rates.
    - **Budget Enforcement**: Accepts a hard budget limit (e.g., "$2.00") and halts execution gracefully if the limit is exceeded.

### 5. Configuration
Configuration is handled via a **YAML** file (`config.yaml`), allowing users to define:
- **Providers**: List of enabled providers with their `base_url`, `model`, and API key paths.
- **Generation Settings**: Concurrency limits, retry policies, and temperature settings.
- **Subject Settings**: Custom prompts and source directories for different subjects.

### 6. Command Line Interface (CLI)
A robust CLI manages the workflow:
- `generate`: Trigger card generation for a subject.
- `ingest`: Process a directory of documents.
- `query`: Inspect database for past runs, success rates, and generated cards.
- `cache`: Manage and clear the response cache.
- `convert`: Manually convert JSON archives to `.apkg`.

## Target User Experience
A user should be able to clone the repository, add their API keys to a generic config, and immediately start generating flashcards from any OpenAI-compatible endpoint without needing to write code or install vendor-specific libraries.
