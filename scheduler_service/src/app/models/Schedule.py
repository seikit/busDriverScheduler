from sqlalchemy import Column, Integer, Date, Enum
from app.config.database import Base


class ScheduleModel(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True)
    bus_id = Column(Integer)
    driver_id = Column(Integer)
    shift = Column(Date)
