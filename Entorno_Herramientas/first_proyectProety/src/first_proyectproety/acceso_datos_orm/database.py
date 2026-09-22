from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

RAIZ_PROYECTO = Path(__file__).resolve().parents[3]

RUTA_BD = RAIZ_PROYECTO / "data" / "tienda.db"

DATABASE_URL = f"sqlite:///{RUTA_BD}"


class Base(DeclarativeBase):
    pass


engine = create_engine(
    DATABASE_URL,
    echo=False,
)


SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
