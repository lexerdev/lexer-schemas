#!/bin/bash

set -euxo pipefail

mkdir -p docs/schema

generate-schema-doc --config template_name=md "jsonschema/*.jsonschema" docs/schema
