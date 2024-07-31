import json
import jsonschema
import unittest
from lexer_schemas.validation import setup_lexer_validator




class TestValidator(unittest.TestCase):
    def setUp(self):
        self.events = [
            {
                "required_field": "test_1",
                "enum_field": "manual",
                "number_field": 32.23,
                "datetime_field": "2023-03-06T12:26:47Z",
                "date_field": "2023-03-06",
                "integer_field": 32,
                "boolean_field": True,
                "array_field": ["yes", "no", "maybe", "can you repeat the question?"],
                "object_field": {
                    "entity_ref": {
                        "id": "ting",
                        "id_type": "typeos",
                        "dataset_id": "big_tests",
                    }
                },
            },
            {
                "required_field": "test_2",
                "enum_field": None,
                "number_field": None,
                "datetime_field": None,
                "date_field": None,
                "integer_field": None,
                "boolean_field": None,
                "array_field": None,
                "object_field": None,
            },
            {
                "required_field": "test_3",
            },
            {
                "not": "an_event"
            },
            {
                "required_field": None,
                "enum_field": "manual",
                "number_field": 32.23,
                "datetime_field": "2023-03-06T12:26:47Z",
                "date_field": "2023-03-06",
                "integer_field": 32,
                "boolean_field": True,
                "array_field": ["yes", "no", "maybe", "can you repeat the question?"],
                "object_field": {
                    "entity_ref": {
                        "id": "ting",
                        "id_type": "typeos",
                        "dataset_id": "big_tests",
                    }
                },
            },
            {
                "required_field": "test_6",
                "enum_field": "not_in_enum",
                "number_field": "NAN",
                "datetime_field": 1738,
                "date_field": 32,
                "integer_field": "NAN",
                "boolean_field": "true",
                "array_field": "None",
                "object_field": "None",
            },
            {
                "required_field": "test_7",
                "array_field": ["None", 7],
                "object_field": {
                    "entity_ref": {
                        "id": None,
                        "id_type": "typeos",
                        "dataset_id": "big_tests",
                    }
                },
            },
            {
                "required_field": "test_8",
                "datetime_field": "right type wrong format",
                "date_field": "right_type_wrong_format",
            },
        ]
        self.schema = {
                "record_table": "schema_event",
                "title": "Test Event",
                "description": "An example of an event",
                "type": "object",
                "properties": {
                    "required_field": {
                        "title": "Required String field",
                        "type": "string",
                    },
                    "enum_field": {
                        "title": "Nullable Enum field",
                        "enum": ["manual", "auto", "anonymous", "location_change", None],
                    },
                    "number_field": {
                        "title": "Nullable number Field",
                        "type": ["number", "null"],
                    },
                    "datetime_field": {
                        "title": "Nullable date Field",
                        "type": ["string", "null"],
                        "format": "date-time",
                    },
                    "date_field": {
                        "title": "Nullable date Field",
                        "type": ["string", "null"],
                        "format": "date",
                    },
                    "integer_field": {
                        "title": "Nullable integer Field",
                        "type": ["integer", "null"],
                    },
                    "boolean_field": {
                        "title": "Nullable boolean Field",
                        "type": ["boolean", "null"],
                    },
                    "array_field": {
                        "title": "Nullable array of strings Field",
                        "type": ["array", "null"],
                        "items": {"type": "string"},
                    },
                },
                "required": ["required_field"],
            }


    def test_lexer_validator(self):
        events = self.events

        expected_valid = [json.dumps(e) for e in [
            {
                "required_field": "test_1",
                "enum_field": "manual",
                "number_field": 32.23,
                "datetime_field": "2023-03-06T12:26:47Z",
                "date_field": "2023-03-06",
                "integer_field": 32,
                "boolean_field": True,
                "array_field": ["yes", "no", "maybe", "can you repeat the question?"],
                "object_field": {
                    "entity_ref": {
                        "id": "ting",
                        "id_type": "typeos",
                        "dataset_id": "big_tests",
                    }
                },
            },
            {
                "required_field": "test_2",
                "enum_field": None,
                "number_field": None,
                "datetime_field": None,
                "date_field": None,
                "integer_field": None,
                "boolean_field": None,
                "array_field": None,
                "object_field": None,
            },
            {
                "required_field": "test_3",
            }
        ]]

        expected_errors = [
            ["'required_field' is a required property"],
            ["Value is not of type 'string'"],
            ["Value is not one of ['manual', 'auto', 'anonymous', 'location_change', None]", "Value is not of type 'number', 'null'", "Value is not of type 'string', 'null'", "Value is not of type 'string', 'null'", "Value is not of type 'integer', 'null'", "Value is not of type 'boolean', 'null'", "Value is not of type 'array', 'null'"],
            ["Value is not of type 'string'"],
            ["'right type wrong format' is not a 'date-time'", "'right_type_wrong_format' is not a 'date'"]
        ]

        raw_events = [json.dumps(e) for e in events]
        validator = setup_lexer_validator(schema=self.schema)
        parsed_records = []
        errors = []
        for record in raw_events:
            error_list = list(validator.iter_errors(json.loads(record)))
            if len(error_list) == 0:
                parsed_records.append(record)
            else:
                errors.append([str(e.message) for e in error_list])

        self.assertEqual(len(parsed_records), 3)
        self.assertEqual(len(errors), 5)
        self.assertEqual(expected_valid, parsed_records)
        self.assertEqual(expected_errors, errors)


    def test_json_draft_7_validator(self):
        events = self.events

        expected_valid = [json.dumps(e) for e in [
            {
                "required_field": "test_1",
                "enum_field": "manual",
                "number_field": 32.23,
                "datetime_field": "2023-03-06T12:26:47Z",
                "date_field": "2023-03-06",
                "integer_field": 32,
                "boolean_field": True,
                "array_field": ["yes", "no", "maybe", "can you repeat the question?"],
                "object_field": {
                    "entity_ref": {
                        "id": "ting",
                        "id_type": "typeos",
                        "dataset_id": "big_tests",
                    }
                },
            },
            {
                "required_field": "test_2",
                "enum_field": None,
                "number_field": None,
                "datetime_field": None,
                "date_field": None,
                "integer_field": None,
                "boolean_field": None,
                "array_field": None,
                "object_field": None,
            },
            {
                "required_field": "test_3",
            }
        ]]

        expected_errors = [
            ["'required_field' is a required property"],
            ["None is not of type 'string'"],
            ["'not_in_enum' is not one of ['manual', 'auto', 'anonymous', 'location_change', None]", "'NAN' is not of type 'number', 'null'", "1738 is not of type 'string', 'null'", "32 is not of type 'string', 'null'", "'NAN' is not of type 'integer', 'null'", "'true' is not of type 'boolean', 'null'", "'None' is not of type 'array', 'null'"],
            ["7 is not of type 'string'"],
            ["'right type wrong format' is not a 'date-time'", "'right_type_wrong_format' is not a 'date'"]
        ]

        raw_events = [json.dumps(e) for e in events]
        validator = setup_lexer_validator(schema=self.schema, validator=jsonschema.Draft7Validator)
        parsed_records = []
        errors = []
        for record in raw_events:
            error_list = list(validator.iter_errors(json.loads(record)))
            if len(error_list) == 0:
                parsed_records.append(record)
            else:
                errors.append([str(e.message) for e in error_list])

        self.assertEqual(len(parsed_records), 3)
        self.assertEqual(len(errors), 5)
        self.assertEqual(expected_valid, parsed_records)
        self.assertEqual(expected_errors, errors)
