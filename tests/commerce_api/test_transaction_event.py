import json

import pytest
from pydantic import ValidationError

from lexer_schemas.commerce_api.product_entity import ProductRecord
from lexer_schemas.commerce_api.transaction_event import PurchaseEvent, ReturnEvent


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
            "categories": None,
            "url": None,
            "images": [],
        }

        assert json.loads(actual_record.json()) == expected_record

    def test_product_record_invalid_product_id(self):

        expected_error = (
            r"If product_reference_type is specified as 'product_id', product_id should not be None"
        )

        with pytest.raises(ValueError, match=expected_error):
            ProductRecord(name="spooky product")


class TestPurchaseEvent:
    def test_purchase_event(self):
        expected_record = {
            "link": {"email": "phephen@phephmail.com"},
            "action_at": "2022-04-23T14:15:22+00:00",
            "purchase_id": "10939084127",
            "type": "ecommerce",
            "currency": "USD",
            "payment_types": [{"name": "visa", "total": 100.0}],
            "adjustments": [
                {
                    "price_adjustment": 50.0,
                    "adjusted_at": "2022-04-23T14:15:22+00:00",
                    "reason": "gift card",
                }
            ],
            "products": [
                {
                    "product_reference": {
                        "id": "fg8987fg78",
                        "id_type": "sku",
                        "dataset_id": "j3k4j52k",
                    },
                    "price_paid": 90.0,
                    "quantity": 2,
                    "full_price": 50.0,
                    "discount": 10.0,
                }
            ],
            "custom_fields": {"is_gift": True, "gift_message": "Happy Birthday Kevin!"},
        }
        actual_record = PurchaseEvent.parse_obj(expected_record)

        assert json.loads(actual_record.json()) == expected_record

    def test_purchase_event_price_invalid(self):
        expected_error = (
            r"2 validation errors for PurchaseEvent\nproducts -> 0 -> price_paid"
        )

        with pytest.raises(ValidationError, match=expected_error):
            PurchaseEvent(
                link={"email": "phephen@phephmail.com"},
                action_at="2022-04-23T14:15:22Z",
                purchase_id="10939084127",
                type="ecommerce",
                products=[
                    {
                        "product_reference": {
                            "id": "fg8987fg78",
                            "id_type": "sku",
                            "dataset_id": "j3k4j52k",
                        },
                        "price_paid": -90,
                        "quantity": -2,
                        "full_price": 50,
                        "discount": 10,
                    }
                ],
            )

    def test_purchase_event_invalid(self):

        expected_error = (
            r"1 validation error for PurchaseEvent\nproducts\n  field required"
        )

        with pytest.raises(ValidationError, match=expected_error):
            PurchaseEvent(
                link={"email": "phephen@phephmail.com"},
                action_at="2022-04-23T14:15:22Z",
                purchase_id="10939084127",
                type="ecommerce",
            )


class TestReturnEvent:
    def test_purchase_event(self):
        expected_record = {
            "link": {"email": "phephen@phephmail.com"},
            "action_at": "2022-04-23T14:15:22+00:00",
            "return_id": "10939084127",
            "type": "ecommerce",
            "currency": "USD",
            "adjustments": [
                {
                    "price_adjustment": 50.0,
                    "adjusted_at": "2022-04-23T14:15:22+00:00",
                    "reason": "gift card",
                }
            ],
            "products": [
                {
                    "product_reference": {
                        "id": "fg8987fg78",
                        "id_type": "sku",
                        "dataset_id": "j3k4j52k",
                    },
                    "price_paid": -90.0,
                    "quantity": -2,
                }
            ],
            "custom_fields": {"is_full_return": True},
        }
        actual_record = ReturnEvent.parse_obj(expected_record)

        assert json.loads(actual_record.json()) == expected_record

    def test_purchase_event_price_invalid(self):
        expected_error = (
            r"2 validation errors for ReturnEvent\nproducts -> 0 -> price_paid"
        )

        with pytest.raises(ValidationError, match=expected_error):
            ReturnEvent(
                link={"email": "phephen@phephmail.com"},
                action_at="2022-04-23T14:15:22Z",
                return_id="10939084127",
                type="ecommerce",
                products=[
                    {
                        "product_reference": {
                            "id": "fg8987fg78",
                            "id_type": "sku",
                            "dataset_id": "j3k4j52k",
                        },
                        "price_paid": 90,
                        "quantity": 2,
                        "full_price": 50,
                        "discount": 10,
                    }
                ],
            )

    def test_purchase_event_invalid(self):

        expected_error = (
            r"1 validation error for ReturnEvent\nproducts\n  field required"
        )

        with pytest.raises(ValidationError, match=expected_error):
            ReturnEvent(
                link={"email": "phephen@phephmail.com"},
                action_at="2022-04-23T14:15:22Z",
                return_id="10939084127",
                type="ecommerce",
            )
