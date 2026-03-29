#!/bin/bash
# ─────────────────────────────────────────────
#  SocialHub – Quick Setup Script (Python 3.7+)
# ─────────────────────────────────────────────
set -e

echo ""
echo "========================================"
echo "  SocialHub – Social Media App Setup"
echo "========================================"
echo ""

# 1. Create & activate virtual environment
if [ ! -d "venv" ]; then
    echo "[1/5] Creating virtual environment..."
    python3 -m venv venv
fi

echo "[2/5] Activating virtual environment..."
source venv/bin/activate

# 2. Install dependencies
echo "[3/5] Installing dependencies (Django 2.2, Pillow)..."
pip install -r requirements.txt --quiet

# 3. Run migrations
echo "[4/5] Running database migrations..."
python manage.py makemigrations core
python manage.py migrate

# 4. Create superuser (optional)
echo ""
echo "[5/5] Would you like to create an admin superuser? (y/n)"
read -r answer
if [ "$answer" = "y" ] || [ "$answer" = "Y" ]; then
    python manage.py createsuperuser
fi

echo ""
echo "========================================"
echo "  Setup complete! Starting server..."
echo "  Open: http://127.0.0.1:8000"
echo "  Admin: http://127.0.0.1:8000/admin"
echo "========================================"
echo ""

python manage.py runserver
