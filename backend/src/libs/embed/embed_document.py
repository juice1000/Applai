import os
import shutil

from langchain.schema.document import Document
from langchain_chroma import Chroma
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from libs.llm.init_llm import init_embedding_function
from libs.logger.init_logger import logger

# Get the project root directory (where main.py is located)
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CUR_DIR, "..", "..", ".."))
CHROMA_PATH = os.path.join(ROOT_DIR, "chroma")
CHROMA_PATH_DE = os.path.join(ROOT_DIR, "chroma_de")
DATA_PATH = os.path.join(ROOT_DIR, "data")


def load_document(language: str = "en") -> list[Document]:
    """
    Load the resume document using a relative path from the project root.

    Returns:
        list[Document]: A list containing the loaded document
    """

    if language == "de":
        resume_path = os.path.join(ROOT_DIR, "data", "input", "resume.de.md")
    else:
        resume_path = os.path.join(ROOT_DIR, "data", "input", "resume.en.md")
    logger.info(f"Loading document from: {resume_path}")

    if not os.path.exists(resume_path):
        logger.error(f"Resume file not found at: {resume_path}")
        raise FileNotFoundError(f"Resume file not found at: {resume_path}")

    loader = UnstructuredMarkdownLoader(resume_path)
    documents = loader.load()
    return documents


def split_documents(documents: list[Document]):
    """
    Splits a list of documents into smaller chunks using the RecursiveCharacterTextSplitter.
    Args:
        documents (list[Document]): A list of Document objects to be split.
    Returns:
        list: A list of smaller chunks obtained from the original documents.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)


def calculate_chunk_ids(chunks: list[Document]) -> list[Document]:

    # This will create IDs like "data/monopoly.pdf:6:2"
    # Page Source : Page Number : Chunk Index

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id

    return chunks


def add_to_chroma(chunks: list[Document], language: str = "en"):
    """
    Adds new document chunks to the Chroma database if they do not already exist.
    Args:
        chunks (list[Document]): A list of Document objects to be added to the database.
    Returns:
        None
    """
    # Load the existing database.
    if language == "de":
        db = Chroma(
            persist_directory=CHROMA_PATH_DE,
            embedding_function=init_embedding_function(),
        )
    else:
        db = Chroma(
            persist_directory=CHROMA_PATH, embedding_function=init_embedding_function()
        )

    # Calculate Page IDs.
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
    else:
        print("✅ No new documents to add")


def clear_database(language: str = "en"):
    """
    Clears the Chroma database.
    Args:
        language (str): The language of the database.
    """
    logger.info("Clearing database...")
    if language == "de" and os.path.exists(CHROMA_PATH_DE):
        shutil.rmtree(CHROMA_PATH_DE)
    elif language == "en" and os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)


def embed_document(clear: bool = False, language: str = "en"):
    """
    Embeds the resume document into the Chroma database.
    Args:
        clear (bool): If True, the database will be cleared before adding the document.
        language (str): The language of the document.
    """
    logger.info("Embedding document...")
    if clear:
        clear_database(language)

    documents = load_document(language)
    chunks = split_documents(documents)
    add_to_chroma(chunks, language)
