import json

import pytest
from pydantic import ValidationError

from lexer_schemas.marketing_api.sms_event import SMSClick, SMSSend, SMSSubscribe


class TestSMSClick:
    def test_sms_click_valid(self):
        expected_record = {
            "link": {"email": "phephen@phephmail.com"},
            "action_at": "2022-04-23T14:15:22+00:00",
            "sms_id": "10939084127",
            "campaign_id": "Menswear Sale Apr 2022",
            "from": {"name": "My Brand", "number": "61456758345"},
            "to": {"name": "Phephen", "number": "61408309237"},
            "list": None,
        }

        actual_record = SMSClick.parse_obj(expected_record)

        assert json.loads(actual_record.json(by_alias=True)) == expected_record

    def test_sms_click_invalid(self):

        expected_error = r"1 validation error for SMSClick\nsms_id\n  field required"

        with pytest.raises(ValidationError, match=expected_error):
            SMSClick.parse_obj(
                {
                    "link": {"email": "phephen@phephmail.com"},
                    "action_at": "2022-04-23T14:15:22+00:00",
                }
            )


class TestSMSSend:
    def test_sms_send_valid(self):
        expected_record = {
            "link": {"email": "phephen@phephmail.com"},
            "action_at": "2022-04-23T14:15:22+00:00",
            "sms_id": "10939084127",
            "campaign_id": "Menswear Sale Apr 2022",
            "from": {"name": "My Brand", "number": "61456758345"},
            "to": {"name": "Phephen", "number": "61408309237"},
            "list": None,
            "body": None,
        }

        actual_record = SMSSend.parse_obj(expected_record)

        assert json.loads(actual_record.json(by_alias=True)) == expected_record

    def test_sms_send_invalid(self):

        expected_error = r"1 validation error for SMSSend\nsms_id\n  field required"

        with pytest.raises(ValidationError, match=expected_error):
            SMSSend.parse_obj(
                {
                    "link": {"email": "phephen@phephmail.com"},
                    "action_at": "2022-04-23T14:15:22+00:00",
                }
            )


class TestSMSSubscribe:
    def test_sms_subscribe_valid(self):
        expected_record = {
            "link": {"email": "phephen@phephmail.com"},
            "action_at": "2022-04-23T14:15:22+00:00",
            "sms_id": "10939084127",
            "list": None,
            "status": "subscribed",
        }

        actual_record = SMSSubscribe.parse_obj(expected_record)

        assert json.loads(actual_record.json(by_alias=True)) == expected_record

    def test_sms_subscribe_invalid(self):

        expected_error = r"1 validation error for SMSSubscribe\nstatus\n  value is not a valid enumeration"

        with pytest.raises(ValidationError, match=expected_error):
            SMSSubscribe.parse_obj(
                {
                    "link": {"email": "phephen@phephmail.com"},
                    "action_at": "2022-04-23T14:15:22+00:00",
                    "sms_id": "10939084127",
                    "status": "NotARealStatus",
                }
            )
