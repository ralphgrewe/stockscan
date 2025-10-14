import os
import requests
from typing import List, Dict

def search_company_news_perplexity(company: str, max_results: int = 5) -> List[Dict]:
    """
    Search for recent news and web results about a company using Perplexity API.

    Args:
        company (str): The company name or symbol to search for.
        max_results (int): Maximum number of search results to return.

    Returns:
        List[Dict]: List of search result dicts (title, url, snippet, etc.)
    """
    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        raise ValueError("PERPLEXITY_API_KEY environment variable not set.")

    url = "https://api.perplexity.ai/search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "query": company,
        "num_results": max_results
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print("Perplexity API call failed.")
        print("Status code:", response.status_code)
        print("Response text:", response.text)
        print("Request payload:", payload)
        print("Request headers:", headers)
        raise RuntimeError(f"Perplexity API error: {response.status_code} {response.text}")

    data = response.json()
    # Normalize results to match Tavily format
    results = []
    for item in data.get("results", []):
        results.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "snippet": item.get("snippet", item.get("text", "")),
        })
    return results[:max_results]
