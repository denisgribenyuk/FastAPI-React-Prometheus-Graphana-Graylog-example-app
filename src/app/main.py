from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from app.api import items, ping
from app.config import logger
from app.db import engine, metadata, database

metadata.create_all(engine)


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        logger.info(
            str(request.url),
            extra={
                "req": {"method": request.method, "url": str(request.url)},
                "res": {"status_code": response.status_code},
            },
        )
        return response


app = FastAPI()
app.add_middleware(LogMiddleware)
Instrumentator().instrument(app).expose(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    logger.info("Starting up")
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    logger.info("Shutting down")
    await database.disconnect()
    logger.info("DB Disconnected")
    logger.info("Bye")


app.include_router(ping.router)
app.include_router(items.router, prefix="/items", tags=["items"])
