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
    parser.add_argument("--llm", default="openai", choices=["openai", "perplexity"], help="LLM provider")
    parser.add_argument("--max_results", type=int, default=5, help="Max web search results per company")
    args = parser.parse_args()

    companies = read_companies(args.input)
    os.makedirs(args.output_dir, exist_ok=True)

    for company in companies:
        print(f"Processing: {company}")
        try:
            # Tavily + OpenAI
            tavily_results = search_company_news(company, max_results=args.max_results)
            openai_summary = summarize_company_news(company, tavily_results, llm_provider="openai")

            # Perplexity search + Perplexity LLM
            perplexity_results = search_company_news_perplexity(company, max_results=args.max_results)
            perplexity_summary = summarize_company_news(company, perplexity_results, llm_provider="perplexity")

            output_path = os.path.join(args.output_dir, f"{company.replace(' ', '_')}_report.pdf")
            generate_pdf_report(company, openai_summary, perplexity_summary, output_path)
            print(f"Report saved: {output_path}")
        except Exception as e:
            print(f"Error processing {company}: {e}")

if __name__ == "__main__":
    main()
