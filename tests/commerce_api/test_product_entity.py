import pytest

from lexer_schemas.commerce_api.product_entity import ProductRecord

class TestProductEntity:

    def test_product_record(self):
        result = ProductRecord(
            product_id="123"
        )
        assert result.product_id == "123"
        assert result.sku is None
