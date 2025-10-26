import argparse
import os
import csv
from dotenv import load_dotenv

load_dotenv()

from sources.tavily_search import search_company_news
from sources.perplexity_search import search_company_news_perplexity
from summarizer.llm_summarizer import summarize_company_news
from output.pdf_report import generate_pdf_report

def read_companies(input_path):
    companies = []
    with open(input_path, "r", encoding="utf-8") as f:
        if input_path.endswith(".csv"):
            reader = csv.reader(f)
            for row in reader:
                if row:
                    # Handle both list and dict rows robustly
                    if isinstance(row, dict):
                        # If row is a dict, get the first value
                        value = next(iter(row.values()))
                    else:
                        value = row[0]
                    if isinstance(value, str):
                        companies.append(value.strip())
        else:
            for line in f:
                name = line.strip()
                if name:
                    companies.append(name)
    return companies

def main():
    parser = argparse.ArgumentParser(description="InvestChecker CLI")
    parser.add_argument("--input", required=True, help="Path to company list (CSV or TXT)")
    parser.add_argument("--output_dir", default="reports", help="Directory to save PDF reports")
    parser.add_argument(
        "--llm",
        nargs="*",
        choices=["openai", "perplexity"],
        default=None,
        help="LLM provider(s) to use. Specify one or both. If omitted, all providers are used."
    )
    parser.add_argument("--max_results", type=int, default=5, help="Max web search results per company")
    args = parser.parse_args()

    companies = read_companies(args.input)
    os.makedirs(args.output_dir, exist_ok=True)

    # Determine which providers to use based on --llm argument
    # If --llm is omitted or empty, use all providers. Otherwise, use only the selected ones.
    if args.llm is None or len(args.llm) == 0:
        providers = ["openai", "perplexity"]
    else:
        providers = args.llm

    for company in companies:
        try:
            # Initialize summaries as empty strings
            openai_summary = ""
            perplexity_summary = ""

            # Only use the selected model providers
            if "openai" in providers:
                tavily_results = search_company_news(company, max_results=args.max_results)
                openai_summary = summarize_company_news(company, tavily_results, llm_provider="openai")

            if "perplexity" in providers:
                perplexity_results = search_company_news_perplexity(company, max_results=args.max_results)
                perplexity_summary = summarize_company_news(company, perplexity_results, llm_provider="perplexity")

            output_path = os.path.join(args.output_dir, f"{company.replace(' ', '_')}_report.pdf")
            # Only the selected providers' summaries will be included in the report
            generate_pdf_report(
                company,
                openai_summary,
                perplexity_summary,
                output_path
            )
        except Exception as e:
            pass

if __name__ == "__main__":
    main()
