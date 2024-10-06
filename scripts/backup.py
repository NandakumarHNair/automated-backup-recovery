#!/usr/bin/env python3

import os
import json
import pyodbc
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(
    filename='../logs/backup.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

def load_config():
    with open('../config/config.json') as config_file:
        return json.load(config_file)

def perform_backup(config):
    try:
        server = config['sql_server']['server']
        database = config['sql_server']['database']
        username = config['sql_server']['username']
        password = config['sql_server']['password']
        port = config['sql_server']['port']

        backup_dir = config['backup']['backup_directory']
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_filename = f"{database}_backup_{timestamp}.bak"
        backup_path = os.path.join(backup_dir, backup_filename)

        # Establish connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};' \
                            f'SERVER={server},{port};DATABASE={database};' \
                            f'UID={username};PWD={password}'
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Perform backup
        backup_query = f"BACKUP DATABASE [{database}] TO DISK = N'{backup_path}' WITH NOFORMAT, NOINIT, NAME = N'{database}-Full Database Backup', SKIP, NOREWIND, NOUNLOAD, STATS = 10"
        cursor.execute(backup_query)
        cursor.commit()
        logging.info(f"Backup successful: {backup_path}")

        # Cleanup old backups
        retention_days = config['backup']['backup_retention_days']
        cutoff_date = datetime.now() - timedelta(days=retention_days)
        for file in os.listdir(backup_dir):
            if file.endswith('.bak'):
                file_path = os.path.join(backup_dir, file)
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_time < cutoff_date:
                    os.remove(file_path)
                    logging.info(f"Old backup deleted: {file_path}")

    except Exception as e:
        logging.error(f"Backup failed: {str(e)}")

def main():
    config = load_config()
    perform_backup(config)

if __name__ == "__main__":
    main()

