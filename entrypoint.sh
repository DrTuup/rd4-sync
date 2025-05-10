#!/bin/sh

# Run with Gunicorn
exec gunicorn -b 0.0.0.0:8080 serve:app
