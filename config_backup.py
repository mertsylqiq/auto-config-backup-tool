from netmiko import ConnectHandler
import os
from datetime import datetime

def backup_device_config(device):
    try:
        with ConnectHandler(**device) as net_connect:
            hostname = net_connect.find_prompt().split("#")[0]
            config = net_connect.send_command("show running-config")

            backup_dir = f"backups/{hostname}"
            os.makedirs(backup_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{backup_dir}/config_{timestamp}.txt"
            with open(filename, "w") as file:
                file.write(config)

            print(f"Backup successful for {hostname}. Config saved to {filename}")

    except Exception as e:
        print(f"Error during backup: {str(e)}")

if __name__ == "__main__":
    device = {
        "device_type": "cisco_ios",
        "ip": "192.168.1.1",
        "username": "your_username",
        "password": "your_password",
    }

    backup_device_config(device)
