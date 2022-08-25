import logging

from sqlalchemy.orm import Session
from app.repositories.BusRepository import BusRepository
from app.schemas.bus import BusDb, BusSchema

logger = logging.getLogger(__name__)


class BusService:
    def __init__(self, db_session: Session):
        self.bus_repo = BusRepository(session=db_session)

    def create_bus(self, payload: BusSchema) -> BusDb:
        return self.bus_repo.post(payload)
