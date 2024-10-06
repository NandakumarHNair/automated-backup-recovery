
# Automated Backup and Recovery System

## Project Overview

Automated Backup and Recovery System is designed to automate the backup and recovery processes for SQL Server databases. This system ensures that your databases are regularly backed up and can be quickly restored in case of data loss or corruption. The project uses:

- **Python**: For scripting backup and recovery operations.
- **Bash**: For scheduling and automating tasks using cron jobs.
- **SQL Server**: As the target database system for backup and recovery.
- **Backup and Recovery**: Implementing reliable data protection strategies.
- **Automation**: Streamlining repetitive tasks to enhance efficiency.

## Directory Structure

```
automated-backup-recovery/
  scripts/
    backup.py
    restore.py
    backup.sh
    restore.sh
  config/
    config.json
  logs/
    backup.log
    restore.log
  requirements.txt
  README.md
```

- **scripts/**: Contains Python and Bash scripts for backup and recovery.
- **config/**: Holds configuration files.
- **logs/**: Stores log files for monitoring operations.
- **requirements.txt**: Lists Python dependencies.
- **README.md**: Project documentation.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/automated-backup-recovery.git
cd automated-backup-recovery
```

### 2. Install Python Dependencies

Ensure you have Python 3.6 or higher installed. Install required packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Configure Settings

Edit the `config/config.json` file with your SQL Server details and backup preferences.

### 4. Set Up Permissions

Make Bash scripts executable:

```bash
chmod +x scripts/backup.sh
chmod +x scripts/restore.sh
```

### 5. Schedule Backups

Use cron to schedule automated backups by editing the crontab:

```bash
crontab -e
```

Add the following line to schedule a daily backup at 2 AM:

```bash
0 2 * * * /bin/bash /path/to/automated-backup-recovery/scripts/backup.sh
```

## Configuration File

Modify the `config/config.json` file to store configuration settings:

- **sql_server**: Connection details for SQL Server.
- **backup**: Settings related to backup storage and retention.
- **recovery**: Directory where backups are stored for recovery.

## Note

Ensure that the ODBC Driver for SQL Server is installed on your system.

### Installation of ODBC Driver (Example for Ubuntu):

```bash
# Import the public repository GPG keys
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

# Register the Microsoft Ubuntu repository
sudo curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list -o /etc/apt/sources.list.d/mssql-release.list

# Update the package lists
sudo apt-get update

# Install the ODBC driver
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
```

## Logging

All operations are logged for monitoring and troubleshooting.

- **Backup Logs**: `logs/backup.log`
- **Restore Logs**: `logs/restore.log`

Ensure the `logs/` directory exists and has appropriate write permissions.

## Testing the System

### 1. Manual Backup

Execute the backup script manually to verify functionality:

```bash
./scripts/backup.sh
```

Check `logs/backup.log` for success messages.

### 2. Manual Restore

To restore from a backup, provide the backup file name:

```bash
./scripts/restore.sh YourDatabaseName_backup_20240425120000.bak
```

Verify restoration in `logs/restore.log` and by checking the database.

### 3. Automated Backup

Ensure the cron job is set up correctly and monitor `backup.log` for automated backups.

## Security Considerations

- **Credentials Management**: Storing plaintext credentials in `config.json` is insecure for production environments. Consider using environment variables or a secrets manager.
- **Access Permissions**: Restrict access to backup directories and log files to authorized users only.
- **Encryption**: Implement encryption for backup files to protect sensitive data.

## Enhancements

Future improvements can include:

- **Email Notifications**: Alert administrators on backup and restore success or failure.
- **Compression**: Compress backup files to save storage space.
- **Cloud Storage**: Integrate with cloud services (e.g., AWS S3, Azure Blob Storage) for offsite backups.
- **GUI Interface**: Develop a web-based interface for managing backups and restores.


## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Please follow the code of conduct when contributing.