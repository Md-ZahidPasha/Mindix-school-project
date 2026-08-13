from typing import Any

from pydantic import BaseModel


class AIChatRequest(BaseModel):
    message: str


class AIChatResponse(BaseModel):
    status: str
    answer: str
    role: str | None = None
    institution_id: str | None = None