from starlette.config import Config

config = Config(".env-dev")

# APPLICATION
ENTRYPOINT = "main:app"
VERSION = "1.0.0"

# OpenAPI Documentation
TITLE = "Driver service"
DESCRIPTION = "Service focused on managing the driver resource."
DOCS_PATH = "/"

# Server (Uvicorn)
HOST = "127.0.0.1"
PORT = 8081
RELOAD = True

# Database
CONN = config("CONN", default=None)
SCHEMA = config("SCHEMA", default="driver")
DEBUG = False

# CORS
ALLOW_ORIGINS = ["*"]
ALLOW_METHODS = ["POST", "GET", "PUT", "DELETE"]
ALLOW_HEADERS = ["*"]
