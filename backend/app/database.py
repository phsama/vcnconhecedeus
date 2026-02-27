import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import settings


class Base(DeclarativeBase):
    pass


# --- Lazy engine -----------------------------------------------------------
# We defer engine creation so that the DATABASE_URL set at startup
# (e.g. /tmp/data/subscribers.db on read-only Vercel serverless) is respected.

_engine = None
_SessionLocal = None


def _get_engine():
    global _engine, _SessionLocal
    if _engine is None:
        db_url = os.environ.get("DATABASE_URL", settings.database_url)
        connect_args = {}
        if db_url.startswith("sqlite"):
            connect_args["check_same_thread"] = False
        _engine = create_engine(db_url, connect_args=connect_args)
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
    return _engine


def get_db():
    session_factory = _SessionLocal or sessionmaker(bind=_get_engine())
    db = session_factory()
    try:
        yield db
    finally:
        db.close()


def init_db():
    import app.models  # noqa: F401 — ensure models are registered
    Base.metadata.create_all(bind=_get_engine())
