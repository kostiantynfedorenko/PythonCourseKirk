'''
2. Use send_command() to send a show command down the SSH channel.
 Retrieve the results and print the results to the screen.
'''
from netmiko import Netmiko
from getpass import getpass


command = 'show interface ethernet 1'
password = getpass()
my_device = {
    'host': '10.128.64.69',
    'username': 'admin',
    'password': password,
    'device_type': 'a10'
}

dev_conn = Netmiko(**my_device)
com_output = dev_conn.send_command(command)

print('*' * 80)
print('Output of "{}" command on "{}"'.format(command, my_device['host']))
print('*' * 80)
print('{}'.format(com_output))
print('*' * 80)
