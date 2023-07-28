from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, confloat

from lexer_schemas.link import Link

# Root Record Schemas that have been imported.
imported_api_names = {}


def api_name(name):
    def wrapped(cls):
        imported_api_names[name] = cls
        return cls

    return wrapped


class ProductReferenceType(Enum):
    sku = "sku"
    upc = "upc"
    product_id = "product_id"


class GeoCoordinate(BaseModel):
    latitude: confloat(ge=-90, lt=90)  # type: ignore
    longitude: confloat(ge=-180, lt=180)  # type: ignore


class GeoLocation(BaseModel):
    name: Optional[str] = Field(
        title="Location Name", examples=["St Kilda"], default=None
    )
    coordinate: Optional[GeoCoordinate] = None


class StoreType(Enum):
    physical = "physical"
    online = "online"
    concession = "concession"
    outlet = "outlet"


class Store(BaseModel):
    """A store entity."""

    store_id: Optional[str] = Field(examples=["40bf96..."], default=None)
    type: StoreType
    name: str
    location: Optional[GeoLocation] = None


class ClickedLink(BaseModel):
    name: Optional[str] = Field(None, description="The plain text name of the link.")
    url: Optional[str] = Field(None, description="The URL link.")


class MarketingList(BaseModel):
    id: str = Field(examples=["7bff7a..."])
    name: str = Field(examples=["All Customers List", "Lapsed Customers"])


class SMSSubscriptionStatus(Enum):
    subscribed = "subscribed"
    unsubscribed = "unsubscribed"
    transactional = "transactional"
    undeliverable = "undeliverable"
    list_subscribed = "list_subscribed"
    list_unsubscribed = "list_unsubscribed"


class EmailSubscriptionStatus(Enum):
    """
    The type of subscribe event:
    `subscribed` - explicitly subscribed to marketing emails
    `unsubscribed` - explicitly unsubscribed to marketing emails
    `transactional` - **not** explicitly subscribed but can still be sent 'transactional' emails
    `undeliverable` - **not** explicitly unsubscribed but emails sent to them are bouncing or are otherwise undeliverable
    """

    subscribed = "subscribed"
    unsubscribed = "unsubscribed"
    transactional = "transactional"
    undeliverable = "undeliverable"


class BaseEvent(BaseModel):
    link: Link
    action_at: datetime
