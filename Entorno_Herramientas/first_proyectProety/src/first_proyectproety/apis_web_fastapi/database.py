from collections.abc import Generator
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

RAIZ_PROYECTO = Path(__file__).resolve().parents[3]
RUTA_BD = RAIZ_PROYECTO / "data" / "fastapi.db"

DATABASE_URL = f"sqlite:///{RUTA_BD}"


class Base(DeclarativeBase):
    pass


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session
