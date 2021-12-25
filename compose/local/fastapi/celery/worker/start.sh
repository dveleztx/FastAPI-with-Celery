#!/bin/bash

set -o errexit
set -o nounset

python -c "from main import celery_worker; celery_worker()"
