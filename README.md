# Lexer Schemas

This repository contains schemas for Lexer public data ingestion API's

[![Build status](https://badge.buildkite.com/71b600da5678c24261116bf2ba456e9760207385a5d1cce223.svg)](https://buildkite.com/lexer/lexer-schemas)

## Installation
Simpily run `pip install git+http://git.camplexer.com/lexer-schemas@0.0.0` in the command line. Or add `lexer_schemas @ git+http://git.camplexer.com/lexer-schemas@0.0.0` to your requrements file.

## Usage
```python
from lexer_schemas.commerce_api.product_entity import ProductRecord

ProductRecord(product_id="123", name="Real Cool Hat")
```

## Development

### Testing
You can run tests by first building the test docker image `docker-compose build test` then running `docker-compose run test`

## Deployment
For now the package is installed from git.camplexer, we use tags to denote different versions of the package, we follow the `major.minor[.patch][sub]` format [as recommended by python](https://docs.python.org/3/distutils/setupscript.html#additional-meta-data).
The process of deploying changes should be:
1. Open a PR for your changes
    - Increment the `VERSION`` file to reflect your changes
2. Once approved merge your PR
3. Tag the latest `main` commit with the same version, either through the UI or the cli `git tag -a 0.0.0 -m "first release" && git push origin --tags`
