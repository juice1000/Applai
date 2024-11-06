from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

Settings.llm = Ollama(model="llama3.2", request_timeout=120.0)
# bge-base embedding model
Settings.embed_model = OllamaEmbedding(
    model_name="nomic-embed-text",
    # base_url="http://localhost:11434",
    ollama_additional_kwargs={"mirostat": 0},
)

# Consult the LlamaIndex docs if you're unsure what this does
documents = SimpleDirectoryReader("./data/input").load_data()
index = VectorStoreIndex.from_documents(documents)
rag_application = index.as_query_engine()


# An example input to your RAG application
user_input = "What is LlamaIndex?"

# LlamaIndex returns a response object that contains
# both the output string and retrieved nodes
response_object = rag_application.query(user_input)

# Process the response object to get the output string
# and retrieved nodes
if response_object is not None:
    actual_output = response_object.response
    retrieval_context = [node.get_content() for node in response_object.source_nodes]

# Create a test case and metric as usual
test_case = LLMTestCase(
    input=user_input, actual_output=actual_output, retrieval_context=retrieval_context
)
answer_relevancy_metric = AnswerRelevancyMetric()

# Evaluate
print(test_case)
answer_relevancy_metric.measure(test_case)
print(answer_relevancy_metric.score)
print(answer_relevancy_metric.reason)
