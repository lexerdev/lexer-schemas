#!/bin/bash

set -euxo pipefail

mkdir -p docs/md/schemas
mkdir -p docs/html

generate-schema-doc --config template_name=md "jsonschema/*.jsonschema" docs/md/schemas/
generate-schema-doc --config template_name=js "jsonschema/*.jsonschema" docs/html/
