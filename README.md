# Lexer Schemas

This repository contains schemas for Lexer public data ingestion API's

## Installation
Simpily run `pip install git+http://git.camplexer.com/lexer-schemas`

## Usage
```python
from lexer_schemas.commerce_api.product_entity import ProductRecord

ProductRecord(product_id="123", name="Real Cool Hat")
```

## Development

### Testing
You can run tests by first building the test docker image `docker-compose build test` then running `docker-compose run test`
