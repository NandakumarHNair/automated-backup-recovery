#!/usr/bin/env python3

import os
import json
import pyodbc
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='../logs/restore.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

def load_config():
    with open('../config/config.json') as config_file:
        return json.load(config_file)

def perform_restore(config, backup_file):
    try:
        server = config['sql_server']['server']
        database = config['sql_server']['database']
        username = config['sql_server']['username']
        password = config['sql_server']['password']
        port = config['sql_server']['port']

        backup_dir = config['backup']['backup_directory']
        backup_path = os.path.join(backup_dir, backup_file)

        if not os.path.exists(backup_path):
            logging.error(f"Backup file does not exist: {backup_path}")
            return

        # Establish connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};' \
                            f'SERVER={server},{port};DATABASE=master;' \
                            f'UID={username};PWD={password}'
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Set database to single user mode
        single_user_query = f"ALTER DATABASE [{database}] SET SINGLE_USER WITH ROLLBACK IMMEDIATE"
        cursor.execute(single_user_query)
        conn.commit()

        # Restore database
        restore_query = f"RESTORE DATABASE [{database}] FROM DISK = N'{backup_path}' WITH REPLACE"
        cursor.execute(restore_query)
        conn.commit()
        logging.info(f"Restore successful from: {backup_path}")

        # Set database back to multi-user mode
        multi_user_query = f"ALTER DATABASE [{database}] SET MULTI_USER"
        cursor.execute(multi_user_query)
        conn.commit()

    except Exception as e:
        logging.error(f"Restore failed: {str(e)}")

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Restore SQL Server Database from Backup')
    parser.add_argument('backup_file', help='The backup file to restore from')
    args = parser.parse_args()

    config = load_config()
    perform_restore(config, args.backup_file)

if __name__ == "__main__":
    main()

