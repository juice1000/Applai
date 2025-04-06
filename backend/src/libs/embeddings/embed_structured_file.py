import json

from libs.embeddings.init_chroma import init_databases
from libs.logger.init_logger import logger
from libs.utils.load_and_save_file import get_input_file_path


def load_document(language: str = "en"):
    """
    Load the resume document.
    Args:
        language (str): The language of the document.
    Returns:
        dict: The resume document.
    """
    with open(
        get_input_file_path(f"resume.{language}.json"), "r", encoding="utf-8"
    ) as f:
        resume_data = json.load(f)

    return resume_data


def embed_file(language: str = "en"):
    logger.info("Embedding document...")

    # Initialize ChromaDB client
    db_projects, db_technologies, db_global_information = init_databases(language)

    resume = load_document(language)

    # Add each experience to ChromaDB with Ollama embeddings
    projects_stringified = [
        (
            f"Title: {proj['title']}\n"
            f"Role: {proj['role']}\n"
            f"Company: {proj['company']}\n"
            f"Period: {proj['period']}\n"
            f"Year: {proj['year']}\n"
            f"Description: {proj['description']}\n"
            f"Technologies: {', '.join(proj['technologies'])}"
        )
        for proj in resume["projects"]
    ]
    projects_metadata = [
        {
            "title": proj["title"],
            "role": proj["role"],
            "company": proj["company"],
            "period": proj["period"],
            "year": proj["year"],
            "description": proj["description"],
            "technologies": ", ".join(proj["technologies"]),
        }
        for proj in resume["projects"]
    ]

    # Store in ChromaDB
    db_projects.add_texts(
        texts=projects_stringified,
        metadatas=projects_metadata,
    )

    logger.info("Projects added to ChromaDB")
