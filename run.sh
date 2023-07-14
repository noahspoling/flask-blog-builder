#!/bin/bash

#If directory exists
if [ ! -d ".venv"]
then
    echo "Creating python virtual environment..."

    python3 -m venv .venv
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

#Run app
echo "Running app.py..."
python3 app.py