import re
from os.path import abspath, dirname, join

import pdfplumber

skills_categories = [
    "Data Science & Machine Learning",
    "Frontend Development",
    "Programming Languages",
    "Software Architecture/ Deployment",
    "Backend Development",
    "Languages",
]


def extract_text_from_pdf(pdf_path):
    """Extracts structured text from a given PDF file."""
    text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text.append(extracted_text)

    return "\n".join(text).strip()


def format_as_markdown(text):
    """Converts raw PDF text into a structured Markdown resume."""
    lines = text.split("\n")
    markdown_lines = []
    current_section = None
    skills_section_found = False
    current_skill_category = None

    for line in lines:
        line = line.strip()

        # Extract name & role
        if re.match(r"^[A-Za-z\s]+$", line) and not current_section:
            markdown_lines.append(f"# {line}")
            current_section = "header"

        elif "LinkedIn:" in line or "Github:" in line:
            markdown_lines.append(
                f"- **{line.split(':')[0]}:** {line.split(':')[1].strip()}:{line.split(':')[2].strip()}"
            )

        # Identify sections
        elif "SKILLS" in line.upper():
            markdown_lines.append("\n## Skills\n")
            current_section = "skills"
            skills_section_found = True

        elif "EXPERIENCE" in line.upper():
            markdown_lines.append("\n## Experience\n")
            current_section = "experience"
            skills_section_found = False
        elif "EDUCATION" in line.upper():
            markdown_lines.append("\n## Education\n")
            current_section = "education"
            skills_section_found = False
        elif "PROJECTS" in line.upper():
            markdown_lines.append("\n## Projects\n")
            current_section = "projects"
            skills_section_found = False

        # Extract skills if inside the skills section
        elif skills_section_found:
            if line in skills_categories:
                if current_skill_category:
                    markdown_lines.append(current_skill_category)
                else:
                    current_skill_category = f"- **{line}:**"
            else:
                current_skill_category.join(f" {line}")

        # Extract experience
        elif current_section == "projects":
            parts = re.split(r",\s*", line)
            if len(parts) >= 3:
                markdown_lines.append(f"\n### {parts[0]}")
                markdown_lines.append(f"- **Role:** {parts[1]}")
                markdown_lines.append(f"- **Company:** {parts[2]}")
                markdown_lines.append(f"- **Dates:** {parts[-1]}")

        elif current_section == "projects" and line.startswith("⬩"):
            markdown_lines.append(f"- {line.replace('⬩', '').strip()}")

    return "\n".join(markdown_lines)


def save_markdown(md_text, output_path):
    """Saves formatted Markdown to a file."""
    with open(output_path, "w", encoding="utf-8") as md_file:
        md_file.write(md_text)


def convert_pdf_to_markdown(pdf_path, output_md_path):
    """Full pipeline: Extract text, convert to Markdown, and save."""
    print(f"Extracting text from: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)

    print("Formatting text as Markdown...")
    markdown_text = format_as_markdown(text)

    print(f"Saving Markdown file to: {output_md_path}")
    save_markdown(markdown_text, output_md_path)

    print("✅ Conversion complete!")


# Get the project root directory (where main.py is located)
CUR_DIR = dirname(abspath(__file__))
ROOT_DIR = abspath(join(CUR_DIR, "..", "..", ".."))
DATA_PATH = join(ROOT_DIR, "data", "input")

# Example usage
pdf_file = join(DATA_PATH, "resume.pdf")  # Replace with your actual PDF file path
markdown_output = join(DATA_PATH, "resume.md")

convert_pdf_to_markdown(pdf_file, markdown_output)
