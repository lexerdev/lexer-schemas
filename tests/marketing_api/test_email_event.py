import json

import pytest
from pydantic import ValidationError

from lexer_schemas.marketing_api.email_event import (
    EmailBounce,
    EmailClick,
    EmailOpen,
    EmailSend,
    EmailSubscribe,
)


class TestEmailSend:
    def test_email_send_valid(self):
        expected_record = {
            "link": {"email": "jane@fake.com"},
            "action_at": "2022-04-23T14:15:22+00:00",
            "email_id": "10939084127",
            "campaign_id": "Menswear Sale Apr 2022",
            "from": {"name": "Jane Doe", "email": "jane@fake.com"},
            "to": {"name": "Jane Doe", "email": "jane@fake.com"},
            "subject": "April Deals!",
            "list": None,
            "body": None,
        }

        actual_record = EmailSend.parse_obj(expected_record)

        assert json.loads(actual_record.json(by_alias=True)) == expected_record

    def test_email_send_invalid(self):

        expected_error = r"1 validation error for EmailSend\nemail_id\n  field required"

        with pytest.raises(ValidationError, match=expected_error):
            EmailSend.parse_obj(
                {
                    "link": {"email": "jane@fake.com"},
                    "action_at": "2022-04-23T14:15:22+00:00",
                }
            )


class TestEmailOpen:
    def test_email_open_valid(self):
        expected_record = {
            "link": {"email": "jane@fake.com"},
            "action_at": "2022-04-23T14:15:22+00:00",
            "email_id": "10939084127",
            "campaign_id": "Menswear Sale Apr 2022",
            "from": {"name": "Jane Doe", "email": "jane@fake.com"},
            "to": {"name": "Jane Doe", "email": "jane@fake.com"},
            "list": None,
        }

        actual_record = EmailOpen.parse_obj(expected_record)

        assert json.loads(actual_record.json(by_alias=True)) == expected_record

    def test_email_open_invalid(self):

        expected_error = r"1 validation error for EmailOpen\nemail_id\n  field required"

        with pytest.raises(ValidationError, match=expected_error):
            EmailOpen.parse_obj(
                {
                    "link": {"email": "jane@fake.com"},
                    "action_at": "2022-04-23T14:15:22+00:00",
                }
            )


class TestEmailClick:
    def test_email_click_valid(self):
        expected_record = {
            "link": {"email": "jane@fake.com"},
            "action_at": "2022-04-23T14:15:22+00:00",
            "email_id": "10939084127",
            "campaign_id": "Menswear Sale Apr 2022",
            "from": {"name": "Jane Doe", "email": "jane@fake.com"},
            "to": {"name": "Jane Doe", "email": "jane@fake.com"},
            "clicked_link": {"name": "string", "url": "string"},
            "list": None,
        }

        actual_record = EmailClick.parse_obj(expected_record)

        assert json.loads(actual_record.json(by_alias=True)) == expected_record

    def test_email_click_invalid(self):

        expected_error = (
            r"1 validation error for EmailClick\nemail_id\n  field required"
        )

        with pytest.raises(ValidationError, match=expected_error):
            EmailClick.parse_obj(
                {
                    "link": {"email": "jane@fake.com"},
                    "action_at": "2022-04-23T14:15:22+00:00",
                }
            )


class TestEmailBounce:
    def test_email_bounce_valid(self):
        expected_record = {
            "link": {"email": "jane@fake.com"},
            "action_at": "2022-04-23T14:15:22+00:00",
            "email_id": "10939084127",
            "from": {"name": "Jane Doe", "email": "jane@fake.com"},
            "to": {"name": "Jane Doe", "email": "jane@fake.com"},
            "list": None,
        }

        actual_record = EmailBounce.parse_obj(expected_record)

        assert json.loads(actual_record.json(by_alias=True)) == expected_record

    def test_email_bounce_invalid(self):

        expected_error = (
            r"1 validation error for EmailBounce\nemail_id\n  field required"
        )

        with pytest.raises(ValidationError, match=expected_error):
            EmailBounce.parse_obj(
                {
                    "link": {"email": "jane@fake.com"},
                    "action_at": "2022-04-23T14:15:22+00:00",
                }
            )


class TestEmailSubscribe:
    def test_email_subscribe_valid(self):
        expected_record = {
            "link": {"email": "jane@fake.com"},
            "action_at": "2022-04-23T14:15:22+00:00",
            "email_id": "10939084127",
            "list": None,
            "status": "subscribed",
        }

        actual_record = EmailSubscribe.parse_obj(expected_record)

        assert json.loads(actual_record.json(by_alias=True)) == expected_record

    def test_email_subscribe_invalid(self):

        expected_error = r"1 validation error for EmailSubscribe\nstatus\n  value is not a valid enumeration"

        with pytest.raises(ValidationError, match=expected_error):
            EmailSubscribe.parse_obj(
                {
                    "link": {"email": "jane@fake.com"},
                    "action_at": "2022-04-23T14:15:22+00:00",
                    "email_id": "10939084127",
                    "status": "NotARealStatus",
                }
            )
