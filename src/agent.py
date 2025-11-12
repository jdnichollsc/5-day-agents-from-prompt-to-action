"""
Core agent implementation using Google ADK and Gemini API
Provides reusable agent logic for natural-language instruction processing
"""

import os
from typing import Optional
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types


def get_retry_config() -> types.HttpRetryOptions:
    """
    Configure retry options for LLM requests.
    
    When working with LLMs, you may encounter transient errors like rate limits
    or temporary service unavailability. Retry options automatically handle these
    failures by retrying the request with exponential backoff.
    
    Returns:
        HttpRetryOptions: Configured retry options
    """
    return types.HttpRetryOptions(
        attempts=5,  # Maximum retry attempts
        exp_base=7,  # Delay multiplier
        initial_delay=1,  # Initial delay before first retry (in seconds)
        http_status_codes=[429, 500, 503, 504]  # Retry on these HTTP errors
    )


def create_agent(
    name: str = "helpful_assistant",
    model_name: str = "gemini-2.5-flash-lite",
    description: str = "A simple agent that can answer general questions.",
    instruction: str = "You are a helpful assistant. Use Google Search for current info or if unsure.",
    use_google_search: bool = True
) -> Agent:
    """
    Create an AI Agent using Google ADK.
    
    This function configures an Agent by setting its key properties, which tell it
    what to do and how to operate.
    
    Args:
        name: A simple name to identify the agent
        model_name: The specific LLM that will power the agent's reasoning
        description: A description of what the agent does
        instruction: The agent's guiding prompt - tells the agent its goal and behavior
        use_google_search: Whether to give the agent access to google_search tool
        
    Returns:
        Agent: A configured Agent instance ready to use
    """
    # Configure retry options for robustness
    retry_config = get_retry_config()
    
    # Set up the list of tools available to the agent
    tools = [google_search] if use_google_search else []
    
    # Create and configure the agent
    agent = Agent(
        name=name,
        model=Gemini(
            model=model_name,
            retry_options=retry_config
        ),
        description=description,
        instruction=instruction,
        tools=tools,
    )
    
    return agent


def create_runner(agent: Agent) -> InMemoryRunner:
    """
    Create an InMemoryRunner for the given agent.
    
    The Runner is the central component within ADK that acts as the orchestrator.
    It manages the conversation, sends messages to the agent, and handles responses.
    
    Args:
        agent: The Agent instance to run
        
    Returns:
        InMemoryRunner: A runner ready to execute the agent
    """
    return InMemoryRunner(agent=agent)


async def run_agent(prompt: str, agent: Optional[Agent] = None) -> str:
    """
    Run the agent with a given prompt and return the response.
    
    This is a convenience function that creates a default agent if none is provided,
    creates a runner, and executes the prompt using run_debug().
    
    Args:
        prompt: The natural language instruction or query
        agent: Optional Agent instance. If None, creates a default agent
        
    Returns:
        str: The agent's response
    """
    if agent is None:
        agent = create_agent()
    
    runner = create_runner(agent)
    response = await runner.run_debug(prompt)
    
    return response


# For backwards compatibility and standalone script execution
if __name__ == "__main__":
    import asyncio
    
    # Set API key from environment
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found in environment variables")
        print("Please set your API key: export GEMINI_API_KEY='your-api-key-here'")
        exit(1)
    
    # Note: The API key is automatically picked up by the ADK from the environment
    print("✅ API key configured")
    
    async def main():
        print("🤖 Creating AI Agent...")
        agent = create_agent()
        print(f"✅ Agent '{agent.name}' created successfully!\n")
        
        # Example usage
        print("=" * 50)
        print("Example: Asking the agent a question")
        print("=" * 50)
        prompt = "What is the Google Agent Development Kit (ADK)? What languages is the SDK available in?"
        print(f"Prompt: {prompt}\n")
        
        response = await run_agent(prompt, agent)
        print(f"Response: {response}")
    
    asyncio.run(main())
