#!/usr/bin/env python3

import argparse
import os
import sys

import requests
from lexer_schemas.commerce_api.product_entity import ProductRecord
from lexer_schemas.commerce_api.transaction_event import PurchaseEvent, ReturnEvent
from lexer_schemas.marketing_api.email_event import (
    EmailBounce,
    EmailClick,
    EmailOpen,
    EmailSend,
    EmailSubscribe,
)
from lexer_schemas.marketing_api.sms_event import SMSClick, SMSSend, SMSSubscribe
from lexer_schemas.profile_api.customer_record import CustomerRecord
from lexer_schemas.common import imported_api_names


def upload_file(
    local_filename: str,
    record_type: str,
    destination_filename: str,
    destination_dataset_id: str,
    api_token: str,
) -> None:

    # A HTTP POST request to api.lexer.io/v1/uploads, if successful, will return a url that an api user
    # can run a PUT request on to upload a file. The destination parameters here allow lexer to automatically
    # trigger a dataset load after the upload of the file.
    uploads_response = requests.post(
        url="https://api.lexer.io/v1/uploads",
        headers={"Auth-Api-Token": api_token, "Content-Type": "application/json"},
        json={
            "filename": destination_filename,
            "destination": {
                "destination_type": "dataset_load",
                "dataset_id": destination_dataset_id,
                "record_type": record_type,
            },
        },
    )

    if uploads_response.status_code == 201:
        uploads_response_json = uploads_response.json()

        upload_id = uploads_response_json["id"]
        upload_url = uploads_response_json["url"]

        print(f"upload_id is: {upload_id}")

        with open(local_filename, "rb") as f:
            response = requests.put(upload_url, data=f.read())
            if response.status_code != 200:
                raise RuntimeError("Upload failed")

    else:
        print(f"Status Code: {uploads_response.status_code}")
        print(f"Response body: {uploads_response.text}")
        raise RuntimeError("Request to create upload failed")


def validate_file(local_filename: str, record_type: str) -> bool:
    """Validate the files against the schema for the record type"""

    # This refers to the pydantic schema from lexer_schemas that can be used to validate
    # the rows in the file.
    record_schema = imported_api_names[record_type]
    valid_records = 0
    invalid_records = 0
    row_number = 0

    # Note that an NDJSON file is a file containing one json object per line.
    # We open the file, and iterate it line-by-line, parsing each line into the specific
    # record schema. The record schema will raise an exception if there is an issue with any record.
    # This will print out the details of any exceptions encountered alongside the row number of the record.
    with open(local_filename, "r") as f:
        for line in f:
            try:
                record_schema.parse_raw(
                    line
                )  # Use the record schema to parse a string expected to contain a json object.
                valid_records += 1
            except Exception as error:
                print(f"At row number {row_number}: {error}")
                invalid_records += 1
            row_number += 1

    total_records = valid_records + invalid_records

    print(
        "Validation Complete.\n "
        + f"{total_records} total records\n "
        + f"{valid_records} valid records\n "
        + f"{invalid_records} invalid records"
    )

    if invalid_records > 0:
        return False
    else:
        return True


def validate_upload(
    local_filename: str,
    record_type: str,
    destination_filename: str,
    destination_dataset_id: str,
    api_token: str,
) -> bool:
    """Validate the file against the schema for the record type, then if it passes the validation, upload the file using the lexer file upload api."""
    if validate_file(local_filename, record_type):
        upload_file(
            local_filename,
            record_type,
            destination_filename,
            destination_dataset_id,
            api_token,
        )
        return True
    else:
        return False


if __name__ == "__main__":

    def get_env_if_empty(env_name):
        return lambda x: x if x != "" else os.environ.get(env_name)

    argp = argparse.ArgumentParser()

    subargps = argp.add_subparsers(dest="action")

    api_token_argp = argparse.ArgumentParser(add_help=False)
    api_token_argp.add_argument(
        "--api-token",
        type=get_env_if_empty("LEXER_UPLOAD_API_TOKEN"),
        help="Lexer File Upload API token",
        default="",
    )

    upload_params_argp = argparse.ArgumentParser(add_help=False)
    upload_params_argp.add_argument(
        "--destination-dataset-id",
        type=str,
        help="The id of the Lexer Dataset to upload the file to.",
        required=True,
    )
    upload_params_argp.add_argument(
        "--destination-filename",
        type=str,
        help="A name for the file that Lexer can use",
        required=True,
    )

    read_file_argp = argparse.ArgumentParser(add_help=False)
    read_file_argp.add_argument(
        "--local-filename",
        type=str,
        help="local filename of ndjson file to validate or upload",
        required=True,
    )
    read_file_argp.add_argument(
        "--record-type",
        type=str,
        choices=list(imported_api_names.keys()),
        help="The record type to upload or validate against",
        required=True,
    )

    subargps.add_parser(
        "upload_validate", parents=[api_token_argp, upload_params_argp, read_file_argp]
    )
    subargps.add_parser(
        "upload", parents=[api_token_argp, upload_params_argp, read_file_argp]
    )
    subargps.add_parser("validate", parents=[read_file_argp])

    args = argp.parse_args()

    if args.action == "upload":
        assert (
            args.api_token != ""
        ), "API Token must be provided in --api-token command line argument or in environment as LEXER_UPLOAD_API_TOKEN"
        upload_file(
            args.local_filename,
            args.record_type,
            args.destination_filename,
            args.destination_dataset_id,
            args.api_token,
        )
    elif args.action == "upload_validate":
        assert (
            args.api_token != ""
        ), "API Token must be provided in --api-token command line argument or in environment as LEXER_UPLOAD_API_TOKEN"
        if validate_upload(
            args.local_filename,
            args.record_type,
            args.destination_filename,
            args.destination_dataset_id,
            args.api_token,
        ):
            print("file validated and uploaded successfully")
        else:
            print("file validation failed")
            sys.exit(1)
    elif args.action == "validate":
        if validate_file(args.local_filename, args.record_type):
            print("file validation successful")
        else:
            print("file validation failed")
            sys.exit(1)
