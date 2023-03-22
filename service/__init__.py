from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
import fastapi.openapi.utils as fu
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import config

def create_app() -> FastAPI:
    app = FastAPI()

    app.mount("/static", StaticFiles(directory="static"), name="static")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from .lab1 import lab1
    from .lab2 import lab2

    app.include_router(lab1)
    app.include_router(lab2)

    return app
