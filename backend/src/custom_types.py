from typing import List, Literal, Optional

from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str


class JobUpdate(BaseModel):
    status: str


class FieldRequest(BaseModel):
    field_name: str
    field_type: Literal["INTEGER", "TEXT", "BOOLEAN"]


class ColumnInfo(BaseModel):
    name: str
    type: str
    notnull: bool


class TableSchema(BaseModel):
    columns: List[ColumnInfo]
