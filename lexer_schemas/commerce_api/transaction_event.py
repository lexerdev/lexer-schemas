from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, confloat, conint

from lexer_schemas.link import Link


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
    product_reference: Optional[ProductReference] = None
    price_paid: confloat(ge=0)  # type: ignore
    quantity: conint(ge=1)  # type: ignore
    full_price: Optional[float] = None
    discount: Optional[float] = None


class ReturnProductReference(BaseModel):
    product_reference: Optional[ProductReference] = None
    price_paid: confloat(le=0)  # type: ignore
    quantity: conint(le=-1)  # type: ignore


class TransactionAdjustment(BaseModel):
    price_adjustment: confloat(ge=0)  # type: ignore
    adjusted_at: Optional[datetime] = None
    reason: Optional[str] = None


class PaymentType(BaseModel):
    name: str
    total: Optional[float] = None


class PurchaseEvent(BaseModel):
    link: Link
    action_at: datetime
    purchase_id: str
    type: PurchaseType
    currency: Optional[str] = None
    payment_types: Optional[List[PaymentType]] = None
    adjustments: Optional[List[TransactionAdjustment]] = None
    products: List[PurchaseProductReference]  # TODO: validate at least one
    custom_fields: Optional[Dict[str, Any]] = None


class ReturnEvent(BaseModel):
    link: Link
    action_at: datetime
    return_id: str
    type: Optional[PurchaseType] = None
    currency: Optional[str] = None
    adjustments: Optional[List[TransactionAdjustment]] = None
    products: List[PurchaseProductReference]  # TODO: validate at least one
    custom_fields: Optional[Dict[str, Any]] = None
