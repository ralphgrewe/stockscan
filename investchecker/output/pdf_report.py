from fpdf import FPDF
import os

def generate_pdf_report(company: str, openai_summary: str, perplexity_summary: str, output_path: str):
    """
    Generate a PDF report for a company with both OpenAI and Perplexity analyses.

    Args:
        company (str): The company name or symbol.
        openai_summary (str): The OpenAI summary text.
        perplexity_summary (str): The Perplexity summary text.
        output_path (str): Path to save the PDF file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Investor Report: {company}", ln=True, align="C")
    pdf.ln(10)

    # OpenAI Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "OpenAI Analysis", ln=True)
    pdf.set_font("Arial", "", 12)
    for line in openai_summary.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf.ln(5)

    # Perplexity Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Perplexity Analysis", ln=True)
    pdf.set_font("Arial", "", 12)
    for line in perplexity_summary.split('\n'):
        pdf.multi_cell(0, 10, line)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
