#!/bin/bash

# Usage: ./restore.sh backup_filename.bak

if [ -z "$1" ]; then
    echo "Usage: $0 backup_filename.bak"
    exit 1
fi

BACKUP_FILE=$1

# Navigate to the script directory
cd "$(dirname "$0")"

# Activate virtual environment if using one
# source ../venv/bin/activate

# Execute the restore script
python3 restore.py "$BACKUP_FILE"

# Deactivate virtual environment if activated
# deactivate

