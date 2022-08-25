from typing import Optional

from pydantic import BaseModel, Field


class BusSchema(BaseModel):
    capacity: int = Field(gt=0)
    model: str = Field(max_length=100)
    maker: str = Field(max_length=100)
    driver_id: int


class BusDb(BusSchema):
    id: int

    class Config:
        orm_mode = True
