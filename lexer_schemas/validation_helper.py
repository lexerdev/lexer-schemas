# taken from https://github.com/python-jsonschema/jsonschema/blob/9882dbeb1a0a0cb1c7e521837132a91cfcc9e0f0/jsonschema/_keywords.py
# Forked to swap the messages sent by the validation errors to remove PII
from fractions import Fraction
from typing import TYPE_CHECKING
import re

from jsonschema._utils import (
    ensure_list,
    equal,
    extras_msg,
    find_additional_properties,
    uniq,
)

if TYPE_CHECKING:
    from jsonschema._utils import (
        find_evaluated_item_indexes_by_schema,
        find_evaluated_property_keys_by_schema,
    )
from jsonschema.exceptions import FormatError, ValidationError


def patternProperties(validator, patternProperties, instance, schema):
    if not validator.is_type(instance, "object"):
        return

    for pattern, subschema in patternProperties.items():
        for k, v in instance.items():
            if re.search(pattern, k):
                yield from validator.descend(
                    v,
                    subschema,
                    path=k,
                    schema_path=pattern,
                )


def propertyNames(validator, propertyNames, instance, schema):
    if not validator.is_type(instance, "object"):
        return

    for property in instance:
        yield from validator.descend(instance=property, schema=propertyNames)


def additionalProperties(validator, aP, instance, schema):
    if not validator.is_type(instance, "object"):
        return

    extras = set(find_additional_properties(instance, schema))

    if validator.is_type(aP, "object"):
        for extra in extras:
            yield from validator.descend(instance[extra], aP, path=extra)
    elif not aP and extras:
        if "patternProperties" in schema:
            verb = "does" if len(extras) == 1 else "do"
            joined = ", ".join(repr(each) for each in sorted(extras))
            patterns = ", ".join(
                repr(each) for each in sorted(schema["patternProperties"])
            )
            error = f"Value not match any of the regexes: {patterns}"
            yield ValidationError(error)
        else:
            error = "Additional properties are not allowed (%s %s unexpected)"
            yield ValidationError(error % extras_msg(sorted(extras, key=str)))


def items(validator, items, instance, schema):
    if not validator.is_type(instance, "array"):
        return

    prefix = len(schema.get("prefixItems", []))
    total = len(instance)
    extra = total - prefix
    if extra <= 0:
        return

    if items is False:
        rest = instance[prefix:] if extra != 1 else instance[prefix]
        item = "items" if prefix != 1 else "item"
        yield ValidationError(
            f"Expected at most {prefix} {item} but found {extra} extra",
        )
    else:
        for index in range(prefix, total):
            yield from validator.descend(
                instance=instance[index],
                schema=items,
                path=index,
            )


def const(validator, const, instance, schema):
    if not equal(instance, const):
        yield ValidationError(f"{const!r} was expected")


def contains(validator, contains, instance, schema):
    if not validator.is_type(instance, "array"):
        return

    matches = 0
    min_contains = schema.get("minContains", 1)
    max_contains = schema.get("maxContains", len(instance))

    contains_validator = validator.evolve(schema=contains)

    for each in instance:
        if contains_validator.is_valid(each):
            matches += 1
            if matches > max_contains:
                yield ValidationError(
                    "Too many items match the given schema "
                    f"(expected at most {max_contains})",
                    validator="maxContains",
                    validator_value=max_contains,
                )
                return

    if matches < min_contains:
        if not matches:
            yield ValidationError(
                f"Value does not contain items matching the given schema",
            )
        else:
            yield ValidationError(
                "Too few items match the given schema (expected at least "
                f"{min_contains} but only {matches} matched)",
                validator="minContains",
                validator_value=min_contains,
            )


def exclusiveMinimum(validator, minimum, instance, schema):
    if not validator.is_type(instance, "number"):
        return

    if instance <= minimum:
        yield ValidationError(
            f"Value is less than or equal to the minimum of {minimum!r}",
        )


def exclusiveMaximum(validator, maximum, instance, schema):
    if not validator.is_type(instance, "number"):
        return

    if instance >= maximum:
        yield ValidationError(
            f"Value is greater than or equal to the maximum of {maximum!r}",
        )


def minimum(validator, minimum, instance, schema):
    if not validator.is_type(instance, "number"):
        return

    if instance < minimum:
        message = f"Value is less than the minimum of {minimum!r}"
        yield ValidationError(message)


def maximum(validator, maximum, instance, schema):
    if not validator.is_type(instance, "number"):
        return

    if instance > maximum:
        message = f"Value is greater than the maximum of {maximum!r}"
        yield ValidationError(message)


