from typing import List, Dict
import os

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def summarize_company_news(
    company: str,
    search_results: List[Dict],
    llm_provider: str = "openai"
) -> str:
    """
    Summarize recent news/search results for a company using an LLM via LangChain.

    Args:
        company (str): The company name or symbol.
        search_results (List[Dict]): List of search result dicts.
        llm_provider (str): "openai" or "perplexity" (default: "openai").

    Returns:
        str: Investor-focused summary.
    """
    # Prepare context from search results
    context = ""
    for idx, result in enumerate(search_results, 1):
        context += f"{idx}. {result.get('title', '')}\n{result.get('snippet', '')}\nURL: {result.get('url', '')}\n\n"

    # Prompt template
    prompt = PromptTemplate(
        input_variables=["company", "context"],
        template=(
            "You are an expert financial analyst. Summarize the most important, up-to-date, investor-relevant information "
            "about the company '{company}' based on the following search results. Focus on news, projects, deals, IPOs, "
            "analyst recommendations, and significant social/media activity. Be concise and actionable.\n\n"
            "Search Results:\n{context}\n\nSummary:"
        )
    )

    # Select LLM
    if llm_provider == "openai":
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo")
    elif llm_provider == "perplexity":
        import requests
        perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")
        if not perplexity_api_key:
            raise ValueError("PERPLEXITY_API_KEY environment variable not set.")

        # Prepare prompt text
        prompt_text = prompt.format(company=company, context=context)

        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {perplexity_api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar-pro",  # see https://docs.perplexity.ai/getting-started/models for more options
            "messages": [
                {"role": "system", "content": "You are an expert financial analyst."},
                {"role": "user", "content": prompt_text}
            ],
            "temperature": 0.3
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            raise RuntimeError(f"Perplexity LLM API error: {response.status_code} {response.text}")
        data = response.json()
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        summary = str(content).strip()
        return summary
    else:
        raise ValueError(f"Unknown LLM provider: {llm_provider}")

    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.invoke({"company": company, "context": context})
    if isinstance(summary, dict) and "text" in summary:
        return summary["text"].strip()
    return str(summary).strip()
