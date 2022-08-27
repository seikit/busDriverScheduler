from starlette.config import Config

config = Config(".env-scheduler-dev")

# APPLICATION
ENTRYPOINT = "main:app"
VERSION = "1.0.0"

# OpenAPI Documentation
TITLE = "Scheduler service"
DESCRIPTION = "Service focused on managing the scheduler resource."
DOCS_PATH = "/"

# Server (Uvicorn)
HOST = "127.0.0.1"
PORT = 8082
RELOAD = True

# Database
CONN = config("CONN", default=None)
SCHEMA = config("SCHEMA", default="scheduler")
DEBUG = False

# CORS
ALLOW_ORIGINS = ["http://localhost", "http://localhost:3000"]
ALLOW_METHODS = ["POST", "GET", "PUT", "DELETE"]
ALLOW_HEADERS = ["*"]