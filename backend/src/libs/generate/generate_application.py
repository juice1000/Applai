import json

from langchain.prompts import ChatPromptTemplate
from libs.llm.init_llm import init_completion_function
from libs.llm.prompt_adjust_tone import (
    tone_adjustment_prompt_de,
    tone_adjustment_prompt_en,
)
from libs.llm.prompt_cleanup_content import cleanup_prompt_de, cleanup_prompt_en
from libs.llm.prompt_cleanup_misinformation import (
    remove_misinformation_prompt_de,
    remove_misinformation_prompt_en,
)
from libs.llm.prompt_write_application import application_prompt, application_prompt_de
from libs.logger.init_logger import logger
from libs.utils.load_and_save_file import get_cover_letters_file_path


def load_cover_letters(lang: str) -> list:
    """
    Load cover letters from JSON file based on the specified language.
    """
    file = f"cover_letters_{lang}.json"

    # Load cover letters
    with open(get_cover_letters_file_path(file), "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["cover_letters"]


def generate_application(
    title: str,
    description: str,
    resume_context: str,
    contact_person: str = None,
    lang: str = "en",
) -> str:
    logger.info(f"Generating application for job: '{title}'...")

    # Prepare the prompt with cover letter template
    if lang == "de":
        prompt_template = ChatPromptTemplate.from_template(application_prompt_de)
    else:
        prompt_template = ChatPromptTemplate.from_template(application_prompt)

    prompt = prompt_template.format(
        context=resume_context,
        description=description,
        contact_person=contact_person or "",
    )

    model = init_completion_function()
    response_text = model.invoke(prompt)
    logger.info("Application generated.")

    return response_text


def remove_misleading_info(
    application_letter: str, resume_context: str, lang: str
) -> str:
    """
    Deletes misleading information from the application letter.
    This function is a placeholder for the actual implementation.
    """
    # Prepare the prompt with cover letter template
    if lang == "de":
        prompt_template = ChatPromptTemplate.from_template(
            remove_misinformation_prompt_de
        )
    else:
        prompt_template = ChatPromptTemplate.from_template(
            remove_misinformation_prompt_en
        )

    prompt = prompt_template.format(
        application_letter=application_letter, resume_context=resume_context
    )

    model = init_completion_function()
    response_text = model.invoke(prompt)
    logger.info("Filtered out misleading information.")

    return response_text


def adjust_tone(application: str, lang: str) -> str:
    """
    Adjusts the tone of the application letter to match the style of the sample letters.
    This function is a placeholder for the actual implementation.
    """
    # Placeholder for tone adjustment logic
    # In a real-world scenario, this could involve using a language model or other NLP techniques
    # Load cover letters

    cover_letters = load_cover_letters(lang)
    template_letter_1 = cover_letters[0]["letter"]  # Using first letter as template
    template_letter_2 = cover_letters[1]["letter"]  # Using second letter as template
    template_letter_3 = cover_letters[2]["letter"]  # Using third letter as template

    if lang == "de":
        prompt_template = ChatPromptTemplate.from_template(tone_adjustment_prompt_de)
    else:
        prompt_template = ChatPromptTemplate.from_template(tone_adjustment_prompt_en)

    # Adjust the application letter to match the tone of the template letters
    prompt = prompt_template.format(
        application_letter=application,
        template_letter_1=template_letter_1,
        template_letter_2=template_letter_2,
        template_letter_3=template_letter_3,
    )

    model = init_completion_function()
    response_text = model.invoke(prompt)

    logger.info("Application letter adjusted.")
    return response_text


def cleanup_application(application: str, lang: str) -> str:
    if lang == "de":
        prompt_template = ChatPromptTemplate.from_template(cleanup_prompt_de)
    else:
        prompt_template = ChatPromptTemplate.from_template(cleanup_prompt_en)

    prompt = prompt_template.format(application_letter=application)
    model = init_completion_function()
    response_text = model.invoke(prompt)

    logger.info("Application letter finalized")
    return response_text
