#!/bin/bash

set -euxo pipefail

mkdir -p docs/md/schemas
mkdir -p docs/html

generate-schema-doc --config template_name=md --config footer_show_time=false "jsonschema/*.jsonschema" docs/md/schemas/
generate-schema-doc --config template_name=js --config footer_show_time=false "jsonschema/*.jsonschema" docs/html/
