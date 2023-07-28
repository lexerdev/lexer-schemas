from typing import Dict, List, Optional

from pydantic import BaseModel, Field, root_validator
from pydantic.networks import HttpUrl

from lexer_schemas.common import ProductReferenceType, api_name


@api_name("product")
class ProductRecord(BaseModel):
    product_id: Optional[str] = None
    sku: Optional[str] = None
    upc: Optional[str] = None
    product_reference_type: ProductReferenceType = ProductReferenceType.product_id
    name: Optional[str] = None
    description: Optional[str] = None
    brand: Optional[str] = None
    size: Optional[str] = None
    color: Optional[str] = None
    price: Optional[float] = None
    options: Optional[Dict[str, List[str]]] = None
    url: Optional[str] = None
    images: List[HttpUrl] = []

    @root_validator
    def validate_reference_type(cls, values: dict) -> dict:
        product_reference_type, product_id, sku, upc = (
            values.get("product_reference_type"),
            values.get("product_id"),
            values.get("sku"),
            values.get("upc"),
        )
        if (
            product_reference_type == ProductReferenceType.product_id
            and product_id is None
        ):
            raise ValueError(
                "If product_reference_type is specified as 'product_id', product_id should not be None"
            )
        elif product_reference_type == ProductReferenceType.sku and sku is None:
            raise ValueError(
                "If product_reference_type is specified as 'sku', sku should not be None"
            )
        elif product_reference_type == ProductReferenceType.upc and upc is None:
            raise ValueError(
                "If product_reference_type is specified as 'upc', upc should not be None"
            )
        elif product_reference_type is None:
            raise ValueError("product_reference_type should not be None.")
        return values
