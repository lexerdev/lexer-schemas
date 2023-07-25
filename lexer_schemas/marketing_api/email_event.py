import re
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, validator
from pydantic.fields import Field

from lexer_schemas.common import (
    api_name,
    BaseEvent,
    ClickedLink,
    EmailSubscriptionStatus,
    MarketingList,
)
from lexer_schemas.link import Link

# https://emailregex.com/
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class EmailAddress(BaseModel):
    name: Optional[str] = None
    email: str

    @validator("email")
    def validate_email(cls, v: str, values: dict) -> str:
        if not re.match(EMAIL_REGEX, v):
            raise ValueError("email link value does not match email regex pattern")
        return v.strip()


class BaseEmailEvent(BaseEvent):
    email_id: str
    list: Optional[MarketingList] = None


@api_name("email_send")
class EmailSend(BaseEmailEvent):
    campaign_id: Optional[str] = None
    from_: Optional[EmailAddress] = Field(None, alias="from")
    to: Optional[EmailAddress] = None
    subject: Optional[str] = None
    body: Optional[str] = None


@api_name("email_open")
class EmailOpen(BaseEmailEvent):
    campaign_id: Optional[str] = None
    from_: Optional[EmailAddress] = Field(None, alias="from")
    to: Optional[EmailAddress] = None


@api_name("email_click")
class EmailClick(BaseEmailEvent):
    campaign_id: Optional[str] = None
    from_: Optional[EmailAddress] = Field(None, alias="from")
    to: Optional[EmailAddress] = None
    clicked_link: Optional[ClickedLink] = None


@api_name("email_bounce")
class EmailBounce(BaseEmailEvent):
    from_: Optional[EmailAddress] = Field(None, alias="from")
    to: Optional[EmailAddress] = None


@api_name("email_subscribe")
class EmailSubscribe(BaseEmailEvent):
    status: EmailSubscriptionStatus
