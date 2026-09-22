from fastapi import FastAPI

from .config import settings

app = FastAPI(
    title=settings.app_name,
)


@app.get("/health")
def health() -> dict[str, object]:
    return {
        "status": "ok",
        "debug": settings.debug,
    }
