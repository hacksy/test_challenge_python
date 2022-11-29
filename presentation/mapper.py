from data.models.product_model import Product
from data.repository.cache_repository import CacheRepository
from presentation.schema.response.product_schema import ProductSchema


def product_mapper(product: Product, repository: CacheRepository) -> ProductSchema:
    """ Converts the Product DB Object into the JSON Happy Format for browser output"""
    product_dict = {
        "productId": product.product_id,
        "name": product.name,
        "statusName": repository.get(product.product_id, product.status),
        "stock": product.stock,
        "description": product.description,
        "price": product.price,
        "discount": product.discount,
        "finalPrice": product.final_price,
    }
    return ProductSchema(**product_dict)
