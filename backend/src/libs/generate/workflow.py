from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph
from libs.db.init_db import Job
from libs.db.write_job import update_job
from libs.generate.generate_application import (
    adjust_tone,
    cleanup_application,
    generate_application,
    remove_misleading_info,
)
from libs.generate.retrieve_from_rag import retrieve_from_rag
from libs.generate.retrieve_language import retrieve_language
from libs.utils.load_and_save_file import save_file_to_data
from typing_extensions import TypedDict


# Graph state
class WorkflowState(TypedDict):
    job: dict
    language: str
    rag_retrieval_context: str
    application_letter: str
    cleaned_misformation_letter: str
    tone_adjusted_letter: str
    finalized_letter: str


# Wrapper
def track_and_return(name, func):
    def wrapper(state: WorkflowState, *args, **kwargs):
        result = func(state, *args, **kwargs)
        print(f"\n[{name} output]:\n", result)
        return result

    return wrapper


# Nodes
def retrieve_job_language(state: WorkflowState):
    """Retrieve language from the job description"""
    job = state["job"]
    title = job["title"]
    description = job["description"]
    # detect the language of the job description
    language = retrieve_language(title, description)
    job["language"] = language
    state["language"] = language
    return {"language": language}


def retrieve_job_experience(state: WorkflowState):
    """Retrieve job experience from the database"""
    job = state["job"]
    # retrieve the context from the resume in regards to the job description
    rag_retrieval_context = retrieve_from_rag(
        job["title"], job["description"], job["keywords"], job["language"]
    )
    job["resume_context"] = rag_retrieval_context
    return {"rag_retrieval_context": rag_retrieval_context}


def generate_application_letter(state: WorkflowState):
    """First LLM call to generate initial application letter"""
    job = state["job"]
    title = job["title"]
    description = job["description"]
    resume_context = job["resume_context"]
    contact_person = job["contact_person"]
    language = job["language"]
    # generate the application letter
    application_letter = generate_application(
        title, description, resume_context, contact_person, language
    )

    return {"application_letter": application_letter}


def remove_misinformation(state: WorkflowState):
    application_letter = state["application_letter"]
    resume_context = state["rag_retrieval_context"]
    language = state["language"]
    # delete misleading information from the application letter
    application_letter = remove_misleading_info(
        application_letter, resume_context, language
    )
    return {"cleaned_misformation_letter": application_letter}


def adjust_application_tone(state: WorkflowState):
    """Gate function to check if the joke has a punchline"""
    # Adjust the tone of the application letter
    application_letter = adjust_tone(
        state["cleaned_misformation_letter"], state["language"]
    )

    return {"tone_adjusted_letter": application_letter}


def cleanup_application_letter(state: WorkflowState):
    """Gate function to check if the joke has a punchline"""
    # Adjust the tone of the application letter
    job = state["job"]
    application_letter = cleanup_application(
        state["tone_adjusted_letter"], job["language"]
    )
    job["application_letter"] = application_letter
    return {"finalized_letter": application_letter}


def init_application_workflow() -> CompiledStateGraph:
    # Build workflow
    workflow = StateGraph(WorkflowState)

    # Add nodes
    workflow.add_node("retrieve_job_language", retrieve_job_language)
    workflow.add_node(
        "retrieve_job_experience",
        track_and_return("retrieve_job_experience", retrieve_job_experience),
    )
    workflow.add_node(
        "generate_application_letter",
        track_and_return("generate_application_letter", generate_application_letter),
    )
    workflow.add_node(
        "remove_misinformation",
        track_and_return("remove_misinformation", remove_misinformation),
    )
    workflow.add_node(
        "adjust_application_tone",
        track_and_return("adjust_application_tone", adjust_application_tone),
    )
    workflow.add_node(
        "cleanup_application_letter",
        track_and_return("cleanup_application_letter", cleanup_application_letter),
    )

    # Add edges
    workflow.add_edge(START, "retrieve_job_language")
    workflow.add_edge("retrieve_job_language", "retrieve_job_experience")
    workflow.add_edge("retrieve_job_experience", "generate_application_letter")
    workflow.add_edge("generate_application_letter", "remove_misinformation")
    workflow.add_edge("remove_misinformation", "adjust_application_tone")
    workflow.add_edge("adjust_application_tone", "cleanup_application_letter")
    workflow.add_edge("cleanup_application_letter", END)

    # Compile
    chain = workflow.compile()

    graph_path = "workflow_graph.png"
    png_graph = chain.get_graph().draw_mermaid_png()
    save_file_to_data(graph_path, png_graph)

    return chain


def run_workflow(job: Job, chain: CompiledStateGraph):
    # Convert the job object to a dictionary and pass it to the chain
    job_dict = job.model_dump()
    result = chain.invoke({"job": job_dict})

    # Save the state to the database
    job = Job(**result["job"])

    update_job(job)
