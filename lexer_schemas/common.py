from datetime import datetime
from enum import Enum
from typing import Optional

from lexer_schemas.link import Link
from pydantic import BaseModel, Field, confloat


class GeoCoordinate(BaseModel):
    latitude: confloat(ge=-90, lt=90)  # type: ignore
    longitude: confloat(ge=-180, lt=180)  # type: ignore


class GeoLocation(BaseModel):
    name: Optional[str]
    coordinate: Optional[GeoCoordinate]


class StoreType(Enum):
    physical = "physical"
    online = "online"
    concession = "concession"
    outlet = "outlet"


class Store(BaseModel):
    store_id: str
    type: Optional[StoreType]
    name: Optional[str]
    location: Optional[GeoLocation]


class ClickedLink(BaseModel):
    name: Optional[str] = Field(None, description="The plain text name of the link.")
    url: Optional[str] = Field(None, description="The URL link.")


class MarketingList(BaseModel):
    id: str
    name: str


class SMSSubscriptionStatus(Enum):
    subscribed = "subscribed"
    unsubscribed = "unsubscribed"
    transactional = "transactional"
    undeliverable = "undeliverable"
    list_subscribed = "list_subscribed"
    list_unsubscribed = "list_unsubscribed"


class EmailSubscriptionStatus(Enum):
    subscribed = "subscribed"
    unsubscribed = "unsubscribed"
    transactional = "transactional"
    undeliverable = "undeliverable"


class BaseEvent(BaseModel):
    link: Link
    action_at: datetime
