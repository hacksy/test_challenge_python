"""Services module."""

from uuid import uuid4
from typing import Iterator

from data.models.product_model import Product
from data.repository.discount_repository import DiscountRepository
from data.repository.product_repository import ProductRepository


class ProductsService:

    def __init__(self, product_repository: ProductRepository, discount_repository: DiscountRepository) -> None:
        self._repository: ProductRepository = product_repository
        self._discount_repository: DiscountRepository = discount_repository

    def get_products(self) -> Iterator[Product]:
        return self._repository.get_all()

    def get_product_by_id(self, product_id: int) -> Product:
        product = self._repository.get_by_id(product_id)
        return product

    def create_product(self, product: Product) -> Product:
        uid = uuid4()
        discount = self._discount_repository.get_discount()
        product = Product(product_id=str(uid), name=product.name, status=product.status, stock=product.stock,
                          description=product.description, price=product.price, discount=discount)
        return self._repository.add(product)

    def update_product(self, product_id: str, product: Product) -> Product:
        return self._repository.update_by_id(product_id, product)

    def delete_product_by_id(self, product_id: int) -> None:
        return self._repository.delete_by_id(product_id)
