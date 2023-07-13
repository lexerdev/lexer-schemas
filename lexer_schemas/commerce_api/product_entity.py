from typing import List, Optional

from pydantic import BaseModel
from pydantic.networks import HttpUrl


class Category(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class ProductRecord(BaseModel):
    product_id: str
    sku: Optional[str] = None
    upc: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    brand: Optional[str] = None
    size: Optional[str] = None
    color: Optional[str] = None
    price: Optional[float] = None
    categories: Optional[List[Category]] = None
    url: Optional[str] = None
    images: List[HttpUrl] = []
