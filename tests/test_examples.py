import unittest
from lexer_schemas.commerce_api import product_entity, transaction_event
from lexer_schemas.marketing_api import email_event, sms_event
from lexer_schemas.profile_api import customer_record


class TestExamples(unittest.TestCase):

    def test_example_data(self):
        example_to_model = {
            "examples/data/batch_commerce_product.ndjson": product_entity.ProductRecord,
            "examples/data/batch_commerce_purchase.ndjson": transaction_event.PurchaseEvent,
            "examples/data/batch_commerce_return.ndjson": transaction_event.ReturnEvent,
            "examples/data/batch_marketing_email_send.ndjson": email_event.EmailSend,
            "examples/data/batch_marketing_email_open.ndjson": email_event.EmailOpen,
            "examples/data/batch_marketing_email_click.ndjson": email_event.EmailClick,
            "examples/data/batch_marketing_email_bounce.ndjson": email_event.EmailBounce,
            "examples/data/batch_marketing_email_subscribe.ndjson": email_event.EmailSubscribe,
            "examples/data/batch_marketing_sms_subscribe.ndjson": sms_event.SMSSubscribe,
            "examples/data/batch_marketing_sms_send.ndjson": sms_event.SMSSend,
            "examples/data/batch_marketing_sms_click.ndjson": sms_event.SMSClick,
            "examples/data/batch_profile_customer_record.ndjson": customer_record.CustomerRecord,
            "examples/csv_to_ndjson/example.csv.ndjson": customer_record.CustomerRecord,
        }
        errors = []

        for example_file, model in example_to_model.items():
            with open(example_file, "r") as f:
                for row_number, line in enumerate(f):
                    try:
                        model.parse_raw(line)
                    except Exception as error:
                        errors.append(f"At row number {row_number}: {error}")

        self.assertEqual(errors, [])
