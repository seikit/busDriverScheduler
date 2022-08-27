import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.ScheduleRepository import ScheduleRepository
from app.schemas.Schedule import ScheduleDb, ScheduleSchema

logger = logging.getLogger(__name__)


class ScheduleService:
    def __init__(self, db_session: Session):
        self.schedule_repo = ScheduleRepository(session=db_session)

    def create_schedule(self, payload: ScheduleSchema) -> ScheduleDb:
        return self.schedule_repo.post(payload)

    def get_schedule(self, id: int) -> ScheduleDb:
        schedule: ScheduleDb = self.schedule_repo.get(id)
        if not schedule:
            raise HTTPException(status_code=404, detail="Schedule not found.")
        return schedule

    def update_schedule(self, payload: ScheduleSchema, id: int) -> ScheduleDb:
        schedule = self.get_schedule(id)
        return self.schedule_repo.update(schedule_model=schedule, payload=payload)

    def delete_schedule(self, id: int) -> None:
        schedule = self.get_schedule(id)
        self.schedule_repo.delete(schedule_model=schedule)
