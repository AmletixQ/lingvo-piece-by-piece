#!/bin/bash

if [ -f gunicorn.pid ]; then
	kill $(cat gunicorn.pid)
	rm gunicorn.pid
else
	echo "PID-file doesn't exist"
fi

