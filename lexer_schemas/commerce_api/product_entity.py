from typing import Dict, List, Optional
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, root_validator, NonNegativeFloat
from pydantic.networks import HttpUrl

from lexer_schemas.common import ProductReferenceType, api_name


@api_name("product")
class ProductRecord(BaseModel):
    """
    A product object `record_type=product`.
    Product records are used to represent the current and historical products offered by your brand, including your product taxonomy.
    The field referenced in `product_reference_type` should be unique and used in purchase and return events.
    """

    product_id: Optional[str] = Field(
        title="Product ID",
        description="Unique product_id. Required if `product_id` is used as the product identifier in `product_reference_type`.",
        examples=["b7c901..."],
        default=None,
    )
    sku: Optional[str] = Field(
        title="SKU",
        description="Unique SKU. Required if `sku` is used as a product identifier in `product_reference_type`.",
        examples=["ac6674..."],
        default=None,
    )
    upc: Optional[str] = Field(
        title="UPC",
        description="Unique UPC. Required if `upc` is used as a product identifier in `product_reference_type`.",
        examples=["ce6378..."],
        default=None,
    )
    product_reference_type: ProductReferenceType = Field(
        title="Product Reference Type",
        description="Which field is used to identify the product entity. A value must be provided in the specified field.",
        default=ProductReferenceType.product_id,
    )
    name: Optional[str] = Field(
        title="Product Name", examples=["Organic Sawyer Rib Crew Knit"], default=None
    )
    description: Optional[str] = Field(
        title="Description",
        examples=[
            "Whether your look is clean and casual or sharp and sophisticated, Staple Superior has what you need to achieve that effortlessly cool style."
        ],
    )
    brand: Optional[str] = Field(title="Brand Name", examples=["Sawyer"], default=None)
    size: Optional[str] = Field(title="Size", examples=["L"], default=None)
    color: Optional[str] = Field(title="Color", examples=["Navy"], default=None)
    price: Optional[float] = Field(title="Price", examples=[89.00], default=None)
    options: Optional[Dict[str, List[str]]] = Field(
        title="Categories",
        description="Key value pairs of options that define the product, such as departments, categories, styles, etc.",
        examples=[
            {
                "department": ["menswear"],
                "category": ["outerwear"],
                "subcategory": ["knits", "wool"],
            }
        ],
        default=None,
    )
    url: Optional[str] = Field(
        title="Product URL",
        description="A URL to the product listed on the public internet - i.e., an ecommerce link.",
        examples=["https://fake.com/menswear/sawyer-rib-crew-knit"],
        default=None,
    )
    images: Optional[List[HttpUrl]] = Field(
        title="Image URLs",
        description="An array of Product Image URLs listed on the public internet.",
        examples=[["https://fake.com/images/menswear/sawyer-rib-crew-knit.jpg"]],
        default=None,
    )
    availability: Optional['ProductAvailability'] = Field(
        title="Product Availability",
        default=None,
    )
    inventory: Optional['ProductInventory'] = Field(
        title="Product Inventory",
        default=None,
    )

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


class ProductInventory(BaseModel):
    id: Optional[str] = Field(
        description="Identifier of product in the inventory system"
    )
    source: Optional[str] = Field(
        description="Source of inventory product data, e.g. Shopify, Magento.."
    )
    quantity: Optional[int] = Field(
        description="Total number of remaining product units"
    )
    cost: Optional[NonNegativeFloat] = Field(
        description="Total expenditure incurred to produce, store and sell one unit of product"
    )
    backorder_allowed: Optional[bool] = Field(
        description="Can the product item be ordered when it's out of stock?"
    )
    tracked: Optional[bool] = Field(
        description="Is the product quantity being tracked?"
    )
    updated_at: Optional[datetime] = Field(
        description="When the product inventory status was last updated"
    )

class ProductChannel(str, Enum):
    instore = "instore"
    ecommerce = "ecommerce"


class ProductChannelAvailability(BaseModel):
    type: ProductChannel
    available: bool = Field(
        description="Is the product available for purchase via this specific channel?"
    )
    published_at: Optional[datetime] = Field(
        description="When the product was published, or is going to be published to this channel."
    )
    unpublished_at: Optional[datetime] = Field(
        description="When the product was unpublished, or is going to be unpublished to this channel."
    )


class ProductAvailability(BaseModel):
    available: bool = Field(
        description="A product is available when it is suitable for sale in any channel, or can be promoted in marketing communications."
    )
    channels_availability: Optional[List[ProductChannelAvailability]]


class LexerProductConfig(BaseModel):
    recommendable: Optional[bool] = Field(
        description="When set to False, the product will be excluded from the output of Product Recommender, e.g.: Free Shipping, Enviro Bag.",
    )
    marketable: Optional[bool] = Field(
        description="When set to False, the product will be excluded from the output of Product Recommender, and Product Attributes, e.g.: Promotional Stickers, any low-margin products.",
    )