def multipleOf(validator, dB, instance, schema):
    if not validator.is_type(instance, "number"):
        return

    if isinstance(dB, float):
        quotient = instance / dB
        try:
            failed = int(quotient) != quotient
        except OverflowError:
            # When `instance` is large and `dB` is less than one,
            # quotient can overflow to infinity; and then casting to int
            # raises an error.
            #
            # In this case we fall back to Fraction logic, which is
            # exact and cannot overflow.  The performance is also
            # acceptable: we try the fast all-float option first, and
            # we know that fraction(dB) can have at most a few hundred
            # digits in each part.  The worst-case slowdown is therefore
            # for already-slow enormous integers or Decimals.
            failed = (Fraction(instance) / Fraction(dB)).denominator != 1
    else:
        failed = instance % dB

    if failed:
        yield ValidationError(f"Value is not a multiple of {dB}")


def minItems(validator, mI, instance, schema):
    if validator.is_type(instance, "array") and len(instance) < mI:
        message = "should be non-empty" if mI == 1 else "is too short"
        yield ValidationError(f"Value {message}")


def maxItems(validator, mI, instance, schema):
    if validator.is_type(instance, "array") and len(instance) > mI:
        message = "is expected to be empty" if mI == 0 else "is too long"
        yield ValidationError(f"Value {message}")


def uniqueItems(validator, uI, instance, schema):
    if uI and validator.is_type(instance, "array") and not uniq(instance):
        yield ValidationError(f"Value has non-unique elements")


def pattern(validator, patrn, instance, schema):
    if validator.is_type(instance, "string") and not re.search(patrn, instance):
        yield ValidationError(f"Value does not match {patrn!r}")


def format(validator, format, instance, schema):
    if validator.format_checker is not None:
        try:
            validator.format_checker.check(instance, format)
        except FormatError as error:
            yield ValidationError(error.message, cause=error.cause)


def minLength(validator, mL, instance, schema):
    if validator.is_type(instance, "string") and len(instance) < mL:
        message = "should be non-empty" if mL == 1 else "is too short"
        yield ValidationError(f"Value {message}")


def maxLength(validator, mL, instance, schema):
    if validator.is_type(instance, "string") and len(instance) > mL:
        message = "is expected to be empty" if mL == 0 else "is too long"
        yield ValidationError(f"Value {message}")


def dependentRequired(validator, dependentRequired, instance, schema):
    if not validator.is_type(instance, "object"):
        return

    for property, dependency in dependentRequired.items():
        if property not in instance:
            continue

        for each in dependency:
            if each not in instance:
                message = f"{each!r} is a dependency of {property!r}"
                yield ValidationError(message)


def dependentSchemas(validator, dependentSchemas, instance, schema):
    if not validator.is_type(instance, "object"):
        return

    for property, dependency in dependentSchemas.items():
        if property not in instance:
            continue
        yield from validator.descend(
            instance,
            dependency,
            schema_path=property,
        )


def enum(validator, enums, instance, schema):
    if all(not equal(each, instance) for each in enums):
        yield ValidationError(f"Value is not one of {enums!r}")


def ref(validator, ref, instance, schema):
    yield from validator._validate_reference(ref=ref, instance=instance)


def dynamicRef(validator, dynamicRef, instance, schema):
    yield from validator._validate_reference(ref=dynamicRef, instance=instance)


def type(validator, types, instance, schema):
    types = ensure_list(types)

    if not any(validator.is_type(instance, type) for type in types):
        reprs = ", ".join(repr(type) for type in types)
        yield ValidationError(f"Value is not of type {reprs}")


def properties(validator, properties, instance, schema):
    if not validator.is_type(instance, "object"):
        return

    for property, subschema in properties.items():
        if property in instance:
            yield from validator.descend(
                instance[property],
                subschema,
                path=property,
                schema_path=property,
            )


def required(validator, required, instance, schema):
    if not validator.is_type(instance, "object"):
        return
    for property in required:
        if property not in instance:
            yield ValidationError(f"{property!r} is a required property")


def minProperties(validator, mP, instance, schema):
    if validator.is_type(instance, "object") and len(instance) < mP:
        message = (
            "should be non-empty" if mP == 1 else "does not have enough properties"
        )
        yield ValidationError(f"Value {message}")


def maxProperties(validator, mP, instance, schema):
    if not validator.is_type(instance, "object"):
        return
    if validator.is_type(instance, "object") and len(instance) > mP:
        message = "is expected to be empty" if mP == 0 else "has too many properties"
        yield ValidationError(f"Value {message}")


def allOf(validator, allOf, instance, schema):
    for index, subschema in enumerate(allOf):
        yield from validator.descend(instance, subschema, schema_path=index)


