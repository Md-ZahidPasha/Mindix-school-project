from typing import Any

from pydantic import BaseModel, Field


class DocumentExtractionResponse(BaseModel):
    document_type: str = Field(
        description="The detected type/category of the document"
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="AI confidence score from 0 to 1"
    )

    data: dict[str, Any] = Field(
        default_factory=dict,
        description="Dynamically extracted information from the document"
    )