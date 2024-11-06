import os

from deepeval.metrics import AnswerRelevancyMetric, BiasMetric, FaithfulnessMetric
from deepeval.metrics.ragas import (
    RAGASContextualPrecisionMetric,
    RAGASContextualRecallMetric,
    RAGASFaithfulnessMetric,
)

# initialize model
# os.environ["OPENAI_API_BASE"] = "http://localhost:11434/"
# os.environ["OPENAI_API_KEY"] = "ollama"

#######################################
# Initialize metrics with thresholds ##
#######################################
bias = BiasMetric(threshold=0.5)
contextual_precision = RAGASContextualPrecisionMetric(threshold=0.5)
contextual_recall = RAGASContextualRecallMetric(threshold=0.5)
faithfulness = FaithfulnessMetric(threshold=0.5)
answer_relevancy = AnswerRelevancyMetric(threshold=0.5)


#######################################
# Specify evaluation metrics to use ###
#######################################
evaluation_metrics = [
    bias,
    # contextual_precision,
    # contextual_recall,
    # faithfulness,
    answer_relevancy,
]
