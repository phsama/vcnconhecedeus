from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db
from app.routers import subscribe, verify, unsubscribe, health, admin

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s — %(message)s")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: initialise DB tables
    import os
    # On Vercel (and other read-only serverless runtimes), only /tmp is writable.
    # Try the local ./data path first; fall back to /tmp/data.
    try:
        os.makedirs("data", exist_ok=True)
    except OSError:
        os.makedirs("/tmp/data", exist_ok=True)
        # Override DATABASE_URL so SQLAlchemy points to the writable path
        if "sqlite" in os.environ.get("DATABASE_URL", "sqlite:///./data/subscribers.db"):
            os.environ["DATABASE_URL"] = "sqlite:////tmp/data/subscribers.db"
    init_db()
    yield
    # Shutdown: nothing to clean up


app = FastAPI(
    title="Você não conhece Deus — API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(subscribe.router, prefix="/api")
app.include_router(verify.router, prefix="/api")
app.include_router(unsubscribe.router, prefix="/api")
app.include_router(health.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
