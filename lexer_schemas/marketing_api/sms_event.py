from datetime import datetime
from typing import Optional

from lexer_schemas.link import Link
from lexer_schemas.common import BaseEvent, MarketingList, SMSSubscriptionStatus
from pydantic import BaseModel
from pydantic.fields import Field


class SMSRecipient(BaseModel):
    name: Optional[str]
    mobile: Optional[str]


class BaseSMSEvent(BaseEvent):
    list: Optional[MarketingList]


class SMSSubscribe(BaseModel):
    link: Link
    action_at: datetime
    list: Optional[MarketingList]
    status: SMSSubscriptionStatus


class SMSSend(BaseModel):
    campaign_id: str
    from_: Optional[SMSRecipient] = Field(None, alias="from")
    to: Optional[SMSRecipient]
    body: Optional[str]


class SMSClick(BaseModel):
    campaign_id: str
    from_: Optional[SMSRecipient] = Field(None, alias="from")
    to: Optional[SMSRecipient]