def anyOf(validator, anyOf, instance, schema):
    all_errors = []
    for index, subschema in enumerate(anyOf):
        errs = list(validator.descend(instance, subschema, schema_path=index))
        if not errs:
            break
        all_errors.extend(errs)
    else:
        yield ValidationError(
            f"Value is not valid under any of the given schemas",
            context=all_errors,
        )


def oneOf(validator, oneOf, instance, schema):
    subschemas = enumerate(oneOf)
    all_errors = []
    for index, subschema in subschemas:
        errs = list(validator.descend(instance, subschema, schema_path=index))
        if not errs:
            first_valid = subschema
            break
        all_errors.extend(errs)
    else:
        yield ValidationError(
            f"Value is not valid under any of the given schemas",
            context=all_errors,
        )

    more_valid = [
        each
        for _, each in subschemas
        if validator.evolve(schema=each).is_valid(instance)
    ]
    if more_valid:
        more_valid.append(first_valid)
        reprs = ", ".join(repr(schema) for schema in more_valid)
        yield ValidationError(f"Value is valid under each of {reprs}")


def not_(validator, not_schema, instance, schema):
    if validator.evolve(schema=not_schema).is_valid(instance):
        message = f"Value should not be valid under {not_schema!r}"
        yield ValidationError(message)


def if_(validator, if_schema, instance, schema):
    if validator.evolve(schema=if_schema).is_valid(instance):
        if "then" in schema:
            then = schema["then"]
            yield from validator.descend(instance, then, schema_path="then")
    elif "else" in schema:
        else_ = schema["else"]
        yield from validator.descend(instance, else_, schema_path="else")


def unevaluatedItems(validator, unevaluatedItems, instance, schema):
    if not validator.is_type(instance, "array"):
        return
    evaluated_item_indexes = find_evaluated_item_indexes_by_schema(
        validator,
        instance,
        schema,
    )
    unevaluated_items = [
        item
        for index, item in enumerate(instance)
        if index not in evaluated_item_indexes
    ]
    if unevaluated_items:
        yield ValidationError("Unevaluated items are not allowed")


def unevaluatedProperties(validator, unevaluatedProperties, instance, schema):
    if not validator.is_type(instance, "object"):
        return
    evaluated_keys = find_evaluated_property_keys_by_schema(
        validator,
        instance,
        schema,
    )
    unevaluated_keys = []
    for property in instance:
        if property not in evaluated_keys:
            for _ in validator.descend(
                instance[property],
                unevaluatedProperties,
                path=property,
                schema_path=property,
            ):
                # FIXME: Include context for each unevaluated property
                #        indicating why it's invalid under the subschema.
                unevaluated_keys.append(property)  # noqa: PERF401

    if unevaluated_keys:
        if unevaluatedProperties is False:
            error = "Unevaluated properties are not allowed (%s %s unexpected)"
            extras = sorted(unevaluated_keys, key=str)
            yield ValidationError(error % extras_msg(extras))
        else:
            error = (
                "Unevaluated properties are not valid under "
                "the given schema (%s %s unevaluated and invalid)"
            )
            yield ValidationError(error % extras_msg(unevaluated_keys))


def prefixItems(validator, prefixItems, instance, schema):
    if not validator.is_type(instance, "array"):
        return

    for (index, item), subschema in zip(enumerate(instance), prefixItems):
        yield from validator.descend(
            instance=item,
            schema=subschema,
            schema_path=index,
            path=index,
        )


# -----------------------LEGACY VALIDATIONS------------------------------


def additionalItems(validator, aI, instance, schema):
    if not validator.is_type(instance, "array") or validator.is_type(
        schema.get("items", {}), "object"
    ):
        return

    len_items = len(schema.get("items", []))
    if validator.is_type(aI, "object"):
        for index, item in enumerate(instance[len_items:], start=len_items):
            yield from validator.descend(item, aI, path=index)
    elif not aI and len(instance) > len(schema.get("items", [])):
        error = "Additional items are not allowed (%s %s unexpected)"
        yield ValidationError(
            error % extras_msg(instance[len(schema.get("items", [])) :]),
        )


def dependencies(
    validator,
    dependencies,
    instance,
    schema,
):
    if not validator.is_type(instance, "object"):
        return

    for property, dependency in dependencies.items():
        if property not in instance:
            continue

        if validator.is_type(dependency, "array"):
            for each in dependency:
                if each not in instance:
                    message = f"{each!r} is a dependency of {property!r}"
                    yield ValidationError(message)
        else:
            yield from validator.descend(
                instance,
                dependency,
                schema_path=property,
            )
