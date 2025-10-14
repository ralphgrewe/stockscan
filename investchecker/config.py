"""
Configuration for InvestChecker.

Set your API keys as environment variables or in a .env file in the project root:
- TAVILY_API_KEY: Your Tavily web search API key
- OPENAI_API_KEY: Your OpenAI API key
- (Optional) PERPLEXITY_API_KEY: Your Perplexity API key

You can use a .env file for convenience:
TAVILY_API_KEY=your_tavily_key
OPENAI_API_KEY=your_openai_key
PERPLEXITY_API_KEY=your_perplexity_key

This file can be extended for more configuration options.
"""

from dotenv import load_dotenv
import os

# Load environment variables from .env if present
load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
