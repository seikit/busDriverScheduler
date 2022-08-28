from datetime import datetime, date
from typing import List

from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from app.models.Schedule import ScheduleModel
from app.schemas.Schedule import ScheduleSchema, ScheduleDb


class ScheduleRepository:
    def __init__(self, session: Session):
        self.db = session

    def post(self, payload: ScheduleSchema) -> ScheduleDb:
        schedule_model = ScheduleModel(**payload.dict())
        self.db.add(schedule_model)
        self.db.commit()
        self.db.refresh(schedule_model)
        return schedule_model

    def get(self, id: int) -> ScheduleDb:
        return self.db.query(ScheduleModel).filter(ScheduleModel.id == id).first()

    def get_schedule_between(self, start_dt: date, end_dt: date) -> List[ScheduleDb]:
        return self.db.query(ScheduleModel).filter(or_(func.DATE(ScheduleModel.start_dt) >= start_dt,
                                                   func.DATE(ScheduleModel.start_dt) <= end_dt)).all()

    def update(self, schedule_model: ScheduleModel, payload: ScheduleSchema) -> ScheduleDb:
        schedule_model.bus_id = payload.bus_id
        schedule_model.driver_id = payload.driver_id
        schedule_model.start_dt = payload.start_dt
        schedule_model.end_dt = payload.end_dt
        self.db.commit()
        return schedule_model

    def delete(self, schedule_model: ScheduleModel) -> None:
        self.db.delete(schedule_model)
        self.db.commit()
