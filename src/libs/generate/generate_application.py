from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from libs.db.init_db import Job
from libs.llm.init_llm import init_completion_function
from libs.llm.prompts import application_prompt as PROMPT_TEMPLATE
from libs.logger.init_logger import logger


def generate_application(job: Job):
    logger.info(f"Generating application for job {job.url}...")
    # Extract the job description
    job_description = job.description
    # Extract the context
    context = job.resume_context

    # Prepare the prompt for the LLM.
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context, description=job_description)

    model = init_completion_function()
    response_text = model.invoke(prompt)
    logger.info("Application generated.")
    return response_text
