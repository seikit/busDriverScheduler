import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.DriverRepository import DriverRepository
from app.schemas.driver import DriverDb, DriverSchema

logger = logging.getLogger(__name__)


class DriverService:
    def __init__(self, db_session: Session):
        self.driver_repo = DriverRepository(session=db_session)

    def create_driver(self, payload: DriverSchema) -> DriverDb:
        return self.driver_repo.post(payload)

    def get_driver(self, id: int) -> DriverDb:
        driver: DriverDb = self.driver_repo.get(id)
        if not driver:
            raise HTTPException(status_code=404, detail="Driver not found.")
        return driver

    def update_driver(self, payload: DriverSchema, id: int) -> DriverDb:
        driver = self.get_driver(id)
        return self.driver_repo.update(driver_model=driver, payload=payload)

    def delete_driver(self, id: int) -> None:
        driver = self.get_driver(id)
        self.driver_repo.delete(driver_model=driver)
