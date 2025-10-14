from langchain_community.tools.tavily_search.tool import TavilySearchResults
from typing import List, Dict
import os

def search_company_news(company: str, max_results: int = 5) -> List[Dict]:
    """
    Search for recent news and web results about a company using SerpAPI via LangChain.

    Args:
        company (str): The company name or symbol to search for.
        max_results (int): Maximum number of search results to return.

    Returns:
        List[Dict]: List of search result dicts (title, link, snippet, etc.)
    """
    # TavilySearchResults does not require an API key via env var by default, but you can set TAVILY_API_KEY if needed.
    search_tool = TavilySearchResults()
    results = search_tool._run(company)
    # TavilySearchResults returns a list of dicts directly
    return results[:max_results] if isinstance(results, list) else []
