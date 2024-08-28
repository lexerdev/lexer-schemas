import json
import jsonschema
import unittest
import lexer_schemas
import lexer_schemas.commerce_api
import lexer_schemas.commerce_api.product_entity
import lexer_schemas.commerce_api.transaction_event
import lexer_schemas.marketing_api
import lexer_schemas.marketing_api.email_event
import lexer_schemas.marketing_api.sms_event
import lexer_schemas.profile_api
import lexer_schemas.profile_api.customer_record


class TestExamples(unittest.TestCase):

    def test_example_data(self):
        example_to_model = {
            "examples/data/batch_commerce_product.ndjson": lexer_schemas.commerce_api.product_entity.ProductRecord,
            "examples/data/batch_commerce_purchase.ndjson": lexer_schemas.commerce_api.transaction_event.PurchaseEvent,
            "examples/data/batch_commerce_return.ndjson": lexer_schemas.commerce_api.transaction_event.ReturnEvent,
            "examples/data/batch_marketing_email_send.ndjson": lexer_schemas.marketing_api.email_event.EmailSend,
            "examples/data/batch_marketing_email_open.ndjson": lexer_schemas.marketing_api.email_event.EmailOpen,
            "examples/data/batch_marketing_email_click.ndjson": lexer_schemas.marketing_api.email_event.EmailClick,
            "examples/data/batch_marketing_email_bounce.ndjson": lexer_schemas.marketing_api.email_event.EmailBounce,
            "examples/data/batch_marketing_email_subscribe.ndjson": lexer_schemas.marketing_api.email_event.EmailSubscribe,
            "examples/data/batch_marketing_sms_subscribe.ndjson": lexer_schemas.marketing_api.sms_event.SMSSubscribe,
            "examples/data/batch_marketing_sms_send.ndjson": lexer_schemas.marketing_api.sms_event.SMSSend,
            "examples/data/batch_marketing_sms_click.ndjson": lexer_schemas.marketing_api.sms_event.SMSClick,
            "examples/data/batch_profile_customer_record.ndjson": lexer_schemas.profile_api.customer_record.CustomerRecord,
            "examples/csv_to_ndjson/example.csv.ndjson": lexer_schemas.profile_api.customer_record.CustomerRecord,
        }
        errors = []

        for example_file, model in example_to_model.items():
            with open(example_file, "r") as f:
                for row_number, line in enumerate(f):
                    try:
                        model.parse_raw(
                            line
                        )
                    except Exception as error:
                        errors.append(f"At row number {row_number}: {error}")

        self.assertEqual(errors, [])
