from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field

from lexer_schemas.common import BaseEvent, MarketingList, SMSSubscriptionStatus
from lexer_schemas.link import Link


class SMSRecipient(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None


class BaseSMSEvent(BaseEvent):
    sms_id: str
    list: Optional[MarketingList] = None


class SMSSubscribe(BaseSMSEvent):
    action_at: datetime
    status: SMSSubscriptionStatus


class SMSSend(BaseSMSEvent):
    campaign_id: Optional[str] = None
    from_: Optional[SMSRecipient] = Field(None, alias="from")
    to: Optional[SMSRecipient] = None
    body: Optional[str] = None


class SMSClick(BaseSMSEvent):
    campaign_id: Optional[str] = None
    from_: Optional[SMSRecipient] = Field(None, alias="from")
    to: Optional[SMSRecipient] = None
