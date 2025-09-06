#!/bin/bash

# Prompt for Python alias
read -p "Enter your Python command (e.g., python3, python, py): " PYTHON_CMD

# Check if Python is installed
if ! command -v $PYTHON_CMD &> /dev/null; then
    echo "Error: $PYTHON_CMD is not installed or not found in PATH."
    exit 1
fi

# Check if venv module exists
if ! $PYTHON_CMD -m venv --help &> /dev/null; then
    echo "Error: venv module not found for $PYTHON_CMD."
    exit 1
fi

# Create virtual environment
$PYTHON_CMD -m venv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
if [ ! -f requirements.txt ]; then
    echo "Error: requirements.txt not found."
    deactivate
    exit 1
fi
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install requirements."
    deactivate
    exit 1
fi

echo "Setup complete."
read -p "Do you want to run main.py now? (y/n): " RUN_NOW
if [ "$RUN_NOW" == "y" ] || [ "$RUN_NOW" == "Y" ]; then
    $PYTHON_CMD main.py
else
    echo "run $PYTHON_CMD main.py to run the main script"
fi

deactivate
