"""Models module."""
import uuid

from sqlalchemy import Column, String, Boolean, Integer, Float, select
from sqlalchemy.ext.hybrid import hybrid_property

from config.database import Base


class Product(Base):
    """" Product table using sqlalchemy"""
    __tablename__ = "products"

    product_id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=False)
    status = Column(Boolean, default=False)
    stock = Column(Integer, default=0)
    discount = Column(Integer, default=0)
    description = Column(String, default='')
    price = Column(Float, default=0)

    @hybrid_property
    def final_price(self):
        """Custom property that defines the final price"""
        return self.price * (100 - self.discount) / 100

    def __repr__(self):
        return f"<ProductModel(productId={self.product_id}, " \
               f"name=\"{self.name}\", " \
               f"status=\"{self.status}\", " \
               f"final_price=\"{self.final_price}\", " \
               f"description={self.description})>"
