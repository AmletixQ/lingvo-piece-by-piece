#!/bin/bash

source .venv/bin/activate
exec gunicorn server:app --bind 0.0.0.0:5001 --daemon --pid gunicorn.pid
