import shutil

from custom_types import Collection
from langchain_chroma import Chroma
from libs.llm.init_llm import init_embedding_function
from libs.logger.init_logger import logger
from libs.utils.load_and_save_file import get_vector_db_path


def get_database_by_collection_name(collection_name: Collection, language: str = "en"):
    """
    Initializes the Chroma database by collection name.
    Args:
        collection_name (str): The collection name of the database.
        language (str): The language of the database.
    """
    logger.info("Initializing database...")
    chroma_path = get_vector_db_path(language)
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

    chroma_path = get_vector_db_path(language)

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


def clear_database(language: str):
    """
    Clears the Chroma database.
    Args:
        language (str): The language of the database.
    """
    logger.info("Clearing database...")
    chroma_path = get_vector_db_path(language)
    shutil.rmtree(chroma_path)
