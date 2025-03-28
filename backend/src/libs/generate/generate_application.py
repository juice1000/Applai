import json
from pathlib import Path

from langchain.prompts import ChatPromptTemplate
from libs.db.init_db import Job
from libs.llm.init_llm import init_completion_function
from libs.llm.prompt_optimize_application import optimization_prompt
from libs.llm.prompt_write_application import application_prompt, application_prompt_de
from libs.logger.init_logger import logger


def load_cover_letters():
    cover_letters_path = (
        Path(__file__).parent.parent.parent.parent
        / "data"
        / "cover_letters"
        / "cover_letters.json"
    )
    with open(cover_letters_path) as f:
        data = json.load(f)
    return data["cover_letters"]


def adjust_tone(application: str) -> str:
    """
    Adjusts the tone of the application letter to match the style of the sample letters.
    This function is a placeholder for the actual implementation.
    """
    # Placeholder for tone adjustment logic
    # In a real-world scenario, this could involve using a language model or other NLP techniques
    # Load cover letters
    cover_letters = load_cover_letters()
    template_letter_1 = cover_letters[0]["letter"]  # Using first letter as template
    template_letter_2 = cover_letters[1]["letter"]  # Using second letter as template
    template_letter_3 = cover_letters[2]["letter"]  # Using third letter as template

    prompt_template = ChatPromptTemplate.from_template(optimization_prompt)
    # Adjust the application letter to match the tone of the template letters

    prompt = prompt_template.format(
        application_letter=application,
        template_letter_1=template_letter_1,
        template_letter_2=template_letter_2,
    )

    model = init_completion_function()
    response_text = model.invoke(prompt)

    logger.info("Application letter adjusted.")
    return response_text


def generate_application(job: Job):
    logger.info(f"Generating application for job: '{job.title}'...")

    # Extract job info
    job_description = job.description
    context = job.resume_context
    contact_person = job.contact_person

    # Prepare the prompt with cover letter template
    if job.language == "de":
        prompt_template = ChatPromptTemplate.from_template(application_prompt_de)
    else:
        prompt_template = ChatPromptTemplate.from_template(application_prompt)

    prompt = prompt_template.format(
        context=context,
        description=job_description,
        contact_person=contact_person or "",
    )

    model = init_completion_function()
    response_text = model.invoke(prompt)
    logger.info("Application generated.")

    if job.language == "en":
        # Adjust the tone of the application letter
        response_text = adjust_tone(response_text)
    return response_text
