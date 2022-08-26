from sqlalchemy.orm import Session

from app.models.bus import BusModel
from app.schemas.bus import BusSchema, BusDb


class BusRepository:
    def __init__(self, session: Session):
        self.db = session

    def post(self, payload: BusSchema) -> BusDb:
        bus_model = BusModel(**payload.dict())
        self.db.add(bus_model)
        self.db.commit()
        self.db.refresh(bus_model)
        return bus_model

    def get(self, id: int):
        return self.db.query(BusModel).filter(BusModel.id == id).first()
