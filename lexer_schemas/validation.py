import jsonschema
from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel, ValidationError
from lexer_schemas import validation_helper

json_schema_validator = {
    "$ref": validation_helper.ref,
    "additionalItems": validation_helper.additionalItems,
    "additionalProperties": validation_helper.additionalProperties,
    "allOf": validation_helper.allOf,
    "anyOf": validation_helper.anyOf,
    "const": validation_helper.const,
    "contains": validation_helper.contains,
    "dependencies": validation_helper.dependencies,
    "enum": validation_helper.enum,
    "exclusiveMaximum": validation_helper.exclusiveMaximum,
    "exclusiveMinimum": validation_helper.exclusiveMinimum,
    "format": validation_helper.format,
    "if": validation_helper.if_,
    "items": validation_helper.items,
    "maxItems": validation_helper.maxItems,
    "maxLength": validation_helper.maxLength,
    "maxProperties": validation_helper.maxProperties,
    "maximum": validation_helper.maximum,
    "minItems": validation_helper.minItems,
    "minLength": validation_helper.minLength,
    "minProperties": validation_helper.minProperties,
    "minimum": validation_helper.minimum,
    "multipleOf": validation_helper.multipleOf,
    "not": validation_helper.not_,
    "oneOf": validation_helper.oneOf,
    "pattern": validation_helper.pattern,
    "patternProperties": validation_helper.patternProperties,
    "properties": validation_helper.properties,
    "propertyNames": validation_helper.propertyNames,
    "required": validation_helper.required,
    "type": validation_helper.type,
    "uniqueItems": validation_helper.uniqueItems,
}



class CustomDraft7Validator(jsonschema.Draft7Validator):
    VALIDATORS = json_schema_validator


class DateTimeValidationModel(BaseModel):
    datetime_validation: Optional[datetime]


def setup_lexer_validator(schema: Dict, validator = CustomDraft7Validator):
    """
    A universal way to setup the jsonschema validation for Lexer's schema events, using the raw_schema and the validation class as parameters
    The validation class parameter is defaulted to Lexers custom version of the jsonschema.Draft7Validator class
    """
    format_checker = jsonschema.FormatChecker()
    if "date-time" not in format_checker.checkers:
        @format_checker.checks("date-time", ValidationError)
        def is_date_time(instance):
            DateTimeValidationModel(datetime_validation=instance)
            return True

    return validator(schema, format_checker=format_checker)
