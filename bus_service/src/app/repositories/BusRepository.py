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

    def update(self, bus_model: BusModel, payload: BusSchema) -> BusDb:
        bus_model.model = payload.model
        bus_model.capacity = payload.capacity
        bus_model.driver_id = payload.driver_id
        bus_model.maker = payload.maker
        self.db.commit()
        return bus_model

    def delete(self, bus_model: BusModel) -> None:
        self.db.delete(bus_model)
        self.db.commit()
