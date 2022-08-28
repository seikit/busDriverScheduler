import logging
from datetime import date
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.apis.driver_api import DriverAPI
from app.apis.bus_api import BusAPI
from app.repositories.ScheduleRepository import ScheduleRepository
from app.schemas.BusSchedule import BusSchedule
from app.schemas.DriverSchedule import DriverSchedule
from app.schemas.Calendar import Calendar
from app.schemas.Schedule import ScheduleDb, ScheduleSchema
from app.utils import date_util

logger = logging.getLogger(__name__)


class ScheduleService:
    def __init__(self, db_session: Session):
        self.schedule_repo = ScheduleRepository(session=db_session)
        self.calendar = Calendar()
        self.driver_api = DriverAPI()
        self.bus_api = BusAPI()

    def get_driver_and_bus(self, payload: ScheduleSchema) -> tuple:
        driver: dict = self.driver_api.get_driver_by_id(payload.driver_id)
        if not driver:
            raise HTTPException(status_code=500, detail="Failed to create schedule. Try again later.")

        bus: dict = self.bus_api.get_bus_by_id(payload.bus_id)
        if not bus:
            raise HTTPException(status_code=500, detail="Failed to create schedule. Try again later.")
        return driver, bus

    def update_bus_driver(self, bus: dict, driver: dict) -> None:
        bus["driver_id"] = driver["id"]
        self.bus_api.update_bus(bus)

    def create_schedule(self, payload: ScheduleSchema) -> ScheduleDb:
        driver, bus = self.get_driver_and_bus(payload)

        self.calendar.schedules = self.get_schedule_by_week(payload.start_dt.date())
        is_shift_available = self.calendar.check_availability(payload.start_dt, payload.end_dt, payload.driver_id, payload.bus_id)
        if is_shift_available:
            schedule: ScheduleDb = self.schedule_repo.post(payload)
            print(f">>> Driver {driver['first_name']} will be driving bus model {bus['model']} from maker"
                  f" {bus['maker']} between {schedule.start_dt} and {schedule.end_dt}.")

            self.update_bus_driver(bus, driver)
            return schedule
        raise HTTPException(status_code=500, detail="Shift is not available. Pick another date.")

    def get_schedule_by_week(self, dt: date) -> List[ScheduleDb]:
        start, end = date_util.get_start_and_end_wk_dt(dt)
        return self.schedule_repo.get_schedule_between(start, end)

    def get_bus_week_schedules(self, dt: date) -> List[BusSchedule]:
        start, end = date_util.get_start_and_end_wk_dt(dt)
        schedules: List[ScheduleDb] = self.schedule_repo.get_schedule_between(start, end)
        return [BusSchedule(**ScheduleDb.from_orm(schedule).dict()) for schedule in schedules]

    def get_driver_week_schedules(self, dt: date) -> List[DriverSchedule]:
        start, end = date_util.get_start_and_end_wk_dt(dt)
        schedules: List[ScheduleDb] = self.schedule_repo.get_schedule_between(start, end)
        return [DriverSchedule(**ScheduleDb.from_orm(schedule).dict()) for schedule in schedules]

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
