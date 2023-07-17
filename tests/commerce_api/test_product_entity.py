import json

import pytest
from pydantic import ValidationError

from lexer_schemas.commerce_api.product_entity import ProductRecord


class TestProductEntity:
    def test_product_record(self):
        actual_record = ProductRecord(product_id="123")

        expected_record = {
            "product_id": "123",
            "sku": None,
            "upc": None,
            "name": None,
            "description": None,
            "brand": None,
            "size": None,
            "color": None,
            "price": None,
            "categories": None,
            "url": None,
            "images": [],
        }

        assert json.loads(actual_record.json()) == expected_record

    def test_product_record_invalid_product_id(self):

        expected_error = (
            r"1 validation error for ProductRecord\nproduct_id\n  field required"
        )

        with pytest.raises(ValidationError, match=expected_error):
            ProductRecord(name="spooky product")
