 Quick Script to connect to Cisco devices via SSH

import os

from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("Please enter you SSH username: ")
PASS = getpass("Please enter your SSH password: ")

device = {
    'ip': '192.168.42.31',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios',
}

c = ConnectHandler(**device)

output = c.send_command('show run')

f = open('backup.conf', 'x')

f.write(output)
f.close()
