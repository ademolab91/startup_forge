from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ReviewInputDTO(BaseModel):
    """DTO for creating review."""

    mentor_id: UUID
    content: str


class ReviewUpdateDTO(BaseModel):
    """DTO for updating review."""

    content: str


class ReviewDTO(ReviewInputDTO):
    """
    DTO for reviews.

    It is returned when accessing review from the API.
    """

    id: UUID
    mentor_id: UUID
    content: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
