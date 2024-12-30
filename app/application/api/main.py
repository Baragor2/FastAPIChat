from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

from application.api.lifespan import close_kafka, start_kafka
from application.api.messages.handlers import router as message_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_kafka()
    yield
    await close_kafka()


def create_app() -> FastAPI:
    app = FastAPI(
        title='FastAPIChat',
        docs_url='/api/docs',
        description='FastAPI DDD Chat',
        debug=True,
        lifespan=lifespan,
    )
    app.include_router(message_router, prefix="/chat")

    return app
