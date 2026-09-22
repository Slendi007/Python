from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from first_proyectproety.apis_web_fastapi.database import (
    Base,
    get_db,
)
from first_proyectproety.apis_web_fastapi.main import app


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    test_engine = create_engine(
        "sqlite://",
        connect_args={
            "check_same_thread": False,
        },
        poolclass=StaticPool,
    )

    Base.metadata.create_all(
        bind=test_engine,
    )

    def get_test_db() -> Generator[
        Session,
        None,
        None,
    ]:
        with Session(test_engine) as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()

    Base.metadata.drop_all(
        bind=test_engine,
    )

    test_engine.dispose()
