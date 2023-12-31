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

    def test_product_record_lowercase(self):
        actual_record = CustomerRecord(
            link={"email": "THISSHOULDBELOWERCASED@phephmail.com"},
            email="THISSHOULDALSOBELOWERCASED@phephmail.com",
            email_sha256="DA314EC7B1028CED2FFC0701773BA5DEC6DD7D9E1C363365CD58A5F5D6CE7325",
            first_name="phephen",
            date_of_birth="1989-09-13",
            custom_fields={"vip_status": 3},
        )

        expected_record = {
            "link": {"email": "thisshouldbelowercased@phephmail.com"},
            "email": "thisshouldalsobelowercased@phephmail.com",
            "email_sha256": "da314ec7b1028ced2ffc0701773ba5dec6dd7d9e1c363365cd58a5f5d6ce7325",
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

