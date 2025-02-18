import json
from os.path import abspath, dirname, join


def parse_markdown_resume(md_file):
    """
    Reads a Markdown resume file and converts it into structured JSON.
    """
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    resume_data = {"name": "", "role": "", "contact": {}, "skills": {}, "projects": []}

    current_section = None
    current_project = None

    for line in lines:
        line = line.strip()

        # Extract name and role from the title
        if line.startswith("# "):
            resume_data["name"] = line[2:].strip()
        elif line.startswith("## "):
            section = line[3:].strip().lower()
            if "skills" in section:
                current_section = "skills"
                resume_data["skills"] = {}
            elif "contact" in section:
                current_section = "contact"
                resume_data["contact"] = {}
            elif "projects" in section:
                current_section = "projects"
            else:
                current_section = None
        elif current_section == "contact" and ":" in line:
            key, value = line.split(":", 1)
            resume_data["contact"][key.strip().lower()] = value.strip()
        elif current_section == "skills" and ":" in line:
            key, value = line.split(":", 1)
            resume_data["skills"][key.strip().lower()] = [
                tech.strip() for tech in value.split(",")
            ]
        elif current_section == "projects" and line.startswith("### "):
            if current_project:
                resume_data["projects"].append(current_project)
            current_project = {"title": line[4:].strip()}
        elif current_section == "projects" and current_project:
            if line.startswith("- **Role:**"):
                current_project["role"] = line.replace("- **Role:**", "").strip()
            elif line.startswith("- **Company:**"):
                current_project["company"] = line.replace("- **Company:**", "").strip()
            elif line.startswith("- **Dates:**"):
                current_project["dates"] = line.replace("- **Dates:**", "").strip()
            elif line.startswith("- **Description:**"):
                current_project["description"] = line.replace(
                    "- **Description:**", ""
                ).strip()
            elif line.startswith("- **Technologies:**"):
                current_project["technologies"] = [
                    tech.strip()
                    for tech in line.replace("- **Technologies:**", "").split(",")
                ]

    if current_project:
        resume_data["projects"].append(current_project)

    return resume_data


def save_json(data, output_file):
    """
    Saves structured resume data into a JSON file.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    # Get the project root directory (where main.py is located)
    CUR_DIR = dirname(abspath(__file__))
    ROOT_DIR = abspath(join(CUR_DIR, "..", "..", ".."))
    DATA_PATH = join(ROOT_DIR, "data", "input")

    md_file = join(DATA_PATH, "resume.md")  # Replace with your actual Markdown file
    output_json = join(DATA_PATH, "resume.json")

    resume_json = parse_markdown_resume(md_file)
    save_json(resume_json, output_json)

    print(f"✅ Resume converted and saved to {output_json}")
