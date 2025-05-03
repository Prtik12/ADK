from google.adk.agents import LlmAgent

MODEL = "gemini-2.0-flash-001"

# Idea generation agent
idea_agent = LlmAgent(
    name="IdeaAgent",
    model=MODEL,
    description="Generates creative ideas for a given topic.",
    instruction="Generate 5 creative and unique ideas for the user's topic.",
    disallow_transfer_to_peers=True,
)

# Idea refinement agent
refine_agent = LlmAgent(
    name="RefineAgent",
    model=MODEL,
    description="Refines raw ideas into more specific and actionable ones.",
    instruction="Take the list of ideas and improve them by making each more specific and actionable. Include brief reasoning.",
    disallow_transfer_to_peers=True,
)

# Root agent coordinates the two sub-agents
root_agent = LlmAgent(
    name="RootAgent",
    model=MODEL,
    description="Coordinates idea generation and refinement.",
    instruction="""
You are a coordinator. First, delegate idea generation to IdeaAgent.
Then, send the result to RefineAgent for refinement.
Finally, return the refined list to the user in a clear format.
""",
    sub_agents=[idea_agent, refine_agent],
) 