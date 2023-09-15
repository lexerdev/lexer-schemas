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

The script has 4 command line arguments

- `--input-file` - A CSV file to read
- `--record-type` - A lexer schema record type api name, eg `customer_record`
- `--output-file` - A path to write the output ndjson file to.
- `--debug-csv` - Optional, prints details about the file encoding and headers that were detected.

eg:

    ./csv_to_ndjson.py \
       --input-file example.csv \
       --record-type customer_record \
       --output-file example.csv.ndjson

## What's next?

Once you have a ndjson file, you can use the script in `examples/file_upload_api`
to upload it to a dataset on Lexer


## Troubleshooting

A common pitfall with dealing with CSV files is that they can contain invisible
control characters that interfere with the parsing of the rows and columns, or the
file itself might be using an unexpected encoding.

This example script contains some logic to detect the encoding of the file and 
automatically clean up various "BOM" characters, however you might still encounter files
that it fails to parse.

You can use the `--debug-csv` flag to print out what encoding the script has detected
and also what headers it has found, which can be useful to identify if you 
encountering an issue related to invisible characters or file encoding.

Tools like `vim` can also be used to identify special characters,
e.g. open your CSV file using the `-b` flag:
```
vim -b test_file.csv 

<feff>link.customer_id,custom_fields.loyalty_points^M
1234,16^M
5678,188^M
91011,0^M
1232,99^M
```

If the headers detected by the script don't match what you expect or you can see
special characters in the file you should try manually removing these characters
and making sure the file is saved as UTF-8 before retrying the script.
