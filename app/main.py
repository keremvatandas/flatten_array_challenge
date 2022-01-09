from fastapi import FastAPI

from app.core.constants import API_VERSION, DEBUG, PROJECT_NAME
from app.routes.flatten import router as flatten_router
from mangum import Mangum


def start_app():
    app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=API_VERSION)
    include_router(app)
    return Mangum(app)


def include_router(app):
    app.include_router(flatten_router)


handler = start_app()
