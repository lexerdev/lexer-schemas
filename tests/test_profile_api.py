import json

import pytest
from pydantic import ValidationError

from lexer_schemas.profile_api.customer_record import CustomerRecord


class TestProductEntity:
    def test_product_record(self):
        actual_record = CustomerRecord(
            link={"email": "phephen@phephmail.com"},
            email="phephen@phephmail.com",
            first_name="phephen",
            date_of_birth="1989-09-13",
            custom_fields={"vip_status": 3},
        )

        expected_record = {
            "link": {"email": "phephen@phephmail.com"},
            "email": "phephen@phephmail.com",
            "email_sha256": None,
            "mobile": None,
            "customer_id": None,
            "custom_fields": {"vip_status": 3},
            "first_name": "phephen",
            "last_name": None,
            "gender": None,
            "date_of_birth": "1989-09-13",
            "country": None,
            "state": None,
            "city": None,
            "postcode": None,
            "zip": None,
            "employee_flag": None,
            "customer_type": None,
            "address_1": None,
            "address_2": None,
        }

        assert json.loads(actual_record.json()) == expected_record

    def test_product_record_invalid_link(self):

        expected_error = (
            r"1 validation error for CustomerRecord\nlink\n  field required"
        )

        with pytest.raises(ValidationError, match=expected_error):
            CustomerRecord(first_name="spooky person")

    def test_product_record_invalid_date(self):

        expected_error = r"1 validation error for CustomerRecord\ndate_of_birth\n  invalid date format"

        with pytest.raises(ValidationError, match=expected_error):
            CustomerRecord(
                link={"email": "phephen@phephmail.com"}, date_of_birth="1998-20-09"
            )
