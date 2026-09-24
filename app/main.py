from pathlib import Path

from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from .config import settings

from .database import Base
from .database import engine

from .routes.web import router as web_router

from .routes.api import router as api_router


BASE_DIR = Path(__file__).resolve().parent


(BASE_DIR / "static").mkdir(
    exist_ok=True
)

(BASE_DIR / "templates").mkdir(
    exist_ok=True
)

Path("uploads").mkdir(
    exist_ok=True
)


app = FastAPI(

    title=settings.app_name,

    version="1.0.0",

    description=(
        "AI budget and "
        "recommendation assistant"
    )
)


app.mount(

    "/static",

    StaticFiles(
        directory=str(
            BASE_DIR / "static"
        )
    ),

    name="static"
)


app.include_router(
    web_router
)


app.include_router(
    api_router
)


@app.on_event("startup")
def startup():

    Base.metadata.create_all(
        bind=engine
    )


@app.get("/health")
def health():

    return {

        "status": "ok",

        "service":
            settings.app_name
    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(

        "app.main:app",

        host="127.0.0.1",

        port=8000,

        reload=True
    )