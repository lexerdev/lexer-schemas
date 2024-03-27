from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, confloat, conint

from lexer_schemas.common import BaseEvent, ProductReferenceType, Store, api_name
from lexer_schemas.link import Link


class PurchaseType(Enum):
    physical = "physical"
    ecommerce = "ecommerce"


class ProductReference(BaseModel):
    id: str
    id_type: ProductReferenceType
    dataset_id: Optional[str] = Field(examples=["9wyqa53dnx"], default=None)


class PurchaseProductReference(BaseModel):
    product_reference: Optional[ProductReference] = None
    price_paid: confloat(ge=0) = Field(examples=[90.00])  # type: ignore
    quantity: conint(ge=1) = Field(examples=[2])  # type: ignore
    full_price: Optional[float] = Field(examples=[50.00], default=None)
    discount: Optional[float] = Field(examples=[10.00], default=None)


class ReturnProductReference(BaseModel):
    product_reference: Optional[ProductReference] = None
    price_paid: confloat(le=0)  # type: ignore
    quantity: conint(le=-1)  # type: ignore


class TransactionAdjustment(BaseModel):
    price_adjustment: float = Field(examples=[50.00])
    adjusted_at: Optional[datetime] = None
    reason: Optional[str] = Field(examples=["gift card"], default=None)


class PaymentType(BaseModel):
    name: str = Field(examples=["visa"])
    total: Optional[float] = Field(examples=[100.00], default=None)


class BaseTransactionEvent(BaseEvent):
    type: PurchaseType
    currency: Optional[str] = Field(
        description="Currency code as ISO 4217", examples=["USD"], default=None
    )
    adjustments: Optional[List[TransactionAdjustment]] = None
    custom_fields: Optional[Dict[str, Any]] = Field(
        description="Custom Fields. Properties are open, but a dataset may be configured to accept only particular fields to facilitate automated processing in the Lexer CDP.",
        examples=[{"is_damaged": True, "customer_reason": "glass broken on delivery"}],
        default=None,
    )
    store: Optional[Store] = None


@api_name("purchase")
class PurchaseEvent(BaseTransactionEvent):
    """
    A purchase event object `record_type=purchase`.
    Represents transaction data and is used to enrich profiles with their complete purchase history.
    """

    purchase_id: str = Field(examples=["53059a..."])
    payment_types: Optional[List[PaymentType]] = None
    products: List[PurchaseProductReference] = Field(
        description="Contains the 'order lines' in the purchase event. Each record in this array represents a specific product that was purchased including details such as quantity, price paid etc.",
        min_items=1,
    )


@api_name("return")
class ReturnEvent(BaseTransactionEvent):
    """
    A return event object `record_type=return`.
    Represents transaction data related to customers returning products and is used to enrich profiles with their complete purchase history.
    """

    return_id: str
    products: List[ReturnProductReference] = Field(
        description="Contains the 'order lines' in the return event. Each record in this array represents a specific product that was returned including details such as quantity returned, refund price etc.",
    )
