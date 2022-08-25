from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from . import settings


ENGINE = create_engine(settings.CONN, echo=settings.DEBUG)
SESSION = sessionmaker(bind=ENGINE)
Base = declarative_base()
Base.metadata.schema = settings.SCHEMA


def get_db_session():
    db = SESSION()
    try:
        yield db
    finally:
        db.close()
