from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings

ENGINE = create_engine(settings.CONN, echo=settings.DEBUG)
SESSION = sessionmaker(bind=ENGINE)


def get_db_session():
    db = SESSION()
    try:
        yield db
    finally:
        db.close()
