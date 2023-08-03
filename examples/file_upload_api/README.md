# upload.py

`upload.py` is a python script that uses the Lexer File Upload API
 and Lexer Schemas to validate and upload files.

## Installing dependencies

`upload.py` requires Python 3.7 or later.
 Requirements are defined in `requirements.txt` and can be installed using the command:
`pip3 install -r requirements.txt`

## API Token

The API Token used by this script is the one that the Lexer Hub UI refers to as the "Activity API Token"
This is accessed in Manage -> Integrations -> API Tokens

## Dataset ID

The Dataset ID used in the script is accessible by clicking on the dataset item in the list at Manage -> Datasets, then clicking the view button on the right, to load the Datset Details view.

## Upload commands

The script is invoked with an action sub command, and various argument parameters.

With commands that require an API token, this can be provided on the command line or in the `LEXER_UPLOAD_API_TOKEN` environment variable.

### Upload

Upload a file, skipping validation.

    ./upload.py upload \
         --local-filename my_file.ndjson \
         --record-type customer_record \
         --destination-dataset-id a1b2c3d4 \
         --api-token xxxxxxx

Note: requires api-token

### Validate and upload

Validate a file, and upload if valid.

    ./upload.py upload_validate \
         --local-filename my_file.ndjson \
         --record-type customer_record \
         --destination-dataset-id a1b2c3d4 \
         --api-token xxxxxxx

Note: requires api-token

### Validate

Validate a file

    ./upload.py validate \
        --local-filename my_file.ndjson \
        --record-type customer_record

## More help

More documentation for this script is available through running the help commands, eg:

    ./upload.py --help
    ./upload.py upload --help

