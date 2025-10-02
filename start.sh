#!/bin/bash

# Railway deployment script
set -e  # Exit on error

echo "Starting deployment..."

# Run database migration first (if migration file exists)
if [ -f "migrate_sendgrid_templates.py" ]; then
    echo "Running database migration..."
    python migrate_sendgrid_templates.py || echo "Migration skipped or failed (non-critical)"
fi

# Start the FastAPI server with gunicorn for production
echo "Starting FastAPI server on port ${PORT:-8000}..."
exec gunicorn main:app \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info