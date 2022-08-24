import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.config import settings
from src.config.tags_metadata import tags_metadata

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    docs_url=settings.DOCS_PATH,
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS
)

if __name__ == "__main__":
    uvicorn.run(
        app=settings.ENTRYPOINT,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD
    )
