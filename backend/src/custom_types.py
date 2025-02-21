from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str


class JobField(str, Enum):
    status = "status"
    application_letter = "application_letter"


class UpdateJobRequest(BaseModel):
    field_name: JobField
    update_value: str


class FieldRequest(BaseModel):
    field_name: str
    field_type: Literal["INTEGER", "TEXT", "BOOLEAN"]


class ColumnInfo(BaseModel):
    name: str
    type: str
    notnull: bool


class TableSchema(BaseModel):
    columns: List[ColumnInfo]


class Language(str, Enum):
    de = "de"
    en = "en"


class Collection(str, Enum):
    PROJECTS = "project_embeddings"
    TECHNOLOGIES = "technology_embeddings"
    PERSONAL = "personal_embeddings"
