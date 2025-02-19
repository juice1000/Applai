from langchain.prompts import ChatPromptTemplate
from libs.db.init_db import Job
from libs.llm.init_llm import init_completion_function
from libs.llm.prompt_write_application import application_prompt, application_prompt_de
from libs.logger.init_logger import logger


def generate_application(job: Job):
    logger.info(f"Generating application for job: '{job.title}'...")
    # Extract the job description
    job_description = job.description
    # Extract the context
    context = job.resume_context
    # Extract the keywords
    keywords = job.keywords
    # Extract the contact person
    contact_person = job.contact_person
    # Prepare the prompt for the LLM.
    if job.language == "de":
        prompt_template = ChatPromptTemplate.from_template(application_prompt_de)
    else:
        prompt_template = ChatPromptTemplate.from_template(application_prompt)

    prompt = prompt_template.format(
        context=context,
        description=job_description,
        keywords=keywords,
        contact_person=contact_person or "",
    )

    model = init_completion_function()
    response_text = model.invoke(prompt)
    logger.info("Application generated.")
    return response_text
