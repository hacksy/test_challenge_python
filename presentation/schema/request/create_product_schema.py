from pydantic import BaseModel
from typing import Union


class CreateProductSchema(BaseModel):
    """ Create and Update valid fields """
    name: str
    status: Union[int, None] = None
    stock: Union[int, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
