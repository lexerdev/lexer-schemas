from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field

from lexer_schemas.common import (
    BaseEvent,
    MarketingList,
    SMSSubscriptionStatus,
    api_name,
)
from lexer_schemas.link import Link


class SMSRecipient(BaseModel):
    name: Optional[str] = Field(examples=["Jane Doe"], default=None)
    number: Optional[str] = Field(examples=["+61491570006"], default=None)


class BaseSMSEvent(BaseEvent):
    sms_id: str = Field(
        description="A unique identifier for an individual SMS event.",
        examples=["send-job-a7e23-jane-doe"],
    )
    list: Optional[MarketingList] = None


@api_name("sms_subscribe")
class SMSSubscribe(BaseSMSEvent):
    """An SMS Subscribe Event object `record_type=sms_subscribe`."""

    action_at: datetime
    status: SMSSubscriptionStatus


CampaignField = Field(
    description="Campaign Identifier or Name.",
    examples=["Black friday Menswear Teaser Aug 2020"],
    default=None,
)

FromField = Field(description="Sender Details", alias="from", default=None)

ToField = Field(description="Recipient Details", default=None)


@api_name("sms_send")
class SMSSend(BaseSMSEvent):
    """An SMS Send Event object `record_type=sms_send`."""

    campaign_id: Optional[str] = CampaignField
    from_: Optional[SMSRecipient] = FromField
    to: Optional[SMSRecipient] = ToField
    body: Optional[str] = Field(
        description="Body of the SMS message",
        examples=["Get ready to SAVE BIG at our Exclusive Black Friday Sale!"],
        default=None,
    )


@api_name("sms_click")
class SMSClick(BaseSMSEvent):
    """An SMS Click Event object `record_type=sms_click`."""

    campaign_id: Optional[str] = CampaignField
    from_: Optional[SMSRecipient] = FromField
    to: Optional[SMSRecipient] = ToField
