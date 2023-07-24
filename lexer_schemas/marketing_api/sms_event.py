from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field

from lexer_schemas.common import (
    api_name,
    BaseEvent,
    MarketingList,
    SMSSubscriptionStatus,
)
from lexer_schemas.link import Link


class SMSRecipient(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None


class BaseSMSEvent(BaseEvent):
    sms_id: str
    list: Optional[MarketingList] = None


@api_name("sms_subscribe")
class SMSSubscribe(BaseSMSEvent):
    action_at: datetime
    status: SMSSubscriptionStatus


@api_name("sms_send")
class SMSSend(BaseSMSEvent):
    campaign_id: Optional[str] = None
    from_: Optional[SMSRecipient] = Field(None, alias="from")
    to: Optional[SMSRecipient] = None
    body: Optional[str] = None


@api_name("sms_click")
class SMSClick(BaseSMSEvent):
    campaign_id: Optional[str] = None
    from_: Optional[SMSRecipient] = Field(None, alias="from")
    to: Optional[SMSRecipient] = None
