from typing import Optional

from pydantic import BaseModel, Field, PositiveInt

from src.mongodb.utils import PyMongoModelMixin, PyObjectId


class MotorcycleDetails(BaseModel, PyMongoModelMixin):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    motorcycle_id: int
    model: str
    year: PositiveInt

    class Config:
        collection_name = "motorcycle_specification"
        json_schema_extra = {
            "example": {
                "id": "65d8c068376dcb02571d7947",
                "motorcycle_id": 1,
                "model": "Leoncino Trail",
                "year": 2018,
            }
        }
