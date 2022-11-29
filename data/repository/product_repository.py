"""Repositories module."""

from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from data.models.product_model import Product


class ProductRepository:
    """ Handles all operations for products"""

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Product]:
        """ Retrieves all Products currently in the database"""
        with self.session_factory() as session:
            return session.query(Product).all()

    def get_by_id(self, product_id: int) -> Product:
        """ Retrieve a product by id or throws an exception"""
        with self.session_factory() as session:
            product = session.query(Product).filter(Product.product_id == product_id).first()
            if not product:
                raise ProductNotFoundError(product_id)
            return product

    def update_by_id(self, product_id: int, product: Product) -> Product:
        """ Update a product by id"""
        with self.session_factory() as session:
            saved_product = session.query(Product).filter(Product.product_id == product_id).first()
            if not saved_product:
                raise ProductNotFoundError(product_id)
            for key, value in product.__dict__.items():
                if value is not None:
                    setattr(saved_product, key, value)
            session.add(saved_product)
            session.commit()
            session.refresh(saved_product)
            return saved_product

    def add(self, product: Product) -> Product:
        """ Adds a new product"""
        with self.session_factory() as session:
            session.add(product)
            session.commit()
            session.refresh(product)
            return product

    def delete_by_id(self, product_id: int) -> None:
        """ Try to delete a product by its product id"""
        with self.session_factory() as session:
            entity: Product = session.query(Product).filter(Product.product_id == product_id).first()
            if not entity:
                raise ProductNotFoundError(product_id)
            session.delete(entity)
            session.commit()


class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class ProductNotFoundError(NotFoundError):
    entity_name: str = "Product"
