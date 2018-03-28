'''
1. Using Netmiko, establish a connection to a network device and print
 out the device's prompt.
'''
from netmiko import Netmiko
from getpass import getpass

my_device = {
    'host': '10.128.64.69',
    'username': 'admin',
    'password': getpass(),
    'device_type': 'a10'
}

dev_conn = Netmiko(**my_device)

print('Prompt for device {} is: {}'.format(my_device['host'],
                                           dev_conn.find_prompt()))
