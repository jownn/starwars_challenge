from bson import ObjectId
from pydantic import BaseModel, Field, field_validator
from typing import List
from datetime import datetime


class PlanetModel(BaseModel):
    id: ObjectId = Field(ObjectId, alias="_id")
    name: str
    climate: str
    diameter: int
    population: int | None = None
    films: List[ObjectId] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @field_validator("films", mode="before")
    def transform(cls, raw: list[str] | list[ObjectId]) -> list[ObjectId]:
        return [ObjectId(r) for r in raw]

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True
