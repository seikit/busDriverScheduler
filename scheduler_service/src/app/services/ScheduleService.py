import logging
from datetime import date
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.ScheduleRepository import ScheduleRepository
from app.schemas.Calendar import Calendar
from app.schemas.Schedule import ScheduleDb, ScheduleSchema
from app.utils import date_util

logger = logging.getLogger(__name__)


class ScheduleService:
    def __init__(self, db_session: Session):
        self.schedule_repo = ScheduleRepository(session=db_session)
        self.calendar = Calendar()

    def create_schedule(self, payload: ScheduleSchema) -> ScheduleDb:
        self.calendar.schedules = self.get_schedule_by_week(payload.start_dt.date())
        is_shift_available = self.calendar.check_availability(payload.start_dt, payload.end_dt, payload.driver_id, payload.bus_id)
        if is_shift_available:
            return self.schedule_repo.post(payload)
        raise HTTPException(status_code=500, detail="Shift is not available. Pick another date.")

    def get_schedule_by_driver_bus_and_week(self, driver_id: int, bus_id: int, dt: date) -> List[ScheduleDb]:
        start, end = date_util.get_start_and_end_wk_dt(dt)
        return self.schedule_repo.get_schedules_by_driver_bus_and_week(driver_id, bus_id, start, end)

    def get_schedule_by_week(self, dt: date) -> List[ScheduleDb]:
        start, end = date_util.get_start_and_end_wk_dt(dt)
        return self.schedule_repo.get_schedule_between(start, end)

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
