import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from misc.mock_data import input_output_pairs
from misc.rag_eval_metrics import evaluation_metrics

# Importing the RAG application
from src.libs.generate.generate import (
    generate_response_from_context,
    get_context,
    get_context_list,
    search_docs,
)

# https://www.confident-ai.com/blog/how-to-evaluate-rag-applications-in-ci-cd-pipelines-with-deepeval
# https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation


#######################################
# Loop through input output pairs #####
#######################################
@pytest.mark.parametrize(
    "input_output_pair",
    input_output_pairs,
)
def test_llamaindex(input_output_pair: dict):
    input = input_output_pair.get("input", None)
    expected_output = input_output_pair.get("expected_output", None)

    # getting the retrieval context at evaluation time for each input
    db_results = search_docs(input)
    retrieval_context_list = get_context_list(db_results)
    retrieval_context = get_context(db_results)
    actual_output = generate_response_from_context(input, retrieval_context)
    test_case = LLMTestCase(
        input=input,
        actual_output=actual_output,
        retrieval_context=retrieval_context_list,
        expected_output=expected_output,
    )
    # assert test case
    # print("test_case", test_case)
    assert_test(test_case, evaluation_metrics)
