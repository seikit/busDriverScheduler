from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db_session
from app.schemas.bus import BusSchema, BusDb
from app.services.BusService import BusService

router = APIRouter(
    prefix="/bus",
    tags=["Bus"]
)


@router.post("/", description="Endpoint to create a new bus resource.", response_model=BusDb, status_code=201)
def create_bus(payload: BusSchema, db: Session = Depends(get_db_session)):
    return BusService(db_session=db).create_bus(payload)
