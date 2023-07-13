from datetime import date
from typing import Any, Dict, Optional

from lexer_schemas.link import Link
from pydantic import BaseModel


class CustomerRecord(BaseModel):
    link: Link
    email: Optional[str]
    email_sha256: Optional[str]
    mobile: Optional[str]
    customer_id: Optional[str]
    custom_fields: Optional[Dict[str, Any]]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    date_of_birth: Optional[date]
    country: Optional[str]
    state: Optional[str]
    city: Optional[str]
    postcode: Optional[str]
    zip: Optional[str]
    employee_flag: Optional[bool]
    customer_type: Optional[str]
    address_1: Optional[str]
    address_2: Optional[str]
