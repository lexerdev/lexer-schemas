from datetime import date
from typing import Any, Dict, Optional

from pydantic import BaseModel

from lexer_schemas.link import Link
from lexer_schemas.common import api_name


@api_name("customer_record")
class CustomerRecord(BaseModel):
    link: Link
    email: Optional[str] = None
    email_sha256: Optional[str] = None
    mobile: Optional[str] = None
    customer_id: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    postcode: Optional[str] = None
    zip: Optional[str] = None
    employee_flag: Optional[bool] = None
    customer_type: Optional[str] = None
    address_1: Optional[str] = None
    address_2: Optional[str] = None
