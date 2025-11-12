"""
AI Agent using Google ADK and Gemini API
Provides reusable agent logic for natural-language instruction processing
"""

import os
from typing import Optional, Dict, Any
import google.generativeai as genai


class AIAgent:
    """
    A reusable AI Agent that can understand natural-language instructions
    and perform actions autonomously using the Gemini API.
    """
    
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-pro"):
        """
        Initialize the AI Agent
        
        Args:
            api_key: Google API key (if not provided, will look for GOOGLE_API_KEY env var)
            model_name: Name of the Gemini model to use
        """
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set in GOOGLE_API_KEY environment variable")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)
        self.chat = None
        
    def start_chat(self, history: Optional[list] = None) -> None:
        """
        Start a new chat session
        
        Args:
            history: Optional chat history to initialize the session
        """
        self.chat = self.model.start_chat(history=history or [])
    
    def send_message(self, message: str) -> str:
        """
        Send a message to the agent and get a response
        
        Args:
            message: The natural language instruction or query
            
        Returns:
            The agent's response as a string
        """
        if not self.chat:
            self.start_chat()
        
        response = self.chat.send_message(message)
        return response.text
    
    def generate_content(self, prompt: str) -> str:
        """
        Generate content based on a prompt without maintaining chat history
        
        Args:
            prompt: The prompt for content generation
            
        Returns:
            The generated content as a string
        """
        response = self.model.generate_content(prompt)
        return response.text
    
    def get_chat_history(self) -> list:
        """
        Get the current chat history
        
        Returns:
            List of chat messages
        """
        if not self.chat:
            return []
        return self.chat.history


def create_agent(api_key: Optional[str] = None, model_name: str = "gemini-pro") -> AIAgent:
    """
    Factory function to create an AI Agent instance
    
    Args:
        api_key: Google API key
        model_name: Name of the Gemini model to use
        
    Returns:
        An initialized AIAgent instance
    """
    return AIAgent(api_key=api_key, model_name=model_name)
