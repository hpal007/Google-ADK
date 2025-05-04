# Google Search Agent

This project implements a simple agent using the Google Agent Development Kit (ADK).

## Description

The agent, defined in `agent.py`, is designed to answer questions by utilizing the `google_search` tool provided by the Google ADK. It uses the `gemini-2.0-flash` model.

## Files

*   `agent.py`: Defines the main agent logic, including its description, instructions, and the tools it uses.
*   `__init__.py`: Makes the `agent` module available for import.
*   `.env`: Configuration file for environment variables.

## Setup

1.  **Environment Variables:** Create a `.env` file in this directory with your Google API Key:
    ```properties
    GOOGLE_API_KEY=YOUR_API_KEY_HERE
    ```
    *(Optionally, you can set `GOOGLE_GENAI_USE_VERTEXAI=TRUE` if using Vertex AI, but the current `.env` example shows it set to `FALSE`)*.

2.  **Dependencies:** Ensure you have the `google-adk` library installed.


# Ollama Gemma3 Writing Enhancer Agent

This project implements a Writing Enhancer agent using the Google Agent Development Kit (ADK) and Ollama with the Gemma3 model.

## Description

The agent, defined in `agent.py`, is designed to refine input text. It aims to produce clear, grammatically correct, and professionally polished writing by improving grammar, punctuation, sentence structure, and word choice while preserving the original meaning and tone.

It utilizes the `ollama/gemma3:1b` model via the `LiteLlm` integration from the Google ADK.

## Files

*   `agent.py`: Defines the main agent logic, including its name, description, model configuration (`LiteLlm`), and instructions.
*   `prompt.py`: Contains the detailed instructions (`writing_enhancer_agent_instruction`) provided to the agent model.
*   `__init__.py`: Makes the `agent` module available for import.

## Setup

1.  **Install Dependencies:** Ensure you have the necessary libraries installed:
    ```bash
    pip install google-adk litellm
    ```

2.  **Run Ollama:** Make sure you have Ollama installed and running locally. You also need to have pulled the `gemma3:1b` model:
    ```bash
    ollama pull gemma3:1b
    ollama serve & # or run the Ollama application
    ```

3.  **Run the Agent:** You can now integrate and run this agent within your Google ADK application. The ADK will communicate with the local Ollama service via LiteLLM.