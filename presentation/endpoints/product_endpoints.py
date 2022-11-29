"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from container.containers import Container
from data.models.product_model import Product
from data.repository.cache_repository import CacheRepository
from data.repository.product_repository import NotFoundError
from data.repository.time_logger_repository import TimeLoggerRepository
from domain.services.products_services import ProductsService
from presentation.mapper import product_mapper
from presentation.schema.request.create_product_schema import CreateProductSchema
from presentation.schema.response.product_schema import ProductSchema

router = APIRouter()


@router.get("/products")
@inject
def get_list(
        products_service: ProductsService = Depends(Provide[Container.products_service]),
        timer: TimeLoggerRepository = Depends(Provide[Container.timer]),
) -> [Product]:
    """ Retrieves all Products """
    timer.start('Endpoint: GET /products')
    result = products_service.get_products()
    timer.stop()
    return result


@router.get("/getById/{product_id}")
@inject
def get_by_id(
        product_id: str,
        products_service: ProductsService = Depends(Provide[Container.products_service]),
        cache_repository: CacheRepository = Depends(Provide[Container.cache_repository]),
        timer: TimeLoggerRepository = Depends(Provide[Container.timer]),
) -> ProductSchema:
    """ Retrieves a product by id or 404"""
    timer.start('Endpoint: GET /getById/{}'.format(product_id))
    try:
        result = product_mapper(products_service.get_product_by_id(product_id), cache_repository)
        timer.stop()
        return result
    except NotFoundError:
        result = Response(status_code=status.HTTP_404_NOT_FOUND)
        timer.stop()
        return result


@router.post("/products", status_code=status.HTTP_201_CREATED)
@inject
def add(
        product: CreateProductSchema,
        products_service: ProductsService = Depends(Provide[Container.products_service]),
        cache_repository: CacheRepository = Depends(Provide[Container.cache_repository]),
        timer: TimeLoggerRepository = Depends(Provide[Container.timer]),
) -> ProductSchema:
    """ Creates a Product and set a random uuid as the id"""
    timer.start('Endpoint: POST /products')
    product = products_service.create_product(
        Product(name=product.name, status=product.status, stock=product.stock,
                description=product.description, price=product.price, ))
    result = product_mapper(product, cache_repository)
    timer.stop()
    return result


@router.put("/products/{product_id}", status_code=status.HTTP_200_OK)
@inject
def update(
        product_id: str,
        product: CreateProductSchema,
        products_service: ProductsService = Depends(Provide[Container.products_service]),
        cache_repository: CacheRepository = Depends(Provide[Container.cache_repository]),
        timer: TimeLoggerRepository = Depends(Provide[Container.timer]),
) -> ProductSchema:
    """ Update a product based on its id or 404"""
    timer.start('Endpoint: PUT /products/{}'.format(product_id))
    try:
        result = product_mapper(products_service.update_product(product_id, product), cache_repository)
        timer.stop()
        return result
    except NotFoundError:
        result = Response(status_code=status.HTTP_404_NOT_FOUND)
        timer.stop()
        return result
