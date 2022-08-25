import logging

from bus_service.src.app.config import settings

LEVEL = None
if settings.LOG_LEVEL == "DEBUG":
    LEVEL = logging.DEBUG
elif settings.LOG_LEVEL == "WARNING":
    LEVEL = logging.WARNING
else:
    LEVEL = logging.INFO

logging.basicConfig(level=LEVEL, format=settings.MESSAGE_FORMAT, datefmt=settings.DATE_FORMAT)
