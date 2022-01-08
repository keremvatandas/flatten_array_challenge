from fastapi import FastAPI

from core.config import API_VERSION, DEBUG, PROJECT_NAME
from routes.flatten import router as flatten_router


def start_app() -> FastAPI:
    app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=API_VERSION)
    include_router(app)
    return app


def include_router(app: FastAPI) -> FastAPI:
    app.include_router(flatten_router)


app = start_app()
