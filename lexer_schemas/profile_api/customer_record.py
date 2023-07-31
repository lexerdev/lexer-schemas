from datetime import date
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field

from lexer_schemas.common import api_name
from lexer_schemas.link import Link


@api_name("customer_record")
class CustomerRecord(BaseModel):
    """
    A customer object `record_type=customer_record`.
    Represents customer information, such as traditional CRM entries, user account information, and so on, in the CDXP.
    The Lexer CDXP will resolve related customer records into one profile, creating a single representation of a profile based on the rules configured within the Hub.
    """

    link: Link = Field(
        description="A value that uniquely identifies the customer, i.e. the primary key for customer records.",
        examples=[
            {"email": "jane@example.com"},
            {"customer_id": "C-2819279", "system_name": "super_pos_2000"},
            {"mobile": "61491570006"},
        ],
    )
    email: Optional[str] = Field(
        default=None,
        title="Email Address",
        description="Raw email address. This will not be used for linking, but is available for use as an attribute in the CDE",
        examples=["jane@fake.com"],
    )
    email_sha256: Optional[str] = Field(
        default=None,
        title="Email Sha256",
        description="A hexadecimal string representing SHA 256 sum of a lowercased email address with trimmed whitespace. This will not be used for linking, but is available for use as an attribute in the CDE",
        examples=["8b1885..."],
    )
    mobile: Optional[str] = Field(
        default=None,
        title="Mobile Phone Number",
        description="A mobile phone number including country code, no whitespace or punctuation. This will not be used for linking, but is available for use as an attribute in the CDE",
        examples=["61491570006"],
    )
    customer_id: Optional[str] = Field(
        default=None, title="Customer Id", examples=["b6ef3b..."]
    )
    custom_fields: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Custom Fields. Properties are open, but a dataset may be configured to accept only particular fields to facilitate automated processing in the Lexer CDP.",
        examples=[{"churn_risk": 0.291, "loyalty_status": "platinum"}],
    )
    first_name: Optional[str] = Field(
        default=None, title="First Name", examples=["Jane"]
    )
    last_name: Optional[str] = Field(default=None, title="Last Name", examples=["Doe"])
    gender: Optional[str] = Field(default=None, title="Gender", examples=["Female"])
    date_of_birth: Optional[date] = Field(
        default=None,
        title="Date Of Birth",
        format="date",
        description="An ISO8601 date string referring to the customer's date of birth",
        examples=["2023-07-28"],
    )
    country: Optional[str] = Field(
        default=None, title="Country", examples=["Australia"]
    )
    state: Optional[str] = Field(default=None, title="State", examples=["Victoria"])
    city: Optional[str] = Field(default=None, title="City", examples=["St Kilda"])
    postcode: Optional[str] = Field(default=None, title="Postcode", examples=["3182"])
    zip: Optional[str] = Field(default=None, title="Zip", examples=["90291"])
    employee_flag: Optional[bool] = Field(
        default=None,
        description="`true` if this customer is an employee of the business. Useful for suppressing them from messages, ad campaigns, and excluding them from searches.",
        examples=[False],
    )
    customer_type: Optional[str] = Field(
        default=None, title="Customer Type", examples=["VIP"]
    )
    address_1: Optional[str] = Field(
        default=None, title="Address 1", examples=["Inkerman St"]
    )
    address_2: Optional[str] = Field(default=None, title="Address 2")
