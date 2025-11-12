"""
Example script demonstrating the AI Agent usage
"""

import os
from dotenv import load_dotenv
from src.agent import create_agent


def main():
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY not found in environment variables")
        print("Please set your API key in a .env file or export it as an environment variable")
        return
    
    print("🤖 Creating AI Agent...")
    agent = create_agent()
    print("✅ Agent created successfully!\n")
    
    # Example 1: Simple content generation
    print("=" * 50)
    print("Example 1: Content Generation")
    print("=" * 50)
    prompt = "Explain what an AI agent is in one sentence."
    print(f"Prompt: {prompt}")
    response = agent.generate_content(prompt)
    print(f"Response: {response}\n")
    
    # Example 2: Chat session
    print("=" * 50)
    print("Example 2: Chat Session")
    print("=" * 50)
    agent.start_chat()
    
    messages = [
        "Hello! What can you help me with?",
        "Can you write a haiku about AI?",
    ]
    
    for msg in messages:
        print(f"User: {msg}")
        response = agent.send_message(msg)
        print(f"Agent: {response}\n")
    
    # Show chat history
    history = agent.get_chat_history()
    print(f"Chat history contains {len(history)} messages")


if __name__ == "__main__":
    main()
