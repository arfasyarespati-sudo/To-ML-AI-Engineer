"""
Chat Engine - Handles AI model interactions
"""

import os
from typing import List, Dict


class ChatEngine:
    """Engine for handling chat conversations with AI models."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.model = "gpt-3.5-turbo"
        self._client = None

        if api_key:
            self._init_client()

    def _init_client(self):
        """Initialize the OpenAI client."""
        try:
            from openai import OpenAI #edit this
            self._client = OpenAI(api_key=self.api_key) #edit this
        except ImportError:
            print("OpenAI library not installed. Install with: pip install openai")
            self._client = None

    def get_response(self, messages: List[Dict[str, str]]) -> str:
        """Get AI response for the given messages."""
        if not self._client:
            return self._mock_response(messages)

        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1024
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    def _mock_response(self, messages: List[Dict[str, str]]) -> str:
        """Return a mock response when API is not available."""
        last_message = messages[-1]["content"] if messages else ""
        return f"[Mock Response] I received: '{last_message}'. Please set OPENAI_API_KEY in your .env file for real AI responses."

    def set_model(self, model: str):
        """Set the AI model to use."""
        available_models = self.get_available_models()
        if model in available_models:
            self.model = model
            return True
        return False

    def get_available_models(self) -> List[str]:
        """Get list of available models."""
        return [
            "gpt-3.5-turbo",
            "gpt-4",
            "gpt-4-turbo",
            "gpt-4o",
            "gpt-4o-mini"
        ]

    def stream_response(self, messages: List[Dict[str, str]]):
        """Stream AI response (generator)."""
        if not self._client:
            yield self._mock_response(messages)
            return

        try:
            stream = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1024,
                stream=True
            )
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Error: {str(e)}"
