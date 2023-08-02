# Lexer Schemas

This repository contains schemas for Lexer public data ingestion API's

[![Build status](https://badge.buildkite.com/71b600da5678c24261116bf2ba456e9760207385a5d1cce223.svg)](https://buildkite.com/lexer/lexer-schemas)

## Installation
Install by running `pip install git+https://github.com/lexerdev/lexer-schemas@0.3.2` in the command line.

Or you can add `lexer_schemas @ git+https://github.com/lexerdev/lexer-schemas@0.3.2` to your `requirements.txt` file.

## Usage
```python
from lexer_schemas.commerce_api.product_entity import ProductRecord

ProductRecord(product_id="123", name="Real Cool Hat")
```

## Documentation
A web version of the schemas is available here: https://lexerdev.github.io/lexer-schemas/

## Examples

In `/examples`, there are a few scripts that use the Lexer Schema package and also some example data files.

### [csv\_to\_ndjson](examples/csv_to_ndjson/)
Use Lexer Schemas to convert a file from `csv` to `ndjson`, by mapping the CSV header line to fields in the lexer schema.

### [data](examples/data/)
Some examples of data files that match Lexer Schemas

### [file\_upload\_api](examples/file_upload_api/)
Use Lexer Schemas to validate an `ndjson` file against a given record type, then optionally use Lexer's File Upload API to upload that file into a Lexer Dataset.

## Development

### Testing
You can run tests by first building the test docker image `docker-compose build test` then running `docker-compose run test`

### Documentation
Generate documentation by first building the docs docker image `docker-compose build docs` then running `docker-compose run docs`

## Deployment
For now the package is installed from github, we use tags to denote different versions of the package, we follow the `major.minor[.patch][sub]` format [as recommended by python](https://docs.python.org/3/distutils/setupscript.html#additional-meta-data).
The process of deploying changes should be:
1. Open a PR for your changes
    - Increment the `VERSION`` file to reflect your changes
2. Once approved merge your PR
3. Tag the latest `main` commit with the same version, either through the UI or the cli `git tag -a 0.0.0 -m "first release" --force && git push origin --tags --force`
