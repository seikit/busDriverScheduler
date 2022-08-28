import json
import logging

import requests

from app.config import settings
from fastapi import HTTPException


logger = logging.getLogger(__name__)


class BusAPI:
    def __init__(self):
        self.url = settings.BUS_SERVICE_URL

    def get_bus_by_id(self, id: int) -> dict:
        try:
            response = requests.get(f"{self.url}/{id}")
            if response.status_code == 200:
                return response.json()

            if response.status_code == 404:
                raise HTTPException(status_code=response.status_code, detail="Bus not found. Register the bus first.")

        except requests.exceptions.HTTPError as ehttp:
            logger.error(f"HTTP ERROR: {ehttp}")
        except requests.exceptions.Timeout as etimeout:
            logger.error(f"Timeout ERROR: {etimeout}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to retrieve bus: {e}")

    def update_bus(self, bus: dict) -> dict:
        try:
            response = requests.put(f"{self.url}/{bus['id']}", data=json.dumps(bus))
            if response.status_code == 200:
                return response.json()

        except requests.exceptions.HTTPError as ehttp:
            logger.error(f"HTTP ERROR: {ehttp}")
        except requests.exceptions.Timeout as etimeout:
            logger.error(f"Timeout ERROR: {etimeout}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to retrieve bus: {e}")
