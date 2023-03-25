#!/usr/bin/env sh

set -e
service nginx start
exec "$@"
