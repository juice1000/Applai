import requests
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from libs.logger.init_logger import logger


def check_ollama_health():
    """Check if Ollama server is running"""
    try:
        response = requests.get("http://localhost:11434")
        return (
            response.text == "Ollama is running"
        )  # TODO: this is quite error prone, better start ollama as a conjunction to the backend
    except requests.exceptions.ConnectionError:
        return False


def init_llm_services():
    """Initialize LLM services and check availability"""
    if not check_ollama_health():
        error_msg = "Ollama server is not running. Please start Ollama first."
        logger.error(error_msg)
        raise RuntimeError(error_msg)

    logger.info("Ollama server is running")
    return True


def init_completion_function():
    completion_llm = OllamaLLM(model="gemma3:12b")
    return completion_llm


def init_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
