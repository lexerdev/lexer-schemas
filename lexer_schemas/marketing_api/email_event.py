import re
from datetime import datetime
from enum import Enum
from typing import Optional

from lexer_schemas.link import Link
from lexer_schemas.common import (
    ClickedLink,
    MarketingList,
    EmailSubscriptionStatus,
)
from pydantic import BaseModel, validator
from pydantic.fields import Field

# https://emailregex.com/
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class EmailAddress(BaseModel):
    name: Optional[str]
    email: str

    @validator("email")
    def validate_email(cls, v: str, values: dict) -> str:
        if not re.match(EMAIL_REGEX, v):
            raise ValueError("email link value does not match email regex pattern")
        return v.strip()


class EmailSend(BaseModel):
    link: Link
    action_at: datetime
    campaign_id: str
    list: Optional[MarketingList]
    from_: Optional[EmailAddress] = Field(None, alias="from")
    to: Optional[EmailAddress]
    subject: Optional[str]
    body: Optional[str]


class EmailOpen(BaseModel):
    link: Link
    action_at: datetime
    campaign_id: str
    list: Optional[MarketingList]
    from_: Optional[EmailAddress] = Field(None, alias="from")
    to: Optional[EmailAddress]


class EmailClick(BaseModel):
    link: Link
    action_at: datetime
    campaign_id: str
    list: Optional[MarketingList]
    from_: Optional[EmailAddress] = Field(None, alias="from")
    to: Optional[EmailAddress]
    clicked_link: Optional[ClickedLink]


class EmailBounce(BaseModel):
    link: Link
    action_at: datetime
    list: Optional[MarketingList]
    from_: Optional[EmailAddress] = Field(None, alias="from")
    to: Optional[EmailAddress]


class EmailSubscribe(BaseModel):
    link: Link
    action_at: datetime
    list: Optional[MarketingList]
    status: EmailSubscriptionStatus
