from fastapi import FastAPI


def create_app():
    return FastAPI(
        title='FastAPIChat',
        docs_url='/api/docs',
        description='Chat on FastAPI with DDD architecture',
    )
