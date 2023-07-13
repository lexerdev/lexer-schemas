import re
from typing import Optional, Union

from pydantic import BaseModel, Extra, validator

# https://emailregex.com/
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class EmailLink(BaseModel, extra=Extra.forbid):
    email: str

    @validator("email")
    def validate_email(cls, v: str, values: dict) -> str:
        if not re.match(EMAIL_REGEX, v):
            raise ValueError("email link value does not match email regex pattern")
        return v.strip()


class EmailSha256Link(BaseModel, extra=Extra.forbid):
    email_sha256: str


class EmailMd5Link(BaseModel, extra=Extra.forbid):
    email_md5: str


class MobileLink(BaseModel, extra=Extra.forbid):
    mobile: str


class CustomerLink(BaseModel, extra=Extra.forbid):
    customer_id: str
    system_name: Optional[str] = None


class ExternalLink(BaseModel, extra=Extra.forbid):
    external_id: str
    system_name: str


Link = Union[
    EmailLink,
    EmailSha256Link,
    EmailMd5Link,
    MobileLink,
    CustomerLink,
    ExternalLink,
]
