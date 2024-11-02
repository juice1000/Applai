from langchain_ollama import OllamaEmbeddings


def init_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
