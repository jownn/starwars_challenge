from bson import ObjectId
from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class MovieModel(BaseModel):
    id: ObjectId = Field(ObjectId, alias="_id")
    title: str
    release_date: datetime
    director: str
    planets: list[ObjectId] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @field_validator("planets", mode="before")
    def transform(cls, raw: list[str] | list[ObjectId]) -> list[ObjectId]:
        return [ObjectId(r) for r in raw]

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True

