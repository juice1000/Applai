from langchain.schema.document import Document
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from libs.logger.init_logger import logger
from libs.utils.load_and_save_file import get_input_file_path, load_vector_db


def load_document(language: str = "en") -> list[Document]:
    """
    Load the resume document using a relative path from the project root.

    Returns:
        list[Document]: A list containing the loaded document
    """
    resume_path = get_input_file_path(f"resume.{language}.md")
    logger.info(f"Loading document from: {resume_path}")

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
    db = load_vector_db(language)

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


def embed_document(language: str = "en"):
    """
    Embeds the resume document into the Chroma database.
    Args:
        language (str): The language of the document.
    """
    logger.info("Embedding document...")
    documents = load_document(language)
    chunks = split_documents(documents)
    add_to_chroma(chunks, language)
