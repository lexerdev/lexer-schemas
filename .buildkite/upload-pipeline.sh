#!/bin/bash
set -euxo pipefail
cat .buildkite/pipeline.yml
buildkite-agent pipeline upload
