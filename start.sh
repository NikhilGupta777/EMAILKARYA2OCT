#!/bin/bash

# Run database migration first
echo "Running database migration..."
python migrate_sendgrid_templates.py

# Start the FastAPI server
echo "Starting FastAPI server..."
exec uvicorn main:app --host 0.0.0.0 --port $PORT