#!/usr/bin/env python
"""Main module."""

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from container.containers import Container
from presentation.endpoints import product_endpoints


def create_app() -> FastAPI:
    """ Creates FastAPI instance """
    container = Container()

    db = container.db()
    db.create_database()

    fast_api = FastAPI()
    fast_api.container = container
    fast_api.openapi = custom_openapi
    fast_api.include_router(product_endpoints.router)
    return fast_api


def custom_openapi():
    """ Adds OpenApi Documentation at "/redoc" """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Products API",
        version="1.0.0",
        description="This is he products OpenAPI schema",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = create_app()
