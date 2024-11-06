from langchain_ollama import OllamaEmbeddings, OllamaLLM


def init_completion_function():
    completion_llm = OllamaLLM(model="llama3.2")
    return completion_llm


def init_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
