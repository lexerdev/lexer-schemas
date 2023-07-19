import re
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, constr, validator

# https://emailregex.com/
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

default_id_type = "default"


class LinkType(str, Enum):
    email = "email"
    email_sha256 = "email_sha256"
    customer_id = "customer_id"
    mobile = "mobile"
    engage_id = "engage.id"
    external_id = "external_id"
    email_md5 = "email_md5"


class EmailLink(BaseModel, extra="forbid"):
    email: str

    @validator("email")
    def validate_email(cls, v: str, values: dict) -> str:
        if not re.match(EMAIL_REGEX, v):
            raise ValueError("email link value does not match email regex pattern")
        return v.strip()


class EmailSha256Link(BaseModel, extra="forbid"):
    email_sha256: str


class EmailMd5Link(BaseModel, extra="forbid"):
    email_md5: str


class MobileLink(BaseModel, extra="forbid"):
    mobile: str


class CustomerIdLink(BaseModel, extra="forbid"):
    customer_id: str
    system_name: Optional[str] = None


class ExternalLink(BaseModel, extra="forbid"):
    external_id: str
    system_name: str


class CustomerLink(BaseModel, extra="forbid"):
    link_type: LinkType
    link_value: constr(min_length=1)  # type: ignore
    id_type: Optional[str] = default_id_type


Link = Union[
    EmailLink,
    EmailSha256Link,
    EmailMd5Link,
    MobileLink,
    CustomerLink,
    ExternalLink,
]
