# Network Configuration Backup Tool

This Python script automates the backup of network device configurations, focusing on Cisco devices, using the Netmiko library.

## Features

- Connects to network devices via SSH.
- Retrieves the running configuration of each device.
- Organizes backups by device hostname and timestamp.

## Prerequisites

- Python 3.x installed
- Pip package manager installed

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/network-config-backup.git

Change into the project directory:

cd network-config-backup
Install dependencies:

pip install netmiko

Usage
Customize the script with your network device details.

Run the script:

python config_backup.py
Check the backups directory for organized configuration files.

Configuration
Modify the script file (config_backup.py) with your device details and preferences.

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License.
