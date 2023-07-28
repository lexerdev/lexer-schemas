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
            "product_reference_type": "product_id",
            "name": None,
            "description": None,
            "brand": None,
            "size": None,
            "color": None,
            "price": None,
            "options": None,
            "url": None,
            "images": [],
        }

        assert json.loads(actual_record.json()) == expected_record

    def test_product_record(self):
        actual_record = ProductRecord(sku="123", product_reference_type="sku")

        expected_record = {
            "product_id": None,
            "sku": "123",
            "upc": None,
            "product_reference_type": "sku",
            "name": None,
            "description": None,
            "brand": None,
            "size": None,
            "color": None,
            "price": None,
            "options": None,
            "url": None,
            "images": [],
        }

        assert json.loads(actual_record.json()) == expected_record

    def test_product_record_no_product_id(self):
        expected_error = r"If product_reference_type is specified as 'product_id', product_id should not be None"

        with pytest.raises(ValueError, match=expected_error):
            ProductRecord(product_reference_type="product_id")

    def test_product_record_no_sku(self):
        expected_error = (
            r"If product_reference_type is specified as 'sku', sku should not be None"
        )

        with pytest.raises(ValueError, match=expected_error):
            ProductRecord(product_reference_type="sku")

    def test_product_record_no_upc(self):
        expected_error = (
            r"If product_reference_type is specified as 'upc', upc should not be None"
        )

        with pytest.raises(ValueError, match=expected_error):
            ProductRecord(product_reference_type="upc")
