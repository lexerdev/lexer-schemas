# Convert A CSV file to ndjson with Lexer Schemas

This utility `convert_csv_to_ndjson.py` provides an example of
converting data from a spreadsheet into a Lexer Schema compliant
ndjson (Newline Delimited JSON) file.

It deals with the complexity of converting csv columns into
the nested objects that are required by the schemas.

The approach here does not include handling of nested arrays,
so it is inappropriate for use with commerce transaction records
such as `purchases` and `returns`

It's specifically intended to be useful in importing custom fields
that are associated with customer profiles.

An example (`example.csv`) is included that demonstrates a file
associates customer ids with a loyalty points custom field.

In the example, there are two columns with headers `link.customer_id`
and `custom_fields.loyalty_points`

the `.` characters used in these headers are used to separate the data
into sub-objects, so for example:

    link.customer_id,custom_fields.loyalty_points
    A13567,3600

will be mapped as

    {"link": {"customer_id": "A13567"}, "custom_fields": {"loyalty_points": "3600"}}

Using this behavior, this script will then use `lexer_schemas` to parse
the mapped data into the lexer-schema record type, then output the data
into a ndjson file.

Note: for this script to be useful, it's critical that the csv column
headers do correctly reference the fields available in the Lexer Schema.

## Installing
The script should run on python 3.8 or greater.

The script only requires `lexer_schemas` as a dependency

You may run

    pip3 install -r requirements.txt

to install the dependencies.

## Running

The script has 3 command line arguments

- `--input-file` - A CSV file to read
- `--record-type` - A lexer schema record type api name, eg `customer_record`
- `--output-file` - A path to write the output ndjson file to.

eg:

    ./csv_to_ndjson.py \
       --input-file example.csv \
       --record-type customer_record \
       --output-file example.csv.ndjson

## What's next?

Once you have a ndjson file, you can use the script in `examples/file_upload_api`
to upload it to a dataset on Lexer



