from typing import Optional

from libs.logger.init_logger import logger
from sqlmodel import Field, SQLModel, create_engine

engine = create_engine("sqlite:///./jobs.db")


class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    url: str
    description: str
    keywords: str = None
    date_applied: Optional[str] = None
    resume_context: Optional[str] = None
    application_letter: Optional[str] = None
    status: Optional[str] = None


def initialize_db():
    logger.info("Initializing database...")
    global engine
    SQLModel.metadata.create_all(engine)
    logger.info("Database initialized.")
