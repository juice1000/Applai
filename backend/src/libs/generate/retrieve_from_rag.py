from langchain.prompts import ChatPromptTemplate
from libs.embeddings.init_chroma import init_databases
from libs.llm.init_llm import init_completion_function
from libs.llm.prompt_context_retrieval import (
    project_retrieval_prompt_de,
    project_retrieval_prompt_en,
    project_retrieval_prompt_experimental,
)
from libs.logger.init_logger import logger


def search_docs(job_title: str, keywords: str, language: str = "en"):
    # Prepare the DB.
    db_projects, db_technologies, db_global_information = init_databases(language)

    # Search the DB.
    query_text = f"Job Title: {job_title}\nKeywords: {keywords}"
    db_results = db_projects.similarity_search_with_score(query_text, k=5)
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
        return ChatPromptTemplate.from_template(project_retrieval_prompt_experimental)
    elif language == "de":
        return ChatPromptTemplate.from_template(project_retrieval_prompt_de)
    else:
        return ChatPromptTemplate.from_template(project_retrieval_prompt_en)


def retrieve_rag_response_from_context(
    job_description: str,
    context_text: str,
    keywords: str = "",
    language: str = "en",
    experimental=False,
):
    # Prepare the prompt for the LLM.
    prompt_template = get_prompt_template(language, experimental)
    prompt = prompt_template.format(
        context=context_text, keywords=keywords, description=job_description
    )
    model = init_completion_function()
    response_text = model.invoke(prompt)

    return response_text


def retrieve_from_rag(
    job_title: str, job_description: str, keywords: str = "", language: str = "en"
):
    logger.info(f"Retrieving from RAG for description: {job_description[:100]}")
    # Search the DB for the query text
    db_results = search_docs(job_title, keywords, language)

    # Get the context from the DB results.
    context_text = get_context(db_results)
    # Prompt the LLM.
    response_text = retrieve_rag_response_from_context(
        job_description, context_text, keywords, language
    )
    # logger.info(f"Retrieving response: {response_text}")
    return response_text


# def retrieve_from_rag_experimental(query_text: str):
#     # Search the DB for the query text
#     db_results = search_docs(query_text)

#     # Get the sources and context from the DB results.
#     sources = get_sources(db_results)
#     context_text = get_context(db_results)

#     # Prepare the prompt for the LLM.
#     response_text = retrieve_rag_response_from_context(
#         query_text, context_text, experimental=True
#     )

#     formatted_response = f"Response: {response_text}\nSources: {sources}\n\n"
#     logger.info(f"Retrieving response: {formatted_response[:100]}")
#     return response_text
