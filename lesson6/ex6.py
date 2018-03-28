'''
6. Optional, connect to three networking devices one after the other.
 Use send_command() to execute a show command on each of these devices.
 Print this output to the screen.
'''
from netmiko import Netmiko
from getpass import getpass


my_devices = [
    {
        'host': '10.128.64.69',
        'username': 'admin',
        'password': getpass(),
        'device_type': 'a10',
        'cmd': 'show interface brief'
    },
    {
        'host': '10.128.64.11',
        'username': 'cisco',
        'password': getpass(),
        'device_type': 'cisco_ios',
        'cmd': 'show ip interface brief'
    },
    {
        'host': '10.128.64.15',
        'username': 'juniper',
        'password': getpass(),
        'device_type': 'juniper',
        'cmd': 'show interfaces terse'
    }
]


for device in my_devices:
    command = device.pop('cmd')
    dev_conn = Netmiko(**device)
    com_output = dev_conn.send_command(command)
    print('-' * 80)
    print('Output of "{}" command on "{}({})"'.format(command,
                                                      device['host'],
                                                      device['device_type']))
    print('-' * 80)
    print('{}'.format(com_output))
    print('-' * 80)
