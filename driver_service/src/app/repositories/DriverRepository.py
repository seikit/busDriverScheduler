from sqlalchemy.orm import Session

from app.models.driver import DriverModel
from app.schemas.driver import DriverSchema, DriverDb


class DriverRepository:
    def __init__(self, session: Session):
        self.db = session

    def post(self, payload: DriverSchema) -> DriverDb:
        driver_model = DriverModel(**payload.dict())
        self.db.add(driver_model)
        self.db.commit()
        self.db.refresh(driver_model)
        return driver_model

    def get(self, id: int):
        return self.db.query(DriverModel).filter(DriverModel.id == id).first()

    def update(self, driver_model: DriverModel, payload: DriverSchema) -> DriverDb:
        driver_model.first_name = payload.first_name
        driver_model.last_name = payload.last_name
        driver_model.social_security_number = payload.social_security_number
        driver_model.email = payload.email
        self.db.commit()
        return driver_model

    def delete(self, driver_model: DriverModel) -> None:
        self.db.delete(driver_model)
        self.db.commit()
