# stockscan
An application to scan stock information using LLM's - a first test using Cline for programming

## Font Setup for PDF Reports

This project generates PDF reports using DejaVu fonts. After cloning the repository, you must download the required font files.

**To download and extract the fonts, run:**
```bash
bash scripts/download_fonts.sh
```

This will download and extract the DejaVu fonts into the correct directory for PDF generation.

## Environment Variables

This project requires secret API keys to function. These keys should be stored in a `.env` file in the project root.

1. Copy the example file:
   ```bash
   cp env.example .env
   ```
2. Open `.env` and fill in your secret keys for each variable.

**Do NOT commit your `.env` file to version control.** The `.env` file is already included in `.gitignore`.
