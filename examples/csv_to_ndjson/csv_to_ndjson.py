#!/usr/bin/env python3

import argparse
import csv
from itertools import groupby
from typing import Any, Dict

from lexer_schemas.common import imported_api_names
from lexer_schemas.profile_api.customer_record import CustomerRecord


def nest_dotted_columns(row: Dict[str, str]) -> Dict[str, Any]:
    """Expand fields in a dict to nested objects when the field keys contain dots"""
    column_names = row.keys()

    # split the first part of the dot-seperated field names away from the rest.
    # eg: ["a.b.c", "a.c", "a"] -> [["a", "b.c"], ["a", "c"], ["a"]]
    split_column_names = [column.split(".", 1) for column in column_names]

    # filter the fields down to the ones that do have dot seperation, and
    # therefore will need to be nested.
    # eg: [["a", "b.c"], ["a", "c"], ["a"]] -> [["a", "b.c"], ["a", "c"]]
    nested_columns = [column for column in split_column_names if len(column) > 1]

    # filter the fields down to the ones that do not have dot seperation
    # These fields can just be passed through this method as-is
    # Note that the split has transformed these fields into single element lists
    # eg: [["a", "b.c"], ["a", "c"], ["a"]] -> [["a"]]
    non_nested_columns = [column for column in split_column_names if len(column) == 1]

    # Group the fields that do need to be nested by their common prefix
    # ie: the first element of the split.
    # These groups will be used to create the nested objects.
    # eg: [["a", "b.c"], ["a", "c"], ["b", "d"]]
    #  -> [("a", [["a", "b.c"], ["a", "c"]]), ("b", [["b", "d"]])]
    common_nested_prefixes = groupby(nested_columns, key=lambda i: i[0])

    # Reconsititute the part of the row that doesn't need nesting
    out_row: Dict[str, Any] = {key[0]: row[key[0]] for key in non_nested_columns}

    # Tranforms the nested fields in the row
    nested_row = {
        # Recurse into nested fields to do any nesting on sub groups
        # that may be required.
        group_key: nest_dotted_columns(
            # Reconstitute the sub groups
            # eg : {"b.c": row["a.b.c"]}
            {col[1]: row[".".join(col)] for col in group_val}
        )
        for group_key, group_val in common_nested_prefixes
    }

    # Merge the nested fields of the row with the non-nested fields.
    # Note, this will destroy any overlapping non-nested fields.
    out_row.update(nested_row)

    return out_row


def run_convert(input_file: str, record_type: str, output_file: str) -> None:
    with open(input_file, "r") as input_data:
        reader = csv.DictReader(input_data)

        with open(output_file, "w") as output_data:
            for row in reader:
                output_data.write(
                    imported_api_names[record_type](**nest_dotted_columns(row)).json()
                    + "\n"
                )


if __name__ == "__main__":

    argp = argparse.ArgumentParser()
    argp.add_argument("--input-file", required=True)
    argp.add_argument("--record-type", choices=imported_api_names.keys(), required=True)
    argp.add_argument("--output-file", required=True)

    args = argp.parse_args()

    run_convert(args.input_file, args.record_type, args.output_file)
