import json
import shutil
from os.path import abspath, dirname, exists, join

from langchain.schema.document import Document
from langchain_chroma import Chroma
from libs.llm.init_llm import init_embedding_function
from libs.logger.init_logger import logger

# Get the project root directory (where main.py is located)
CUR_DIR = dirname(abspath(__file__))
ROOT_DIR = abspath(join(CUR_DIR, "..", "..", ".."))
CHROMA_PATH = join(ROOT_DIR, "chroma")
CHROMA_PATH_DE = join(ROOT_DIR, "chroma_de")
DATA_PATH = join(ROOT_DIR, "data")
COLLECTION_NAME = "resume_embeddings"


def load_document(language: str = "en"):
    """
    Load the resume document.
    Args:
        language (str): The language of the document.
    Returns:
        dict: The resume document.
    """
    if language == "de":
        with open("resume.de.json", "r", encoding="utf-8") as f:
            resume_data = json.load(f)
    else:
        with open("resume.json", "r", encoding="utf-8") as f:
            resume_data = json.load(f)
    return resume_data


def clear_database(language: str = "en"):
    """
    Clears the Chroma database.
    Args:
        language (str): The language of the database.
    """
    logger.info("Clearing database...")
    if language == "de" and exists(CHROMA_PATH_DE):
        shutil.rmtree(CHROMA_PATH_DE)
    elif language == "en" and exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)


def embed_file(
    clear: bool = False,
    language: str = "en",
):
    logger.info("Embedding document...")
    if clear:
        clear_database(language)

    # Initialize ChromaDB client
    if language == "de":
        db = Chroma(
            persist_directory=CHROMA_PATH_DE,
            embedding_function=init_embedding_function(),
            collection_name=COLLECTION_NAME,
        )
    else:
        db = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=init_embedding_function(),
            collection_name=COLLECTION_NAME,
        )

    resume = load_document(language)

    # Add each experience to ChromaDB with Ollama embeddings
    projects_stringified = [
        (
            f"Title: {proj['title']}\n"
            f"Role: {proj['role']}\n"
            f"Company: {proj['company']}\n"
            f"Dates: {proj['dates']}\n"
            f"Description: {proj['description']}\n"
            f"Technologies: {', '.join(proj['technologies'])}"
        )
        for proj in resume["projects"]
    ]

    # Store in ChromaDB
    db.add_texts(
        ids=[range(len(projects_stringified))],
        texts=[projects_stringified],
        metadatas=resume["projects"],
    )
