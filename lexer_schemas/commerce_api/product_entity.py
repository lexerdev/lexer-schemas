from typing import List, Optional

from pydantic import BaseModel
from pydantic.networks import HttpUrl


class Category(BaseModel):
    name: Optional[str]
    description: Optional[str]


class ProductRecord(BaseModel):
    product_id: str
    sku: Optional[str]
    upc: Optional[str]
    name: Optional[str]
    description: Optional[str]
    brand: Optional[str]
    size: Optional[str]
    color: Optional[str]
    price: Optional[float]
    categories: Optional[List[Category]]
    url: Optional[str]
    images: List[HttpUrl] = []
