from pydantic import BaseModel, Field
from datetime import date


class ScheduleSchema(BaseModel):
    bus_id: int = Field(gt=0)
    driver_id: int = Field(gt=0)
    shift: date


class ScheduleDb(ScheduleSchema):
    id: int

    class Config:
        orm_mode = True
