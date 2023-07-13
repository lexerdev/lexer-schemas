from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from lexer_schemas.link import Link
from pydantic import BaseModel, confloat, conint


class PurchaseType(Enum):
    physical = "physical"
    ecommerce = "ecommerce"


class ProductRefIdType(Enum):
    sku = "sku"
    upc = "upc"
    product_id = "product_id"


class ProductReference(BaseModel):
    id: str
    id_type: ProductRefIdType  # TODO: either take this away or allow simplified entities to specify an id_type
    dataset_id: str


class PurchaseProductReference(BaseModel):
    product_reference: Optional[ProductReference]
    price_paid: confloat(ge=0)  # type: ignore
    quantity: conint(ge=1)  # type: ignore
    full_price: Optional[float]
    discount: Optional[float]


class ReturnProductReference(BaseModel):
    product_reference: Optional[ProductReference]
    price_paid: confloat(le=0)  # type: ignore
    quantity: conint(le=-1)  # type: ignore


class TransactionAdjustment(BaseModel):
    price_adjustment: confloat(ge=0)  # type: ignore
    adjusted_at: Optional[datetime]
    reason: Optional[str]


class PaymentType(BaseModel):
    name: str
    total: Optional[float]


class PurchaseEvent(BaseModel):
    link: Link
    action_at: datetime
    purchase_id: str
    type: PurchaseType
    currency: Optional[str]
    payment_types: Optional[List[PaymentType]]
    adjustments: Optional[List[TransactionAdjustment]]
    products: List[PurchaseProductReference]  # TODO: validate at least one
    custom_fields: Optional[Dict[str, Any]]


class ReturnEvent(BaseModel):
    link: Link
    action_at: datetime
    return_id: str
    type: Optional[PurchaseType]
    currency: Optional[str]
    adjustments: Optional[List[TransactionAdjustment]]
    products: List[PurchaseProductReference]  # TODO: validate at least one
    custom_fields: Optional[Dict[str, Any]]
