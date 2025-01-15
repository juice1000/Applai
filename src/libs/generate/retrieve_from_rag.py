from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma

from libs.llm.init_llm import init_completion_function, init_embedding_function
from libs.llm.prompts import rag_retrieval_prompt, rag_retrieval_prompt_experimental
from libs.logger.init_logger import logger

CHROMA_PATH = "chroma"


def search_docs(query_text: str):
    # Prepare the DB.
    embedding_function = init_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

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


def retrieve_rag_response_from_context(
    query_text: str, context_text: str, experimental=False
):
    # Prepare the prompt for the LLM.
    if experimental:
        prompt_template = ChatPromptTemplate.from_template(
            rag_retrieval_prompt_experimental
        )
    else:
        prompt_template = ChatPromptTemplate.from_template(rag_retrieval_prompt)

    prompt = prompt_template.format(context=context_text, description=query_text)

    model = init_completion_function()
    response_text = model.invoke(prompt)

    return response_text


def retrieve_from_rag(query_text: str):
    # Search the DB for the query text
    db_results = search_docs(query_text)

    # Get the context from the DB results.
    context_text = get_context(db_results)

    # Prompt the LLM.
    response_text = retrieve_rag_response_from_context(query_text, context_text)
    return response_text


def retrieve_from_rag_experimental(query_text: str):
    logger.info(f"Retrieving response for query: {query_text}")
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
    print(formatted_response)
    return response_text
