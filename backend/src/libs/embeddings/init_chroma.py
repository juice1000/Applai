import shutil
from os.path import abspath, dirname, exists, join

from custom_types import Collection
from langchain_chroma import Chroma
from libs.llm.init_llm import init_embedding_function
from libs.logger.init_logger import logger

# Get the project root directory (where main.py is located)
CUR_DIR = dirname(abspath(__file__))
ROOT_DIR = abspath(join(CUR_DIR, "..", "..", ".."))
CHROMA_PATH = join(ROOT_DIR, "chroma")
CHROMA_PATH_DE = join(ROOT_DIR, "chroma_de")
DATA_PATH = join(ROOT_DIR, "data", "input")


def get_database_by_collection_name(collection_name: Collection, language: str = "en"):
    """
    Initializes the Chroma database by collection name.
    Args:
        collection_name (str): The collection name of the database.
        language (str): The language of the database.
    """
    logger.info("Initializing database...")
    chroma_path = CHROMA_PATH_DE if language == "de" else CHROMA_PATH
    db = Chroma(
        persist_directory=chroma_path,
        embedding_function=init_embedding_function(),
        collection_name=collection_name,
    )

    return db


def init_databases(language: str = "en"):
    """
    Initializes the Chroma database.
    Args:
        language (str): The language of the database because we have one database for each language.
    """
    logger.info("Initializing database...")

    chroma_path = CHROMA_PATH_DE if language == "de" else CHROMA_PATH

    db_projects = Chroma(
        persist_directory=chroma_path,
        embedding_function=init_embedding_function(),
        collection_name=Collection.PROJECTS,
    )
    db_technologies = Chroma(
        persist_directory=chroma_path,
        embedding_function=init_embedding_function(),
        collection_name=Collection.TECHNOLOGIES,
    )
    db_personal = Chroma(
        persist_directory=chroma_path,
        embedding_function=init_embedding_function(),
        collection_name=Collection.PERSONAL,
    )

    return db_projects, db_technologies, db_personal


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
