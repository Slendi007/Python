from fastapi import FastAPI

app = FastAPI(
    title="CI/CD Practice API",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
    }
