#!/bin/bash

# Navigate to the script directory
cd "$(dirname "$0")"

# Activate virtual environment if using one
# source ../venv/bin/activate

# Execute the backup script
python3 backup.py

# Deactivate virtual environment if activated
# deactivate

