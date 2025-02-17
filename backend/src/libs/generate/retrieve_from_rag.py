import os

from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from libs.llm.init_llm import init_completion_function, init_embedding_function
from libs.llm.prompt_context_retrieval import (
    rag_retrieval_prompt,
    rag_retrieval_prompt_de,
    rag_retrieval_prompt_experimental,
)
from libs.logger.init_logger import logger

# Get the project root directory (where main.py is located)
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CUR_DIR, "..", "..", ".."))
CHROMA_PATH = os.path.join(ROOT_DIR, "chroma")
CHROMA_PATH_DE = os.path.join(ROOT_DIR, "chroma_de")


def search_docs(query_text: str, language: str = "en"):
    # Prepare the DB.
    embedding_function = init_embedding_function()
    if language == "de":
        logger.info("Using German DB")
        db = Chroma(
            persist_directory=CHROMA_PATH_DE, embedding_function=embedding_function
        )
    else:
        db = Chroma(
            persist_directory=CHROMA_PATH, embedding_function=embedding_function
        )

    # Search the DB.
    db_results = db.similarity_search_with_score(query_text, k=5)
    return db_results


def get_sources(db_results):
    sources = [doc.metadata.get("id", None) for doc, _score in db_results]
    return sources


def get_context_list(db_results):
    context_list = [doc.page_content for doc, _score in db_results]
    return context_list


def get_context(db_results):
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in db_results])
    return context_text


def get_prompt_template(language: str = "en", experimental=False):
    if experimental:
        return ChatPromptTemplate.from_template(rag_retrieval_prompt_experimental)
    elif language == "de":
        return ChatPromptTemplate.from_template(rag_retrieval_prompt_de)
    else:
        return ChatPromptTemplate.from_template(rag_retrieval_prompt)


def retrieve_rag_response_from_context(
    query_text: str,
    context_text: str,
    keywords: str = "",
    language: str = "en",
    experimental=False,
):
    # Prepare the prompt for the LLM.
    prompt_template = get_prompt_template(language, experimental)
    prompt = prompt_template.format(
        context=context_text, keywords=keywords, description=query_text
    )
    model = init_completion_function()
    response_text = model.invoke(prompt)

    return response_text


def retrieve_from_rag(query_text: str, keywords: str = "", language: str = "en"):
    logger.info(f"Retrieving from RAG for query: {query_text[:100]}")
    # Search the DB for the query text
    db_results = search_docs(query_text, language)

    # Get the context from the DB results.
    context_text = get_context(db_results)
    # print("context_text", context_text)
    print("\n\n\n\n\n\n")
    # Prompt the LLM.
    response_text = retrieve_rag_response_from_context(
        query_text, context_text, keywords, language
    )

    logger.info(f"Retrieving response: {response_text}")
    return response_text


def retrieve_from_rag_experimental(query_text: str):
    # Search the DB for the query text
    db_results = search_docs(query_text)

    # Get the sources and context from the DB results.
    sources = get_sources(db_results)
    context_text = get_context(db_results)

    # Prepare the prompt for the LLM.
    response_text = retrieve_rag_response_from_context(
        query_text, context_text, experimental=True
    )

    formatted_response = f"Response: {response_text}\nSources: {sources}\n\n"
    logger.info(f"Retrieving response: {formatted_response[:100]}")
    return response_text
