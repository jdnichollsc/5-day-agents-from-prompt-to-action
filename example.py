"""
Example script demonstrating the AI Agent usage with Google ADK
"""

import os
import asyncio
from dotenv import load_dotenv
from src.agent import create_agent, create_runner, run_agent


async def main():
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY not found in environment variables")
        print("Please set your API key in a .env file or export it as an environment variable")
        return
    
    print("🤖 Creating AI Agent with Google ADK...")
    agent = create_agent()
    print(f"✅ Agent '{agent.name}' created successfully!\n")
    
    # Example 1: Simple query using the agent
    print("=" * 70)
    print("Example 1: Asking about AI Agents")
    print("=" * 70)
    prompt = "What is the Google Agent Development Kit (ADK)? What languages is the SDK available in?"
    print(f"Prompt: {prompt}\n")
    response = await run_agent(prompt, agent)
    print(f"Response:\n{response}\n")
    
    # Example 2: Using the runner directly
    print("=" * 70)
    print("Example 2: Using the Runner Directly")
    print("=" * 70)
    runner = create_runner(agent)
    prompt2 = "Create a short poem about AI Agents learning from humans."
    print(f"Prompt: {prompt2}\n")
    response2 = await runner.run_debug(prompt2)
    print(f"Response:\n{response2}\n")


if __name__ == "__main__":
    asyncio.run(main())
