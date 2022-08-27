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

    def get(self, id: int):
        return self.db.query(ScheduleModel).filter(ScheduleModel.id == id).first()

    def update(self, schedule_model: ScheduleModel, payload: ScheduleSchema) -> ScheduleDb:
        schedule_model.bus_id = payload.bus_id
        schedule_model.driver_id = payload.driver_id
        schedule_model.shift = payload.shift
        self.db.commit()
        return schedule_model

    def delete(self, schedule_model: ScheduleModel) -> None:
        self.db.delete(schedule_model)
        self.db.commit()
