#!/bin/sh

# Generate once on startup
python3 /app/generate_ics.py

# Start cron
supercronic /app/crontab.txt

# Serve files
cd /app/data
python3 -m http.server 8080
