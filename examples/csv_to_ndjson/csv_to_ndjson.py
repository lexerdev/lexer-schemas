#!/usr/bin/env python3

import argparse
import csv
from itertools import groupby
from typing import Any, Dict

from lexer_schemas.common import imported_api_names
from lexer_schemas.profile_api.customer_record import CustomerRecord


def nest_dotted_columns(row: Dict[str, str]) -> Dict[str, Any]:
    column_names = row.keys()
    split_column_names = [column.split(".", 1) for column in column_names]
    nested_columns = [column for column in split_column_names if len(column) > 1]
    non_nested_columns = [column for column in split_column_names if len(column) == 1]
    common_nested_prefixes = groupby(nested_columns, key=lambda i: i[0])
    out_row: Dict[str, Any] = {key[0]: row[key[0]] for key in non_nested_columns}
    nested_row = {
        group_key: nest_dotted_columns(
            {col[1]: row[".".join(col)] for col in group_val}
        )
        for group_key, group_val in common_nested_prefixes
    }
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
