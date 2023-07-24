# upload.py

`upload.py` is a python script that uses the Lexer File Upload API
 and Lexer Schemas to validate and upload files.

## Installing dependencies

`upload.py` requires Python 3.7 or later.
 Requirements are defined in `requirements.txt` and can be installed using the command:
`pip install -r requirements.txt`

## Upload commands

The script is invoked with an action sub command, and various argument parameters.

With commands that require an API token, this can be provided on the command line or in the `LEXER_UPLOAD_API_TOKEN` environment variable.

### Upload

Upload a file, skipping validation.

    ./upload.py upload \
         --local-filename my_file.ndjson \
         --record-type customer_profile \
         --destination-dataset-id a1b2c3d4 \
         --destination-filename=my_file.ndjson \
         --api-token xxxxxxx

Note: requires api-token

### Validate and upload

Validate a file, and upload if valid.

    ./upload.py validate_upload
         --local-filename my_file.ndjson \
         --record-type customer_profile \
         --destination-dataset-id a1b2c3d4 \
         --destination-filename=my_file.ndjson \
         --api-token xxxxxxx

Note: requires api-token

### Validate

Validate a file

    ./upload.py validate \
        --local-filename my_file.ndjson \
        --record-type customer_profile

## More help

More documentation for this script is available through running the help commands, eg:

    ./upload.py --help
    ./upload.py upload --help

