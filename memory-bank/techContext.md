# Tech Context

**Purpose:**  
Describes the technologies used, development setup, technical constraints, dependencies, and tool usage patterns.

---

## Technologies Used
- [x] Python for core logic and orchestration
- [x] FPDF library for PDF report generation
- [x] DejaVuSans Unicode font for full Unicode character support in PDF output

## Development Setup
- [ ] Document environment setup and configuration

## Technical Constraints
- [x] PDF reports require Unicode font (DejaVuSans.ttf) to support non-ASCII characters.
- [x] Output directory for PDF reports must exist or be created at runtime.

## Dependencies
- [x] fpdf (Python package)
- [x] DejaVuSans.ttf (included in output/dejavu-fonts-ttf-2.37/ttf/)

## Tool Usage Patterns
- [x] PDF reports are generated using FPDF, with DejaVuSans font added for Unicode support.
- [x] Reports include OpenAI and Perplexity analyses if provided.
- [x] Output directory is created automatically if it does not exist.

---

_Last updated: 2025-10-26_
