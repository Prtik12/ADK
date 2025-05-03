# Agent Development Kit

## Overview

ADK is a flexible toolkit that allows you to create and manage AI agents. It enables seamless interaction between multiple agents designed for different purposes such as idea generation, idea refinement, and more. This project is built using the Google ADK library, with the goal of providing easy-to-use and efficient agents for various tasks.

## Features

* **Idea Generation Agent**: Generates creative and unique ideas based on a given topic.
* **Idea Refinement Agent**: Takes the generated ideas and refines them to make them more actionable and specific.
* **Root Agent**: Coordinates between the idea generation and refinement agents to provide the final result to the user.
* **Modular Agent System**: Easily extendable with additional agents and tools.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Prtik12/ADK.git
   cd ADK
   ```

2. Set up a virtual environment (if not already done):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # For macOS/Linux
   .venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once the environment is set up, you can start the ADK server and interact with your agents.

### Start the ADK Web Server

To run the web server locally, use:

```bash
adk web
```

This will start the server at `http://localhost:8000`.

### Example of Agent Setup

In the `agent.py` file, you'll find an example of how to set up and run multiple agents:

```python
from google.adk.agents import LlmAgent

MODEL = "gemini-2.0-flash-001"

# Idea generation agent
idea_agent = LlmAgent(
    name="IdeaAgent",
    model=MODEL,
    description="Generates creative ideas for a given topic.",
    instruction="Generate 5 unique, creative ideas related to the given topic.",
    disallow_transfer_to_peers=True,
)

# Idea refinement agent
refine_agent = LlmAgent(
    name="RefineAgent",
    model=MODEL,
    description="Refines the ideas to make them more actionable.",
    instruction="Take the provided list of ideas and improve them by making each one specific and actionable. Include a short explanation.",
    disallow_transfer_to_peers=True,
)

# Root agent coordinates the sub-agents
root_agent = LlmAgent(
    name="RootAgent",
    model=MODEL,
    description="Coordinates idea generation and refinement.",
    instruction="""
1. Ask IdeaAgent to generate 5 ideas for the topic.
2. Pass those ideas to RefineAgent to make them more actionable.
3. Return the final refined ideas to the user in a clean, readable format.
""",
    sub_agents=[idea_agent, refine_agent],
)
```

### Interact with Your Agents

After setting up the agents, interact with them via the web interface or call them programmatically as needed.
