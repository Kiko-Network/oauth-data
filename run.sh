#!/bin/bash

echo "WORKERS: ${WORKERS:-1}"
gunicorn main:app --workers=${WORKERS:-1} -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --preload
