#!/bin/sh

python3 /app/generate_ics.py
supercronic /app/crontab.txt &

# Run with Gunicorn
exec gunicorn -b 0.0.0.0:8080 serve:app
