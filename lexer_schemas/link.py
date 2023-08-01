import re
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field, constr, validator

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
    email: str = Field(examples=["jane@example.com"], pattern=EMAIL_REGEX)

    @validator("email")
    def validate_email(cls, v: str, values: dict) -> str:
        if not re.match(EMAIL_REGEX, v):
            raise ValueError("email link value does not match email regex pattern")
        return v.lower().strip()


class EmailSha256Link(BaseModel, extra="forbid"):
    email_sha256: str = Field(
        description="Ensure that the email address is lowercase before hashing.",
        examples=["8c87b489ce35cf2e2f39f80e282cb2e804932a56a213983eeeb428407d43b52d"],
    )

    @validator("email_sha256")
    def validate_email_sha256(cls, v: str, values: dict) -> str:
        return v.lower().strip()


class EmailMd5Link(BaseModel, extra="forbid"):
    email_md5: str = Field(
        description="Ensure that the email address is lowercase before hashing.",
        examples=["9e26471d35a78862c17e467d87cddedf"],
    )

    @validator("email_md5")
    def validate_email_md5(cls, v: str, values: dict) -> str:
        return v.lower().strip()


class MobileLink(BaseModel, extra="forbid"):
    mobile: str = Field(
        description="Formatted with the international code with no spaces or symbols.",
        examples=["61491570006"],
    )


class CustomerIdLink(BaseModel, extra="forbid"):
    customer_id: str = Field(
        description="A unique identifier for a customer.",
        examples=["123456789"],
    )
    system_name: Optional[str] = Field(
        description="An optional name for the system of origin.",
        examples=["SuperPOS 2000"],
        default=None,
    )


class ExternalLink(BaseModel, extra="forbid"):
    external_id: str = Field(
        description="A unique identifier for a customer in an external system.",
        examples=["123456789"],
    )
    system_name: str = Field(
        description="A unique identifer for the external system itself.",
        examples=["super_pos_2000"],
    )


class CustomerLink(BaseModel, extra="forbid"):
    """This type of link is deprecated. Please use one of the other specific link types instead."""

    link_type: LinkType
    link_value: constr(min_length=1)  # type: ignore
    id_type: Optional[str] = default_id_type


Link = Union[
    EmailLink,
    EmailSha256Link,
    EmailMd5Link,
    CustomerIdLink,
    MobileLink,
    ExternalLink,
    CustomerLink,
]
