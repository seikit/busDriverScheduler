import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.BusRepository import BusRepository
from app.schemas.bus import BusDb, BusSchema

logger = logging.getLogger(__name__)


class BusService:
    def __init__(self, db_session: Session):
        self.bus_repo = BusRepository(session=db_session)

    def create_bus(self, payload: BusSchema) -> BusDb:
        return self.bus_repo.post(payload)

    def get_bus(self, id: int) -> BusDb:
        bus: BusDb = self.bus_repo.get(id)
        if not bus:
            raise HTTPException(status_code=404, detail="Bus not found.")
        return bus
