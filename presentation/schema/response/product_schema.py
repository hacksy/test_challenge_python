from pydantic import BaseModel


class ProductSchema(BaseModel):
    """ Browser Output Schema """
    productId: str
    name: str
    statusName: str
    stock: int
    description: str
    price: float
    discount: float
    finalPrice: float
