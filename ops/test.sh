#!/bin/bash

set -euxo pipefail

# give the unit-tests their own namespace as multiple build jobs may run at once
p="$(git log -1 --format='%h')_$(date +%s)"

# Cleanup docker containers and exit with correct status
function cleanup() {
  echo "--- stopping existing containers"
  docker-compose --project-name ${p} rm -sfv
}
trap cleanup EXIT

echo "--- building tests"

docker-compose --project-name $p build --build-arg BUSTCACHE=$(date +%U) test

echo "--- running tests"

docker-compose --project-name $p run --rm test
