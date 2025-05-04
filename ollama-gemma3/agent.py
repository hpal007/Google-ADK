from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

AGENT_MODEL = "ollama/gemma3:1b"

from .prompt import writing_enhancer_agent_instruction

root_agent = Agent(
    name="Writing_Enhancer",
    model=LiteLlm(model=AGENT_MODEL),
    description=""" 
                The Writing Enhancer agent refines input text to produce clear, grammatically correct, and professionally polished writing. 
                It improves grammar, punctuation, sentence structure, and word choice while preserving the original meaning and tone. 
                Ideal for emails, articles, essays, social media posts, or any written content that needs a quality boost.
                """,
    instruction=writing_enhancer_agent_instruction,
)
