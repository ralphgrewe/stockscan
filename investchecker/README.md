# InvestChecker

A modular Python CLI app to gather and summarize up-to-date investor-relevant information about companies and stocks using LLMs and web search.

## Features

- Input: List of companies (symbols and/or names)
- Data sources: Web search via Tavily (more sources can be added)
- Summarization: OpenAI/Perplexity LLMs via LangChain
- Output: PDF report (via LangChain)
- Extensible: Add new sources, LLMs, or output formats easily

## Quick Start

1. (Recommended) Create and activate a Python virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies inside the virtual environment:
   ```
   pip install -r requirements.txt
   ```

   > Using a virtual environment helps keep dependencies isolated and avoids conflicts with other Python projects.

2. Set your API keys in `config.py`.

3. Run the CLI:
   ```
   python investchecker/main.py --input companies.csv
   ```

## Project Structure

- `main.py` - CLI entry point
- `config.py` - API keys and settings
- `input_handler.py` - Reads company list
- `sources/` - Data source connectors (e.g., Tavily)
- `summarizer/` - LLM summarization logic
- `output/` - PDF report generation
- `utils.py` - Shared utilities

## Requirements

- Python 3.9+
- LangChain
- Tavily
- OpenAI/Perplexity API keys
