import re
from typing import Optional

from pydantic import BaseModel, validator
from pydantic.fields import Field

from lexer_schemas.common import (
    BaseEvent,
    ClickedLink,
    EmailSubscriptionStatus,
    MarketingList,
    api_name,
)
from lexer_schemas.link import Link

# https://emailregex.com/
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class EmailAddress(BaseModel):
    name: Optional[str] = Field(examples=["Jane Doe"], default=None)
    email: str = Field(examples=["jane@example.com"], pattern=EMAIL_REGEX)

    @validator("email")
    def validate_email(cls, v: str, values: dict) -> str:
        if not re.match(EMAIL_REGEX, v.lower().strip()):
            raise ValueError("email value does not match email regex pattern")
        return v.lower().strip()


class BaseEmailEvent(BaseEvent):
    email_id: str = Field(
        description="A unique identifier for an individual email event.",
        examples=["send-job-a7e23-jane-doe"],
    )
    list: Optional[MarketingList] = None


CampaignField = Field(
    description="Campaign Identifier or Name.",
    examples=["Black friday Menswear Teaser Aug 2020"],
    default=None,
)

FromField = Field(description="Sender Details", alias="from", default=None)

ToField = Field(description="Recipient Details", default=None)


@api_name("email_send")
class EmailSend(BaseEmailEvent):
    """
    An Email Send Event object `record_type=email_send`.
    These events are used to enrich profiles with attributes like “Number of Emails Sent” or “Campaigns Sent”.
    """

    campaign_id: Optional[str] = CampaignField
    from_: Optional[EmailAddress] = FromField
    to: Optional[EmailAddress] = ToField
    subject: Optional[str] = Field(
        title="Subject Line", examples=["Dress Best this Black Friday"], default=None
    )
    body: Optional[str] = Field(
        title="Email Body",
        examples=[
            "Hey Jane, The most awaited shopping event of the year is finally here, and we couldn't be more thrilled to share it with you!"
        ],
        default=None,
    )


@api_name("email_open")
class EmailOpen(BaseEmailEvent):
    """
    An Email Open Event object `record_type=email_open`.
    These events are used to enrich profiles with attributes like “Campaigns Opened” or “Email Open Rate”.
    """

    campaign_id: Optional[str] = CampaignField
    from_: Optional[EmailAddress] = FromField
    to: Optional[EmailAddress] = ToField


@api_name("email_click")
class EmailClick(BaseEmailEvent):
    """
    An Email Click Event object `record_type=email_click`.
    These events are used to enrich profiles with attributes like “Email Click Rate” or “Click Dates”.
    """

    campaign_id: Optional[str] = CampaignField
    from_: Optional[EmailAddress] = FromField
    to: Optional[EmailAddress] = ToField
    clicked_link: Optional[ClickedLink] = None


@api_name("email_bounce")
class EmailBounce(BaseEmailEvent):
    """An Email Bounce Event object `record_type=email_bounce`."""

    from_: Optional[EmailAddress] = FromField
    to: Optional[EmailAddress] = ToField


@api_name("email_subscribe")
class EmailSubscribe(BaseEmailEvent):
    """
    An Email Subscribe Event object `record_type=email_subscribe`.
    These events are used to enrich profiles with attributes like “Email Subscription Status”, "Email Deliverability" or “Email Subscribe Date”
    """

    status: EmailSubscriptionStatus
