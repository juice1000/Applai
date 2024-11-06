from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

engine = create_engine("sqlite:///./job-applications.db")


class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    url: str
    description: str
    date_applied: str
    resume_context: str
    application_letter: str = None


def initialize_db():
    global engine
    SQLModel.metadata.create_all(engine)
