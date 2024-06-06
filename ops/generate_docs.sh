#!/bin/bash

set -euxo pipefail

mkdir -p docs/md/schemas
mkdir -p docs/html

python lexer_schemas/generate_json_schemas.py
generate-schema-doc --config template_name=md --config footer_show_time=false "jsonschema/*.json" docs/md/schemas/
generate-schema-doc --config template_name=js --config footer_show_time=false "jsonschema/*.json" docs/html/
