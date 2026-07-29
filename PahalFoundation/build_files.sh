#!/bin/bash
# Vercel build script for Django
# This runs during the Vercel build phase

echo "==> Installing dependencies..."
pip install -r requirements.txt

echo "==> Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "==> Build complete."
